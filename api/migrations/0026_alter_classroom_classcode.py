# Generated by Django 4.0.3 on 2022-03-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_classroom_classcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='classCode',
            field=models.CharField(default='Classroom Code', max_length=6),
        ),
    ]
