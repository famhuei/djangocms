from django.contrib import admin
from .models import Post, Comment, Course, Student, Registration, Feedback
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.html import format_html

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at' )

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'capacity', 'registered_students')
    search_fields = ('title', 'content')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:course_id>/students/', self.admin_site.admin_view(self.course_student_list))
        ]
        return custom_urls + urls
    
    def course_student_list(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        students = course.registered_students.all()
        # Assuming 'registered_students' is the related name for the Student model ForeignKey
        return render(request, 'admin/course_student_list.html', {'course': course, 'students': students})

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'date_of_birth','school','institue','major','registration_id']

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'registered_at']



def view_registered_students(modeladmin, request, queryset):
    for course in queryset:
        url = reverse('course_students', args=[course.pk])
        return mark_safe(f'<a href="{url}" target="_blank">View Registered Students</a>')
    view_registered_students.short_description = "View Registered Students"

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'registered_students_link']

    def registered_students_link(self, obj):
        url = f"http://127.0.0.1:8000/course/{obj.id}/students/"
        return format_html('<a href="{}">View Registered Students</a>',url)
    registered_students_link.allow_tags = True
    registered_students_link.short_description = "Link to Students List"


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student)
admin.site.register(Registration)
admin.site.register(Feedback)
