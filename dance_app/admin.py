from django.contrib import admin
from .models import DanceGenre, DanceClass

# Register your models here.
admin.site.register(DanceGenre)
admin.site.register(DanceClass)