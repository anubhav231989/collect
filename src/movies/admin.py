from django.contrib import admin
from .models import Actor,Cast,Movie

# Register your models here.
class CastInline(admin.TabularInline):
    model = Cast

class MovieAdmin(admin.ModelAdmin):
    inlines = (CastInline,)

admin.site.register(Actor)
admin.site.register(Movie, MovieAdmin)
#admin.site.register(Cast)