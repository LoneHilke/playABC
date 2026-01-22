from django.shortcuts import render, redirect
from django.views import View
from .models import Alfabet, Bogstav#, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, Æ, Ø, Å, Alfabet, Ekstra
#from .forms import GætForm, EkstraForm
import random

class Base(View):
    def get(self, request, *args, **kwargs):
        a = Alfabet.objects.filter(bogstav__bogstav__contains='A')
        b = Alfabet.objects.filter(bogstav__bogstav__contains='B')
        c = Alfabet.objects.filter(bogstav__bogstav__contains='C')
        d = Alfabet.objects.filter(bogstav__bogstav__contains='D')
        e = Alfabet.objects.filter(bogstav__bogstav__contains='E')
        f = Alfabet.objects.filter(bogstav__bogstav__contains='F')
        g = Alfabet.objects.filter(bogstav__bogstav__contains='G')
        h = Alfabet.objects.filter(bogstav__bogstav__contains='H')
        i = Alfabet.objects.filter(bogstav__bogstav__contains='I')
        j = Alfabet.objects.filter(bogstav__bogstav__contains='J')
        k = Alfabet.objects.filter(bogstav__bogstav__contains='K')
        l = Alfabet.objects.filter(bogstav__bogstav__contains='L')
        m = Alfabet.objects.filter(bogstav__bogstav__contains='M')
        n = Alfabet.objects.filter(bogstav__bogstav__contains='N')
        o = Alfabet.objects.filter(bogstav__bogstav__contains='O')
        p = Alfabet.objects.filter(bogstav__bogstav__contains='P')
        q = Alfabet.objects.filter(bogstav__bogstav__contains='Q')
        r = Alfabet.objects.filter(bogstav__bogstav__contains='R')
        s = Alfabet.objects.filter(bogstav__bogstav__contains='S')
        t = Alfabet.objects.filter(bogstav__bogstav__contains='T')
        u = Alfabet.objects.filter(bogstav__bogstav__contains='U')
        v = Alfabet.objects.filter(bogstav__bogstav__contains='V')
        w = Alfabet.objects.filter(bogstav__bogstav__contains='W')
        x = Alfabet.objects.filter(bogstav__bogstav__contains='X')
        y = Alfabet.objects.filter(bogstav__bogstav__contains='Y')
        z = Alfabet.objects.filter(bogstav__bogstav__contains='Z')
        æ = Alfabet.objects.filter(bogstav__bogstav__contains='Æ')
        ø = Alfabet.objects.filter(bogstav__bogstav__contains='Ø')
        å = Alfabet.objects.filter(bogstav__bogstav__contains='Å')
        
        context = {
            'a': a,
            'b': b,
            'c': c,
            'd': d,
            'e': e,
            'f': f,
            'g': g,
            'h': h,
            'i': i,
            'j': j,
            'k': k,
            'l': l,
            'm': m,
            'n': n,
            'o': o,
            'p': p,
            'q': q,
            'r': r,
            's': s,
            't': t,
            'u': u,
            'v': v,
            'w': w,
            'x': x,
            'y': y,
            'z': z,
            'æ': æ,
            'ø': ø,
            'å': å,
            
        }
        return render(request, 'dansk/info.html', context)

class AView(View):
    def get(self, request, *args, **kwargs):
        a = Alfabet.objects.filter(bogstav__bogstav__contains = 'A')
        context = {
            'a': a
        }
        
        return render(request, 'dansk/danska.html',context) 
    
class BView(View):
    def get(self, request, *args, **kwargs):
        b = Alfabet.objects.filter(bogstav__bogstav__contains='B')
       
        context = {
            'b': b
        }
        return render(request, 'dansk/danskb.html', context)

class CView(View):
    def get(self, request, *args, **kwargs):
        c = Alfabet.objects.filter(bogstav__bogstav__contains='C')
        context = {
            'c': c
        }
        return render(request, 'dansk/danskc.html', context)

class DView(View):
    def get(self, request, *args, **kwargs):
        d = Alfabet.objects.filter(bogstav__bogstav__contains='D')
        context = {
            'd': d
        }
        return render(request, 'dansk/danskd.html', context)

class EView(View):
    def get(self, request, *args, **kwargs):
        e = Alfabet.objects.filter(bogstav__bogstav__contains='E')
        context = {
            'e': e
        }
        return render(request, 'dansk/danske.html', context)
    
class FView(View):
    def get(self, request, *args, **kwargs):
        f = Alfabet.objects.filter(bogstav__bogstav__contains='F')
        context = {
            'f': f
        }
        return render(request, 'dansk/danskf.html', context)
    
class GView(View):
    def get(self, request, *args, **kwargs):
        g = Alfabet.objects.filter(bogstav__bogstav__contains='G')
        context = {
            'g': g
        }
        return render(request, 'dansk/danskg.html', context)
    
class HView(View):
    def get(self, request, *args, **kwargs):
        h = Alfabet.objects.filter(bogstav__bogstav__contains='H')
        context = {
            'h': h
        }
        return render(request, 'dansk/danskh.html', context)
    
class IView(View):
    def get(self, request, *args, **kwargs):
        i = Alfabet.objects.filter(bogstav__bogstav__contains='I')
        context = {
            'i': i
        }
        return render(request, 'dansk/danski.html', context)
    
class JView(View):
    def get(self, request, *args, **kwargs):
        j = Alfabet.objects.filter(bogstav__bogstav__contains='J')
        context = {
            'j': j
        }
        return render(request, 'dansk/danskj.html', context)
    
class KView(View):
    def get(self, request, *args, **kwargs):
        k = Alfabet.objects.filter(bogstav__bogstav__contains='K')
        context = {
            'k': k
        }
        return render(request, 'dansk/danskk.html', context)

class LView(View):
    def get(self, request, *args, **kwargs):
        l = Alfabet.objects.filter(bogstav__bogstav__contains='L')
        context = {
            'l': l
        }
        return render(request, 'dansk/danskl.html', context)
    
class MView(View):
    def get(self, request, *args, **kwargs):
        m = Alfabet.objects.filter(bogstav__bogstav__contains='M')
        context = {
            'm': m
        }
        return render(request, 'dansk/danskm.html', context)
    
class NView(View):
    def get(self, request, *args, **kwargs):
        n = Alfabet.objects.filter(bogstav__bogstav__contains='N')
        context = {
            'n': n
        }
        return render(request, 'dansk/danskn.html', context)
    
class OView(View):
    def get(self, request, *args, **kwargs):
        o = Alfabet.objects.filter(bogstav__bogstav__contains='O')
        context = {
            'o': o
        }
        return render(request, 'dansk/dansko.html', context)
    
class PView(View):
    def get(self, request, *args, **kwargs):
        p = Alfabet.objects.filter(bogstav__bogstav__contains='P')
        context = {
            'p': p
        }
        return render(request, 'dansk/danskp.html', context)
    
class QView(View):
    def get(self, request, *args, **kwargs):
        q = Alfabet.objects.filter(bogstav__bogstav__contains='Q')
        context = {
            'q': q
        }
        return render(request, 'dansk/danskq.html', context)
    
class RView(View):
    def get(self, request, *args, **kwargs):
        r = Alfabet.objects.filter(bogstav__bogstav__contains='R')
        context = {
            'r': r
        }
        return render(request, 'dansk/danskr.html', context)
    
class SView(View):
    def get(self, request, *args, **kwargs):
        s = Alfabet.objects.filter(bogstav__bogstav__contains='S')
        context = {
            's': s
        }
        return render(request, 'dansk/dansks.html', context)
    
class TView(View):
    def get(self, request, *args, **kwargs):
        t = Alfabet.objects.filter(bogstav__bogstav__contains='T')
        context = {
            't': t
        }
        return render(request, 'dansk/danskt.html', context)
    
class UView(View):
    def get(self, request, *args, **kwargs):
        u = Alfabet.objects.filter(bogstav__bogstav__contains='U')
        context = {
            'u': u
        }
        return render(request, 'dansk/dansku.html', context)
    
class VView(View):
    def get(self, request, *args, **kwargs):
        v = Alfabet.objects.filter(bogstav__bogstav__contains='V')
        context = {
            'v': v
        }
        return render(request, 'dansk/danskv.html', context)
    
class WView(View):
    def get(self, request, *args, **kwargs):
        w = Alfabet.objects.filter(bogstav__bogstav__contains='W')
        context = {
            'w': w
        }
        return render(request, 'dansk/danskw.html', context)
    
class XView(View):
    def get(self, request, *args, **kwargs):
        x = Alfabet.objects.filter(bogstav__bogstav__contains='X')
        context = {
            'x': x
        }
        return render(request, 'dansk/danskx.html', context)
    
class YView(View):
    def get(self, request, *args, **kwargs):
        y = Alfabet.objects.filter(bogstav__bogstav__contains='Y')
        context = {
            'y': y
        }
        return render(request, 'dansk/dansky.html', context)
    
class ZView(View):
    def get(self, request, *args, **kwargs):
        z = Alfabet.objects.filter(bogstav__bogstav__contains='Z')
        context = {
            'z': z
        }
        return render(request, 'dansk/danskz.html', context)
    
class ÆView(View):
    def get(self, request, *args, **kwargs):
        æ = Alfabet.objects.filter(bogstav__bogstav__contains='Æ')
        context = {
            'æ': æ
        }
        return render(request, 'dansk/danskæ.html', context)
    
class ØView(View):
    def get(self, request, *args, **kwargs):
        ø = Alfabet.objects.filter(bogstav__bogstav__contains='Ø')
        context = {
            'ø': ø
        }
        return render(request, 'dansk/danskø.html', context)
    
class ÅView(View):
    def get(self, request, *args, **kwargs):
        å = Alfabet.objects.filter(bogstav__bogstav__contains='Å')
        context = {
            'å': å
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
