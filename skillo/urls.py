from django.contrib import admin
from django.urls import path, include;

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('', include('category.urls')),
    path('', include('accounts.urls')),
    path('', include('job.urls')),
    path('', include('application.urls')),
    path('auth/', include('authentication.urls')),
]
