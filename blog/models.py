# blog/models.py

from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()  # Use RichTextField instead of TextField
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()  # Use RichTextField instead of TextField
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    capacity = models.PositiveIntegerField(default=30)
    registered_students = models.ManyToManyField('Student', through='Registration')
    # students = models.ManyToManyField('Student', related_name='courses')
 
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=80)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author}'

class Feedback(models.Model):
    author = models.CharField(max_length=80)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author}'

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    registration_id = models.CharField(max_length=10, unique=True)
    school = models.CharField(max_length=100,null=True, blank=True)
    major = models.CharField(max_length=100,null=True, blank=True) 
    date_of_birth = models.DateField(null=True, blank= True)
    #courses = models.ForeignKey(Course, related_name='registered_students', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def registered_courses(self):
        registrations = Registration.objects.filter(student=self)
        return [registration.course for registration in registrations]

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return f'{self.student} - {self.course}'
    class Meta:
        unique_together = ('student', 'course')