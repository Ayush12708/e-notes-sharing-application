from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):

    STATUS_CHOICES = [
        ("Draft", "Draft"),
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]

    SUBJECT_CHOICES = [
        ('DBMS', 'DBMS'),
        ('OS', 'Operating System'),
        ('CN', 'Computer Networks'),
        ('CC', 'Cloud Computing'),
        ('DSA', 'Data Structures'),
        ('JAVA', 'Java'),
        ('PYTHON', 'Python'),
        ('MATH', 'Mathematics'),
        ('OTHER', 'Other'),
    ]

    BRANCH_CHOICES = [
        ('CSE', 'Computer Science Engineering'),
        ('IT', 'Information Technology'),
        ('ECE', 'Electronics & Comm.'),
        ('ME', 'Mechanical Engineering'),
        ('CIVIL', 'Civil Engineering'),
        ('BCA_MCA', 'BCA / MCA'),
        ('COMMERCE', 'Commerce & Business'),
        ('OTHER', 'General / Other'),
    ]

    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES, default='CSE')
    semester = models.IntegerField()
    description = models.TextField(blank=True)
    content = models.TextField(blank=True, help_text="Rich text or markdown content for online created e-notes")
    drawing_data = models.TextField(blank=True, help_text="Base64 canvas drawing image data")
    is_online_note = models.BooleanField(default=False)

    file = models.FileField(upload_to='notes/', blank=True, null=True)

    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    downloads = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='liked_notes', blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='bookmarked_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'note')

    def __str__(self):
        return f"{self.user.username} - {self.note.title}"


class Comment(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} on {self.note.title}"