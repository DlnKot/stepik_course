from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profile_app.urls')),
    path('news/', include('news_app.urls')),
]
