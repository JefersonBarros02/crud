# Generated by Django 3.0 on 2019-12-11 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='usuario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.Usuario'),
        ),
    ]
