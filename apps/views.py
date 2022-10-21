from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'


class About(TemplateView):
    template_name = 'about.html'


class Blog(TemplateView):
    template_name = 'blog.html'


class SingleBlog(TemplateView):
    template_name = 'blog-single.html'


class Product(TemplateView):
    template_name = 'product.html'


class Cart(TemplateView):
    template_name = 'cart.html'


class Contact(TemplateView):
    template_name = 'contact.html'

# Create your views here.
