from django.shortcuts import render
from django.views.generic import CreateView
from .models import Documentos


class CreateDocument(CreateView):
    model = Documentos
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['id']

        if form.is_valid:
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
