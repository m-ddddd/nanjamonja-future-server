from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Character, User


@api_view(['POST'])
def user_insert(request):
    user_info = User.objects.create(
        user_name=request.data['user_name']
    )
    Character.objects.create(
        content=request.data['content'],
        user=user_info
    )
    print(request.data)
    return Response({'result': 'sucsses'})


@api_view(['GET'])
def user_get(request):
    users = User.objects.all().order_by('-id')
    datas = []
    for row in users:
        char = Character.objects.filter(user=row.id)
        data = [
            {'user_name': row.user_name},
            {'content': char[0].content},
            {'highest_score': row.highest_score},
            {'participant_count': row.participant_count},
            {'default_flg': row.default_flg},
        ]
        datas.append(data)

    return Response(datas)


@api_view(['POST'])
def user_update(request):
    for user_info in request.data:
        user_id = user_info.get('id')
        score = user_info.get('score')
        if isinstance(score, str):
            score = int(score)
        user = User.objects.get(id=user_id)
        if score > user.highest_score:
            user.highest_score = score
        user.participant_count += 1
        user.save()

    return Response({'result': 'sucsses'})
