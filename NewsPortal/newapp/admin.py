from django.contrib import admin
from .models import Post, PostCategory

class PostCategoryInLine(admin.TabularInline):
    model = PostCategory
    fk_name = 'postThrough'
    extra = 3

class PostAdmin(admin.ModelAdmin):
    inlines = [PostCategoryInLine]


admin.site.register(Post, PostAdmin)

