import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from main.forms import ItemForm, Item
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'creator': 'Rizky Prawira Negoro',
        'npm': '2206030956',
        'class': 'PBP E', # Kelas PBP kamu
        'items': items,
        'items_count': len(Item.objects.filter(user=request.user)),
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {
        'form': form,
        'creator': 'Rizky Prawira Negoro',
        'npm': '2206030956',
        'class': 'PBP E', # Kelas PBP kamu
        }
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {
        'form':form,
        'creator': 'Rizky Prawira Negoro',
        'npm': '2206030956',
        'class': 'PBP E', # Kelas PBP kamu
        }
    return render(request, 'register.html', context)

def go_back_login(request):
    if request.method == "POST":
        return redirect('main:login')

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {
        'creator': 'Rizky Prawira Negoro',
        'npm': '2206030956',
        'class': 'PBP E', # Kelas PBP kamu
    }
    return render(request, 'login.html', context)

@csrf_exempt
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def add_amount_button(request, item_id):
    if request.method == 'POST':
        item = Item.objects.get(pk=item_id) #Mengakses item yang ingin dimodifikasi
        item.user = request.user
        if item.amount > 0:
            item.amount += 1
            item.save()
        return HttpResponse(b"ADDED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def reduce_amount_button(request, item_id):
    if request.method == 'POST':
        item = Item.objects.get(pk=item_id)
        item.user = request.user
        if item.amount > 1:
            item.amount -= 1
            item.save()
        else:
            item.delete();
        return HttpResponse(b"REDUCED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def remove_item_button(request, item_id):
    if request.method == 'DELETE':
        item = Item.objects.get(pk=item_id)
        item.user = request.user
        item.delete()
        return HttpResponse(b"REMOVED", status=201)
    return HttpResponseNotFound()
    
def get_item_json(request):
    item = Item.objects.filter(user=request.user)
    item.user = request.user
    return HttpResponse(serializers.serialize('json', item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        price = request.POST.get("price")
        category = request.POST.get("category")
        origin = request.POST.get("origin")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, price=price, category=category, origin=origin, description=description, user=user)
        new_item.user = request.user
        new_item.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def create_item_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["price"]),
            description = data["description"],
            origin = data["origin"],
            amount = int(data["amount"]),
            category = data["category"],
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)