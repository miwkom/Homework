from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Blog


def main(request):
    posts = Blog.objects.all().order_by('-title')
    items_per_page = int(request.GET.get('items_per_page', 5))
    paginator = Paginator(posts, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'title': 'Главная страница'
    }
    return render(request, 'main.html', context)