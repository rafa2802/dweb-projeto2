from django import forms

from . import models

class CadastrarProposta(forms.ModelForm):

	class Meta:
		model = models.Proposta
		fields = ('user', 'name', 'description')
		labels = {
			'user': 'Usuário',
    		'name': 'Nome da Proposta',
    		'description': 'Descrição',
    	}

class AdicionarUsuario(forms.ModelForm):
  
  class Meta:
    model = models.UUIDUser
    fields = ('first_name', 'last_name', 'username', 'email', 'password')
    labels = {
    	'first_name': 'Primeiro Nome',
    	'last_name': 'Sobrenome',
    	'username': 'Nome de Usuário',
    	'email': 'E-mail',
    	'password': 'Senha',
    }
    widgets = {
      'password': forms.PasswordInput()
    }
