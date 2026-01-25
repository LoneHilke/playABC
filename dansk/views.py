from django.shortcuts import render, redirect
from django.views import View
from .models import Alfabet, Bogstav#, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, Æ, Ø, Å, Alfabet, Ekstra
#from .forms import GætForm, EkstraForm
import random

class Base(View):
    def get(self, request, *args, **kwargs):
        dana = Alfabet.objects.filter(bogstav__bogstav__contains='danA')
        danb = Alfabet.objects.filter(bogstav__bogstav__contains='danB')
        danc = Alfabet.objects.filter(bogstav__bogstav__contains='danC')
        dand = Alfabet.objects.filter(bogstav__bogstav__contains='danD')
        dane = Alfabet.objects.filter(bogstav__bogstav__contains='danE')
        danf = Alfabet.objects.filter(bogstav__bogstav__contains='danF')
        dang = Alfabet.objects.filter(bogstav__bogstav__contains='danG')
        danh = Alfabet.objects.filter(bogstav__bogstav__contains='danH')
        dani = Alfabet.objects.filter(bogstav__bogstav__contains='danI')
        danj = Alfabet.objects.filter(bogstav__bogstav__contains='danJ')
        dank = Alfabet.objects.filter(bogstav__bogstav__contains='danK')
        danl = Alfabet.objects.filter(bogstav__bogstav__contains='danL')
        danm = Alfabet.objects.filter(bogstav__bogstav__contains='danM')
        dann = Alfabet.objects.filter(bogstav__bogstav__contains='danN')
        dano = Alfabet.objects.filter(bogstav__bogstav__contains='danO')
        danp = Alfabet.objects.filter(bogstav__bogstav__contains='danP')
        danq = Alfabet.objects.filter(bogstav__bogstav__contains='danQ')
        danr = Alfabet.objects.filter(bogstav__bogstav__contains='danR')
        dans = Alfabet.objects.filter(bogstav__bogstav__contains='danS')
        dant = Alfabet.objects.filter(bogstav__bogstav__contains='danT')
        danu = Alfabet.objects.filter(bogstav__bogstav__contains='danU')
        danv = Alfabet.objects.filter(bogstav__bogstav__contains='danV')
        danw = Alfabet.objects.filter(bogstav__bogstav__contains='danW')
        danx = Alfabet.objects.filter(bogstav__bogstav__contains='danX')
        dany = Alfabet.objects.filter(bogstav__bogstav__contains='danY')
        danz = Alfabet.objects.filter(bogstav__bogstav__contains='danZ')
        danæ = Alfabet.objects.filter(bogstav__bogstav__contains='danÆ')
        danø = Alfabet.objects.filter(bogstav__bogstav__contains='danØ')
        danå = Alfabet.objects.filter(bogstav__bogstav__contains='danÅ')
        
        context = {
            'dana': dana,
            'danb': danb,
            'danc': danc,
            'dand': dand,
            'dane': dane,
            'danf': danf,
            'dang': dang,
            'danh': danh,
            'dani': dani,
            'danj': danj,
            'dank': dank,
            'danl': danl,
            'danm': danm,
            'dann': dann,
            'dano': dano,
            'danp': danp,
            'danq': danq,
            'danr': danr,
            'dans': dans,
            'dant': dant,
            'danu': danu,
            'danv': danv,
            'danw': danw,
            'danx': danx,
            'dany': dany,
            'danz': danz,
            'danæ': danæ,
            'danø': danø,
            'danå': danå,
            
        }
        return render(request, 'dansk/info.html', context)

class AView(View):
    def get(self, request, *args, **kwargs):
        dana = Alfabet.objects.filter(bogstav__bogstav__contains = 'danA')
        context = {
            'dana': dana
        }
        
        return render(request, 'dansk/danska.html',context) 
    
class BView(View):
    def get(self, request, *args, **kwargs):
        danb = Alfabet.objects.filter(bogstav__bogstav__contains='danB')
       
        context = {
            'danb': danb
        }
        return render(request, 'dansk/danskb.html', context)

class CView(View):
    def get(self, request, *args, **kwargs):
        danc = Alfabet.objects.filter(bogstav__bogstav__contains='danC')
        context = {
            'danc': danc
        }
        return render(request, 'dansk/danskc.html', context)

class DView(View):
    def get(self, request, *args, **kwargs):
        dand = Alfabet.objects.filter(bogstav__bogstav__contains='danD')
        context = {
            'dand': dand
        }
        return render(request, 'dansk/danskd.html', context)

class EView(View):
    def get(self, request, *args, **kwargs):
        dane = Alfabet.objects.filter(bogstav__bogstav__contains='danE')
        context = {
            'dane': dane
        }
        return render(request, 'dansk/danske.html', context)
    
class FView(View):
    def get(self, request, *args, **kwargs):
        danf = Alfabet.objects.filter(bogstav__bogstav__contains='danF')
        context = {
            'danf': danf
        }
        return render(request, 'dansk/danskf.html', context)
    
class GView(View):
    def get(self, request, *args, **kwargs):
        dang = Alfabet.objects.filter(bogstav__bogstav__contains='danG')
        context = {
            'dang': dang
        }
        return render(request, 'dansk/danskg.html', context)
    
class HView(View):
    def get(self, request, *args, **kwargs):
        danh = Alfabet.objects.filter(bogstav__bogstav__contains='danH')
        context = {
            'danh': danh
        }
        return render(request, 'dansk/danskh.html', context)
    
class IView(View):
    def get(self, request, *args, **kwargs):
        dani = Alfabet.objects.filter(bogstav__bogstav__contains='danI')
        context = {
            'dani': dani
        }
        return render(request, 'dansk/danski.html', context)
    
class JView(View):
    def get(self, request, *args, **kwargs):
        danj = Alfabet.objects.filter(bogstav__bogstav__contains='danJ')
        context = {
            'danj': danj
        }
        return render(request, 'dansk/danskj.html', context)
    
class KView(View):
    def get(self, request, *args, **kwargs):
        dank = Alfabet.objects.filter(bogstav__bogstav__contains='danK')
        context = {
            'dank': dank
        }
        return render(request, 'dansk/danskk.html', context)

class LView(View):
    def get(self, request, *args, **kwargs):
        danl = Alfabet.objects.filter(bogstav__bogstav__contains='danL')
        context = {
            'danl': danl
        }
        return render(request, 'dansk/danskl.html', context)
    
class MView(View):
    def get(self, request, *args, **kwargs):
        danm = Alfabet.objects.filter(bogstav__bogstav__contains='danM')
        context = {
            'danm': danm
        }
        return render(request, 'dansk/danskm.html', context)
    
class NView(View):
    def get(self, request, *args, **kwargs):
        dann = Alfabet.objects.filter(bogstav__bogstav__contains='danN')
        context = {
            'dann': dann
        }
        return render(request, 'dansk/danskn.html', context)
    
class OView(View):
    def get(self, request, *args, **kwargs):
        dano = Alfabet.objects.filter(bogstav__bogstav__contains='danO')
        context = {
            'dano': dano
        }
        return render(request, 'dansk/dansko.html', context)
    
class PView(View):
    def get(self, request, *args, **kwargs):
        danp = Alfabet.objects.filter(bogstav__bogstav__contains='danP')
        context = {
            'danp': danp
        }
        return render(request, 'dansk/danskp.html', context)
    
class QView(View):
    def get(self, request, *args, **kwargs):
        danq = Alfabet.objects.filter(bogstav__bogstav__contains='danQ')
        context = {
            'danq': danq
        }
        return render(request, 'dansk/danskq.html', context)
    
class RView(View):
    def get(self, request, *args, **kwargs):
        danr = Alfabet.objects.filter(bogstav__bogstav__contains='danR')
        context = {
            'danr': danr
        }
        return render(request, 'dansk/danskr.html', context)
    
class SView(View):
    def get(self, request, *args, **kwargs):
        dans = Alfabet.objects.filter(bogstav__bogstav__contains='danS')
        context = {
            'dans': dans
        }
        return render(request, 'dansk/dansks.html', context)
    
class TView(View):
    def get(self, request, *args, **kwargs):
        dant = Alfabet.objects.filter(bogstav__bogstav__contains='danT')
        context = {
            'dant': dant
        }
        return render(request, 'dansk/danskt.html', context)
    
class UView(View):
    def get(self, request, *args, **kwargs):
        danu = Alfabet.objects.filter(bogstav__bogstav__contains='danU')
        context = {
            'danu': danu
        }
        return render(request, 'dansk/dansku.html', context)
    
class VView(View):
    def get(self, request, *args, **kwargs):
        danv = Alfabet.objects.filter(bogstav__bogstav__contains='danV')
        context = {
            'danv': danv
        }
        return render(request, 'dansk/danskv.html', context)
    
class WView(View):
    def get(self, request, *args, **kwargs):
        danw = Alfabet.objects.filter(bogstav__bogstav__contains='danW')
        context = {
            'danw': danw
        }
        return render(request, 'dansk/danskw.html', context)
    
class XView(View):
    def get(self, request, *args, **kwargs):
        danx = Alfabet.objects.filter(bogstav__bogstav__contains='danX')
        context = {
            'danx': danx
        }
        return render(request, 'dansk/danskx.html', context)
    
class YView(View):
    def get(self, request, *args, **kwargs):
        dany = Alfabet.objects.filter(bogstav__bogstav__contains='danY')
        context = {
            'dany': dany
        }
        return render(request, 'dansk/dansky.html', context)
    
class ZView(View):
    def get(self, request, *args, **kwargs):
        danz = Alfabet.objects.filter(bogstav__bogstav__contains='danZ')
        context = {
            'danz': danz
        }
        return render(request, 'dansk/danskz.html', context)
    
class ÆView(View):
    def get(self, request, *args, **kwargs):
        danæ = Alfabet.objects.filter(bogstav__bogstav__contains='danÆ')
        context = {
            'danæ': danæ
        }
        return render(request, 'dansk/danskæ.html', context)
    
class ØView(View):
    def get(self, request, *args, **kwargs):
        danø = Alfabet.objects.filter(bogstav__bogstav__contains='danØ')
        context = {
            'danø': danø
        }
        return render(request, 'dansk/danskø.html', context)
    
class ÅView(View):
    def get(self, request, *args, **kwargs):
        danå = Alfabet.objects.filter(bogstav__bogstav__contains='danÅ')
        context = {
            'danå': danå
        }
        return render(request, 'dansk/danskå.html', context)
    
"""class Tilføj(View):
    def get(self, request, *args, **kwargs):
        form = EkstraForm()
        alfabet = Alfabet.objects.all()
        return render(request, 'dansk/tilføj.html', {
            'form': form,
            'alfabet': alfabet,
        })

    def post(self, request, *args, **kwargs):
        form = EkstraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dansk/tilføj')

        alfabet = Alfabet.objects.all()
        return render(request, 'dansk/tilføj.html', {
            'form': form,
            'alfabet': alfabet,
        })"""

# Create your views here.
