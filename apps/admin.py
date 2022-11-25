from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Status)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartDetails)

class OrderDetailsTabularInline(admin.TabularInline):
    model = OrderDetails
    extra = 0
    can_delete = False

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj):
        return False


# admin.site.register(Orders)
# admin.site.register(OrderDetails)
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    inlines = [OrderDetailsTabularInline]