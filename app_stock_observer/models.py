from django.db import models


class CourseJournal(models.Model):
    section = models.CharField(
        verbose_name='Название инструмента', 
        max_length=100, blank=True, null=True,
        help_text='''Название инструмента.<br>
        Для демострации была найдена API от tradingview.<br>
        Инструмент SI - это фьючерс на USD/RUB.<br>
        Производный инструмент от спот рынка - поэтому есть разница в котировках.
        '''
    )
    exchange_rate = models.DecimalField(
        verbose_name='Значение инструмента', 
        max_digits=15, decimal_places=5, default=0, 
        blank=True, null=True,
    )
    date_time = models.DateTimeField(
        verbose_name='Дата/Время', 
        auto_now_add=True,
    )


    class Meta:
        verbose_name = 'Валютный курс'
        verbose_name_plural = 'Журнал валютных курсов'


    def __str__(self) -> str:
        return self.section
