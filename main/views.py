from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Adidas Samba',
        'price': 'Rp. 1.850.000',
        'description': 'Kalcer bro'
    }

    return render(request, "main.html", context)