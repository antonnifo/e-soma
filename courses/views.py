from django.views.generic.list import ListView
from .models import Course
from django.views.generic.edit import CreateView, \
    UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin


class OwnerMixin:
    '''
    implements the get_queryset() method, which is used by the views to 
    get the base QuerySet. This mixin will override this method to filter 
    objects by the owner attribute to retrieve objects that belong to the 
    current user (request.user).
    '''

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin:
    '''
    implements the form_valid() method, which is used by views 
    that use Django’s ModelFormMixin mixin, that is, views with 
    forms or model forms such as CreateView and UpdateView. form_valid() 
    is executed when the submitted form is valid. The default behavior
    for this method is saving the instance (for model forms) and redirecting
    the user to success_url. You override this method to automatically set
    the current user in the owner attribute of the object being saved.
    By doing so, you set the owner for an object automatically when it is saved.
    '''

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin):
    model = Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = 'courses/manage/course/form.html'


class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = 'courses/manage/course/list.html'
    permission_required = 'courses.view_course'


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required = 'courses.add_course'


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    permission_required = 'courses.change_course'


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'courses/manage/course/delete.html'
    permission_required = 'courses.delete_course'


    

