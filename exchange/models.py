from django.db import models
from django.utils import timezone


class ExchangeProgram(models.Model):
    university = models.CharField("Університет", max_length=200)
    country = models.CharField("Країна", max_length=100, default="") # дозволили полю бути порожнім
    languages = models.CharField("Мови навчання", max_length=200)
    seats = models.PositiveSmallIntegerField("Кількість місць")
    deadline = models.DateField("Дедлайн подачі")
    description = models.TextField("Опис")

    def __str__(self):
        return self.university

    @property
    def is_open(self):
        return self.deadline >= timezone.localdate()