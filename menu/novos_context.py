from .models import Regiao


def lista_regioes_recentes(request):
    lista_regioes=Regiao.objects.all().order_by('-data_criacao')[0:8]
    if lista_regioes:
        regiao_destaque = lista_regioes[0]
    else:
        regiao_destaque = None
    return {"lista_regioes_recentes": lista_regioes, "regiao_destaque": regiao_destaque}

def lista_regioes_em_alta(request):
    lista_regioes=Regiao.objects.all().order_by('-acessos')[0:8]
    return {"lista_regioes_em_alta": lista_regioes}

