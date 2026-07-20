from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'subject',
            'branch',
            'semester',
            'description',
            'file'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Note Title'
            }),

            'subject': forms.Select(attrs={
                'class': 'form-control'
            }),

            'branch': forms.Select(attrs={
                'class': 'form-control'
            }),

            'semester': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Semester (1-8)'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Add details, topics covered, or course code...'
            }),

            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '*/*'
            }),
        }


class OnlineNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'subject',
            'branch',
            'semester',
            'description',
            'content',
            'drawing_data',
            'file'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter E-Note Title (e.g. DBMS Normalization Notes)'
            }),

            'subject': forms.Select(attrs={
                'class': 'form-control'
            }),

            'branch': forms.Select(attrs={
                'class': 'form-control'
            }),

            'semester': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Semester (1-8)'
            }),

            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Overview summary of this note'
            }),

            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 12,
                'placeholder': 'Type, format, or paste your digital study notes, formulas, and definitions here...'
            }),

            'drawing_data': forms.HiddenInput(attrs={
                'id': 'drawingDataInput'
            }),

            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '*/*'
            }),
        }