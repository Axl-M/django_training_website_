from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category

# def index(request):
#     # print(dir(request))
#     news = News.objects.all()
#     res = '<h1>Список новостей</h1>'
#     for item in news:
#         res += f'\n<div><p>{item.title}</p>\n<p>{item.content}</p>\n</div><hr>\n'
#     return HttpResponse(res)
#     # return HttpResponse("Привет притурки!")

def index(request):
    news = News.objects.all()
    # categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        # 'categories': categories,
    }
    return render(request, 'news/index.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    # categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})


def test(request):
    return HttpResponse('<h1> Тестовая страница </h1>')

# Create your views here.
