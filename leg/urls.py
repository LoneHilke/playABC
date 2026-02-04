from django.urls import path
from . import views
from .views import Base, Gæt2View, Tilføj, GætaView, GætbView

urlpatterns = [
    path('', Base.as_view(), name='base'),
    path("gaet2/", Gæt2View.as_view(), name='gaet2'),
    path("tilføj/", Tilføj.as_view(), name='tilføj'),
    path("gæta/", GætaView.as_view(), name="gæta"),
    path("gætb/", GætbView.as_view(), name='gætb'),
    
]