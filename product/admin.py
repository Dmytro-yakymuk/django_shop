from django.contrib import admin
from .models import Category, Color, Size, Action, Brand, Tag, Product, Quantity, Image, RatingStar, Rating, SocialNetwork, Reviews

from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(label="Опис" ,widget=CKEditorUploadingWidget())
    class Meta:
        model = Product
        fields = '__all__'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug",)
    list_display_links = ("name", )


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "color")
    list_display_links = ("name",)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)

                        # StackedInline
class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email",)


class ImagesInline(admin.StackedInline):
    model = Image
    extra = 1
    # readonly_fields = ("get_image",)
    #
    # def get_image(self, obj):
    #    return mark_safe(f'<img src={obj.name.url} width="100" height="120" >')
    #
    # get_image.short_description = "Фотографія"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "public", "created_at",)
    list_display_links = ("name",)
    list_filter = ("created_at", "brand__name",)
    search_fields = ("name", "category__name")
    inlines = [ImagesInline, ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("public", )
    actions = ["publish", "unpublish"]
    form = ProductAdminForm
    # fields = (("brand", "category", "tag"), )
    # fieldsets = (
    #     (None, {
    #         "fields": (("name", "slug"),)
    #     }),
    #     (None, {
    #         "fields": (("desription", "price"), )
    #     }),
    # )

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(public=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(public=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change',)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)


@admin.register(Quantity)
class QuantityAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "quantity", "size", "color")
    list_display_links = ("id",)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "get_image", "root", "product")
    list_display_links = ("get_image",)
    list_editable = ("root",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.name.url} width="50" height="60" >')

    get_image.short_description = "Image"


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ("id", "value")
    list_display_links = ("value",)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "ip", "star")
    list_display_links = ("id",)


@admin.register(SocialNetwork)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "parent", "product")
    list_display_links = ("name",)
    readonly_fields = ("name", "email",)



admin.site.site_title = "Django Products"
admin.site.site_header = "Django Products"


# Exemple
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Product)