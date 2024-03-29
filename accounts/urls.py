from rest_framework.routers import DefaultRouter;
from django.urls import path, include;
from . import views;

router = DefaultRouter();

router.register('account', views.AccountViewset)

urlpatterns = [
    path('', include(router.urls)),
    # path('register', views.UserRegisterView.as_view(), name='register')
]
