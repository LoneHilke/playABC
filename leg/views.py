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
    
"""class GætView(View):
    def get(self, request, *args, **kwargs):
        
        dana = random.choice(Alfabet.objects.all())
        danb = random.choice(Alfabet.objects.all())
        danc = random.choice(Alfabet.objects.all())
        dand = random.choice(Alfabet.objects.all())
        dane = random.choice(Alfabet.objects.all())
        danf = random.choice(Alfabet.objects.all())
        dang = random.choice(Alfabet.objects.all())
        danh = random.choice(Alfabet.objects.all())
        form1 = GætForm()

        context = {
            'dana': dana, 'danb': danb, 'danc': danc, 'dand': dand, 'dane': dane, 'danf': danf,
              'dang':dang, 'danh':danh,
            'form1': form1
        }
        return render(request, 'leg/gaet.html', context)

    def post(self, request, *args, **kwargs):
        form1 = GætForm(request.POST)
        resultat = None
        aktiv_model = None
        aktiv_id = None

    # Find ud af hvilken form der blev sendt
        if f"{dana}_id" in request.POST:
            aktiv_model = 'Bogstav'
            aktiv_id =  request.POST[f"{dana}_id"]
            obj = Bogstav.objects.get(id=aktiv_id)
        elif 'danb_id' in request.POST:
            aktiv_model = 'Alfabet'
            aktiv_id = request.POST.get('danb_id')
            obj = Bogstav.objects.get(id=aktiv_id)
        elif 'danc_id' in request.POST:
            aktiv_model = 'danc'
            aktiv_id = request.POST.get('c_id')
            obj = danc.objects.get(id=aktiv_id)
        elif 'dand_id' in request.POST:
            aktiv_model = 'dand'
            aktiv_id = request.POST.get('dand_id')
            obj = dand.objects.get(id=aktiv_id)
        elif 'dane_id' in request.POST:
            aktiv_model = 'dane'
            aktiv_id = request.POST.get('dane_id')
            obj = dane.objects.get(id=aktiv_id)
        elif 'danf_id' in request.POST:
            aktiv_model = 'danf'
            aktiv_id = request.POST.get('danf_id')
            obj = danf.objects.get(id=aktiv_id)
        elif 'dang_id' in request.POST:
            aktiv_model = 'dang'
            aktiv_id = request.POST.get('dang_id')
            obj = dang.objects.get(id=aktiv_id)
        elif 'danh_id' in request.POST:
            aktiv_model = 'danh'
            aktiv_id = request.POST.get('danh_id')
            obj = danh.objects.get(id=aktiv_id)
        if 'dani_id' in request.POST:
            aktiv_model = 'dani'
            aktiv_id = request.POST.get('dani_id')
            obj = dani.objects.get(id=aktiv_id)
        elif 'danj_id' in request.POST:
            aktiv_model = 'danj'
            aktiv_id = request.POST.get('danj_id')
            obj = danj.objects.get(id=aktiv_id)
        elif 'dank_id' in request.POST:
            aktiv_model = 'dank'
            aktiv_id = request.POST.get('dank_id')
            obj = danK.objects.get(id=aktiv_id)
        elif 'l_id' in request.POST:
            aktiv_model = 'l'
            aktiv_id = request.POST.get('l_id')
            obj = L.objects.get(id=aktiv_id)
        elif 'm_id' in request.POST:
            aktiv_model = 'm'
            aktiv_id = request.POST.get('m_id')
            obj = M.objects.get(id=aktiv_id)
        elif 'n_id' in request.POST:
            aktiv_model = 'n'
            aktiv_id = request.POST.get('n_id')
            obj = N.objects.get(id=aktiv_id)
        elif 'o_id' in request.POST:
            aktiv_model = 'o'
            aktiv_id = request.POST.get('o_id')
            obj = O.objects.get(id=aktiv_id)
        elif 'p_id' in request.POST:
            aktiv_model = 'p'
            aktiv_id = request.POST.get('p_id')
            obj = P.objects.get(id=aktiv_id)
        else:
            obj = None

    # Vurder gæt
        if obj and form1.is_valid():
            gæt = form1.cleaned_data['gæt'].strip().lower()
            korrekt = obj.ord.strip().lower()

            if gæt == korrekt:
                resultat = "✅ Korrekt!"
                # Vælg et nyt billede efter korrekt svar
                if aktiv_model == 'dana':
                    obj = random.choice(dana.objects.all())
                elif aktiv_model == 'danb':
                    obj = random.choice(danb.objects.all())
                elif aktiv_model == 'c':
                    obj = random.choice(C.objects.all())
                elif aktiv_model == 'd':
                    obj = random.choice(D.objects.all())
                elif aktiv_model == 'e':
                    obj = random.choice(E.objects.all())
                elif aktiv_model == 'f':
                    obj = random.choice(F.objects.all())
                elif aktiv_model == 'g':
                    obj = random.choice(G.objects.all())
                elif aktiv_model == 'h':
                    obj = random.choice(H.objects.all())
            else:
                resultat = f"❌ Forkert. Det rigtige svar er: {obj.danord}"

        # Alt indhold
            context = {
                'dana': random.choice(dana.objects.all()),
                'danb': random.choice(danb.objects.all()),
                'danc': random.choice(danc.objects.all()),
                'dand': random.choice(dand.objects.all()),
                'e': random.choice(E.objects.all()),
                'f': random.choice(F.objects.all()),
                'g': random.choice(G.objects.all()),
                'h': random.choice(H.objects.all()),
                'form1': form1,
                'resultat': resultat,
                'aktiv_model': aktiv_model,
                'aktiv_id': int(aktiv_id) if aktiv_id else None,
            }

            return render(request, 'leg/gaet.html', context

class GætView(View):
    def get(self, request, *args, **kwargs):
            context = {
            'Alfabet':Alfabet,
            'dana': random.choice(Alfabet.objects.all()),
            'danb': random.choice(Alfabet.objects.all()),
            "danc": random.choice(Alfabet.objects.all()),
            "dand": random.choice(Alfabet.objects.all()),
            "dane": random.choice(Alfabet.objects.all()),
            "danf": random.choice(Alfabet.objects.all()),
            "dang": random.choice(Alfabet.objects.all()),
            "danh": random.choice(Alfabet.objects.all()),
            "dani": random.choice(Alfabet.objects.all()),
            "danj": random.choice(Alfabet.objects.all()),
            "dank": random.choice(Alfabet.objects.all()),
            "danl": random.choice(Alfabet.objects.all()),
            "danm": random.choice(Alfabet.objects.all()),
            "dann": random.choice(Alfabet.objects.all()),
            "dano": random.choice(Alfabet.objects.all()),
            "danp": random.choice(Alfabet.objects.all()),
            "danq": random.choice(Alfabet.objects.all()),
            "danr": random.choice(Alfabet.objects.all()),
            "dans": random.choice(Alfabet.objects.all()),
            "dant": random.choice(Alfabet.objects.all()),
            "danu": random.choice(Alfabet.objects.all()),
            "danv": random.choice(Alfabet.objects.all()),
            "danw": random.choice(Alfabet.objects.all()),
            "danx": random.choice(Alfabet.objects.all()),
            "dany": random.choice(Alfabet.objects.all()),
            "danz": random.choice(Alfabet.objects.all()),
            "danæ": random.choice(Alfabet.objects.all()),
            "danø": random.choice(Alfabet.objects.all()),
            "danå": random.choice(Alfabet.objects.all()),
            "form1": GætForm(),
            "resultat": None,
            "aktiv_model": None,
            "aktiv_id": None,
           }

            return render(request, "leg/gaet.html", context)


   
    def post(self, request):
        bogstav_id = request.POST.get("bogstav_id")
        alfabet_id = request.POST.get("alfabet_id")

        bogstav = Bogstav.objects.get(id=bogstav_id)
        obj = Alfabet.objects.get(id=alfabet_id)

        gæt = request.POST.get("gæt", "").strip().lower()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        # NYT billede – KUN fra samme bogstav
        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gaet.html", {
            "obj": nyt_obj,
            "bogstav": bogstav,
            "resultat": resultat,
            "aktiv_id": alfabet_id,
        })"""

class GætView(View):
    def get(self, request):
        bogstaver = Bogstav.objects.all()
        billeder = {
            b.bogstav.lower(): Alfabet.objects.filter(bogstav=b).order_by("?").first()
            for b in bogstaver
        }

        return render(request, "leg/gaet.html", {
            "billeder": billeder,
            "form": GætForm(),
            "resultat": None,
            "aktiv_bogstav": None,
        })

    def post(self, request):
        bogstav_id = request.POST.get("bogstav_id")
        alfabet_id = request.POST.get("alfabet_id")

        bogstav = Bogstav.objects.get(id=bogstav_id)
        obj = Alfabet.objects.get(id=alfabet_id)

        gæt = request.POST.get("gæt", "").lower().strip()
        korrekt = obj.danord.lower()

        resultat = "✅ Korrekt!" if gæt == korrekt else f"❌ Forkert: {obj.danord}"

        nyt_obj = Alfabet.objects.filter(bogstav=bogstav).order_by("?").first()

        return render(request, "leg/gaet.html", {
            "billeder": {bogstav.bogstav.lower(): nyt_obj},
            "form": GætForm(),
            "resultat": resultat,
            "aktiv_bogstav": bogstav.bogstav.lower(),
        })


        

        
