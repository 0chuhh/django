
from django.db import models
from djangoapp import settings
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/images', null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.id} - {self.name}'


class Status(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    discount = models.IntegerField(null=True, )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return f'{self.id} - {self.product.name}'
