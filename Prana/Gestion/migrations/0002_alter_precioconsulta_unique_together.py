# Generated by Django 4.1.7 on 2023-03-18 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='precioconsulta',
            unique_together={('medico', 'obra_social')},
        ),
    ]