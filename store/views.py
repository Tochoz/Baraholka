from django.shortcuts import render, redirect, reverse

def redirectHome(request):
    return redirect(reverse('home'))
def homepage(request):
    return render(request, 'mainpage.html')

