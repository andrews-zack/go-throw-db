from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from . import views


router = routers.SimpleRouter()
router.register(r'courses', CourseViewSet)
router.register(r'holes', HoleViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'rounds', RoundsViewSet)
router.register(r'scores', ScoresViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/create/', views.CustomUserCreate.as_view()),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]