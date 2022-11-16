from unicodedata import category
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from apps.models import *


class Index(TemplateView):
    template_name = 'index.html'


class About(TemplateView):
    template_name = 'about.html'


class Blog(TemplateView):
    template_name = 'blog.html'


class SingleBlog(TemplateView):
    template_name = 'blog-single.html'


class ProductView(TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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


class CartTemplate(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carts'] = Cart.objects.all()
        return context


class Contact(TemplateView):
    template_name = 'contact.html'

# Create your views here.
