"""
create your models here
"""

from django.db.models import (
    Model,
    CharField,
    TextField,
    DateTimeField,
    ForeignKey,
    ManyToManyField,
    ImageField,
    PositiveIntegerField,
    BooleanField,
    DecimalField,
    SET_NULL,
    PositiveSmallIntegerField,
    CASCADE,
)
from django.core.validators import MinValueValidator, MaxValueValidator


class Order(Model):
    """
    Order
    """

    STATUS_CHOICES = {
        "new": "новая",
        "confirmed": "подтвержденная",
        "cancelled": "отмененная",
        "completed": "выполненная",
    }

    client_name: CharField = CharField(max_length=100, verbose_name="Имя клиента")

    phone: CharField = CharField(max_length=20, verbose_name="Телефон")

    comment: TextField = TextField(blank=True, verbose_name="Комментарий")

    status: CharField = CharField(
        max_length=50, choices=STATUS_CHOICES, default="new", verbose_name="Статус"
    )

    date_created: DateTimeField = DateTimeField(auto_now_add=True, verbose_name="Создано")

    date_updated: DateTimeField = DateTimeField(auto_now=True, verbose_name="Обновлено")

    master: ForeignKey = ForeignKey(
        "Master", on_delete=SET_NULL, null=True, blank=True, verbose_name="Мастер"
    )

    services: ManyToManyField = ManyToManyField(
        "Service", related_name="orders", verbose_name="Услуги"
    )

    appointment_date: DateTimeField = DateTimeField(verbose_name="Дата и время записи")


class Master(Model):
    """
    Master
    """

    name: CharField = CharField(max_length=150, verbose_name="Имя")

    bio: TextField = TextField(blank=True, verbose_name="О себе")

    photo: ImageField = ImageField(upload_to="masters/", blank=True, verbose_name="Фотография")

    experience: PositiveIntegerField = PositiveIntegerField(
        verbose_name="Стаж работы", help_text="Опыт работы в годах"
    )

    services: ManyToManyField = ManyToManyField(
        "Service", related_name="masters", verbose_name="Услуги"
    )

    is_active: BooleanField = BooleanField(default=True, verbose_name="Активен")


class Service(Model):
    """
    Service
    """

    name: CharField = CharField(max_length=200, verbose_name="Название")

    description: TextField = TextField(blank=True, verbose_name="Описание")

    price: DecimalField = DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    duration: PositiveIntegerField = PositiveIntegerField(
        verbose_name="Длительность", help_text="Время выполнения в минутах"
    )

    is_popular: BooleanField = BooleanField(default=False, verbose_name="Популярная услуга")

    image: ImageField = ImageField(upload_to="services/", blank=True, verbose_name="Изображение")


class Review(Model):
    """
    Review
    """

    text: TextField = TextField(verbose_name="Текст отзыва")

    client_name: CharField = CharField(max_length=100, blank=True, verbose_name="Имя клиента")

    master: ForeignKey = ForeignKey("Master", on_delete=CASCADE, verbose_name="Мастер")

    photo: ImageField = ImageField(
        upload_to="reviews/", blank=True, null=True, verbose_name="Фотография"
    )
    created_at: DateTimeField = DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    rating: PositiveSmallIntegerField = PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Оценка"
    )
    is_published: BooleanField = BooleanField(default=True, verbose_name="Опубликован")


class DecorImages(Model):
    """
    Images which is just part of layout should be stored somewhere too
    """

    image: ImageField = ImageField(
        upload_to="decor/", blank=True, null=True, verbose_name="Фотография"
    )

    def __str__(self):
        return self.image.name
