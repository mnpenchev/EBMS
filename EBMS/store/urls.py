from django.contrib import admin
from django.urls import path, include
from users.views import WhoAmIView, LoginAPIView, LogoutAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/whoami/', WhoAmIView.as_view(), name='whoami'),
    path('api/v1/login/', LoginAPIView.as_view(), name='login'),
    path('api/v1/logout/', LogoutAPIView.as_view(), name='logout'),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/materials/', include('materials.urls')),
    path('api/v1/products/', include('products.urls')),
]
