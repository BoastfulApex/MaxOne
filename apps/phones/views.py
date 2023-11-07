from django.shortcuts import render
from apps.phones.models import Lead, Visit
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
# import django_filters.rest_framework
import random
import datetime
from dateutil.relativedelta import relativedelta

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ['name_uz']


    def list(self, request):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def list(self, request, *args, **kwargs):
    #     data = []
    #     products = Product.objects.all()
    #     for product in products:
    #         color = Color.objects.filter(product_id=product.id).first()
    #         if color:
    #             dt = {
    #                 "id": product.id,
    #                 "name_uz": product.name_uz,
    #                 "name_ru": product.name_ru,
    #                 "name_en": product.name_en,
    #                 "description_uz": product.description_uz,
    #                 "description_ru": product.description_ru,
    #                 "description_en": product.description_en,
    #                 "category": product.category.id,
    #                 "brand": product.brand.id,
    #                 "type": product.type.id,
    #                 "price": product.price,
    #                 "image": f"https://maxone.abba.uz{color.image1.url}"
    #             }
    #         else:
    #             dt = {
    #                 "id": product.id,
    #                 "name_uz": product.name_uz,
    #                 "name_ru": product.name_ru,
    #                 "name_en": product.name_en,
    #                 "description_uz": product.description_uz,
    #                 "description_ru": product.description_ru,
    #                 "description_en": product.description_en,
    #                 "category": product.category.id,
    #                 "brand": product.brand.id,
    #                 "type": product.type.id,
    #                 "price": product.price,
    #                 "image": ""
    #             }
    #         data.append(dt)
                
    #     return Response(data)
    def list(self, request, *args, **kwargs):
        products = Product.objects.all()
        data = []
        today = datetime.datetime.today()
        visit= Visit.objects.filter(date=today).first()
        if visit:
            visit.count += 1
        else:
            visit = Visit.objects.create(
              date=today  
            )
            visit.count += 1
        visit.save()
        try:
            price = int(request.GET.get('order'))
            products = Product.objects.all()
            bests = []
            cheaps = []
            expensives = []
            others = []
            price_min = price - 0.25 * price
            price_max = price + 0.25 * price
            for product in products:
                if product.price >= price_min and product.price <= price_max:
                    bests.append(product)
                elif product.price >= price_max:
                    expensives.append(product)
                elif product.price <= price_min:
                    cheaps.append(product)
                else:
                    others.append(product)
            data1 = bests + cheaps + others + expensives
            for product in data1:
                color = Color.objects.filter(product_id=product.id).first()
                if color:
                    dt = {
                        "id": product.id,
                        "name_uz": product.name_uz,
                        "name_ru": product.name_ru,
                        "name_en": product.name_en,
                        "characteristic_uz": product.characteristic_uz,
                        "characteristic_en": product.characteristic_ru,
                        "characteristic_ru": product.characteristic_en,
                        "description_uz": product.description_uz,
                        "description_ru": product.description_ru,
                        "description_en": product.description_en,
                        "category": product.category.id,
                        "brand": product.brand.id,
                        "type": product.type.id,
                        "price": product.price,
                        "image": f"https://maxone.abba.uz{color.image1.url}"
                    }
                else:
                    dt = {
                        "id": product.id,
                        "name_uz": product.name_uz,
                        "name_ru": product.name_ru,
                        "name_en": product.name_en,
                        "characteristic_uz": product.characteristic_uz,
                        "characteristic_en": product.characteristic_ru,
                        "characteristic_ru": product.characteristic_en,
                        "description_uz": product.description_uz,
                        "description_ru": product.description_ru,
                        "description_en": product.description_en,
                        "category": product.category.id,
                        "brand": product.brand.id,
                        "type": product.type.id,
                        "price": product.price,
                        "image": ""
                    }
                data.append(dt)
        except:
            for product in products:
                color = Color.objects.filter(product_id=product.id).first()
                if color:
                    dt = {
                        "id": product.id,
                        "name_uz": product.name_uz,
                        "name_ru": product.name_ru,
                        "name_en": product.name_en,
                        "characteristic_uz": product.characteristic_uz,
                        "characteristic_en": product.characteristic_ru,
                        "characteristic_ru": product.characteristic_en,
                        "description_uz": product.description_uz,
                        "description_ru": product.description_ru,
                        "description_en": product.description_en,
                        "category": product.category.id,
                        "brand": product.brand.id,
                        "type": product.type.id,
                        "price": product.price,
                        "image": f"https://maxone.abba.uz{color.image1.url}"
                    }
                else:
                    dt = {
                        "id": product.id,
                        "name_uz": product.name_uz,
                        "name_ru": product.name_ru,
                        "name_en": product.name_en,
                        "characteristic_uz": product.characteristic_uz,
                        "characteristic_en": product.characteristic_ru,
                        "characteristic_ru": product.characteristic_en,
                        "description_uz": product.description_uz,
                        "description_ru": product.description_ru,
                        "description_en": product.description_en,
                        "category": product.category.id,
                        "brand": product.brand.id,
                        "type": product.type.id,
                        "price": product.price,
                        "image": ""
                    }
                data.append(dt)
                    
        return Response(data)

    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = ProductSerializer(queryset, many=True)
    #     return Response(serializer.data)


class dataAdd(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        products = Product.objects.all()
        points = [1, 0.3, 0.5, 0.45, 0.45, 0.55, 0.65, 0.5, 0.8, 0.9, 1.12, 1.42, 1.28, 1.21, 1.2, 1.35, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 3.5, 4, 4.5] 

        for product in products:
            product.description_uz = product.name_uz
            product.description_ru = product.name_ru
            product.description_en = product.name_en
            product.save()
        # colors = Color.objects.all()
        # clrs = ['cadetblue', 'honeydew', "lightblue", "navy", "plum", "royalblue", "teal", "aliceblue", "dark", "blue", "red", "white", "green"]
        
        # for color in colors:
        #     cls = random.choice(clrs)
        #     color.color = cls
        #     color.save()
            # cl1 = Color.objects.create(
            #     product=color.product, 
            #     color=cls,
            #     image1=color.image1
            # )
            # cl1.save()
            # cl1 = Color.objects.create(
            #     product=color.product, 
            #     color=cls,
            #     image1=color.image1
            # )
            # cl1.save()
            # cl1 = Color.objects.create(
            #     product=color.product, 
            #     color=cls,
            #     image1=color.image1
            # )
            # cl1.save()
                
        # categories = Category.objects.all()
        # types = Type.objects.all()
        # brands = Brand.objects.all()
        # test = 2438000
        # points = [0.65, 0.57, 0.7, 1.42, 1.28, 1.21, 1.2, 1.35, 1.4, 1.5] 
        # for product in products:
        #     if product == 0:
        #         point = (random.choice(points))
        #         product.price = test * int(point) 
        #         product.save()

        # for i in range(25):
        #     category = random.choice(categories)
        #     clr = random.choice(colors)
        #     typ = random.choice(types)
        #     brnd = random.choice(brands)
        #     point = (random.choice(points))

        #     product = Product.objects.create(
        #         name_uz=prd.name_uz,
        #         name_ru=prd.name_ru,
        #         name_en=prd.name_en,
        #         category=category,
        #         type=typ,
        #         brand=brnd,
        #         price=prd.price * int(point),
                # characteristic_uz=prd.characteristic_uz,
                # characteristic_en=prd.characteristic_en,
                # characteristic_ru=prd.characteristic_ru,
        #     )
        #     product.save()
            
        #     color = Color.objects.create(
        #         product=product,
        #         color=clr.color,
        #         image1=clr.image1
        #     )
        #     color.save()
            
        return Response({"status": "created"})


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        product_id = kwargs['pk']
        data = []
        product = self.queryset.filter(id=product_id).first()
        try:    
            price = int(request.GET.get('order'))
            products = Product.objects.filter(category_id=product.category.id).all()
            bests = []
            price_min = price - 0.25 * price
            price_max = price + 0.25 * price
            for product in products:
                if product.price >= price_min and product.price <= price_max:
                    bests.append(product)
            for product in bests:
                color = Color.objects.filter(product_id=product.id).first()
                if color:
                    dt = {
                        "id": product.id,
                        "name_uz": product.name_uz,
                        "name_ru": product.name_ru,
                        "name_en": product.name_en,
                        "characteristic_uz": product.characteristic_uz,
                        "characteristic_en": product.characteristic_en,
                        "characteristic_ru": product.characteristic_ru,
                        "description_uz": product.description_uz,
                        "description_ru": product.description_ru,
                        "description_en": product.description_en,
                        "category": product.category.id,
                        "brand": product.brand.id,
                        "type": product.type.id,
                        "price": product.price,
                        "image": f"https://maxone.abba.uz{color.image1.url}"
                    }
                else:
                    dt = {
                        "id": product.id,
                        "name_uz": product.name_uz,
                        "name_ru": product.name_ru,
                        "name_en": product.name_en,
                        "characteristic_uz": product.characteristic_uz,
                        "characteristic_en": product.characteristic_en,
                        "characteristic_ru": product.characteristic_ru,
                        "description_uz": product.description_uz,
                        "description_ru": product.description_ru,
                        "description_en": product.description_en,
                        "category": product.category.id,
                        "brand": product.brand.id,
                        "type": product.type.id,
                        "price": product.price,
                        "image": ""
                    }
                data.append(dt)
        except:
            product_id = kwargs['pk']
            data = []
            colors = []
            product = self.queryset.filter(id=product_id).first()
            clrs = Color.objects.filter(product_id=product_id).all()
            # for color in clrs:
                # cl = [f"https://maxone.abba.uz{color.image1.url}"]
            #     colors.append({f"{color.color}": cl})
            for color in clrs:
                cl = {
                    "color_en": color.color_en,
                    "color_uz": color.color_uz,
                    "color_ru": color.color_ru,
                    "image1": f"https://maxone.abba.uz{color.image1.url}",
                }
                colors.append(cl)
            data = {
                "id": product.id,
                "name_uz": product.name_uz,
                "name_ru": product.name_ru,
                "name_en": product.name_en,
                "description_uz": product.description_uz,
                "description_ru": product.description_ru,
                "description_en": product.description_en,
                "characteristic_uz": product.characteristic_uz,
                "characteristic_en": product.characteristic_ru,
                "characteristic_ru": product.characteristic_en,
                "category": product.category.id,
                "brand": product.brand.id,
                "type": product.type.id,
                "price": product.price,
                "colors": colors            
            }
        return Response(data)


class BestProducts(generics.ListAPIView):
    queryset = Product.objects.filter(best=True).all()
    serializer_class = ProductSerializer
    
    def list(self, request, *args, **kwargs):
        data = []
        products = Product.objects.filter(best=True).all()
        for product in products:
            color = Color.objects.filter(product_id=product.id).first()
            if color:
                dt = {
                    "id": product.id,
                    "name_uz": product.name_uz,
                    "name_ru": product.name_ru,
                    "name_en": product.name_en,
                    "characteristic_uz": product.characteristic_uz,
                    "characteristic_en": product.characteristic_ru,
                    "characteristic_ru": product.characteristic_en,
                    "category": product.category.id,
                    "brand": product.brand.id,
                    "type": product.type.id,
                    "price": product.price,
                    "image": f"https://maxone.abba.uz{color.image1.url}"
                }
            else:
                dt = {
                    "id": product.id,
                    "name_uz": product.name_uz,
                    "name_ru": product.name_ru,
                    "name_en": product.name_en,
                    "characteristic_uz": product.characteristic_uz,
                    "characteristic_en": product.characteristic_ru,
                    "characteristic_ru": product.characteristic_en,
                    "category": product.category.id,
                    "brand": product.brand.id,
                    "type": product.type.id,
                    "price": product.price,
                    "image": ""
                }
            data.append(dt)
        return Response(data)


class SliderList(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer 


class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ['name_uz']


    def list(self, request):
        data = []
        queryset = []
        try:
            type_id = int(request.GET.get('type'))
            print(type_id)
            products = Product.objects.filter(type__id=type_id).all()
            for product in products:
                if product.brand not in queryset:
                    queryset.append(product.brand)
            for i in queryset:
                dt = {
                    "id": i.id,
                    "name_uz": i.name_uz,
                    "name_en": i.name_en,
                    "name_ru": i.name_ru,
                    "image": f"https://maxone.abba.uz/files/{i.image}"
                }
                data.append(dt)
        except:
            queryset = self.get_queryset()
            for i in queryset:
                dt = {
                    "id": i.id,
                    "name_uz": i.name_uz,
                    "name_en": i.name_en,
                    "name_ru": i.name_ru,
                    "image": f"https://maxone.abba.uz/files/{i.image}"
                }
                data.append(dt)
        return Response(data)


class BrandDetail(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class LeadView(generics.ListCreateAPIView):
    queryset = Lead.objects.all()   
    serializer_class = LeadSerializer
    
    def post(self, request, *args, **kwargs):
        prd_id = int(request.data['product'])
        product = Product.objects.get(id=prd_id)
        product.orders += 1
        product.save()
        lead = Lead.objects.create(
            product=product,
            customer_name=request.data["customer_name"],
            phone=request.data["phone"],
            product_name=product.name_uz,
            price=product.price,
            region=request.data["region"]
        )
        lead.save()
        return Response({"status": "created"})


class Dataset(generics.ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def list(self, request, *args, **kwargs):
        this_week_visits = []
        month_totals = []
        leads = 0
        months = []
        today = datetime.datetime.today()
        dates = []
        for i in range(7):
            week_date = today - datetime.timedelta(days=i)
            leads = 0
            ls = []
            visit = Visit.objects.filter(date=week_date).first()
            month_date = today - relativedelta(months=i)
            lds = Lead.objects.all()
            for i in lds:
                if i.date.month == month_date.month:
                    ls.append(i)
            for lead in ls:
                leads += lead.price
            if visit:
                this_week_visits.append(visit.count)
            else:
                this_week_visits.append(0)
            dates.append(week_date.day)            
            month_totals.append(leads)
            months.append(month_date.date().strftime("%b"))
        this_week_visits.reverse()
        dates.reverse()
        months.reverse()
        month_totals.reverse()        
        
        data = {
            "lebels_this_week": dates,
            "visits_this_week": this_week_visits,
            "months": months,
            "month_totals": month_totals
        }
        return Response(data)


class TypeView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
