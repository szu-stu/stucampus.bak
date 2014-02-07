from django.forms import ModelForm
from stucampus.articles.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
