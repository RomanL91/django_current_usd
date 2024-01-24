from django.db import models


class CourseJournal(models.Model):
    section = models.CharField(
        verbose_name='Секция/валютная пара', 
        max_length=10, blank=True, null=True,
        help_text='''Данное поле показывает из какой секции торгов<br>
        была произведена запись. Другими словами, можно воспринимать как<br>
        название инструмента (валютной пары).
        '''
    )
    spread = models.DecimalField(
        verbose_name='Спред', 
        max_digits=15, decimal_places=5, default=0, 
        blank=True, null=True,
        help_text='''Разность между лучшими ценами заявок на продажу (аск) и на покупку (бид)<br>
        в один и тот же момент времени на какой-либо актив.
        '''
    )
    bid = models.DecimalField(
        verbose_name='Бид', 
        max_digits=15, decimal_places=5, default=0, 
        blank=True, null=True,
        help_text='''Цена спроса, наивысшая цена покупателя, по которой он согласен купить.
        '''
    )
    ask = models.DecimalField(
        verbose_name='Аск', 
        max_digits=15, decimal_places=5, default=0, 
        blank=True, null=True,
        help_text='''Цена, по которой продавец согласен продать.
        '''
    )


    class Meta:
        verbose_name = 'Валютный курс'
        verbose_name_plural = 'Журнал валютных курсов'


    def __str__(self) -> str:
        return self.section
