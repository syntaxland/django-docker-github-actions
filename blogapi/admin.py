from django.contrib import admin
from . import models

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title',  'status', 'slug', 'author')
#     prepopulated_fields = {'slug': ('title',), }
# admin.site.register(models.Post, PostAdmin)

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
# admin.site.register(models.Category, CategoryAdmin)


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }

@admin.register(models.Category)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


# @admin.register(models.Post)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('title', 'id', 'status', 'slug', 'author')
#     prepopulated_fields = {'slug': ('title',), }


# admin.site.register(models.Category)
