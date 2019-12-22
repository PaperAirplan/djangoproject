from django.db import models


# from django.contrib.postgres.fields import JSONField


class Booklist(models.Model):
    position = models.AutoField(primary_key=True)
    name_ru = models.CharField(max_length=255)
    name_eng = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    publication_date = models.CharField(max_length=10)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.name_ru
