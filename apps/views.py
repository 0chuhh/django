from unicodedata import category
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.http import HttpResponseRedirect, JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.contrib import admin
from apps.models import *
import json

class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        self.request.session[0] = 'barr'
        sessionid = self.request.COOKIES.get('sessionid')

        try:
            current_cart = Cart(guest_session_id=sessionid)
            current_cart.save()
        except:
            print('error')


        context = super().get_context_data(**kwargs)
        # carts = [{}]
        # if sessionid:
        try:
            carts = CartDetails.objects.filter(cart_id=Cart.objects.filter(guest_session_id=sessionid)[0].id)
            total = 0
            for cart in carts:
                total += cart.count * cart.product.price
            context['total'] = total
            context['carts'] = carts
        except:
            print('error')

        return context

class Index(BaseView, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = BaseView.get_context_data(self,**kwargs)
        return context


class About(BaseView, TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = BaseView.get_context_data(self, **kwargs)


        return context


class Blog(BaseView, TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = BaseView.get_context_data(self, **kwargs)


        return context


class SingleBlog(BaseView, TemplateView):
    template_name = 'blog-single.html'

    def get_context_data(self, **kwargs):
        context = BaseView.get_context_data(self, **kwargs)


        return context


class ProductView(BaseView, TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = BaseView.get_context_data(self,**kwargs)

        try:
            cat = self.request.GET['cat']
            if int(cat) == 1:
                context['products'] = Product.objects.all()
            else:
                context['products'] = Product.objects.filter(category=int(cat))
        except:
            context['products'] = Product.objects.all()

        context['category'] = Category.objects.all()
        return context


class ProductCreate(CreateView):
    model = Cart
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        id = self.request.POST['id']
        sessionid = self.request.COOKIES.get('sessionid')
        product = Product.objects.filter(id=id)[0]
        cart_id = Cart.objects.filter(guest_session_id=sessionid)[0]
        if len(CartDetails.objects.filter(cart_id=cart_id, product_id=product.id)) == 0:
            current_cart = CartDetails(cart_id=cart_id, product=product, count=1)
            current_cart.save()
        else:
            current_cart = CartDetails.objects.filter(cart_id=cart_id, product=product)[0]
            current_cart.count += 1
            current_cart.save()
        print(product)
        return JsonResponse({'product':dict(map(lambda kv: (kv[0], str(kv[1])), model_to_dict(product).items())), 'count':str(current_cart.count), 'len':len(list(CartDetails.objects.filter(cart_id=cart_id))[0])}, safe=False)

class ProductDelete(DeleteView):
    model = Cart
    fields = "__all__"

    def delete(self, request, *args, **kwargs):
        id = self.request.POST
        print(id)





class CartTemplate(BaseView, TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = BaseView.get_context_data(self,**kwargs)
        return context


class Contact(BaseView, TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = BaseView.get_context_data(self, **kwargs)


        return context

# Create your views here.
