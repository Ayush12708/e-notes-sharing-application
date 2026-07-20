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
            'content',
            'drawing_data',
            'file'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter note title (e.g. DBMS Unit 3 BCNF & Normalization Notes)'
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
                'rows': 3,
                'placeholder': 'Short summary, course code, or key topics covered...'
            }),

            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
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