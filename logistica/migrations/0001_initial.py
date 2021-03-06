# Generated by Django 3.2.12 on 2022-02-14 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_da_consulta', models.DateField()),
                ('hospital', models.CharField(max_length=50)),
                ('horario_da_consulta', models.CharField(max_length=20)),
                ('acompanhante', models.CharField(max_length=200)),
                ('local_de_espera', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('rg', models.CharField(max_length=10)),
                ('cpf', models.CharField(max_length=12)),
                ('data_de_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=150)),
                ('rg', models.CharField(max_length=10)),
                ('cpf', models.CharField(max_length=12)),
                ('cns', models.CharField(max_length=20)),
                ('data_de_nascimento', models.DateField(blank=True, null=True)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_da_viagem', models.DateField()),
                ('horario_de_saida', models.CharField(max_length=20)),
                ('consultas', models.ManyToManyField(help_text='Selecione as consultas que iram nessa viagem.', to='logistica.Consulta')),
                ('motorista', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='logistica.motorista')),
            ],
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='logistica.paciente'),
        ),
    ]
