# Generated by Django 3.2.4 on 2021-08-04 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_receitas_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='receitas',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]
