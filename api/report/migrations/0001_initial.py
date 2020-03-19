# Generated by Django 3.0.4 on 2020-03-19 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.PositiveSmallIntegerField(choices=[(11, 'Rondônia'), (12, 'Acre'), (13, 'Amazonas'), (14, 'Roraima'), (15, 'Pará'), (16, 'Amapá'), (17, 'Tocantins'), (21, 'Maranhão'), (22, 'Piauí'), (23, 'Ceará'), (24, 'Rio Grande do Norte'), (25, 'Paraíba'), (26, 'Pernambuco'), (27, 'Alagoas'), (28, 'Sergipe'), (29, 'Bahia'), (31, 'Minas Gerais'), (32, 'Espírito Santo'), (33, 'Rio de Janeiro'), (35, 'São Paulo'), (41, 'Paraná'), (42, 'Santa Catarina'), (43, 'Rio Grande do Sul'), (50, 'Mato Grosso do Sul'), (51, 'Mato Grosso'), (52, 'Goiás'), (53, 'Distrito Federal')])),
                ('suspects', models.PositiveSmallIntegerField(default=0)),
                ('refuses', models.PositiveSmallIntegerField(default=0)),
                ('cases', models.PositiveSmallIntegerField(default=0)),
                ('deaths', models.PositiveSmallIntegerField(default=0)),
                ('recovered', models.PositiveIntegerField(default=0)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Report')),
            ],
            options={
                'verbose_name': 'Caso',
                'ordering': ['report', 'state'],
            },
        ),
    ]