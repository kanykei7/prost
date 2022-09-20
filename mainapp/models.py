from django.db import models


class School(models.Model):
    director: str = models.CharField(max_length=100, verbose_name='Директор:')
    zauchi: str = models.CharField(max_length=100, verbose_name='Заучи:')
    teacher: str = models.CharField(max_length=100, verbose_name='Учитель:')
    clas: str = models.CharField(max_length=100, verbose_name='Класс:')
    student: str = models.CharField(max_length=100, verbose_name='Ученик:')
    lesson: str = models.CharField(max_length=100, verbose_name='Урок:')

    def __str__(self):
        return


class Student(models.Model):
    full_name: str = models.CharField(max_length=200, verbose_name='Ф.И.О.')
    grade: int = models.IntegerField()
    parents_phone: str = models.CharField(max_length=300, verbose_name='Номер родителей')
    address: str = models.CharField(max_length=127, verbose_name='Адрекс')
    photo_of_student = models.ImageField(upload_to='students_avatars')

    def __str__(self):
        return


class Director(models.Model):
    full_name = models.CharField(max_length=127, verbose_name='Ф.И.О.')
    photo_of_director = models.ImageField(upload_to='directors_avatars')
    phone = models.IntegerField()

    def __str__(self):
        return


class Zauch(models.Model):
    full_name = models.CharField(max_length=127, verbose_name='Ф.И.О.')
    photo_of_zauch = models.ImageField(upload_to='directors_avatars')
    phone = models.IntegerField()

    def __str__(self):
        return


class Teacher(models.Model):
    full_name = models.CharField(max_length=127, verbose_name='Ф.И.О.')
    address: str = models.CharField(max_length=127, verbose_name='Адрекс')
    phone = models.IntegerField()
    photo_of_teacher = models.ImageField(upload_to='teachers_avatars')

    def __str__(self):
        return


class Lesson(models.Model):
    lesson_name: str = models.CharField(max_length=127, verbose_name='Название урока')
    teacher: str = models.CharField(max_length=127, verbose_name='Учитель')

    def __str__(self):
        return


class Clas(models.Model):
    word_of_class: str = models.CharField(max_length=1, verbose_name='Буква класса')
    number_of_class: str = models.IntegerField()
    class_teacher: str = models.CharField(max_length=127, verbose_name='Классная руководительница')

    def __str__(self):
        return
