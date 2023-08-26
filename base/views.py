from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .forms import HelpRequestForm
from .models import HelpRequest
from blog.models import Paper
from utils.data import PAPER_TYPE_PRICING, STUDY_LEVEL_PRICING, PRICE_PER_DAY, TOPICS


def index(request):
    topic_names = []
    topic_codes = []

    for item in TOPICS:
        topic_codes.append(item[0])
        topic_names.append(item[1])

    # Search functionality
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    blogs = Paper.objects.filter(
        Q(title__icontains=q) |
        Q(topic__icontains=q) |
        Q(author__username__icontains=q)
    )

    context = {
        "topic_names": topic_names,
        "topic_codes": topic_codes,
        "topics": TOPICS
    }

    return render(request, "base/home.html", context)


@login_required()
def price_calculator(request):
    form = HelpRequestForm(request.POST or None)

    if form.is_valid():
        help_request = form.save(commit=False)

        paper_type = help_request.paper_type
        study_level = help_request.study_level
        days = help_request.days

        help_request.price = (STUDY_LEVEL_PRICING.get(study_level) +
                              PAPER_TYPE_PRICING.get(paper_type)) + PRICE_PER_DAY.get(str(days))
        help_request.client = request.user

        help_request.save()

        messages.success(
            request, "Your help request has been sent successfully.", extra_tags="success")

        form = HelpRequestForm()

    context = {"form": form}

    return render(request, "base/calculator.html", context)
