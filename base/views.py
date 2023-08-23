from django.shortcuts import render
from .forms import HelpRequestForm
from .models import HelpRequest
from utils.data import PAPER_TYPE_PRICING, STUDY_LEVEL_PRICING


def index(request):
    context = {}

    return render(request, "base/home.html", context)


def price_calculator(request):
    form = HelpRequestForm(request.POST or None)

    if form.is_valid():
        help_request = form.save(commit=False)

        paper_type = help_request.paper_type
        study_level = help_request.study_level
        days = help_request.days

        help_request.price = (STUDY_LEVEL_PRICING.get(study_level) +
                              PAPER_TYPE_PRICING.get(paper_type)) * 1/(days / 2)
        help_request.client = request.user

        help_request.save()
        form = HelpRequestForm()

    context = {"form": form}

    return render(request, "base/calculator.html", context)
