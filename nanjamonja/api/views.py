from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Character, User


@api_view(['POST'])
def user_insert(request):
    user_info = User.objects.create(
        user_name=request.data['user_name']
    )
    Character.objects.create(
        content=bytes(request.data['content'], 'utf-8'),
        user=user_info
    )
    print(request.data)
    return Response({"message": "insertです"})


@api_view(['GET'])
def user_get(request):
    users = User.objects.all()
    datas = []
    for row in users:
        char = Character.objects.filter(user=row.id)
        data = [
            {'user_name': row.user_name},
            {'content': char[0].content},
            {'highest_score': row.highest_score},
            {'participant_count': row.participant_count}
        ]
        datas.append(data)

    return Response(datas)


@api_view(['POST'])
def user_update(request):
    return Response({"message": "updです"})
