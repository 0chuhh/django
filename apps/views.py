from unicodedata import category
from django.views.generic import TemplateView
from apps.models import Category, Product

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
        cat = self.request.GET['cat']
        print(self.request.GET['cat'], 'hui')
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['products'] = Product.objects.filter(category=int(cat))
        return context

class Cart(TemplateView):
    template_name = 'cart.html'


class Contact(TemplateView):
    template_name = 'contact.html'

# Create your views here.
