from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("debug/", include("debug_toolbar.urls")),
    path('', include('products.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),

]
