from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as sistema

app_name = 'sistema'

urlpatterns = [
	path('', sistema.Home.as_view(), name = 'home'),
	path('login/', auth_views.LoginView.as_view(template_name='sistema/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('cadastro/', sistema.CriarUsuario.as_view(), name='cadastro'),
	path('adicionar-proposta/', sistema.AdicionarProposta.as_view(), name='adicionar-proposta'),
	path('proposta/<pk>', sistema.DetalhesProposta.as_view(), name='proposta'),
]
