# Generated by Django 4.1.4 on 2022-12-06 13:55

from django.db import migrations, models
import django.db.models.deletion
import organizador.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('cnpj', models.CharField(max_length=14, validators=[organizador.models.is_cnpj_valido])),
            ],
        ),
        migrations.CreateModel(
            name='Condicionante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('numero', models.PositiveSmallIntegerField(default=1)),
                ('data_de_entrega', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequencia', models.IntegerField(choices=[(1, 'Diario'), (2, 'Semanal'), (3, 'Quinzenal'), (4, 'Mensal'), (5, 'Bimestral'), (6, 'Trimestral'), (7, 'Semestral'), (8, 'Anual')])),
                ('parametro', models.CharField(max_length=20)),
                ('condicionante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizador.condicionante')),
            ],
        ),
        migrations.CreateModel(
            name='Licenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20)),
                ('observacao', models.CharField(max_length=120)),
                ('data_de_emissao', models.DateField()),
                ('data_de_entrega', models.DateField()),
                ('arquivo_licenca', models.FileField(upload_to='licencas')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizador.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='condicionante',
            name='licenca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizador.licenca'),
        ),
    ]
