# Generated by Django 4.2 on 2024-10-23 11:54

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
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(default='дома', max_length=200, verbose_name='Место привычки')),
                ('habit_time', models.DateTimeField(verbose_name='Следующая дата и время выполнения привычки')),
                ('action', models.CharField(max_length=200, verbose_name='Действие')),
                ('is_nice', models.BooleanField(default=False, verbose_name='Приятная привычка')),
                ('period', models.PositiveIntegerField(verbose_name='Частота выполнения привычки')),
                ('present', models.CharField(blank=True, max_length=200, null=True, verbose_name='Вознаграждение')),
                ('complete_time', models.DurationField(verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(default=True, verbose_name='Публичная привычка')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='Связанная привычка')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Обладатель привычки')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
