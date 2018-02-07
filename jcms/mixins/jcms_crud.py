from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.urls import path
from abc import ABCMeta, abstractmethod
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Q


# Creates all views needed for a model
class JcmsCrud(object):
    __metaclass__ = ABCMeta

    def __init__(self, model, create_edit_list, list_fields=[], icon=''):
        self.model = model
        self.create_edit_list = create_edit_list
        self.list_fields = list_fields if list_fields else create_edit_list
        self.icon = icon
        self.model_name = model.__name__.lower()

    # Mixin with permission and login
    class PermissionMixin(LoginRequiredMixin, PermissionRequiredMixin):
        pass

    # Gets all url objects for to create the urls
    def get_crud_urls(self):
        return [
            path(self.model_name + '/', list_view(self), name=self.model_name + 'List'),
            path(self.model_name + '/<int:pk>/', detail_view(self), name=self.model_name + 'Detail'),
            path(self.model_name + '/create/', create_view(self), name=self.model_name + 'Create'),
            path(self.model_name + '/<int:pk>/delete/', delete_view(self), name=self.model_name + 'Delete'),
            path(self.model_name + '/<int:pk>/edit/', edit_view(self), name=self.model_name + 'Edit'),
        ]


# List view with permission create_model_name
def list_view(crud):
    class ObjectList(crud.PermissionMixin, ListView):
        fields = crud.list_fields
        model = crud.model
        template_name = 'jcms-admin/crud/list.html'
        permission_required = 'jcms.create_' + crud.model_name

        def get_queryset(self):
            query_set = get_search_queryset(self)
            if query_set:
                return query_set

            return super(ObjectList, self).get_queryset()

    return ObjectList.as_view()


# Detail view with permission create_model_name
def detail_view(crud):
    class ObjectDetail(crud.PermissionMixin, DetailView):
        model = crud.model
        template_name = 'jcms-admin/crud/detail.html'
        permission_required = 'jcms.create_' + crud.model_name

    return ObjectDetail.as_view()


# Create view with permission create_model_name
def create_view(crud):
    class ObjectCreate(crud.PermissionMixin, SuccessMessageMixin, CreateView):
        model = crud.model
        fields = crud.create_edit_list
        template_name = 'jcms-admin/crud/edit_or_create.html'
        success_url = reverse_lazy('jcms:' + crud.model_name + 'List')
        permission_required = 'jcms.create_' + crud.model_name
        success_message = 'Successfully created ' + crud.model_name

    return ObjectCreate.as_view()


# Edit view with permission change_model_name
def edit_view(crud):
    class ObjectEdit(crud.PermissionMixin, SuccessMessageMixin, UpdateView):
        model = crud.model
        fields = crud.create_edit_list
        template_name = 'jcms-admin/crud/edit_or_create.html'
        success_url = reverse_lazy('jcms:' + crud.model_name + 'List')
        permission_required = 'jcms.change_' + crud.model_name
        success_message = 'Successfully edited ' + crud.model_name

    return ObjectEdit.as_view()


# Delete view with permission delete_model_name
def delete_view(crud):
    class ObjectDelete(crud.PermissionMixin, DeleteView):
        model = crud.model
        permission_required = 'jcms.delete_' + crud.model_name
        success_url = reverse_lazy('jcms:' + crud.model_name + 'List')
        success_message = 'Successfully deleted ' + crud.model_name

        def delete(self, request, *args, **kwargs):
            messages.success(self.request, self.success_message)
            return super(ObjectDelete, self).delete(request, *args, **kwargs)

    return ObjectDelete.as_view()


def get_search_queryset(crud):
    search_term = crud.request.GET.get('search')
    if search_term:
        print(search_term)
        queries = [Q(**{f: search_term}) for f in crud.fields]
        qs = Q()
        for query in queries:
            qs = qs | query

        return crud.model.objects.filter(qs)

    return None
