from django.urls import path
from Users import views
from django.contrib import admin

urlpatterns = [
path('admin/', admin.site.urls),
path('api/token/', views.CustomTokenView.as_view(), name='token_obtain_pair'),
]