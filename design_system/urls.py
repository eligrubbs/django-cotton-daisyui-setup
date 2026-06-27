from django.urls import path
from django.views.generic import TemplateView

from .intermal_data import (
    APP_NAME,
    SHOWCASE_URL_NAME,
    COMMON_URL_PREFIX,
    COMPONENTS_METADATA
)


class DesignSystemTemplateView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['design_system'] = {
            "app_name": APP_NAME,
            "base_url": f"{APP_NAME}:{SHOWCASE_URL_NAME}",
            "metadata": COMPONENTS_METADATA,
            "colors": ["neutral", "primary", "secondary", "accent", "info", "success", "warning", "error"],
            "sizes": ["xs", "sm", "md", "lg", "xl"]
        }
        return context


app_name=APP_NAME

urlpatterns = (
    [
        path(f"{COMMON_URL_PREFIX}", DesignSystemTemplateView.as_view(template_name="showcase/index.html"), name=SHOWCASE_URL_NAME)
    ]
    +
    [
        path(
            f"{COMMON_URL_PREFIX}/{x.url_path_prefix}",
            DesignSystemTemplateView.as_view(template_name=x.showcase_template_path_str),
            name=x.url_name
        ) for _, x in COMPONENTS_METADATA.items()
    ]
)
