# Generated by Django 4.1.7 on 2023-04-24 13:36

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('biografia', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=250)),
                ('slug', models.SlugField(default=0, unique=True)),
                ('subtitulo', models.CharField(max_length=250)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('imagen', models.ImageField(upload_to='blog')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('num_visitas', models.PositiveIntegerField(default=0)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='blog.autor')),
            ],
            options={
                'verbose_name': 'noticia',
                'verbose_name_plural': 'noticias',
                'ordering': ['-fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('slug', models.SlugField(default=0, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('aprobado', models.BooleanField(default=False)),
                ('blog', models.ManyToManyField(related_name='comentarios', to='blog.blog')),
                ('perfil', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.perfil')),
            ],
            options={
                'ordering': ['fecha_creacion'],
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='categorias',
            field=models.ManyToManyField(related_name='categorias', to='blog.categoria'),
        ),
    ]
