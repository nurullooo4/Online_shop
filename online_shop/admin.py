from django.contrib import admin
from django.contrib.auth import User, Group

from online_shop.models import Product, Category, Comment

# Register your models here.

# admin.site.register(Product)
# admin.site.register(Category)
admin.site.register(Comment)


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    search_fields = ['title', 'id']
    # exclude = ['slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category', 'discount', 'get_image_url']
