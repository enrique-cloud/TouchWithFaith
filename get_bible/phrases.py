from django.shortcuts import render


def languages(request):
  test = "Hola kike"
  if request.GET.get("idiom") == "valera":
    print("hooooooooola")
  if request.GET.get("idiom") == "asv":
    print("adiooooooooos")
  return render(request, 'language.html', {"test":test})