from django.shortcuts import render


def languages(request):
  return render(request, 'language.html')