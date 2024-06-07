# blog/forms.py

from django import forms
from .models import Comment, Post, Feedback, Student, Registration
from ckeditor.widgets import CKEditorWidget

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['author','body']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'content']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'school', 'major']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'dateofbirth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'school': forms.TextInput(attrs={'class': 'form-control'}),
            'major': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['course']
