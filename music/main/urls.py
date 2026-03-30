from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('genres/', views.genres, name='genres'),
    path('tracks/', views.tracks, name='tracks'),
    path('add_genre/', views.add_genre),
    path('editgenre/<int:id_genre>', views.add_genre),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
