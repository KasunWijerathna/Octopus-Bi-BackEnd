# Generated by Django 4.2.6 on 2023-10-18 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_app', '0003_alter_assessmentarea_name_alter_awards_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
