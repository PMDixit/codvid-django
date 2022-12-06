# Generated by Django 4.0 on 2022-01-06 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covidmgmt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recptionalist',
            fields=[
                ('r_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Treats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covidmgmt.doctor')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covidmgmt.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covidmgmt.patient')),
                ('symptom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covidmgmt.symptom')),
            ],
        ),
        migrations.CreateModel(
            name='Prescribed_to',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covidmgmt.medicine')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covidmgmt.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Avails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covidmgmt.patient')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covidmgmt.service')),
            ],
        ),
    ]
