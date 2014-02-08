from django.forms import ModelForm

from stucampus.articles.models import Article, Category


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = ['editor', 'create_ip', 'click_count',
                   'deleted', 'important']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
