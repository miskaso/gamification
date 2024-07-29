from django.contrib import admin
from .models import AboutMe, Projects, Media, Contact, VisitedPage

# Register your models here.

admin.site.register(AboutMe)
admin.site.register(Projects)
admin.site.register(Media)
admin.site.register(Contact)
admin.site.register(VisitedPage)