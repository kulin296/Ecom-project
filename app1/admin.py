from django.contrib import admin

from app1.models import *
# Register your models here.

admin.site.register(Category)


class userregister(admin.ModelAdmin):
    list_display=['name','email','phone']
admin.site.register(Userregister,userregister)

class productregister(admin.ModelAdmin):
    list_display=['name','price','description']
admin.site.register(Product,productregister)

class contactdisplay(admin.ModelAdmin):
    list_display=['name','email','phone']
admin.site.register(Contactus,contactdisplay)

admin.site.register(Ordermodel)