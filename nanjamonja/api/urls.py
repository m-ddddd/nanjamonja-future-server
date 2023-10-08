from django.urls import path
from api.views import user_insert, user_get, user_update


urlpatterns = [
    path('user/insert/', user_insert),
    path('user/get/', user_get),
    path('user/update/', user_update)
]
