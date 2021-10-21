from django.db import models
from django.urls import reverse

# Create your models here.
class News(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    content = models.TextField('контент', blank=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('отредактирована', auto_now=True)
    photo = models.ImageField('фото', upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField('опубликована', default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True,verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']