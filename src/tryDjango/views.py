from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):
    mytitle = "Blogs"
    qs = BlogPost.objects.all()[:5]
    context = {"title": mytitle, "blog_list": qs}
    return render(request, "home.html", context)


def contact_page(request):
    form = ContactForm(data=request.POST or None)
    context = {}
    if form.is_valid():
        print(form.cleaned_data)
        context = {
            "title": "Contact Us", 
            "form": form
        }
    return render(request, "form.html",context )


def about_page(request):
    return render(request, "about.html", {"title": "About Us"})


def example_page(request):
    context = {"title" : "Example"}
    template_name = "helloworld.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)