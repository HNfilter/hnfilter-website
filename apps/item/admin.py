from django.contrib import admin

from .models import Item, Vote

admin.site.register(Vote)
admin.site.register(Item)
