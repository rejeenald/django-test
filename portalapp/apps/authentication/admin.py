# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from authentication import models

# Register your models here.
admin.site.register(models.TenantUser)
