from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'submission/$', views.conversion_api, name= 'conversion_api'),
    url(r'conversion$', views.conversion_page, name = 'conversion_page'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

