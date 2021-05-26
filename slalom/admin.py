from django.contrib import admin
from .models import Level, Trick, Done
from django.contrib import admin
from embed_video.admin import AdminVideoMixin





admin.site.register(Level)
admin.site.register(Trick)

admin.site.register(Done)
# Register your models here.
