from django.views import generic
from django.http import HttpResponse, JsonResponse
from investimentos.models import Acao


class IndexView(generic.TemplateView):
    template_name = 'investimentos/index.html'


def importar_preferencias(request):
    return HttpResponse(status=200)


def exportar_preferencias(request):
    return HttpResponse(status=200)


def buscar_acao(request):
    sigla = request.GET.get('sigla')
    acoes = []
    if sigla:
        acoes = Acao.objects.filter(sigla__icontains=sigla)

    return JsonResponse({'status': 200, 'data': [acao.sigla for acao in acoes]})
