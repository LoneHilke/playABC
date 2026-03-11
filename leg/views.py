from django.shortcuts import render, redirect
from django.views import View
from dansk.models import  Alfabet, Bogstav
from .forms import GætForm, EkstraForm
import random

class Base(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'leg/base.html')
# Create your views here.

class Tilføj(View):
    def get(self, request, *args, **kwargs):
        form = EkstraForm()
        alfabet = Alfabet.objects.all()
        return render(request, 'leg/tilføj.html', {
            'form': form,
            'alfabet': alfabet,
        })

    def post(self, request, *args, **kwargs):
        form = EkstraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/leg/tilføj')

        alfabet = Alfabet.objects.all()
        return render(request, 'leg/tilføj.html', {
            'form': form,
            'alfabet': alfabet,
        })
    

class Gæt2View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'leg/gaet2.html')

class GætaView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="dana")
        dana = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gæta.html", {
            "dana": dana,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gæta.html", {
            "dana": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })

        

class GætbView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danb")
        danb = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætb.html", {
            "danb": danb,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætb.html", {
            "danb": nyt_obj,
            "form1": GætForm(),
            "resultat": resultat,
        })

class GætcView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danc")
        danc = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætc.html", {
            "danc": danc,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætc.html", {
            "danc": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætdView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="dand")
        dand = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætd.html", {
            "dand": dand,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætd.html", {
            "dand": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })

class GæteView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="dane")
        dane = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gæte.html", {
            "dane": dane,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gæte.html", {
            "dane": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætfView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danf")
        danf = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætf.html", {
            "danf": danf,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætf.html", {
            "danf": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætgView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="dang")
        dang = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætg.html", {
            "dang": dang,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætg.html", {
            "dang": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GæthView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danh")
        danh = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gæth.html", {
            "danh": danh,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gæth.html", {
            "danh": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætiView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="dani")
        dani = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gæti.html", {
            "dani": dani,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gæti.html", {
            "dani": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætjView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danj")
        danj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætj.html", {
            "danj": danj,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætj.html", {
            "danj": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætkView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="dank")
        dank = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætk.html", {
            "dank": dank,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætk.html", {
            "dank": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætlView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danl")
        danl = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætl.html", {
            "danl": danl,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætl.html", {
            "danl": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætmView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danm")
        danm = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætm.html", {
            "danm": danm,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætm.html", {
            "danm": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætnView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="dann")
        dann = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætn.html", {
            "dann": dann,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætn.html", {
            "dann": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætoView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="dano")
        dano = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gæto.html", {
            "dano": dano,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gæto.html", {
            "dano": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætpView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danp")
        danp = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætp.html", {
            "danp": danp,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætp.html", {
            "danp": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætqView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danq")
        danq = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætq.html", {
            "danq": danq,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætq.html", {
            "danq": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætrView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danr")
        danr = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætr.html", {
            "danr": danr,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætr.html", {
            "danr": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætsView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="dans")
        dans = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gæts.html", {
            "dans": dans,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gæts.html", {
            "dans": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GættView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="dant")
        dant = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætt.html", {
            "dant": dant,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætt.html", {
            "dant": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætuView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danu")
        danu = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætu.html", {
            "danu": danu,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætu.html", {
            "danu": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætvView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danv")
        danv = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætv.html", {
            "danv": danv,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætv.html", {
            "danv": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætwView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danw")
        danw = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætw.html", {
            "danw": danw,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætw.html", {
            "danw": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætxView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danx")
        danx = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætx.html", {
            "danx": danx,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætx.html", {
            "danx": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætyView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="dany")
        dany = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gæty.html", {
            "dany": dany,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gæty.html", {
            "dany": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætzView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danz")
        danz = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætz.html", {
            "danz": danz,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætz.html", {
            "danz": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætæView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danæ")
        danæ = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætæ.html", {
            "danæ": danæ,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætæ.html", {
            "danæ": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætøView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danø")
        danø = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætø.html", {
            "danø": danø,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætø.html", {
            "danø": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GætåView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="danå")
        danå = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætå.html", {
            "danå": danå,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gætå.html", {
            "danå": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'leg/gues.html')
    
class GuesaView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="enga")
        enga = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesa.html", {
            "enga": enga,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesa.html", {
            "enga": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuesbView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engb")
        engb = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesb.html", {
            "engb": engb,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesb.html", {
            "engb": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuescView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engc")
        engc = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesc.html", {
            "engc": engc,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesc.html", {
            "engc": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuesdView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engd")
        engd = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesd.html", {
            "engd": engd,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesd.html", {
            "engd": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GueseView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="enge")
        enge = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guese.html", {
            "enge": enge,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guese.html", {
            "enge": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuesfView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engf")
        engf = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesf.html", {
            "engf": engf,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesf.html", {
            "engf": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuesgView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engg")
        engg = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesg.html", {
            "engg": engg,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesg.html", {
            "engg": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GueshView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engh")
        engh = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesh.html", {
            "engh": engh,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesh.html", {
            "engh": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuesiView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engi")
        engi = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesi.html", {
            "engi": engi,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesi.html", {
            "engi": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuesjView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engj")
        engj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesj.html", {
            "engj": engj,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesj.html", {
            "engj": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GueskView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engk")
        engk = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesk.html", {
            "engk": engk,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesk.html", {
            "engk": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GueslView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engl")
        engl = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesl.html", {
            "engl": engl,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesl.html", {
            "engl": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuesmView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engm")
        engm = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesm.html", {
            "engm": engm,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesm.html", {
            "engm": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuesnView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engn")
        engn = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesn.html", {
            "engn": engn,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesn.html", {
            "engn": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuesoView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engo")
        engo = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gueso.html", {
            "engo": engo,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gueso.html", {
            "engo": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuespView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engp")
        engp = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesp.html", {
            "engp": engp,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesp.html", {
            "engp": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuesqView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engq")
        engq = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesq.html", {
            "engq": engq,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesq.html", {
            "engq": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuesrView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engr")
        engr = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesr.html", {
            "engr": engr,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesr.html", {
            "engr": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuessView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engs")
        engs = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guess.html", {
            "engs": engs,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guess.html", {
            "engs": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuestView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engt")
        engt = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guest.html", {
            "engt": engt,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guest.html", {
            "engt": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuesuView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engu")
        engu = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesu.html", {
            "engu": engu,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesu.html", {
            "engu": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuesvView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engv")
        engv = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesv.html", {
            "engv": engv,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesv.html", {
            "engv": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GueswView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engw")
        engw = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesw.html", {
            "engw": engw,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesw.html", {
            "engw": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuesxView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engx")
        engx = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesx.html", {
            "engx": engx,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesx.html", {
            "engx": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GuesyView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engy")
        engy = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesy.html", {
            "engy": engy,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesy.html", {
            "engy": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class GueszView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="engz")
        engz = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesz.html", {
            "engz": engz,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/guesz.html", {
            "engz": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'leg/rad.html')
    
class RadaView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysa")
        tysa = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/rada.html", {
            "tysa": tysa,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/rada.html", {
            "tysa": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadbView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysb")
        tysb = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radb.html", {
            "tysb": tysb,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radb.html", {
            "tysb": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadcView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysc")
        tysc = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radc.html", {
            "tysc": tysc,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radc.html", {
            "tysc": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RaddView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysd")
        tysd = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radd.html", {
            "tysd": tysd,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radd.html", {
            "tysd": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadeView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tyse")
        tyse = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/rade.html", {
            "tyse": tyse,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/rade.html", {
            "tyse": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadfView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysf")
        tysf = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radf.html", {
            "tysf": tysf,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radf.html", {
            "tysf": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadgView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysg")
        tysg = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radg.html", {
            "tysg": tysg,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radg.html", {
            "tysg": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadhView(View):
    def get(self, request):
            bogstav = Bogstav.objects.get(bogstav="tysh")
            tysh = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

            return render(request, "leg/radh.html", {
            "tysh": tysh,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radh.html", {
            "tysh": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadiView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysi")
        tysi = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radi.html", {
            "tysi": tysi,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radi.html", {
            "tysi": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadjView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysj")
        tysj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radj.html", {
            "tysj": tysj,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radj.html", {
            "tysj": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadkView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysk")
        tysk = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radk.html", {
            "tysk": tysk,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radk.html", {
            "tysk": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadlView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysl")
        tysl = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radl.html", {
            "tysl": tysl,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radl.html", {
            "tysl": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadmView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysm")
        tysm = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radm.html", {
            "tysm": tysm,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radm.html", {
            "tysm": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })

class RadnView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysn")
        tysn = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radn.html", {
            "tysn": tysn,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radn.html", {
            "tysn": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadoView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tyso")
        tyso = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/rado.html", {
            "tyso": tyso,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/rado.html", {
            "tyso": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadpView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysp")
        tysp = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radp.html", {
            "tysp": tysp,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radp.html", {
            "tysp": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadqView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysq")
        tysq = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radq.html", {
            "tysq": tysq,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radq.html", {
            "tysq": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadrView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysr")
        tysr = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radr.html", {
            "tysr": tysr,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radr.html", {
            "tysr": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadsView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tyss")
        tyss = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/rads.html", {
            "tyss": tyss,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/rads.html", {
            "tyss": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadtView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tyst")
        tyst = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radt.html", {
            "tyst": tyst,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radt.html", {
            "tyst": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RaduView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysu")
        tysu = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radu.html", {
            "tysu": tysu,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radu.html", {
            "tysu": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadvView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysv")
        tysv = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radv.html", {
            "tysv": tysv,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radv.html", {
            "tysv": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadwView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysw")
        tysw = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radw.html", {
            "tysw": tysw,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radw.html", {
            "tysw": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadxView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysx")
        tysx = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radx.html", {
            "tysx": tysx,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radx.html", {
            "tysx": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadyView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysy")
        tysy = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/rady.html", {
            "tysy": tysy,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/rady.html", {
            "tysy": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class RadzView(View):
    def get(self, request):
        bogstav = Bogstav.objects.get(bogstav="tysz")
        tysz = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radz.html", {
            "tysz": tysz,
            "form": GætForm(),
            "resultat": None,
        })

    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)
        bogstav = obj.bogstav.first()

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/radz.html", {
            "tysz": nyt_obj,
            "form": GætForm(),
            "resultat": resultat,
        })
    
class ManglerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'leg/mangler.html')
    
class OpgaveView(View):
    def get(self, request):
        obj = Alfabet.objects.order_by("?").first()

        return render(request, "leg/opgave.html", {
            "obj": obj,
            "resultat": None,
        })
    
    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.order_by("?").first()

        return render(request, "leg/opgave.html", {
            "obj": nyt_obj,
            "resultat": resultat,
        })
    
class Opgave1View(View):
    def get(self, request):
        obj = Alfabet.objects.order_by("?").first()

        return render(request, "leg/opgave1.html", {
            "obj": obj,
            "resultat": None,
        })
    
    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.tysord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.tysord}"

        nyt_obj = Alfabet.objects.order_by("?").first()

        return render(request, "leg/opgave1.html", {
            "obj": nyt_obj,
            "resultat": resultat,
        })
    
class Opgave2View(View):
    def get(self, request):
        obj = Alfabet.objects.order_by("?").first()

        return render(request, "leg/opgave2.html", {
            "obj": obj,
            "resultat": None,
        })
    
    def post(self, request):
        alfabet_id = request.POST.get("alfabet_id")
        obj = Alfabet.objects.get(id=alfabet_id)

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.engord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.engord}"

        nyt_obj = Alfabet.objects.order_by("?").first()

        return render(request, "leg/opgave2.html", {
            "obj": nyt_obj,
            "resultat": resultat,
        })
    
class MemoryView(View):

    def get(self, request):

        items = list(Alfabet.objects.all())
        valgt = random.sample(items, 8)

        cards = []

        for item in valgt:
            cards.append({
                "type": "image",
                "value": item.image.url,
                "match": item.id
            })

            cards.append({
                "type": "letter",
                "value": item.danord[0],   # første bogstav
                "match": item.id
            })

        random.shuffle(cards)

        return render(request, "leg/memory.html", {
            "cards": cards
        })
    
class MemoryengView(View):

    def get(self, request):

        items = list(Alfabet.objects.all())
        valgt = random.sample(items, 8)

        cards = []

        for item in valgt:
            cards.append({
                "type": "image",
                "value": item.image.url,
                "match": item.id
            })

            cards.append({
                "type": "letter",
                "value": item.engord[0],   # første bogstav
                "match": item.id
            })

        random.shuffle(cards)

        return render(request, "leg/memoryeng.html", {
            "cards": cards
        })
    
class MemorytysView(View):

    def get(self, request):

        items = list(Alfabet.objects.all())
        valgt = random.sample(items, 8)

        cards = []

        for item in valgt:
            cards.append({
                "type": "image",
                "value": item.image.url,
                "match": item.id
            })

            cards.append({
                "type": "letter",
                "value": item.tysord[0],   # første bogstav
                "match": item.id
            })

        random.shuffle(cards)

        return render(request, "leg/memory.html", {
            "cards": cards
        })