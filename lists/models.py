from django.db import models


class List(models.Model):
    text = models.TextField(default="")


class Item(models.Model):
    text = models.TextField(default="")
    list = models.ForeignKey(
        List, default=None, on_delete=models.SET_NULL, null=True
    )
