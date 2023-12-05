from django.urls import path, reverse_lazy
from .views import Homepage, HomeRegioes, DetalhesRegiao, PesquisaRegiao, Paginaperfil, Criarconta
from django.contrib.auth import views as auth_view

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('regioes/', HomeRegioes.as_view(), name='homeregioes'),
    path('regioes/<int:pk>', DetalhesRegiao.as_view(), name='detalhesregiao'),
    path('pesquisa/', PesquisaRegiao.as_view(), name='pesquisaregiao'),
    path('login/', auth_view.LoginView.as_view(template_name='Login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='Logout.html'), name='logout'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html', success_url=reverse_lazy('menu:homeregioes')), name='mudarsenha'),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name="criarconta"),
]
