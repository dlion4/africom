from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from africom.services.models import Category
from typing import Any


class AfricomHomeView(TemplateView):
    category = Category

    template_name = "pages/home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = self.category.objects.all()  # type: ignore
        return context


class AfricomAboutView(TemplateView):

    template_name = "pages/about.html"
