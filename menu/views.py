from django.shortcuts import redirect, reverse
from .models import Regiao, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('menu:homeregioes')
        else:
            return super().get(self, request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('menu:login')
        else:
            return reverse('menu:criarconta')

class HomeRegioes(LoginRequiredMixin, ListView):
    template_name = "homeregioes.html"
    model = Regiao

class DetalhesRegiao(LoginRequiredMixin, DetailView):
    template_name = "detalhesregiao.html"
    model = Regiao
    # object -> 1 item do modelo

    def get_context_data(self, **kwargs):
        # Esta linha garante que o método get_context_data continue a executar suas funcionalidades
        context = super(DetalhesRegiao, self).get_context_data(**kwargs)
        regioes_relacionadas = Regiao.objects.filter(macro_regiao=self.get_object().macro_regiao).exclude(categoria=self.get_object().categoria)[0:5]
        context['regioes_relacionadas'] = regioes_relacionadas
        return context

    def get(self, request, *args, **kwargs):
        # Para descobrir qual Regiao o usuário está acessando, usa-se o método get_object()
        Regiao = self.get_object()
        # Somar uma unidade às acessos desta Regiao
        Regiao.acessos += 1
        # Salvar modificações feitas no banco de dados
        Regiao.save()
        # Resgatando o usuário que acesso um determinado Regiao
        usuario = request.user
        # Adicionando o Regiao acessado à lista de regioes visto
        # por um determinado usuário
        usuario.regioes_vistas.add(Regiao)
        # Redireciona o usuário à URL do Regiao desejado, ou seja, um Regiao na página detalhesRegiao.html
        return super().get(self, request, *args, **kwargs)

class PesquisaRegiao(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Regiao

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = Regiao.objects.filter(nome_regiao__icontains=termo_pesquisa)
            return object_list
        else:
            return None

class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('menu:homeregioes')

class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('menu:login')