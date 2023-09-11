from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app' : 'Geprek Lensu',
        'name': 'Elena Zahra Kurniawan',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)