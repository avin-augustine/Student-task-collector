# Generated by Django 4.2.4 on 2023-08-08 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=45)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.course')),
                ('Days', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.days')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.course')),
                ('Days', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.days')),
            ],
        ),
    ]
