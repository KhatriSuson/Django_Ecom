from django.shortcuts import render
from django.views.generic import View
from .models import *


# Create your views here.

class Base(View):
    views = {}



class HomeView(Base):
    def get(self, request):
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        return render(request, 'index.html',self.views)