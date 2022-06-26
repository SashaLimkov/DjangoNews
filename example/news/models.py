from django.db import models


# Create your models here.
class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")


class News(TimeBasedModel):
    title = models.CharField(max_length=150, verbose_name="Наименование")
    content = models.TextField(blank=True, verbose_name="Контент")
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True
    )
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        null=True,
        verbose_name="Категория"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at", "title"]


class Category(models.Model):
    title = models.CharField(
        max_length=150, db_index=True, verbose_name="Наименование категории"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]
