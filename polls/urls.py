from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^main/', views.main, name='polls_main'),
]
#if settings.DEBUG :
    #urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)