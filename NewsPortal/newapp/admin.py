from django.contrib import admin
from .models import Post, PostCategory, Category

class PostCategoryInLine(admin.TabularInline):
    model = PostCategory
    fk_name = 'postThrough'
    extra = 3




class PostAdmin(admin.ModelAdmin):
    inlines = [PostCategoryInLine]
    list_display = ('title', 'author', 'text')
    list_filter = ('title', 'author', 'text', 'postCategory')
    search_fields =('title', 'author', 'text', 'postCategory')






admin.site.register(Post, PostAdmin)
admin.site.register(Category)

