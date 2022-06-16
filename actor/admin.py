from django.contrib import admin
from .models import Actor, Zodic, Surname

class ActorAdmin(admin.ModelAdmin):
    list_display = ['actor_name', 'zodic_sign', 'drama_name', 'date']
    list_filter = ['actor_name', 'zodic_sign', 'drama_name', 'surname']

admin.site.register(Actor,ActorAdmin)
admin.site.register(Zodic)
admin.site.register(Surname)
