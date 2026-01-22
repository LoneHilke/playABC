from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class Forside(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'forside/forside.html')