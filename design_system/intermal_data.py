from typing import Optional
from dataclasses import dataclass
from enum import StrEnum, auto


COMMON_URL_PREFIX="__showcase__"
APP_NAME="design_system"
SHOWCASE_URL_NAME="index"
TEMPLATE_COMMON_PREFIX="showcase/components"

class ComponentCategory(StrEnum):
    """
    What type of component this is. Copied one-to-one from what you see on DaisyUI website sidebar
    """
    actions = auto()
    data_display = auto()
    navigation = auto()
    feedback = auto()
    data_input = auto()
    layout = auto()
    mockup = auto()



@dataclass
class ComponentInfo:
    name: str
    """Name displayed on showcase page"""
    category: ComponentCategory
    """What type of component this is. action, navigation, etc."""
    url_path_prefix: str
    """what appears in the url for this view"""
    url_name: str
    """how django internally reverses urls to this view"""
    template_path_str: str
    """what template to render for this view"""
    url_path: Optional[str] = None
    """We will set this for you!"""


    def __post_init__(self):
        self.url_path = f"{APP_NAME}:{self.url_name}"


COMPONENTS_METADATA = {
    "button": ComponentInfo(
        name="Button",
        category=ComponentCategory.actions,
        url_path_prefix="button",
        url_name="button",
        template_path_str=f"{TEMPLATE_COMMON_PREFIX}/button.html"
    ),
    "alert": ComponentInfo(
        name="Alert",
        category=ComponentCategory.feedback,
        url_path_prefix="alert",
        url_name="alert",
        template_path_str=f"{TEMPLATE_COMMON_PREFIX}/alert.html"
    ),
    "loading": ComponentInfo(
        name="Loading",
        category=ComponentCategory.feedback,
        url_path_prefix="loading",
        url_name="loading",
        template_path_str=f"{TEMPLATE_COMMON_PREFIX}/loading.html"
    ),
    "progress": ComponentInfo(
        name="Progress",
        category=ComponentCategory.feedback,
        url_path_prefix="progress",
        url_name="progress",
        template_path_str=f"{TEMPLATE_COMMON_PREFIX}/progress.html"
    ),
    "skeleton": ComponentInfo(
        name="Skeleton",
        category=ComponentCategory.feedback,
        url_path_prefix="skeleton",
        url_name="skeleton",
        template_path_str=f"{TEMPLATE_COMMON_PREFIX}/skeleton.html"
    ),
    "tooltip": ComponentInfo(
        name="Tooltip",
        category=ComponentCategory.feedback,
        url_path_prefix="tooltip",
        url_name="tooltip",
        template_path_str=f"{TEMPLATE_COMMON_PREFIX}/tooltip.html"
    ),
    "checkbox": ComponentInfo(
        name="Checkbox",
        category=ComponentCategory.data_input,
        url_path_prefix="checkbox",
        url_name="checkbox",
        template_path_str=f"{TEMPLATE_COMMON_PREFIX}/checkbox.html"
    ),
    "fieldset": ComponentInfo(
        name="Fieldset",
        category=ComponentCategory.data_input,
        url_path_prefix="fieldset",
        url_name="fieldset",
        template_path_str=f"{TEMPLATE_COMMON_PREFIX}/fieldset.html"
    ),
    "input": ComponentInfo(
        name="Input",
        category=ComponentCategory.data_input,
        url_path_prefix="input",
        url_name="input",
        template_path_str=f"{TEMPLATE_COMMON_PREFIX}/input.html"
    ),
}
