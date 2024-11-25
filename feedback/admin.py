from django.contrib import admin
from .models import Item, Feedback

# Register the models in the admin
admin.site.register(Item)
admin.site.register(Feedback)
