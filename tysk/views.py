from django.shortcuts import render, redirect
from django.views import View
from dansk.models import Alfabet, Bogstav#, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, Æ, Ø, Å, Alfabet, Ekstra
#from .forms import GætForm, EkstraForm
import random

class Base(View):
    def get(self, request, *args, **kwargs):
        tysa = Alfabet.objects.filter(bogstav__bogstav__contains='A')
        tysb = Alfabet.objects.filter(bogstav__bogstav__contains='B')
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
        
        
        context = {
            'a': tysa,
            'b': tysb,
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
            
            
        }
        return render(request, 'tysk/info.html', context)

class TyskaView(View):
    def get(self, request, *args, **kwargs):
        tysa = Alfabet.objects.filter(bogstav__bogstav__contains = 'A')
        context = {
            'a': tysa
        }
        
        return render(request, 'tysk/tyska.html',context) 
    
class TyskbView(View):
    def get(self, request, *args, **kwargs):
        tysb = Alfabet.objects.filter(bogstav__bogstav__contains='B')
        context = {
            'b': tysb
        }
        return render(request, 'tysk/tyskb.html', context)
    
class TyskCView(View):
    def get(self, request, *args, **kwargs):
        c = Alfabet.objects.filter(bogstav__bogstav__contains='C')
        context = {
            'c': c
        }
        return render(request, 'tysk/tyskc.html', context)
    
class TyskDView(View):
    def get(self, request, *args, **kwargs):
        d = Alfabet.objects.filter(bogstav__bogstav__contains='D')
        context = {
            'd': d
        }
        return render(request, 'tysk/tyskd.html', context)
    
class TyskEView(View):
    def get(self, request, *args, **kwargs):
        e = Alfabet.objects.filter(bogstav__bogstav__contains='E')
        context = {
            'e': e
        }
        return render(request, 'tysk/tyske.html', context)
    
class TyskFView(View):
    def get(self, request, *args, **kwargs):
        f = Alfabet.objects.filter(bogstav__bogstav__contains='F')
        context = {
            'f': f
        }
        return render(request, 'tysk/tyskf.html', context)
    
class TyskGView(View):
    def get(self, request, *args, **kwargs):
        g = Alfabet.objects.filter(bogstav__bogstav__contains='G')
        context = {
            'g': g
        }
        return render(request, 'tysk/tyskg.html', context)
    
class TyskHView(View):
    def get(self, request, *args, **kwargs):
        h = Alfabet.objects.filter(bogstav__bogstav__contains='H')
        context = {
            'h': h
        }
        return render(request, 'tysk/tyskh.html', context)
    
class TyskIView(View):
    def get(self, request, *args, **kwargs):
        i = Alfabet.objects.filter(bogstav__bogstav__contains='I')
        context = {
            'i': i
        }
        return render(request, 'tysk/tyski.html', context)
    
class TyskJView(View):
    def get(self, request, *args, **kwargs):
        j = Alfabet.objects.filter(bogstav__bogstav__contains='J')
        context = {
            'j': j
        }
        return render(request, 'tysk/tyskj.html', context)
    
class TyskKView(View):
    def get(self, request, *args, **kwargs):
        k = Alfabet.objects.filter(bogstav__bogstav__contains='K')
        context = {
            'k': k
        }
        return render(request, 'tysk/tyskk.html', context)
    
class TyskLView(View):
    def get(self, request, *args, **kwargs):
        l = Alfabet.objects.filter(bogstav__bogstav__contains='L')
        context = {
            'l': l
        }
        return render(request, 'tysk/tyskl.html', context)
    
class TyskMView(View):
    def get(self, request, *args, **kwargs):
        m = Alfabet.objects.filter(bogstav__bogstav__contains='M')
        context = {
            'm': m
        }
        return render(request, 'tysk/tyskm.html', context)
    
class TyskNView(View):
    def get(self, request, *args, **kwargs):
        n = Alfabet.objects.filter(bogstav__bogstav__contains='N')
        context = {
            'n': n
        }
        return render(request, 'tysk/tyskn.html', context)
    
class TyskOView(View):
    def get(self, request, *args, **kwargs):
        o = Alfabet.objects.filter(bogstav__bogstav__contains='O')
        context = {
            'o': o
        }
        return render(request, 'tysk/tysko.html', context)
    
class TyskPView(View):
    def get(self, request, *args, **kwargs):
        p = Alfabet.objects.filter(bogstav__bogstav__contains='P')
        context = {
            'p': p
        }
        return render(request, 'tysk/tyskp.html', context)
    
class TyskQView(View):
    def get(self, request, *args, **kwargs):
        q = Alfabet.objects.filter(bogstav__bogstav__contains='Q')
        context = {
            'q': q
        }
        return render(request, 'tysk/tyskq.html', context)
    
class TyskRView(View):
    def get(self, request, *args, **kwargs):
        r = Alfabet.objects.filter(bogstav__bogstav__contains='R')
        context = {
            'r': r
        }
        return render(request, 'tysk/tyskr.html', context)
    
class TyskSView(View):
    def get(self, request, *args, **kwargs):
        s = Alfabet.objects.filter(bogstav__bogstav__contains='S')
        context = {
            's': s
        }
        return render(request, 'tysk/tysks.html', context)
    
class TyskTView(View):
    def get(self, request, *args, **kwargs):
        t = Alfabet.objects.filter(bogstav__bogstav__contains='T')
        context = {
            't': t
        }
        return render(request, 'tysk/tyskt.html', context)
    
class TyskUView(View):
    def get(self, request, *args, **kwargs):
        u = Alfabet.objects.filter(bogstav__bogstav__contains='U')
        context = {
            'u': u
        }
        return render(request, 'tysk/tysku.html', context)
    
class TyskVView(View):
    def get(self, request, *args, **kwargs):
        v = Alfabet.objects.filter(bogstav__bogstav__contains='V')
        context = {
            'v': v
        }
        return render(request, 'tysk/tyskv.html', context)
    
class TyskWView(View):
    def get(self, request, *args, **kwargs):
        w = Alfabet.objects.filter(bogstav__bogstav__contains='W')
        context = {
            'w': w
        }
        return render(request, 'tysk/tyskw.html', context)
    
class TyskXView(View):
    def get(self, request, *args, **kwargs):
        x = Alfabet.objects.filter(bogstav__bogstav__contains='X')
        context = {
            'x': x
        }
        return render(request, 'tyskx.html', context)
    
class TyskYView(View):
    def get(self, request, *args, **kwargs):
        y = Alfabet.objects.filter(bogstav__bogstav__contains='Y')
        context = {
            'y': y
        }
        return render(request, 'tysk/tysky.html', context)

class TyskZView(View):
    def get(self, request, *args, **kwargs):
        z = Alfabet.objects.filter(bogstav__bogstav__contains='Z')
        context = {
            'z': z
        }
        return render(request, 'tysk/tyskz.html', context)
    
"""class Tilføj(View):
    def get(self, request, *args, **kwargs):
        form = EkstraForm()
        Alfabet = Alfabet.objects.all()
        return render(request, 'tysk/tyskplus.html', {
            'form': form,
            'Alfabet': Alfabet,
        })

    def post(self, request, *args, **kwargs):
        form = EkstraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/tysk/tyskplus')

        Alfabet = Alfabet.objects.all()
        return render(request, 'tysk/tyskplus.html', {
            'form': form,
            'Alfabet': Alfabet,
        })"""








# Create your views here.
