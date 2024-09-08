from django.contrib import admin

# Register your models here.
import main.models as m
admin.site.register(m.UserID)
admin.site.register(m.ImportFile)
admin.site.register(m.ExportFile)