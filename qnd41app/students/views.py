from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from editorial_literaria.models import Course
from .forms import CourseEnrollForm
from usuarios.models import Profile, DeclaracionVeracidad
from django.shortcuts import redirect, get_object_or_404


class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_course_list')

    def form_valid(self, form):
        result = super(StudentRegistrationView,
                       self).form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'])
        login(self.request, user)
        return result


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
    #    self.course.projects.add(self.request.project)
        return super(StudentEnrollCourseView,
                     self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('students:student_course_detail',
                            args=[self.course.id])
    


class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        
        qs = super(StudentCourseListView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])


class StudentCourseDetailView(DetailView):
    model = Course
    template_name = 'students/course/detail.html'
    context_object_name = 'course'  # Cambié el nombre del objeto de contexto para mayor claridad

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Mover esta línea al principio para evitar errores
        # get course object
        course = self.get_object()
        if 'module_id' in self.kwargs:
            # get current module
            context['module'] = course.modules.get(id=self.kwargs['module_id'])
        else:
            # get first module
            context['module'] = course.modules.first()
        # Agregar actividad y acepta_terminos_condiciones al contexto
        context['actividad'] = self.get_profile()
        context['acepta_terminos_condiciones'] = self.get_declaracion()
        return context
    
    def get_profile(self):
        user = self.request.user
        profile = get_object_or_404(Profile, user=user)
        return profile.activity
    
    def get_declaracion(self):
        user = self.request.user
        declaracion = get_object_or_404(DeclaracionVeracidad, user=user)
        return declaracion.acepta_terminos_condiciones