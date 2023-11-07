from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.phones.models import *
from django.shortcuts import redirect, render
from apps.phones.forms import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


@login_required(login_url="/login/")
def index(request):
    today = datetime.today()
    year = today.year
    week = today.strftime("%V")
    visit_this_week = 0
    visit_last_week = 0
    product_update = ""
    best_products = []
    all = 0
    all_lead_amount = 0
    week_update = ""
    lead_update = ""
    last_month_amount = 0
    the_month_before_amount = 0
    visits = Visit.objects.all()
    leads = Lead.objects.all()
    today = datetime.today()
    last_month = today - relativedelta(months=1)
    the_month_before = today - relativedelta(months=2)
    for lead in leads:
        all_lead_amount += int(lead.price)
        if lead.date.month == last_month.month:
            last_month_amount += lead.price
        elif lead.date.month == the_month_before.month:
            the_month_before_amount += lead.price
    lead_pount = abs(the_month_before_amount-last_month_amount)/(the_month_before_amount+1)
    if the_month_before_amount > last_month_amount:
        lead_update = "down"
    else:
        lead_update = "up"
    for visit in visits:
        all += visit.count
        if int(visit.date.strftime("%V")) == int(int(week)-1) and visit.date.year == year:
            visit_this_week += visit.count
        elif int(visit.date.strftime("%V")) == int(int(week) - 2) and int(visit.date.year) == int(year):
            visit_last_week += visit.count 
    # week_pount = abs(100 -  100 * ((visit_this_week+1)/visit_last_week+1))
    week_pount = 3
    if visit_this_week > visit_last_week:
        week_update = "up"
    else:
        week_update = "down"
    products = Product.objects.all().order_by('-orders')
    for product in products[0:4]:
        pount = abs(100 - 100 * ((product.orders - product.this_week_orders+1)/(product.orders - product.last_week_orders - product.this_week_orders+1)))
        if (product.orders - product.this_week_orders) > (product.orders - product.last_week_orders - product.this_week_orders):
            product_update = "up"
        else:
            product_update = "down"        
        prd = {
            "id": product.id,
            "name": product.name_uz,
            "orders": product.orders,
            "price": product.price,
            "product_update": product_update,
            'pount': round(pount,2),
            'image': product.image,
        }
        best_products.append(prd)
    week_date = today - relativedelta(months=1)
    last_week_date = today - relativedelta(months=2)
    leads_last_count = 0
    leads_before_count = 0
    ls = []
    visit = Visit.objects.filter(date=week_date).first()
    lds = Lead.objects.all()
    for i in lds:
        if i.date.month == week_date.month:
            leads_last_count += 1
        elif i.date.month == last_week_date.month:
            leads_before_count += 1
    leads_mont_edit = abs(100 -  100 * ((leads_last_count+1)/(leads_before_count+1)))
        
    
    context = {
        'segment': 'index',
        'week_pount': round(week_pount,2),
        'lead_pount': round(lead_pount,2),
        'leads_mont_edit': round(leads_mont_edit, 2),
        'week_update': week_update,
        'lead_update': lead_update,
        'all_visits': all,
        'all_lead_amount': all_lead_amount,
        'best_products': best_products,
        }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        print(request.path.split('/')[-1])

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def sliders(request):
    
    sliders = Slider.objects.all()
    context = {
        "sliders": sliders,
        "segment":"sliders"
    }
    
    html_template = loader.get_template('home/sliders.html')
    return HttpResponse(html_template.render(context, request))

    
def slider_detail(request, pk):
    slider = Slider.objects.get(id=pk)

    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES, instance=slider)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sliders')
    else:
        form = SliderForm(instance=slider)

    return render(request,
                'home/slider_update.html',
                {'form': form, 'slider': slider})

    
def slider_create(request):
    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sliders')
    else:
        form = SliderForm()

    return render(request,
                'home/slider_create.html',
                {'form': form})


class SliderDelete(DeleteView):
    model = Slider
    fields = '__all__'
    success_url = reverse_lazy('sliders')
  

def brands(request):
    
    brands = Brand.objects.all()
    context = {
        "brands": brands,
        "segment":"brands"
    }
    
    html_template =loader.get_template('home/brands.html')
    return HttpResponse(html_template.render(context, request))


def brand_create(request):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('brands')
    else:
        form = BrandForm()

    return render(request,
                'home/brand_create.html',
                {'form': form})

    
def brand_detail(request, pk):
    brand = Brand.objects.get(id=pk)

    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('brands')
    else:
        form = BrandForm(instance=brand)

    return render(request,
                'home/brand_update.html',
                {'form': form, 'brand': brand})


class BrandDelete(DeleteView):
    model = Brand
    fields = '__all__'
    success_url = reverse_lazy('brands')


def categories(request):
    
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "segment":"categories"
    }
    
    html_template =loader.get_template('home/categories.html')
    return HttpResponse(html_template.render(context, request))


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()

    return render(request,
                'home/category_create.html',
                {'form': form})

    
def category_detail(request, pk):
    category = Category.objects.get(id=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)

    return render(request,
                'home/category_update.html',
                {'form': form, 'category': category})


class CategoryDelete(DeleteView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('categories')


def products(request):
    
    products = Product.objects.all()
    context = {
        "products": products,
        "segment":"products"
    }
    
    html_template =loader.get_template('home/products.html')
    return HttpResponse(html_template.render(context, request))


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()

    return render(request,
                'home/product_create.html',
                {'form': form})

    
def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    colors = Color.objects.filter(product_id=product.id).all()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)

    return render(request,
                'home/product_update.html',
                {'form': form, 'product': product, 'colors': colors})


class ProductDelete(DeleteView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')


def types(request):
    
    types = Type.objects.all()
    context = {
        "types": types,
        "segment":"types"
    }
    
    html_template =loader.get_template('home/types.html')
    return HttpResponse(html_template.render(context, request))

    
def type_detail(request, pk):
    type = Type.objects.get(id=pk)

    if request.method == 'POST':
        form = TypeForm(request.POST, request.FILES, instance=type)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('types')
    else:
        form = TypeForm(instance=type)

    return render(request,
                'home/type_update.html',
                {'form': form, 'type': type})



def type_create(request):
    if request.method == 'POST':
        form = TypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('types')
    else:
        form = TypeForm()

    return render(request,
                'home/type_create.html',
                {'form': form})


class TypeDelete(DeleteView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('types')


def product_by_category(request, pk):
    products = Product.objects.filter(category_id=pk).all()
    context = {
        "products": products,
        "segment":"products"
    }
    
    html_template =loader.get_template('home/products.html')
    return HttpResponse(html_template.render(context, request))


def product_by_brand(request, pk):
    products = Product.objects.filter(brand_id=pk).all()
    context = {
        "products": products,
        "segment":"products"
    }
    
    html_template =loader.get_template('home/products.html')
    return HttpResponse(html_template.render(context, request))


def product_by_type(request, pk):
    products = Product.objects.filter(type_id=pk).all()
    context = {
        "products": products,
        "segment":"products"
    }
    
    html_template =loader.get_template('home/products.html')
    return HttpResponse(html_template.render(context, request))


def color_create(request, pk):
    if request.method == 'POST':
        form = ColorForm(request.POST, request.FILES)
        if form.is_valid():
            print("aaaaaaaaaaaaaaaaaaaaa")
            color = form.save()
            product = Product.objects.get(id=pk)
            color.product = product
            color.save()
            return redirect('product_detail', pk)
    else:
        form = ColorForm()

    return render(request,
                'home/color_create.html',
                {'form': form})


class ColorDelete(DeleteView):
    model = Color
    fields = '__all__'
    success_url = reverse_lazy('products')

    
def color_detail(request, pk):
    color = Color.objects.get(id=pk)

    if request.method == 'POST':
        form = ColorForm(request.POST, request.FILES, instance=color)
        if form.is_valid():
            pr_pk = color.product.id
            form.save()
            return redirect('product_detail', pr_pk)
    else:
        form = ColorForm(instance=color)

    return render(request,
                'home/color_detail.html',
                {'form': form, 'color': color})

