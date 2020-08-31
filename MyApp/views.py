from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from home.models import *
from django.core.paginator import Paginator
from django.views import View
from django.views.generic import TemplateView
from . models import ProductInfo
from django.contrib import messages

from MyApp.forms import Productform


# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'MyApp/home.html')

    def post(self, request):
        vp = request.POST['vp']
        dfv = request.POST['dfv']
        variation = request.POST['variation']
        color = request.POST['cls']
        sku = request.POST['sku']
        checkboxs = request.POST['checkboxs']
        rp = request.POST['rp']
        sch = request.POST['sch']
        stock = request.POST['stock']

        products = ProductInfo(productData=vp,
                               dfv=dfv,
                               variation=variation,
                               color=color,
                               sku=sku,
                               checks=checkboxs,
                               price=rp,
                               schedule=sch,
                               stock=stock
                               )
        products.save()
        messages.success(
            request, 'Congratulations! Product has been Added Successfully...')
        return render(request, 'MyApp/home.html')


class Viewproducts(View):
    def get(self, request):
        products = ProductInfo.objects.all()
        param = {'products': products}
        return render(request, 'MyApp/products.html', param)


class Delete(View):
    def get(self, request, id):
        products = ProductInfo.objects.get(id=id)
        products.delete()
        products = ProductInfo.objects.all()
        param = {'products': products}
        return render(request, "MyApp/products.html", param)

class Edit(View):
    def get(self, request, id):
        products = ProductInfo.objects.get(id=id)
        return render(request, 'MyApp/edit.html', {'products': products})

class Update(View):
    def post(self, request, id):
        products = ProductInfo.objects.get(id=id)
        products.delete()
        vp = request.POST['vp']
        dfv = request.POST['dfv']
        variation = request.POST['variation']
        color = request.POST['cls']
        sku = request.POST['sku']
        checkboxs = request.POST['checkboxs']
        rp = request.POST['rp']
        sch = request.POST['sch']
        stock = request.POST['stock']

        products = ProductInfo(productData=vp,
                            dfv=dfv,
                            variation=variation,
                            color=color,
                            sku=sku,
                            checks=checkboxs,
                            price=rp,
                            schedule=sch,
                            stock=stock
                            )
        products.save()
        messages.success(
            request, 'Congratulations! Product has been Updated Successfully...')
        products = ProductInfo.objects.all()
        param = {'products': products}
        return render(request, 'MyApp/products.html', param)

# /////////// udate  

    # products.id= request.GET('id')
    # products.productData = request.GET('vp')
    # products.dfv = request.GET('dfv')
    # products.variation = request.GET('variation')
    # products.color = request.GET('cls')
    # products.sku = request.GET('sku')
    # products.checks = request.GET('checkboxs')
    # products.price = request.GET('rp')
    # products.schedule = request.GET('sch')
    # products.stock = request.GET('stock')
    # products.update(products)
    # products.save()
    # return redirect("products.html")

# /////////////////////////// UPDATE 
# form = Productform(instance=products)
    # if request.method == 'POST':
    #     form = Productform(request.POST, instance=products)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')
    # context ={'form':form}
    # messages.success(request, 'Congratulations! Product has been Updated Successfully...')
    # return render(request,"MyApp/products.html",context)
