from django.urls import path

from post import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cat-filter/<int:id>', views.cat_filter, name='cat_filter'),
    path('author-filter/<int:id>', views.aut_filter, name='aut_filter'),
    path('books/crud/', views.books_crud, name='crud_books'),
    path('add-book', views.create_book, name='add_book'),
    path('delete-book/<int:id>', views.delete_book, name='delete_book'),
    path('book/update/<int:id>', views.update_book, name='update_book'),
    path('book/info/<int:id>', views.info_book, name='info_book'),
    path('ctategories/crud/', views.crud_cats, name='crud_cats'),
    path('add_category/', views.add_cat, name='add_cat'),
    path('category/delete/<int:id>', views.delete_cat, name='delete_cat'),
    path('category/update/<int:id>', views.update_cat, name='update_cat'),
    path('authors/crud/', views.crud_authors, name='crud_authors'),
    path('author/add/', views.add_author, name='add_author'),
    path('author/delete/<int:id>', views.delete_author, name='delete_author'),
    path('author/update/<int:id>', views.update_author, name='update_author'),
    path('info/author/<int:id>', views.info_author, name='info_author'),
]
