# Generated by Django 4.1.7 on 2023-06-03 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercises_number_one', models.TextField()),
                ('exercises_number_two', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EyeExercises',
            fields=[
                ('exercises_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fitnes.exercises')),
            ],
            bases=('fitnes.exercises',),
        ),
        migrations.CreateModel(
            name='HandExercises',
            fields=[
                ('exercises_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fitnes.exercises')),
            ],
            bases=('fitnes.exercises',),
        ),
        migrations.CreateModel(
            name='NeckExercises',
            fields=[
                ('exercises_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fitnes.exercises')),
            ],
            bases=('fitnes.exercises',),
        ),
    ]
