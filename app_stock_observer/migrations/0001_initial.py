# Generated by Django 5.0.1 on 2024-01-25 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseJournal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(blank=True, help_text='Название инструмента.<br>\n        Для демострации была найдена API от tradingview.<br>\n        Инструмент SI - это фьючерс на USD/RUB.<br>\n        Производный инструмент от спот рынка - поэтому есть разница в котировках.\n        ', max_length=100, null=True, verbose_name='Название инструмента')),
                ('exchange_rate', models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=15, null=True, verbose_name='Значение инструмента')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата/Время')),
            ],
            options={
                'verbose_name': 'Валютный курс',
                'verbose_name_plural': 'Журнал валютных курсов',
            },
        ),
    ]
