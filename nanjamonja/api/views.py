from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def user_insert(request):
    return Response({"message": "insertです"})


@api_view(['GET'])
def user_get(request):
    return Response({"message": "getです"})


@api_view(['POST'])
def user_update(request):
    return Response({"message": "updです"})
