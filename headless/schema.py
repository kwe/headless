import graphene

import news.schema


class Query(news.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)