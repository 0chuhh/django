from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'


class About(TemplateView):
    template_name = 'about.html'


class Blog(TemplateView):
    template_name = 'blog.html'


class SingleBlog(TemplateView):
    template_name = 'single-blog.html'

# Create your views here.
