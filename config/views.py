from django.shortcuts import HttpResponse
from article.models import Article
import random


def hello(request):
    # HTML_STRING="<h1>hello</h1> <h2>world</h2>"
    obj_id = random.randint(1, 3)
    article = Article.objects.get(id=obj_id)
    title = f"<h1>{article.title} ({article.id})</h1>"
    content = f"<p>{article.content}</p>"
    html = title + content
    return HttpResponse(html)
