from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify

from .forms import PaperForm
from .models import Paper

# Blog_Create view
def create_blog(request):
    form = PaperForm(request.POST, request.FILES or None)

    if form.is_valid():
        paper = form.save(commit=False)

        paper.slug = slugify(paper.title)

        paper.save()
        form = PaperForm()

    context = {"form": form}

    return render(request, "blog/uploadPaper.html", context)


# Blog_list view
def blog_list(request):
    blogs = Paper.objects.all()


    context = {
        "blogs": blogs
    }

    return render(request, "blog/blog_list.html", context)


# Blog_detail view
def blog_detail(request, blog_slug):
    blogs = Paper.objects.all()
    active_blog = get_object_or_404(Paper, slug = blog_slug)
    
    context = {
        "blogs": blogs,
        "active_blog": active_blog
    }   

    return render(request, "blog/blog_detail.html", context)
