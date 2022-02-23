# Generated by Django 4.0.2 on 2022-02-23 16:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('deadline', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('score', models.BooleanField(choices=[(0, 'Ungraded'), ('1', '1 - Very Poor'), ('2', '2 - Below Average'), ('3', '3 - Average'), ('4', '4 - Good'), ('5', '5 - Excellent')], default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.classroom')),
                ('students', models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(choices=[(True, 'Completed'), (False, 'Incomplete')], default=False)),
                ('assignment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.assignment')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.classroom'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
