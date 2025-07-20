# backend/real_estate/admin.py (simplified version to avoid conflicts)
from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Count
from django.urls import reverse
from django.contrib.admin import SimpleListFilter
from .models import TelegramUser, Property, Favorite, UserActivity, Region, District

# Custom filters
class PropertyStatusFilter(SimpleListFilter):
    title = 'Property Status'
    parameter_name = 'property_status'

    def lookups(self, request, model_admin):
        return (
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('premium', 'Premium'),
            ('pending', 'Pending Approval'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'active':
            return queryset.filter(is_approved=True, is_active=True)
        elif self.value() == 'inactive':
            return queryset.filter(is_active=False)
        elif self.value() == 'premium':
            return queryset.filter(is_premium=True)
        elif self.value() == 'pending':
            return queryset.filter(is_approved=False)

# Enhanced User Admin
@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = [
        'telegram_id', 'full_name', 'username', 'language', 
        'balance', 'is_blocked', 'properties_count', 'created_at'
    ]
    list_filter = ['language', 'is_blocked', 'created_at']
    search_fields = ['telegram_id', 'username', 'first_name', 'last_name']
    list_editable = ['is_blocked', 'language', 'balance']
    readonly_fields = ['telegram_id', 'created_at', 'updated_at']
    
    fieldsets = (
        ('User Information', {
            'fields': ('telegram_id', 'username', 'first_name', 'last_name')
        }),
        ('Settings', {
            'fields': ('language', 'is_blocked', 'balance')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def full_name(self, obj):
        return f"{obj.first_name or ''} {obj.last_name or ''}".strip() or "No Name"
    full_name.short_description = "Full Name"
    
    def properties_count(self, obj):
        count = obj.properties.count()
        if count > 0:
            url = reverse('admin:real_estate_property_changelist')
            return format_html(
                '<a href="{}?user__telegram_id={}">{} properties</a>',
                url, obj.telegram_id, count
            )
        return "0 properties"
    properties_count.short_description = "Properties"

# Enhanced Property Admin
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title_short', 'user_link', 'property_type', 
        'location_display', 'price_display', 'status_badge',
        'is_approved', 'is_premium', 'is_active', 'views_count', 'created_at'
    ]
    list_display = [
        'id', 'title_short', 'user_link', 'property_type', 
        'location_display', 'price_display', 'status_badge',
        'views_count', 'created_at'
    ]
    list_filter = [
        'property_type', PropertyStatusFilter, 'status', 'condition',
        'is_premium', 'is_approved', 'is_active', 'region', 'created_at'
    ]
    search_fields = [
        'title', 'description', 'address', 'full_address',
        'user__first_name', 'user__last_name', 'user__username'
    ]
    # Remove list_editable to avoid the error - users can edit via the detail page
    readonly_fields = ['views_count', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'title', 'description', 'property_type')
        }),
        ('Location', {
            'fields': ('region', 'district', 'address', 'full_address')
        }),
        ('Property Details', {
            'fields': ('price', 'area', 'rooms', 'condition', 'status')
        }),
        ('Contact & Media', {
            'fields': ('contact_info', 'photo_file_ids')
        }),
        ('Settings', {
            'fields': ('is_premium', 'is_approved', 'is_active', 'expires_at')
        }),
        ('Statistics', {
            'fields': ('views_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['approve_properties', 'make_premium', 'make_regular']
    
    def title_short(self, obj):
        return obj.title[:50] + ('...' if len(obj.title) > 50 else '')
    title_short.short_description = "Title"
    
    def user_link(self, obj):
        url = reverse('admin:real_estate_telegramuser_change', args=[obj.user.pk])
        return format_html(
            '<a href="{}">{}</a>',
            url, obj.user.first_name or obj.user.username or f"ID: {obj.user.telegram_id}"
        )
    user_link.short_description = "User"
    
    def location_display(self, obj):
        if obj.region and obj.district:
            return f"{obj.district}, {obj.region}"
        return obj.address[:30] + ('...' if len(obj.address) > 30 else '')
    location_display.short_description = "Location"
    
    def price_display(self, obj):
        return f"{obj.price:,.0f} UZS"
    price_display.short_description = "Price"
    
    def status_badge(self, obj):
        if not obj.is_approved:
            return format_html('<span style="color: orange;">⏳ Pending</span>')
        elif not obj.is_active:
            return format_html('<span style="color: red;">❌ Inactive</span>')
        elif obj.is_premium:
            return format_html('<span style="color: gold;">⭐ Premium</span>')
        else:
            return format_html('<span style="color: green;">✅ Active</span>')
    status_badge.short_description = "Status"
    
    def approve_properties(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f'{updated} properties approved.')
    approve_properties.short_description = "Approve selected properties"
    
    def make_premium(self, request, queryset):
        updated = queryset.update(is_premium=True)
        self.message_user(request, f'{updated} properties made premium.')
    make_premium.short_description = "Make premium"
    
    def make_regular(self, request, queryset):
        updated = queryset.update(is_premium=False)
        self.message_user(request, f'{updated} properties made regular.')
    make_regular.short_description = "Make regular"

# Region Admin
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name_uz', 'name_ru', 'name_en', 'key', 'is_active']
    list_editable = ['is_active']
    search_fields = ['name_uz', 'name_ru', 'name_en', 'key']
    list_filter = ['is_active']

# District Admin
@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name_uz', 'region', 'name_ru', 'name_en', 'key', 'is_active']
    list_filter = ['region', 'is_active']
    list_editable = ['is_active']
    search_fields = ['name_uz', 'name_ru', 'name_en', 'key']

# Favorite Admin
@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'property', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__first_name', 'property__title']

# User Activity Admin
@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'created_at']
    list_filter = ['action', 'created_at']
    search_fields = ['user__first_name', 'user__last_name', 'user__username']
    readonly_fields = ['created_at']

# Customize admin site
admin.site.site_header = "Real Estate Bot Admin Panel"
admin.site.site_title = "Real Estate Bot"
admin.site.index_title = "Dashboard"

# Optional: Custom admin dashboard view (for future use)
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_dashboard(request):
    """Custom admin dashboard with basic statistics"""
    try:
        # Get basic statistics
        total_users = TelegramUser.objects.count()
        active_users = TelegramUser.objects.filter(is_blocked=False).count()
        total_properties = Property.objects.count()
        active_properties = Property.objects.filter(is_approved=True, is_active=True).count()
        premium_properties = Property.objects.filter(is_premium=True).count()
        
        context = {
            'total_users': total_users,
            'active_users': active_users,
            'total_properties': total_properties,
            'active_properties': active_properties,
            'premium_properties': premium_properties,
        }
        
        return render(request, 'admin/dashboard.html', context)
    except Exception as e:
        # Fallback to default admin index
        from django.contrib.admin.sites import site
        return site.index(request)