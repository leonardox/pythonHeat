# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
    user = models.CharField(max_length=50)
    docfile = models.FileField(upload_to='documents/')
