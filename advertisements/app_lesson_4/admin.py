from django.contrib import admin

from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display=['id','title','description','price', 'created_at','updated_at','auction']
    list_filter=['auction', 'created_at']
    actions=['make_auction_as_false', 'make_auction_as_true']
    
    fieldsets =(
        (
            'общее',{
            'fields':('title','description')
            }
        ),
        
        (
            'финансы',{
            'fields':('price','auction')
            'classes':['collapse']
            }
        ),
    )
    
    
    
    @admin.action(disription="убрать возможность торга")
    def make_auction_as_false(selfm,request, queryset):
        queryset.update(auction=False)
    @admin.action(disription="добавить возможность торга")
    def make_auction_as_true(selfm,request, queryset):
        queryset.update(auction=True)
admin.site.register(Advertisement, AdvertisementAdmin)


class AdvertisementAdmin(admin.ModelAdmin):
    def get_updated_display(self, obj):
        if obj.updated_at.date() == datetime.now().date():
            return f"<span style='color: {your_color};'>Сегодня в {obj.updated_at.time()}</span>"
        else:
            return super().get_updated_display(obj)

admin.site.register(Advertisement, AdvertisementAdmin)
