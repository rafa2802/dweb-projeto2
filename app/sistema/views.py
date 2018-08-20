from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import *
from .forms import *

class Home(ListView):
	model = Proposta
	template_name = 'sistema/base.html'

class AdicionarProposta(CreateView):
	model = Proposta
	template_name = 'sistema/adicionar.html'
	success_url = reverse_lazy('sistema:home')
	form_class = CadastrarProposta

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.save()
		return super(AdicionarProposta, self).form_valid(form)

class CriarUsuario(CreateView):
    model = UUIDUser
    template_name = 'sistema/cadastrar-usuario.html'
    success_url = reverse_lazy('sistema:home')
    form_class = AdicionarUsuario

    def form_valid(self, form):
    	obj = form.save(commit=False)
    	obj.set_password(obj.password)
    	obj.save()
    	return super(CriarUsuario, self).form_valid(form)

class DetalhesProposta(DetailView):
	model = Proposta
	template_name = 'sistema/proposta.html'
