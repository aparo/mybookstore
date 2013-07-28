from django.contrib import admin
from bookshop.models import Book, Author, Tag

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'available', "in_stock", "price")
    search_fields = ['title', "description"]
    list_filter = ('available', "in_stock", "price")

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Tag)

