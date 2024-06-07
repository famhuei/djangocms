# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Course, Feedback, Student, Registration
from .forms import CommentForm, PostForm, FeedbackForm, StudentForm, RegistrationForm
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required 
def index(request):
    return render(request,'blog/index.html')

def courses(request):
    query = request.GET.get('q')
    if query:
        courses = Course.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    else:
        courses = Course.objects.all()
    return render(request,'blog/courses.html', {'courses':courses})

def news(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    else:
        posts = Post.objects.all()
    return render(request,'blog/news.html', {'posts':posts})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = FeedbackForm()
    
    feedbacks = Feedback.objects.all()
    return render(request, 'blog/feedback.html', {'form': form, 'feedbacks': feedbacks})

    # _feedback = Feedback.objects.all()
    # return render(request,'blog/feedback.html', {'feedbacks':_feedback})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    comments = post.comments.all()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

def post_list(request):
   
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        registration_form = RegistrationForm(request.POST)
        if student_form.is_valid() and registration_form.is_valid():
            student = student_form.save(commit=False)
            student.registration_id = generate_unique_registration_id()
            student.save()
            registration = registration_form.save(commit=False)
            registration.student = student
            
            # Get the selected course from the form
            course_id = registration_form.cleaned_data['course'].id
            course = get_object_or_404(Course, pk=course_id)
            
            # Check if the course has reached its capacity
            registered_students_count = Registration.objects.filter(course=course).count()
            if registered_students_count < course.capacity:
                registration.course = course  # Associate the selected course with the registration
                registration.save()
                return render(request, 'blog/registration_success.html', {'student': student, 'course': course})

            else:
                return HttpResponse('Course is full')
    else:
        student_form = StudentForm()
        registration_form = RegistrationForm()
    courses = Course.objects.all()  # Retrieve all available courses
    return render(request, 'blog/register.html', {'student_form': student_form, 'registration_form': registration_form, 'courses': courses})


# blog/views.py

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    # registered_students = course.students.all()
    registered_students_count = course.registered_students.count()
    return render(request, 'blog/course_detail.html', {'course': course,
                                                    #    'register_students': registered_students,
                                                       'registered_students_count': registered_students_count})


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Student, Course, Registration
from .forms import StudentForm, RegistrationForm



def generate_unique_registration_id():
    import random
    import string
    while True:
        registration_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        if not Student.objects.filter(registration_id=registration_id).exists():
            return registration_id

@staff_member_required
def course_student_list(request, pk):
    course = get_object_or_404(Course, pk=pk)
    students = course.registered_students.all()
    return render(request, 'blog/course_student_list.html', {'course': course, 'students': students})

def course_register(request, pk):
    course = get_object_or_404(Course, pk=pk)
    registered_students = course.students.all()  # Fetch students related to this course
    registered_students_count = registered_students.count()
    return render(request, 'blog/register.html', {
        'course': course,
        'registered_students': registered_students,
        'registered_students_count': registered_students_count,
    })


def lookup_registration(request):
    if request.method == 'POST':
        registration_id = request.POST.get('registration_id')
        try:
            student = Student.objects.get(registration_id=registration_id)
            courses = student.registered_courses()
            return render(request, 'blog/student_registration_detail.html', {'student': student, 'courses': courses})
        except Student.DoesNotExist:
            return HttpResponse('No registration found for this ID.')
    return render(request, 'blog/lookup_registration.html')

