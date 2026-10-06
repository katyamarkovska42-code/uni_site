from django.db import models


class HomePage(models.Model):
    title = models.CharField("Назва факультету", max_length=200)
    description = models.TextField("Опис")
    contacts = models.TextField("Контакти")

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField("Назва", max_length=100)
    head = models.CharField("Завідувач кафедри", max_length=100)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField("Назва", max_length=200)
    code = models.CharField("Код", max_length=10)
    description = models.TextField("Опис")
    coordinator_name = models.CharField("Координатор набору", max_length=100)
    coordinator_contact = models.CharField("Контакт координатора", max_length=50)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="programs",
        verbose_name="Випускова кафедра",
    )
    subjects = models.TextField("Дисципліни", blank=True)

    def __str__(self):
        return f"{self.code} {self.name}"


class Teacher(models.Model):
    name = models.CharField("Ім'я", max_length=100)
    position = models.CharField("Посада", max_length=100)
    degree = models.CharField("Науковий ступінь", max_length=100, blank=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="teachers",
        verbose_name="Кафедра",
    )

    def __str__(self):
        return self.name
