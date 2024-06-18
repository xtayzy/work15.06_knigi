from django.shortcuts import render, redirect

# Create your views here.
from post.models import Book, Author, Category


def index(request):
    ctx = {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),
        'categories': Category.objects.all()
    }

    return render(request, 'post/index.html', ctx)


def create_book(request):
    if request.method == 'POST':
        author = Author.objects.get(pk=request.POST['author'])
        cat = Category.objects.get(pk=request.POST['category'])
        book = Book()
        book.name = request.POST['name']
        book.image = request.FILES['image']
        book.description = request.POST['description']
        book.author = author
        book.category = cat
        book.save()

    return redirect('crud_books')


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('crud_books')


def cat_filter(request, id):
    cat = Category.objects.get(id=id)
    books = cat.books.all()

    ctx = {
        'books': books,
        'authors': Author.objects.all(),
        'categories': Category.objects.all()
    }

    return render(request, 'post/index.html', ctx)


def aut_filter(request, id):
    aut = Author.objects.get(id=id)
    books = aut.books.all()

    ctx = {
        'books': books,
        'authors': Author.objects.all(),
        'categories': Category.objects.all()
    }

    return render(request, 'post/index.html', ctx)


def books_crud(request):
    ctx = {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),
        'categories': Category.objects.all()
    }

    return render(request, 'post/crud_books.html', ctx)


def update_book(request, id):
    if request.method == 'POST':
        cat = Category.objects.get(id=request.POST['category'])
        author = Author.objects.get(id=request.POST['author'])
        book = Book.objects.get(id=id)
        book.name = request.POST['name']
        book.image = request.FILES['image']
        book.description = request.POST['description']
        book.author = author
        book.category = cat
        book.save()
        return redirect('crud_books')

    ctx = {
        'book': Book.objects.get(id=id),
        'authors': Author.objects.all(),
        'categories': Category.objects.all()
    }

    return render(request, 'post/update_book.html', ctx)


def info_book(request, id):
    ctx = {
        'book': Book.objects.get(id=id),
    }
    return render(request, 'post/info_book.html', ctx)


def crud_cats(request):
    ctx = {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),
        'categories': Category.objects.all()
    }

    return render(request, 'post/crud_cats.html', ctx)


def add_cat(request):
    if request.method == 'POST':
        cat = Category()
        cat.name = request.POST['name']
        cat.img = request.FILES['image']
        cat.save()

    return redirect('crud_cats')


def delete_cat(request, id):
    cat = Category.objects.get(id=id)
    cat.delete()
    return redirect('crud_cats')


def update_cat(request, id):
    if request.method == 'POST':
        cat = Category.objects.get(id=id)
        cat.name = request.POST['name']
        cat.img = request.FILES['image']
        cat.save()
        return redirect('crud_cats')

    ctx = {
        'cat': Category.objects.get(id=id)
    }

    return render(request, 'post/update_cat.html', ctx)


def crud_authors(request):
    ctx = {
        'authors': Author.objects.all()
    }

    return render(request, 'post/crud_authors.html', ctx)


def add_author(request):
    if request.method == 'POST':
        author = Author()
        author.name = request.POST['name']
        author.bio = request.POST['bio']
        author.img = request.FILES['image']
        author.save()

    return redirect('crud_authors')


def delete_author(request, id):
    author = Author.objects.get(id=id)
    author.delete()
    return redirect('crud_authors')


def update_author(request, id):
    if request.method == 'POST':
        author = Author.objects.get(id=id)
        author.name = request.POST['name']
        author.img = request.FILES['image']
        author.bio = request.POST['bio']
        author.save()
        return redirect('crud_authors')

    ctx = {
        'author': Author.objects.get(id=id)
    }

    return render(request, 'post/update_author.html', ctx)


def info_author(request, id):
    author = Author.objects.get(id=id)
    books = author.books.all()

    ctx = {
        'author': author,
        'books': books
    }

    return render(request, 'post/info_author.html', ctx)

