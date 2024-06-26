from django.contrib import admin
from .views import JobCategoryView;
from django.urls import path, include;

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('', include('category.urls')),
    path('account/', include('accounts.urls')),
    path('', include('job.urls')),
    path('', include('application.urls')),
    path('job/category/<int:id>', JobCategoryView.as_view()),
    path('auth/', include('authentication.urls')),
    path('auth/', include('authentication.urls')),
]
