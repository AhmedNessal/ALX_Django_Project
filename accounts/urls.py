from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterView, LoginView
from django.urls import path

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]

urlpatterns += router.urls