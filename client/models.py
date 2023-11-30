from django.db import models


class Bid(models.Model):
    '''данные о клиенте, который оставил заявку'''
    number = models.CharField('Номер телефона', max_length=12, )
    name = models.CharField('Имя клиента', max_length=50)
    descr = models.CharField('Описание проблемы', max_length=100, default="Проблема не описана.")
    date = models.DateField('Дата подачи заявки')

    def __str__(self):
        return f'{self.id}, {self.name}, {self. date}'

    def save(self, **kwargs):
        super(Bid, self).save(**kwargs)
        bidstate = BidState(BidID=self)
        bidstate.save()

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class BidState(models.Model):
    STATE = [
        ("А", "Активная"),
        ("Н", "Необработанная"),
        ("З", "Завершенная"),
    ]
    BidID = models.ForeignKey(Bid, on_delete=models.CASCADE)
    state = models.CharField('Состояние', max_length=1, choices=STATE, default="Н")

    def __str__(self):
        return f'{self.BidID}, {self. state}'

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния'
