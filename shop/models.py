from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, SlugField


class Category(models.Model):
    name = models.CharField(
        max_length=100, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)

    name = models.CharField(
        max_length=150, db_index=True, verbose_name='Название')
    slug = models.CharField(max_length=150, db_index=True,
                            unique=True, verbose_name='Ссылка')
    image = models.ImageField(
        upload_to='product/%Y/%m/%d', blank=True, verbose_name='Изображение')
    description = models.TextField(
        max_length=1000, blank=True, verbose_name='Описание')
    price = models.DecimalField(
        max_digits=10, decimal_places=0, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    uploaded = models.DateTimeField(auto_now=True, verbose_name='Загружено')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'))

    def __str__(self):
        return self.name
