import io

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from reportlab.pdfgen import canvas

from . models import Funcionario

# PDF via Html.

# Usar pare fazer o carregamento do template
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa


class ListFuncionario(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class EditFuncionario(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamento']


class DeleteFuncionario(DeleteView):
    model = Funcionario

    def get_success_url(self):
        return reverse_lazy('list_funcionario')


class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ['nome', 'departamento']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioNovo, self).form_valid(form)


def pdf_reportlab(request):
    # constroe a requisicao
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=" mypdf.pdf"'
    #               ||          Faz baixar o arquivo (download) ao invés de abrir em nova aba ou janela

    # constroe o arquivo
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(10, 810, 'Hello, World!')

    palavras = ['palavra 1', 'palavra 2', 'palavra 3']

    y = 790
    for palavra in palavras:
        p.drawString(10, y , palavra)
        y -= 40

    # injeta o arquivo dentro da response
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    # e envia a response
    return response


# Classe criada para criacao de relatorio. Assim nao precisa sempre repetir
# a escrita do codigo abaixo
class Render:
    # com staticmethod nao eh preciso instanciar um objeto render para utilizar
    @staticmethod
    # render vai receber o path do template, os parametros que euq euro contextualizar e o nore do arquivo.
    def render(path: str, params: dict, filename: str):
        # 1o. carrega o template, depois renderizo o html utilizando os parametros(variaveis, querysets, listas, dicionarios)
        # crio a response, cria o objeto pdf com encode UTF8, e passo a response como parametro. O objeto pdf vai conter o
        # objeto pdf em si que eu quero estar renderizando
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            # Se nao constar nenhum erro, iniciar a response. Cria o Httpreponse, faz o getvalues, seto o content type para pdf
            # e no percent s (% s) passo o nome do relatorio
            response = HttpResponse(
                response.getvalue(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error rendering PDF", status=400)


class Pdf(View):
    # Essa def vai responder o metodo get. Criar a lista de parametros(pode passar variaveis, querysets, requests.
    #
    def get(self, request):
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel sales',
            'request': request,
        }
        return Render.render('funcionario/relatorio.html', params, 'myfile')
        # retorno o moetodo render(staticmethod) e passar o tejmplate que voce
        # quer renderizar.
        # Criar o arquivo relatorio .html em funcionarios
