import re

from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, RegexValidator


class Schedule(models.Model):
    name = models.CharField(
        'Заголовок',
        max_length=200,
        help_text='Введите заголовок мероприятия'
    )
    address = models.CharField(
        'Адрес',
        max_length=200,
        help_text='Введите адрес проведения'
    )
    date = models.DateTimeField(
        'Запланировано',
        default=timezone.now,
        help_text='Введите запланированную дату'
    )

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"

    def __str__(self):
        return self.name


class Feedback(models.Model):
    date = models.DateTimeField(
        'Дата создания',
        default=timezone.now,
        help_text='Введите дату создания'
    )
    description = models.TextField(
        'Отзыв',
        max_length=500,
        help_text='Напишите отзыв',
        validators=[
            MinLengthValidator(
                limit_value=10,
                message='Введите не менее 10 символов'
            )
        ]
    )
    name = models.CharField(
        'Автор',
        max_length=200,
        help_text='Введите своё Имя и Фамилию',
        validators=[
            RegexValidator(
                regex=r"^[a-zа-яё ,.'-]+$",
                message='Введите корректное значение',
                flags=re.I or re.U
            ),
            MinLengthValidator(
                limit_value=2,
                message='Введите не менее 2 символов'
            )
        ]
    )
    images = models.ImageField(
        'Фото',
        blank=True,
        upload_to='feedback_photo/%Y/%m/%d/',
        help_text='Ваша фотография'
    )

    class Meta:
        ordering = ['-date']
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.name


class Playbill(models.Model):
    name = models.CharField(
        'Наименование',
        max_length=200,
        help_text='Введите наименование мероприятия'
    )
    address = models.CharField(
        'Адрес',
        max_length=200,
        help_text='Введите адрес мероприятия'
    )
    date = models.DateTimeField(
        'Время проведения',
        help_text='Введите время проведения'
    )
    price = models.DecimalField(
        'Цена билета',
        max_digits=19,
        decimal_places=2,
        help_text='Укажите цену за билет'
    )

    class Meta:
        verbose_name = "Афиша"
        verbose_name_plural = "Афиши"

    def __str__(self):
        return self.name


class News(models.Model):
    date = models.DateTimeField(
        'Дата создания',
        help_text='Введите дату создания'
    )
    name = models.CharField(
        'Заголовок',
        max_length=200,
        help_text='Введите заголовок новости'
    )
    description = models.TextField(
        'Содержание',
        help_text='Введите текст новости'
    )
    video = models.URLField(
        'Видео',
        blank=True,
        help_text='Вставьте ссылку на видео'
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости студии"

    def __str__(self):
        return self.name


class NewsImage(models.Model):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(
        'Изображение',
        blank=True,
        upload_to='news_images/%Y/%m/%d/',
        help_text='Выберите изображение'
    )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return self.news.name


class People(models.Model):
    images = models.ImageField(
        'Фотография',
        upload_to='people_photo/%Y/%m/%d/',
        help_text='Выберите фотографию человека'
    )
    first_name = models.CharField(
        'Имя',
        max_length=200,
        help_text='Введите ваше имя'
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=200,
        help_text='Введите вашу фамилию'
    )
    description = models.CharField(
        'Описание',
        max_length=200,
        help_text='Напишите роль в проекте'
    )

    class Meta:
        verbose_name = "Люди"
        verbose_name_plural = "Люди"

    def __str__(self):
        return self.last_name


class Companies(models.Model):
    images = models.ImageField(
        'Логотип',
        upload_to='company_logo/%Y/%m/%d/',
        help_text='Выберете логотип'
    )
    name = models.CharField(
        'Наименование',
        max_length=200,
        help_text='Укажите наименование компании'
    )
    description = models.CharField(
        'Описание',
        max_length=200,
        help_text='Опишите, чем помогла компания'
    )

    class Meta:
        verbose_name = "Компании"
        verbose_name_plural = "Компании"

    def __str__(self):
        return self.name
