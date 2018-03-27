import graphene
from graphene_django import DjangoObjectType

from .models import Article


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article


class Query(graphene.ObjectType):
    articles = graphene.List(ArticleType)

    def resolve_articles(self, info, **kwargs):
        return Article.objects.all()