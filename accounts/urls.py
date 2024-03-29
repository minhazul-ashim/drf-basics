from django.urls import path, include;
from . import views;

urlpatterns = [
    path('register/', views.AccountCreationView.as_view(), name='register'),

    path('update/', views.UserUpdateView.as_view(), name="accountUpdate"),

    path('get/', views.UserAccountView.as_view(), name="accountGet"),

    path('<int:id>/', views.UserAccountView.as_view(), name="accountGet"),
]
