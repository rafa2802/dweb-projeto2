from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid

class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, blank=True, related_name="uuiduser_set", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

# CreateUpdateModel
# - - - - - - - - - - - - - - - - - - -
class CreateUpdateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        abstract = True

class Proposta(CreateUpdateModel):
	user = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, verbose_name='usuario', related_name='users')
	name = models.CharField(max_length = 255, verbose_name = 'nome')
	description = models.TextField(verbose_name = 'descrição') 
	favor = models.IntegerField(default = 0, verbose_name = 'favor')
	contra = models.IntegerField(default = 0, verbose_name = 'contra')
	criado = models.DateTimeField(auto_now_add = True, verbose_name = 'criação')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'proposta'
		verbose_name_plural = 'propostas'

class Comentario(CreateUpdateModel):
	usuario = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='user', verbose_name='usuário')
	proposta = models.ForeignKey(Proposta, on_delete=models.CASCADE, related_name='propostas', verbose_name='proposta')
	comentario = models.TextField(verbose_name='comentário')

	def __str__(self):
		return self.comentario

	class Meta:
		verbose_name = 'comentário'
		verbose_name_plural = 'comentários'

