from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("auth/", include('authapp.urls')),
    #path('api-auth/', include('rest_framework.urls')),
    #path('', include('frontend.urls'))
]