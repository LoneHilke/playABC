from django.urls import path
from . import views
from .views import Base, GætView, Tilføj

urlpatterns = [
    path('', Base.as_view(), name='base'),
    path("gaet/", GætView.as_view(), name='gaet'),
    path("tilføj/", Tilføj.as_view(), name='tilføj'),
    
]