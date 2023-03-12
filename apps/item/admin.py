from django.contrib import admin

from .models import Item, Vote, Comment

admin.site.register(Comment)
admin.site.register(Vote)
admin.site.register(Item)
