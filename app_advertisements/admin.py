from django.contrib import admin
import .models import Advertisement
# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','price','created_date','auction']
    list_filter= ['auction','price','created_data','id']
    auction=['make_auction_as_false','make_auction_as_true']

    @admin.action(description="Убрать возможность торга ")
    def make_auction_as_false (self,request,queryset):
        queryset.update(auction=False)

    @admin.action(description="Добавить возможность торга ")
    def make_auction_as_true (self,request,queryset):
        queryset.update(auction=True)
    
    fieldsets=(
        ("Общее",{'fields':('title','description')}),
        ("Финансы",{'fields':('auction','price'),'classes':['collapse']})
    )


admin.site.register(Advertisement,AdvertisementAdmin)
    
