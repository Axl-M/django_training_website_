from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm

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


# def test(request):
#     return HttpResponse('<h1> Тестовая страница </h1>')

def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'news_item':news_item})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = News.objects.create(**form.cleaned_data)
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})