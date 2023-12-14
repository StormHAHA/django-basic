from django.db import models

class Room(models.Model):

    room_number = models.IntegerField('Номер комнаты')
    room_resident = models.CharField('Имя резидента', max_length=100)
    room_status = models.BooleanField("Занято", default=False)

    def __str__(self):
        return f'{self.room_number}, {self.room_status}'

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

