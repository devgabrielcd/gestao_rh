from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from . models import Departamento


class ListDepartamento(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class CreateDepartamento(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(CreateDepartamento, self).form_valid(form)


class EditDepartamento(UpdateView):
    model = Departamento
    fields = ['nome']


class DeleteDepartamento(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamento')


