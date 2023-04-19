from django.contrib import admin
from .models import Shoppinglist, UserList, Mallist, Item

admin.site.register(Shoppinglist)
admin.site.register(UserList)
admin.site.register(Mallist)
admin.site.register(Item)
