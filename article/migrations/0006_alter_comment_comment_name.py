# Generated by Django 5.0.7 on 2024-08-05 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_alter_comment_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_name',
            field=models.CharField(max_length=40, verbose_name='Name'),
        ),
    ]
