from django.urls import path
from . import views
from .views import Base, TyskaView, TyskbView, TyskCView, TyskDView, TyskEView, TyskFView, TyskGView, TyskHView, TyskIView, TyskJView, TyskKView, TyskLView, TyskMView, TyskNView, TyskOView, TyskPView, TyskQView, TyskRView, TyskSView, TyskTView, TyskUView, TyskVView, TyskWView, TyskXView, TyskYView, TyskZView#, Tilføj

urlpatterns = [
    path('', Base.as_view(), name='base'),
    path('tyska/', TyskaView.as_view(), name='tyska'),
    path('tyskb/', TyskbView.as_view(), name='tyskb'),
    path('tyskc/', TyskCView.as_view(), name='tyskc'),
    path('tyskd/', TyskDView.as_view(), name='tyskd'),
    path('tyske/', TyskEView.as_view(), name='tyske'),
    path('tyskf/', TyskFView.as_view(), name='tyskf'),
    path('tyskg/', TyskGView.as_view(), name='tyskg'),
    path('tyskh/', TyskHView.as_view(), name='tyskh'),
    path('tyski/', TyskIView.as_view(), name='tyski'),
    path('tyskj/', TyskJView.as_view(), name='tyskj'),
    path('tyskk/', TyskKView.as_view(), name='tyskk'),
    path('tyskl/', TyskLView.as_view(), name='tyskl'),
    path('tyskm/', TyskMView.as_view(), name='tyskm'),
    path('tyskn/', TyskNView.as_view(), name='tyskn'),
    path('tysko/', TyskOView.as_view(), name='tysko'),
    path('tyskp/', TyskPView.as_view(), name='tyskp'),
    path('tyskq/', TyskQView.as_view(), name='tyskq'),
    path('tyskr/', TyskRView.as_view(), name='tyskr'),
    path('tysks/', TyskSView.as_view(), name='tysks'),
    path('tyskt/', TyskTView.as_view(), name='tyskt'),
    path('tysku/', TyskUView.as_view(), name='tysku'),
    path('tyskv/', TyskVView.as_view(), name='tyskv'),
    path('tyskw/', TyskWView.as_view(), name='tyskw'),
    path('tyskx/', TyskXView.as_view(), name='tyskx'),
    path('tysky/', TyskYView.as_view(), name='tysky'),
    path('tyskz/', TyskZView.as_view(), name='tyskz'),
    #path('tyskplus/', Tilføj.as_view(), name='tyskplus'),
]