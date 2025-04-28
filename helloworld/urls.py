from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
    path('', RedirectView.as_view(url='/hello/', permanent=False)),  # Redirect root to /hello/
]
