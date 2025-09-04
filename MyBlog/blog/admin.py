from django.contrib import admin
from .models import Post, Author

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'is_recent')
    list_filter = ('author', 'published_date')
    search_fields = ('title', 'content')

    @admin.display(boolean=True, ordering='published_date', description='<7 Days')
    def is_recent(self, obj):
        return obj.published_recently()


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)