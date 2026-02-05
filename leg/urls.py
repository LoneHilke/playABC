from django.urls import path
from . import views
from .views import Base, Gæt2View, Tilføj, GætaView, GætbView,GætcView,GætdView,GæteView,GætfView

urlpatterns = [
    path('', Base.as_view(), name='base'),
    path("gaet2/", Gæt2View.as_view(), name='gaet2'),
    path("tilføj/", Tilføj.as_view(), name='tilføj'),
    path("gæta/", GætaView.as_view(), name="gæta"),
    path("gætb/", GætbView.as_view(), name='gætb'),
    path("gætc/", GætcView.as_view(), name='gætc'),
    path("gætd/", GætdView.as_view(), name='gætd'),
    path("gæte/", GæteView.as_view(), name='gæte'),
    path("gætf/", GætfView.as_view(), name='gætf'),
    
]