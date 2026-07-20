from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


def ensure_default_users():
    """Ensure standard seed accounts (admin, ayush, bala) exist with verified passwords."""
    try:
        # 1. Admin Account
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={'email': 'admin@notehub.com', 'is_staff': True, 'is_superuser': True}
        )
        if not admin_user.check_password('admin123'):
            admin_user.set_password('admin123')
            admin_user.save()
        Profile.objects.get_or_create(user=admin_user, defaults={'college': 'NoteHub University', 'semester': 1})

        # 2. Ayush Account
        ayush_user, created = User.objects.get_or_create(
            username='ayush',
            defaults={'email': 'ayush@notehub.com', 'first_name': 'Ayush', 'last_name': 'Kumar'}
        )
        if not ayush_user.check_password('ayush123'):
            ayush_user.set_password('ayush123')
            ayush_user.save()
        Profile.objects.get_or_create(user=ayush_user, defaults={'college': 'Lovely Professional Univ.', 'semester': 5})

        # 3. Bala Account
        bala_user, created = User.objects.get_or_create(
            username='bala',
            defaults={'email': 'bala@notehub.com', 'first_name': 'Bala'}
        )
        if not bala_user.check_password('bala123'):
            bala_user.set_password('bala123')
            bala_user.save()
        Profile.objects.get_or_create(user=bala_user, defaults={'college': 'Chandigarh Univ.', 'semester': 3})

    except Exception:
        pass


def register(request):
    ensure_default_users()

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username'].strip()
            if User.objects.filter(username__iexact=username).exists():
                messages.error(request, f"Username '{username}' is already taken. Please choose another one.")
                return render(request, 'accounts/register.html', {'form': form})

            user = User.objects.create_user(
                username=username,
                first_name=form.cleaned_data['first_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            Profile.objects.create(
                user=user,
                phone=form.cleaned_data.get('phone', ''),
                college=form.cleaned_data.get('college', ''),
                semester=form.cleaned_data.get('semester', 1)
            )

            # Automatically log the user in immediately after registration!
            login(request, user)
            messages.success(request, f"Welcome to NoteHub, {user.first_name or user.username}! Your account has been created successfully.")
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.replace('_', ' ').title()}: {error}")

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    ensure_default_users()

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username or not password:
            messages.error(request, "Please enter both username and password.")
            return render(request, 'accounts/login.html')

        # Try exact username match first
        user = authenticate(request, username=username, password=password)

        # Fallback to case-insensitive username match
        if user is None:
            try:
                user_obj = User.objects.get(username__iexact=username)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, f"Welcome back, {user.first_name or user.username}!")
                next_url = request.GET.get('next') or request.POST.get('next')
                if next_url and next_url.startswith('/'):
                    return redirect(next_url)
                return redirect('dashboard')
            else:
                messages.error(request, "This user account is disabled.")
        else:
            messages.error(request, "Invalid username or password. Please check your credentials or click 'Register here' below!")

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')


@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={'phone': '', 'college': 'Not specified', 'semester': 1}
    )

    success_msg = False
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile details updated successfully!")
            success_msg = True
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile': profile,
        'success_msg': success_msg,
    }
    return render(request, 'accounts/profile.html', context)