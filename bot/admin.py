from django import forms
from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html

from .models import Car, CarImage, Search, TgUser, Region, District


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'post', 'seen_count',
                    'likes_count', 'dislikes_count', 'created_at')
    list_filter = ('post', 'model', 'year')
    readonly_fields = ('created_at', 'seen_count',
                       'likes_count', 'dislikes_count', 'owner', 'description', 'year', 'price', 'model', 'name', 'contact_number', 'complate')
    ordering = ('-created_at', 'name')
    actions = ['mark_as_posted', 'mark_as_not_posted']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(seen_count=Count('seen'))
        queryset = queryset.annotate(likes_count=Count('likes'))
        queryset = queryset.annotate(dislikes_count=Count('dislikes'))
        return queryset

    def seen_count(self, obj):
        return obj.seen.count()
    seen_count.admin_order_field = 'seen_count'
    seen_count.short_description = 'Seen Count'

    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.admin_order_field = 'likes_count'
    likes_count.short_description = 'Likes Count'

    def dislikes_count(self, obj):
        return obj.dislikes.count()
    dislikes_count.admin_order_field = 'dislikes_count'
    dislikes_count.short_description = 'Dislikes Count'

    def mark_as_posted(self, request, queryset):
        rows_updated = queryset.update(post=True)
        self.message_user(request, f"{rows_updated} car(s) marked as posted.")
    mark_as_posted.short_description = "Mark selected cars as posted"

    def mark_as_not_posted(self, request, queryset):
        rows_updated = queryset.update(post=False)
        self.message_user(
            request, f"{rows_updated} car(s) marked as not posted.")
    mark_as_not_posted.short_description = "Mark selected cars as not posted"

    change_form_template = 'admin/car_change_form.html'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['car'] = self.get_object(request, object_id)
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    fieldsets = (
        ('General Infos', {
            'fields': ('owner', 'name', 'model', 'year', 'price')
        }),
        ('Additional Details', {
            'fields': ('description', 'contact_number', 'created_at')
        }),
        ('Status', {
            'fields': ('complate', 'post', 'seen_count', 'likes_count', 'dislikes_count')
        })
    )


@admin.register(TgUser)
class TgUserAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'phone', 'car_count', 'created_at')
    readonly_fields = ('car_count',)

    actions = ['sort_by_car_count']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(car_count=Count('car'))
        return queryset

    def car_count(self, obj):
        return obj.car_set.count()
    car_count.short_description = 'Car Count'
    car_count.admin_order_field = 'car_count'

    def sort_by_car_count(self, request, queryset):
        queryset = queryset.annotate(
            car_count=Count('car')).order_by('-car_count')
        self.message_user(request, 'Sorted by Car Count')
        return queryset
    sort_by_car_count.short_description = 'Sort by Car Count'

    fieldsets = (
        ("User Information", {
            'fields': ('telegram_id', 'first_name', 'last_name', 'phone', 'username'),
        }),
        ('Additional Information', {
            'fields': ('created_at', 'car_count', 'step', 'deleted'),
        }),
    )

    def has_change_permission(self, *args, **kwargs):
        return False

    def has_add_permission(self, *args, **kwargs):
        return False


@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    def has_change_permission(self, *args, **kwargs):
        return False

    def has_add_permission(self, *args, **kwargs):
        return False


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    def has_change_permission(self, *args, **kwargs):
        return False

    def has_add_permission(self, *args, **kwargs):
        return False
    
@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    def has_change_permission(self, *args, **kwargs):
        return False

    def has_add_permission(self, *args, **kwargs):
        return False