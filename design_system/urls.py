from typing import Optional
from dataclasses import dataclass

from django.urls import path
from django.views.generic import TemplateView


COMMON_URL_PREFIX="__showcase__"
APP_NAME="design_system"
SHOWCASE_URL_NAME="index"
TEMPLATE_COMMON_PREFIX="showcase/components"


@dataclass
class ComponentInfo:
    name: str
    url_path_prefix: str
    url_name: str
    template_path_str: str
    url_path: Optional[str] = None
    """We will set this for you!"""

    def __post_init__(self):
        self.url_path = f"{APP_NAME}:{self.url_name}"



COMPONENTS_METADATA = {
    "button": ComponentInfo("button", "button", "button", f"{TEMPLATE_COMMON_PREFIX}/button.html"),
}



class DesignSystemTemplateView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['design_system'] = {
            "app_name": APP_NAME,
            "base_url": f"{APP_NAME}:{SHOWCASE_URL_NAME}",
            "metadata": COMPONENTS_METADATA
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
            DesignSystemTemplateView.as_view(template_name=x.template_path_str),
            name=x.url_name
        ) for _, x in COMPONENTS_METADATA.items()
    ]
)
