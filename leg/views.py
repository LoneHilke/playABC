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

        return render(request, "leg/dang.html", {
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