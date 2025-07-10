from django.contrib import admin
from django.urls import include, path

from news_app.views import page_not_found


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profile_app.urls')),
    path('news/', include('news_app.urls')),
]


handler404 = page_not_found
