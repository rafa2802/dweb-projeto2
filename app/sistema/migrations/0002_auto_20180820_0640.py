# Generated by Django 2.1 on 2018-08-20 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('comentario', models.TextField(verbose_name='Comentário')),
            ],
            options={
                'verbose_name': 'comentário',
                'verbose_name_plural': 'comentários',
            },
        ),
        migrations.CreateModel(
            name='Proposta',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('description', models.TextField(verbose_name='descrição')),
                ('favor', models.IntegerField(default=0, verbose_name='favor')),
                ('contra', models.IntegerField(default=0, verbose_name='contra')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='criação')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'lei',
                'verbose_name_plural': 'leis',
            },
        ),
        migrations.AddField(
            model_name='comentario',
            name='lei',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leis', to='sistema.Proposta', verbose_name='Lei'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
