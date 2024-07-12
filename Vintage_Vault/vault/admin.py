from django.contrib import admin
from .models import *


# Register your models here.
class showuser(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'date_joined')
    list_per_page = 2


admin.site.register(User, showuser)


class showcountry(admin.ModelAdmin):
    list_display = ('c_name',)
    list_per_page = 2


admin.site.register(Country, showcountry)


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('s_name', 'country')
    list_per_page = 2


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'state')
    list_per_page = 2


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'address', 'phone_no', 'image')
    list_per_page = 2


@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name',)
    list_per_page = 2


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'user', 'category', 'price', 'condition', 'upload_date', 'i_image')
    list_per_page = 2


@admin.register(ProductCart)
class ProductCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'price', 'quantity', 'order_id', 'order_status')
    list_per_page = 2
    list_filter = ['item', 'price', 'order_id']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity', 'total_price', 'order_date', 'shipping_address',
                    'delivery_date', 'status')
    list_per_page = 2


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'order', 'amount', 'payment_mode', 'payment_status', 'payment_date')
    list_per_page = 2


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'rating', 'comment', 'review_date')
    list_per_page = 2
    list_filter = ['rating',]


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('cu_name', 'email', 'subject', 'phone', 'created_at')
    list_per_page = 2
    list_filter = ['subject', ]
