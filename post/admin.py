from django.contrib import admin

# Register your models here.

from post.models import Book, Category, Author

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Author)









