from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib import messages


def index(request):
    query = request.GET.get('q')
    articles = Article.objects.search(query=query)
    # articles = Article.objects.all()
    # t = articles.count()
    # query = request.GET.get('q')
    # if query:
    #     articles = Article.objects.filter(title__icontains=query)
    context = {
            "articles": articles,
            # 't': t
    }
    return render(request, 'article/index.html', context)
# Create your views here.


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    context = {
        'article': article,
    }
    return render(request, 'article/detail.html', context)


def article_create(request):
    context = {
        'created': False
    }
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if request.FILES.get("image"):
            image = request.FILES["image"]
            obj = Article.objects.create(title=title, content=content, image=image)
        else:
            obj = Article.objects.create(title=title, content=content)
        context['created'] = True
        context["object"] = obj
        messages.success(request, f"Article '{obj.title}' successfully created")
    return render(request, 'article/create.html', context)


def article_change(request, slug):
    obj = Article.objects.get(slug=slug)
    form = ArticleForm(instance=obj)
    if request.method == "POST":
        form = ArticleForm(data=request.POST, instance=obj, files=request.FILES)
        if form.is_valid():
            form.save()
            reverse_url = reverse('list')
            messages.info(request, f"Article '{obj.title}' successfully changed")
            return redirect(reverse_url)
    context = {
        'object': obj,
        'form': form

    }
    return render(request, 'article/edit.html', context)


def article_create_form(request):
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save()
            reverse_url = reverse("info", args=[obj.pk])
            messages.success(request, f"Article '{obj.title}' successfully created")
            return redirect(reverse_url)
    context = {
        'form': form,
    }
    return render(request, "article/create_form.html", context)


def article_delete(request, slug):
    obj = get_object_or_404(Article, slug=slug)
    if request.method == "POST":
        messages.error(request, f"Article '{obj.title}' successfully deleted")
        obj.delete()
        return redirect("list")
    context = {
        "obj": obj
    }
    return render(request, "article/delete.html", context)





































