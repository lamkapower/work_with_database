from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Phone(models.Model):
    name = models.CharField(u'Название', max_length=100)
    image = models.CharField(u'Ссылка на изображение', max_length=300)
    price = models.IntegerField(u'Стоимость')
    release_date = models.DateField(u'Дата публикации')
    lte_exists = models.BooleanField(u'LTE')
    slug = models.SlugField(u'ЧПУ')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-price"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})
