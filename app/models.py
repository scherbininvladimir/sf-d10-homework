from django.db import models

class Car(models.Model):
    MANUAL = 1
    AUTOMATIC = 2
    ROBOT = 3
    TRANSMISSON_CHOICES = [
        (MANUAL, "Механическая коробка передач"),
        (AUTOMATIC, "Автоматическая коробка передач"),
        (ROBOT, "Робот"),
    ]
    manufacturer = models.CharField("Производитель", max_length=50)
    model = models.CharField("Модель", max_length=50)
    year = models.IntegerField("Год выпуска")
    transmission = models.IntegerField("Коробка передач", choices=TRANSMISSON_CHOICES)
    color = models.CharField("Цвет", max_length=50)

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"