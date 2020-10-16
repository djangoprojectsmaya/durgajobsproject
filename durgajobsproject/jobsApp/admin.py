from django.contrib import admin
from .models import hydjobs,bngjobs,chnnjobs,punejobs

# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

class bngjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

class chnnjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

class punejobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']


admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(bngjobs,bngjobsAdmin)
admin.site.register(chnnjobs,chnnjobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
