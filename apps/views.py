from unicodedata import category
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import admin
from apps.models import *

class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carts'] = Cart.objects.all()
        total = 0
        for cart in Cart.objects.all():
            total += cart.count * cart.product.price
        context['total'] = total
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
        product = Product.objects.filter(id=id)[0]
        if len(Cart.objects.filter(product=product)) == 0:
            current_cart = Cart(product=product, count=1)
            current_cart.save()
        else:
            current_cart = Cart.objects.filter(product=product)[0]
            current_cart.count += 1
            current_cart.save()

        print(len(Cart.objects.filter(product=product)))
        return render(request, 'product.html')

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
