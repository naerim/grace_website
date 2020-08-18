from django.shortcuts import render, redirect
from .models import Recommend
from django.views.generic import ListView
from django.contrib import auth


class RecommendList(ListView):
    model = Recommend

    def get_queryset(self):
        return Recommend.objects.order_by('-created')


def index(request):
    recommends = Recommend.objects.all()
    return render(
        request,
        'grace/main.html',
        {
            'recommends': recommends,
        }
    )


def logout(request):
    auth.logout(request)
    return redirect('../')


def myPage(request):
    return render(request, 'grace/myPage.html')


def tutor(request):
    return render(request, 'grace/tutor.html')
