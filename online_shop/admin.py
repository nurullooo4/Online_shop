from django.contrib import admin
from django.contrib.auth import User, Group
from online_shop.admin_filter import IsVeryExpensiveFilter
from online_shop.models import Product, Category, Comment

# Register your models here.

# admin.site.register(Product)
# admin.site.register(Category)
admin.site.register(Comment)


admin.site.unregister(User)
admin.site.unregister(Group)



@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'product_count']
    search_fields = ['title', 'id']
    prepopulated_fields = {'slug': ('title',)}

    def product_count(self, obj):
        return obj.products.count()

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category', 'discount', 'get_image_url', 'is_very_expensive_product']
    search_fields = ['name']
    list_filter = ['category', IsVeryExpensiveFilter]

    def is_very_expensive_product(self, obj):
        return obj.price > 14_000_000

    is_very_expensive_product.boolean = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    resource_class = ProductResource
    fieldsets = (
        ("general", {"fields": ("title")}),
        ("other", {"fields": ("genre", "summary", "isbn", "published_on")}),
    )
    inlines = (ProductLoanInline,)

    # Order the sections within the change form
    jazzmin_section_order = ("product loans", "general", "other")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    resource_class = ProductResource
    fieldsets = (
        ("general", {"fields": ("title", "author", "library")}),
        ("other", {"fields": ("genre", "summary", "isbn", "published_on")}),
    )
    list_filter = ("title",)

    # Render filtered options only after 5 characters were entered
    filter_input_length = {
        "title": 5,
    }

