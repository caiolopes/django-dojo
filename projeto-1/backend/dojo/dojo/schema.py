import graphene
from graphene_django import DjangoObjectType
from core.models import Joke


class JokeNode1(graphene.ObjectType):
    text = graphene.String()

    @classmethod
    def from_joke_model(cls, joke):
        return cls(text=joke.text)


class JokeNode2(DjangoObjectType):
    class Meta:
        model = Joke


class Query(graphene.ObjectType):
    jokes1 = graphene.List(JokeNode1)
    jokes2 = graphene.List(JokeNode2)

    def resolve_jokes2(self, info):
        return Joke.objects.all()

    def resolve_jokes1(self, info):
        return [JokeNode1.from_joke_model(joke)
                for joke in Joke.objects.all()]


class JokeMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        text = graphene.String(required=True)

    # The class attributes define the response of the mutation
    joke = graphene.Field(JokeNode2)

    def mutate(self, info, text):
        joke = Joke.objects.create(text=text)
        # Notice we return an instance of this mutation
        return JokeMutation(joke=joke)


class Mutation(graphene.ObjectType):
    create_joke = JokeMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
