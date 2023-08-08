import csv
import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from .forms import RegistroHoraExtraForm
from .models import RegistroHoraExtra

import xlwt


class ListHoraExtra(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class CreateHoraExtra(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(CreateHoraExtra, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class EditHoraExtraBase(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_success_url(self):
        return reverse_lazy('update_hora_extra_base', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(EditHoraExtraBase, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class EditHoraExtra(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(EditHoraExtra, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class DeleteHoraExtra(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')


class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):

        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()

        funcionario = self.request.user.funcionario

        response = json.dumps({'mensagem': 'Requisicao solicitada com sucesso!!!', 'horas': funcionario.total_hora_extra})

        return HttpResponse(response, content_type='application/json')


class NaoUtilizouHoraExtra(View):
    def post(self, *args, **kwargs):

        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = False
        registro_hora_extra.save()

        funcionario = self.request.user.funcionario

        response = json.dumps({'mensagem': 'Requisicao solicitada com sucesso!!!', 'horas': funcionario.total_hora_extra})

        return HttpResponse(response, content_type='application/json')


class ExportarParaCsv(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'Attachment; filename="myfile.csv"'

        registro_he = RegistroHoraExtra.objects.filter(utilizada=False)

        writer = csv.writer(response)
        writer.writerow(['First Row', 'Id', 'Motivo', 'Funcionario', 'Total_horas_extras', 'horas'])

        for registro in registro_he:
            writer.writerow([registro.id, registro.motivo, registro.funcionario, registro.funcionario.total_hora_extra,
                             registro.horas])
        return response


class ExportarParaExcel(View):
    def get(self, request):
        # contruir a requisicao
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'Attachment; filename="MyExcelFile.xls"'
        # wb seta o encode padrao. ws adiciona uma aba nova na tabela
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Banco de Horas')
        # comecar a escrever desde a linha 0
        row_num = 0
        # definir o estilo da fonte para Bold. Cabeçalho
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        # Nomear as colunas
        columns = ['Id', 'Motivo', 'Funcionario', 'Rest. Func', 'Horas']
        # Este For cria colunas ja com os nomes que foram inseridos acima
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
        # Retirar o Estilo Bold
        font_style = xlwt.XFStyle()
        # Pegar info do banco de dados(RegistroHoraExtra)
        registros = RegistroHoraExtra.objects.filter(utilizada=False)
        # comecar a ecsrever na coluna 1
        row_num = 1
        # passar os valores dos items do objeto(registros)
        for registro in registros:
            ws.write(row_num, 0, registro.id, font_style)
            ws.write(row_num, 1, registro.motivo, font_style)
            ws.write(row_num, 2, registro.funcionario.nome, font_style)
            ws.write(row_num, 3, registro.funcionario.total_hora_extra, font_style)
            ws.write(row_num, 4, registro.horas, font_style)
            row_num += 1
        # salvar
        wb.save(response)
        # retornar response
        return response



