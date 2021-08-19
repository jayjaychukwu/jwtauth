from django.urls import path
from .views import UserDetail, UserDetailDo

urlpatterns = [
    path('', UserDetail.as_view()),
    path('<int:id>/', UserDetailDo.as_view()),
]
