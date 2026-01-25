from django.shortcuts import render, redirect
from django.views import View
from dansk.models import Alfabet, Bogstav
#from .forms import EkstraForm

# Create your views here.
class Base(View):
    def get(self, request, *args, **kwargs):
        enga = Alfabet.objects.filter(bogstav__bogstav__contains='enga')
        engb = Alfabet.objects.filter(bogstav__bogstav__contains='engb')
        engc = Alfabet.objects.filter(bogstav__bogstav__contains='engc')
        engd = Alfabet.objects.filter(bogstav__bogstav__contains='engd')
        enge = Alfabet.objects.filter(bogstav__bogstav__contains='enge')
        engf = Alfabet.objects.filter(bogstav__bogstav__contains='engf')
        engg = Alfabet.objects.filter(bogstav__bogstav__contains='engg')
        engh = Alfabet.objects.filter(bogstav__bogstav__contains='engh')
        engi = Alfabet.objects.filter(bogstav__bogstav__contains='engi')
        engj = Alfabet.objects.filter(bogstav__bogstav__contains='engj')
        engk = Alfabet.objects.filter(bogstav__bogstav__contains='engk')
        engl = Alfabet.objects.filter(bogstav__bogstav__contains='engl')
        engm = Alfabet.objects.filter(bogstav__bogstav__contains='engm')
        engn = Alfabet.objects.filter(bogstav__bogstav__contains='N')
        engo = Alfabet.objects.filter(bogstav__bogstav__contains='O')
        engp = Alfabet.objects.filter(bogstav__bogstav__contains='P')
        engq = Alfabet.objects.filter(bogstav__bogstav__contains='Q')
        engr = Alfabet.objects.filter(bogstav__bogstav__contains='R')
        engs = Alfabet.objects.filter(bogstav__bogstav__contains='S')
        engt = Alfabet.objects.filter(bogstav__bogstav__contains='T')
        engu = Alfabet.objects.filter(bogstav__bogstav__contains='U')
        engv = Alfabet.objects.filter(bogstav__bogstav__contains='V')
        engw = Alfabet.objects.filter(bogstav__bogstav__contains='W')
        engx = Alfabet.objects.filter(bogstav__bogstav__contains='X')
        engy = Alfabet.objects.filter(bogstav__bogstav__contains='Y')
        engz = Alfabet.objects.filter(bogstav__bogstav__contains='Z')
       
        
        context = {
            'enga': enga,
            'engb': engb,
            'engc': engc,
            'engd': engd,
            'enge': enge,
            'engf': engf,
            'engg': engg,
            'engh': engh,
            'engi': engi,
            'engj': engj,
            'engk': engk,
            'engl': engl,
            'engm': engm,
            'n': engn,
            'o': engo,
            'p': engp,
            'q': engq,
            'r': engr,
            's': engs,
            't': engt,
            'u': engu,
            'v': engv,
            'w': engw,
            'x': engx,
            'y': engy,
            'z': engz,
                        
        }
        return render(request, 'engelsk/info.html')
    
class EngelskAView(View):
    def get(self, request, *args, **kwargs):
        enga = Alfabet.objects.filter(bogstav__bogstav__contains = 'enga')
        context = {
            'enga': enga
        }
        return render(request, 'engelsk/engelska.html', context)
    
class EngelskBView(View):
    def get(self, request, *args, **kwargs):
        engb = Alfabet.objects.filter(bogstav__bogstav__contains = 'engb')
        context = {
            'engb': engb
        }
        return render(request, 'engelsk/engelskb.html', context)
    
class EngelskCView(View):
    def get(self, request, *args, **kwargs):
        engc = Alfabet.objects.filter(bogstav__bogstav__contains = 'engc')
        context = {
            'engc': engc
        }
        return render(request, 'engelsk/engelskc.html', context)   

class EngelskDView(View):
    def get(self, request, *args, **kwargs):
        engd = Alfabet.objects.filter(bogstav__bogstav__contains = 'engd')
        context = {
            'engd': engd
        }
        return render(request, 'engelsk/engelskd.html', context) 
    
class EngelskEView(View):
    def get(self, request, *args, **kwargs):
        enge = Alfabet.objects.filter(bogstav__bogstav__contains = 'enge')
        context = {
            'enge': enge
        }
        return render(request, 'engelsk/engelske.html', context)
    
class EngelskFView(View):
    def get(self, request, *args, **kwargs):
        engf = Alfabet.objects.filter(bogstav__bogstav__contains = 'engf')
        context = {
            'engf': engf
        }
        return render(request, 'engelsk/engelskf.html', context)
    
class EngelskGView(View):
    def get(self, request, *args, **kwargs):
        engg = Alfabet.objects.filter(bogstav__bogstav__contains = 'engg')
        context = {
            'engg': engg
        }
        return render(request, 'engelsk/engelskg.html', context)
    
class EngelskHView(View):
    def get(self, request, *args, **kwargs):
        engh = Alfabet.objects.filter(bogstav__bogstav__contains = 'engh')
        context = {
            'engh': engh
        }
        return render(request, 'engelsk/engelskh.html', context)
    
class EngelskIView(View):
    def get(self, request, *args, **kwargs):
        engi = Alfabet.objects.filter(bogstav__bogstav__contains = 'engi')
        context = {
            'engi': engi
        }
        return render(request, 'engelsk/engelski.html', context)   

class EngelskJView(View):
    def get(self, request, *args, **kwargs):
        engj = Alfabet.objects.filter(bogstav__bogstav__contains = 'engj')
        context = {
            'engj': engj
        }
        return render(request, 'engelsk/engelskd.html', context) 
    
class EngelskKView(View):
    def get(self, request, *args, **kwargs):
        engk = Alfabet.objects.filter(bogstav__bogstav__contains = 'engk')
        context = {
            'engk': engk
        }
        return render(request, 'engelsk/engelskk.html', context)
    
class EngelskLView(View):
    def get(self, request, *args, **kwargs):
        engl = Alfabet.objects.filter(bogstav__bogstav__contains = 'engl')
        context = {
            'engl': engl
        }
        return render(request, 'engelsk/engelskl.html', context)
    
class EngelskMView(View):
    def get(self, request, *args, **kwargs):
        engm = Alfabet.objects.filter(bogstav__bogstav__contains = 'engm')
        context = {
            'engm': engm
        }
        return render(request, 'engelsk/engelskm.html', context)
    
class EngelskNView(View):
    def get(self, request, *args, **kwargs):
        engn = Alfabet.objects.filter(bogstav__bogstav__contains = 'engn')
        context = {
            'engn': engn
        }
        return render(request, 'engelsk/engelskn.html', context)
    
class EngelskOView(View):
    def get(self, request, *args, **kwargs):
        engo = Alfabet.objects.filter(bogstav__bogstav__contains = 'engo')
        context = {
            'engo': engo
        }
        return render(request, 'engelsk/engelsko.html', context)
    
class EngelskPView(View):
    def get(self, request, *args, **kwargs):
        engp = Alfabet.objects.filter(bogstav__bogstav__contains = 'engp')
        context = {
            'engp': engp
        }
        return render(request, 'engelsk/engelskp.html', context)
    
class EngelskQView(View):
    def get(self, request, *args, **kwargs):
        engq = Alfabet.objects.filter(bogstav__bogstav__contains = 'engq')
        context = {
            'engq': engq
        }
        return render(request, 'engelsk/engelskq.html', context)
    
class EngelskRView(View):
    def get(self, request, *args, **kwargs):
        engr = Alfabet.objects.filter(bogstav__bogstav__contains = 'engr')
        context = {
            'engr': engr
        }
        return render(request, 'engelsk/engelskr.html', context)
    
class EngelskSView(View):
    def get(self, request, *args, **kwargs):
        engs = Alfabet.objects.filter(bogstav__bogstav__contains = 'engs')
        context = {
            'engs': engs
        }
        return render(request, 'engelsk/engelsks.html', context)
    
class EngelskTView(View):
    def get(self, request, *args, **kwargs):
        engt = Alfabet.objects.filter(bogstav__bogstav__contains = 'engt')
        context = {
            'engt': engt
        }
        return render(request, 'engelsk/engelskt.html', context)
    
class EngelskUView(View):
    def get(self, request, *args, **kwargs):
        engu = Alfabet.objects.filter(bogstav__bogstav__contains = 'engu')
        context = {
            'engu': engu
        }
        return render(request, 'engelsk/engelsku.html', context)

class EngelskVView(View):
    def get(self, request, *args, **kwargs):
        engv = Alfabet.objects.filter(bogstav__bogstav__contains = 'engv')
        context = {
            'engv': engv
        }
        return render(request, 'engelsk/engelskv.html', context)
    
class EngelskWView(View):
    def get(self, request, *args, **kwargs):
        engw = Alfabet.objects.filter(bogstav__bogstav__contains = 'engw')
        context = {
            'engw': engw
        }
        return render(request, 'engelsk/engelskw.html', context)
    
class EngelskXView(View):
    def get(self, request, *args, **kwargs):
        engx = Alfabet.objects.filter(bogstav__bogstav__contains = 'engx')
        context = {
            'engx': engx
        }
        return render(request, 'engelsk/engelskx.html', context)
    
class EngelskYView(View):
    def get(self, request, *args, **kwargs):
        engy = Alfabet.objects.filter(bogstav__bogstav__contains = 'engy')
        context = {
            'engy': engy
        }
        return render(request, 'engelsk/engelsky.html', context)   

class EngelskZView(View):
    def get(self, request, *args, **kwargs):
        engz = Alfabet.objects.filter(bogstav__bogstav__contains = 'engz')
        context = {
            'engz': engz
        }
        return render(request, 'engelsk/engelskz.html', context) 
    
"""class Tilføj(View):
    def get(self, request, *args, **kwargs):
        form = EkstraForm()
        Alfabet = Alfabet.objects.all()
        return render(request, 'engelsk/engadd.html', {
            'form': form,
            'Alfabet': Alfabet,
        })

    def post(self, request, *args, **kwargs):
        form = EkstraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/engelsk/engadd')

        Alfabet = Alfabet.objects.all()
        return render(request, 'dansk/tilføj.html', {
            'form': form,
            'Alfabet': Alfabet,
        })"""
# Create your views here.
