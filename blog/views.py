from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages

from .forms import PaperForm
from .models import Paper


@login_required()
def create_blog(request):
    form = PaperForm(request.POST, request.FILES or None)

    if form.is_valid():
        paper = form.save(commit=False)

        paper.slug = slugify(paper.title)

        paper.save()

        messages.success(request, "Blog created successfully.",
                         extra_tags="success")
        form = PaperForm()

    context = {"form": form}

    return render(request, "blog/uploadPaper.html", context)


# Blog_list view
@login_required()
def blog_list(request):
    # blogs = Paper.objects.all()

    # Search functionality
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    blogs = Paper.objects.filter(
        Q(title__icontains=q) |
        Q(topic__icontains=q) |
        Q(author__username__icontains=q)
    )


    context = {
        "blogs": blogs
    }

    return render(request, "blog/blog_list.html", context)


# Blog_detail view
@login_required()
def blog_detail(request, blog_slug):
    blogs = Paper.objects.all()
    active_blog = get_object_or_404(Paper, slug=blog_slug)

    context = {
        "blogs": blogs,
        "active_blog": active_blog
    }

    return render(request, "blog/blog_detail.html", context)


def category_detail(request, topic):
    blogs = Paper.objects.filter(topic=topic)    

    print(blogs)

    context = {
        "blogs": blogs.all(),
    }

    return render(request, "blog/blog_list.html", context)
