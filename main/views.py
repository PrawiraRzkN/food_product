from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Rizky Prawira Negoro',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)