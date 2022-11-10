from unicodedata import category
from django.views.generic import TemplateView
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


class CartTemplate(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carts'] = Cart.objects.all()
        return context


class Contact(TemplateView):
    template_name = 'contact.html'

# Create your views here.
