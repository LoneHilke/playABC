from django.shortcuts import render, redirect
from django.views import View
from dansk.models import Alfabet, Bogstav#, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, Æ, Ø, Å, Alfabet, Ekstra
#from .forms import GætForm, EkstraForm
import random

class Base(View):
    def get(self, request, *args, **kwargs):
        tysa = Alfabet.objects.filter(bogstav__bogstav__contains='tysA')
        tysb = Alfabet.objects.filter(bogstav__bogstav__contains='tysB')
        tysc = Alfabet.objects.filter(bogstav__bogstav__contains='tysC')
        tysd = Alfabet.objects.filter(bogstav__bogstav__contains='tysD')
        tyse = Alfabet.objects.filter(bogstav__bogstav__contains='tysE')
        tysf = Alfabet.objects.filter(bogstav__bogstav__contains='tysF')  
        tysg = Alfabet.objects.filter(bogstav__bogstav__contains='tysG')
        tysh = Alfabet.objects.filter(bogstav__bogstav__contains='tysH')
        tysi = Alfabet.objects.filter(bogstav__bogstav__contains='tysI')
        tysj = Alfabet.objects.filter(bogstav__bogstav__contains='tysJ')
        tysk = Alfabet.objects.filter(bogstav__bogstav__contains='tysK')
        tysl = Alfabet.objects.filter(bogstav__bogstav__contains='tysL')
        tysm = Alfabet.objects.filter(bogstav__bogstav__contains='tysM')
        tysn = Alfabet.objects.filter(bogstav__bogstav__contains='tysN')
        tyso = Alfabet.objects.filter(bogstav__bogstav__contains='tysO')
        tysp = Alfabet.objects.filter(bogstav__bogstav__contains='tysP')
        tysq = Alfabet.objects.filter(bogstav__bogstav__contains='tysQ')
        tysr = Alfabet.objects.filter(bogstav__bogstav__contains='tysR')
        tyss = Alfabet.objects.filter(bogstav__bogstav__contains='tysS')
        tyst = Alfabet.objects.filter(bogstav__bogstav__contains='tysT')
        tysu = Alfabet.objects.filter(bogstav__bogstav__contains='tysU')
        tysv = Alfabet.objects.filter(bogstav__bogstav__contains='tysV')
        tysw = Alfabet.objects.filter(bogstav__bogstav__contains='tysW')
        tysx = Alfabet.objects.filter(bogstav__bogstav__contains='tysX')
        tysy = Alfabet.objects.filter(bogstav__bogstav__contains='tysY')
        tysz = Alfabet.objects.filter(bogstav__bogstav__contains='tysZ')
        
        
        context = {
            'tysa': tysa,
            'tysb': tysb,
            'tysc': tysc,
            'tysd': tysd,
            'tyse': tyse,
            'tysf': tysf,
            'tysg': tysg,
            'tysh': tysh,
            'tysi': tysi,
            'tysj': tysj,
            'tysk': tysk,
            'tysl': tysl,
            'tysm': tysm,
            'tysn': tysn,
            'tyso': tyso,
            'tysp': tysp,
            'tysq': tysq,
            'tysr': tysr,
            'tyss': tyss,
            'tyst': tyst,
            'tysu': tysu,
            'tysv': tysv,
            'tysw': tysw,
            'tysx': tysx,
            'tysy': tysy,
            'tysz': tysz,
            
            
        }
        return render(request, 'tysk/info.html', context)

class TyskaView(View):
    def get(self, request, *args, **kwargs):
        tysa = Alfabet.objects.filter(bogstav__bogstav__contains = 'tysA')
        tysa = tysa.order_by("tysord")
        context = {
            'tysa': tysa
        }
        
        return render(request, 'tysk/tyska.html',context) 
    
class TyskbView(View):
    def get(self, request, *args, **kwargs):
        tysb = Alfabet.objects.filter(bogstav__bogstav__contains='tysB')
        tysb = tysb.order_by("tysord")
        context = {
            'tysb': tysb
        }
        return render(request, 'tysk/tyskb.html', context)
    
class TyskCView(View):
    def get(self, request, *args, **kwargs):
        tysc = Alfabet.objects.filter(bogstav__bogstav__contains='tysC')
        tysc = tysc.order_by("tysord")
        context = {
            'tysc': tysc
        }
        return render(request, 'tysk/tyskc.html', context)
    
class TyskDView(View):
    def get(self, request, *args, **kwargs):
        tysd = Alfabet.objects.filter(bogstav__bogstav__contains='tysD')
        tysd = tysd.order_by("tysord")
        context = {
            'tysd': tysd
        }
        return render(request, 'tysk/tyskd.html', context)
    
class TyskEView(View):
    def get(self, request, *args, **kwargs):
        tyse = Alfabet.objects.filter(bogstav__bogstav__contains='tysE')
        tyse = tyse.order_by("tysord")
        context = {
            'tyse': tyse
        }
        return render(request, 'tysk/tyske.html', context)
    
class TyskFView(View):
    def get(self, request, *args, **kwargs):
        tysf = Alfabet.objects.filter(bogstav__bogstav__contains='tysF')
        tysf = tysf.order_by("tysord")
        context = {
            'tysf': tysf
        }
        return render(request, 'tysk/tyskf.html', context)
    
class TyskGView(View):
    def get(self, request, *args, **kwargs):
        tysg = Alfabet.objects.filter(bogstav__bogstav__contains='tysG')
        tysg = tysg.order_by("tysord")
        context = {
            'tysg': tysg
        }
        return render(request, 'tysk/tyskg.html', context)
    
class TyskHView(View):
    def get(self, request, *args, **kwargs):
        tysh = Alfabet.objects.filter(bogstav__bogstav__contains='tysH')
        tysh = tysh.order_by("tysord")
        context = {
            'tysh': tysh
        }
        return render(request, 'tysk/tyskh.html', context)
    
class TyskIView(View):
    def get(self, request, *args, **kwargs):
        tysi = Alfabet.objects.filter(bogstav__bogstav__contains='tysvI')
        tysi = tysi.order_by("tysord")
        context = {
            'tysi': tysi
        }
        return render(request, 'tysk/tyski.html', context)
    
class TyskJView(View):
    def get(self, request, *args, **kwargs):
        tysj = Alfabet.objects.filter(bogstav__bogstav__contains='tysJ')
        tysj = tysj.order_by("tysord")
        context = {
            'tysj': tysj
        }
        return render(request, 'tysk/tyskj.html', context)
    
class TyskKView(View):
    def get(self, request, *args, **kwargs):
        tysk = Alfabet.objects.filter(bogstav__bogstav__contains='tysK')
        tysk = tysk.order_by("tysord")
        context = {
            'tysk': tysk
        }
        return render(request, 'tysk/tyskk.html', context)
    
class TyskLView(View):
    def get(self, request, *args, **kwargs):
        tysl = Alfabet.objects.filter(bogstav__bogstav__contains='tysL')
        tysl = tysl.order_by("tysord")
        context = {
            'tysl': tysl
        }
        return render(request, 'tysk/tyskl.html', context)
    
class TyskMView(View):
    def get(self, request, *args, **kwargs):
        tysm = Alfabet.objects.filter(bogstav__bogstav__contains='tysM')
        tysm = tysm.order_by("tysord")
        context = {
            'tysm': tysm
        }
        return render(request, 'tysk/tyskm.html', context)
    
class TyskNView(View):
    def get(self, request, *args, **kwargs):
        tysn = Alfabet.objects.filter(bogstav__bogstav__contains='tysN')
        tysn = tysn.order_by("tysord")
        context = {
            'tysn': tysn
        }
        return render(request, 'tysk/tyskn.html', context)
    
class TyskOView(View):
    def get(self, request, *args, **kwargs):
        tyso = Alfabet.objects.filter(bogstav__bogstav__contains='tysO')
        tyso = tyso.order_by("tysord")
        context = {
            'tyso': tyso
        }
        return render(request, 'tysk/tysko.html', context)
    
class TyskPView(View):
    def get(self, request, *args, **kwargs):
        tysp = Alfabet.objects.filter(bogstav__bogstav__contains='tysP')
        tysp = tysp.order_by("tysord")
        context = {
            'tysp': tysp
        }
        return render(request, 'tysk/tyskp.html', context)
    
class TyskQView(View):
    def get(self, request, *args, **kwargs):
        tysq = Alfabet.objects.filter(bogstav__bogstav__contains='tysQ')
        tysq = tysq.order_by("tysord")
        context = {
            'tysq': tysq
        }
        return render(request, 'tysk/tyskq.html', context)
    
class TyskRView(View):
    def get(self, request, *args, **kwargs):
        tysr = Alfabet.objects.filter(bogstav__bogstav__contains='tysR')
        tysr = tysr.order_by("tysord")
        context = {
            'tysr': tysr
        }
        return render(request, 'tysk/tyskr.html', context)
    
class TyskSView(View):
    def get(self, request, *args, **kwargs):
        tyss = Alfabet.objects.filter(bogstav__bogstav__contains='tysS')
        tyss = tyss.order_by("tysord")
        context = {
            'tyss': tyss
        }
        return render(request, 'tysk/tysks.html', context)
    
class TyskTView(View):
    def get(self, request, *args, **kwargs):
        tyst = Alfabet.objects.filter(bogstav__bogstav__contains='tysT')
        tyst = tyst.order_by("tysord")
        context = {
            'tyst': tyst
        }
        return render(request, 'tysk/tyskt.html', context)
    
class TyskUView(View):
    def get(self, request, *args, **kwargs):
        tysu = Alfabet.objects.filter(bogstav__bogstav__contains='tysU')
        tysu = tysu.order_by("tysord")
        context = {
            'tysu': tysu
        }
        return render(request, 'tysk/tysku.html', context)
    
class TyskVView(View):
    def get(self, request, *args, **kwargs):
        tysv = Alfabet.objects.filter(bogstav__bogstav__contains='tysV')
        tysv = tysv.order_by("tysord")
        context = {
            'tysv': tysv
        }
        return render(request, 'tysk/tyskv.html', context)
    
class TyskWView(View):
    def get(self, request, *args, **kwargs):
        tysw = Alfabet.objects.filter(bogstav__bogstav__contains='tysW')
        tysw = tysw.order_by("tysord")
        context = {
            'tysw': tysw
        }
        return render(request, 'tysk/tyskw.html', context)
    
class TyskXView(View):
    def get(self, request, *args, **kwargs):
        tysx = Alfabet.objects.filter(bogstav__bogstav__contains='tysX')
        tysx = tysx.order_by("tysord")
        context = {
            'tysx': tysx
        }
        return render(request, 'tyskx.html', context)
    
class TyskYView(View):
    def get(self, request, *args, **kwargs):
        tysy = Alfabet.objects.filter(bogstav__bogstav__contains='tysY')
        tysy = tysy.order_by("tysord")
        context = {
            'tysy': tysy
        }
        return render(request, 'tysk/tysky.html', context)

class TyskZView(View):
    def get(self, request, *args, **kwargs):
        tysz = Alfabet.objects.filter(bogstav__bogstav__contains='tysZ')
        tysz = tysz.order_by("tysord")
        context = {
            'tysz': tysz
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
