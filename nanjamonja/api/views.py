from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Character, User


@api_view(['POST'])
def user_insert(request):
    Character.objects.create(

    )
    print(request.data)
    return Response({"message": "insertです"})


@api_view(['GET'])
def user_get(request):
    hoge = [
        {'test': 'a'},
        {'test': 'a'},
        {'test': 'a'},
        {'test': 'a'}
    ]
    return Response(hoge)


@api_view(['POST'])
def user_update(request):
    return Response({"message": "updです"})
