from typing import Optional
from dataclasses import dataclass
from enum import StrEnum, auto


COMMON_URL_PREFIX="__showcase__"
APP_NAME="design_system"
SHOWCASE_URL_NAME="index"
SHOWCASE_COMMON_PREFIX="showcase/components"

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
    showcase_template_path_str: str
    """what showcase template to render for this view"""
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
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/button.html"
    ),
    "alert": ComponentInfo(
        name="Alert",
        category=ComponentCategory.feedback,
        url_path_prefix="alert",
        url_name="alert",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/alert.html"
    ),
    "loading": ComponentInfo(
        name="Loading",
        category=ComponentCategory.feedback,
        url_path_prefix="loading",
        url_name="loading",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/loading.html"
    ),
    "progress": ComponentInfo(
        name="Progress",
        category=ComponentCategory.feedback,
        url_path_prefix="progress",
        url_name="progress",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/progress.html"
    ),
    "skeleton": ComponentInfo(
        name="Skeleton",
        category=ComponentCategory.feedback,
        url_path_prefix="skeleton",
        url_name="skeleton",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/skeleton.html"
    ),
    "tooltip": ComponentInfo(
        name="Tooltip",
        category=ComponentCategory.feedback,
        url_path_prefix="tooltip",
        url_name="tooltip",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/tooltip.html"
    ),
    "checkbox": ComponentInfo(
        name="Checkbox",
        category=ComponentCategory.data_input,
        url_path_prefix="checkbox",
        url_name="checkbox",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/checkbox.html"
    ),
    "fieldset": ComponentInfo(
        name="Fieldset",
        category=ComponentCategory.data_input,
        url_path_prefix="fieldset",
        url_name="fieldset",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/fieldset.html"
    ),
    "input": ComponentInfo(
        name="Input",
        category=ComponentCategory.data_input,
        url_path_prefix="input",
        url_name="input",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/input.html"
    ),
    "select": ComponentInfo(
        name="Select",
        category=ComponentCategory.data_input,
        url_path_prefix="select",
        url_name="select",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/select.html"
    ),
    "textarea": ComponentInfo(
        name="Textarea",
        category=ComponentCategory.data_input,
        url_path_prefix="textarea",
        url_name="textarea",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/textarea.html"
    ),
    "toggle": ComponentInfo(
        name="Toggle",
        category=ComponentCategory.data_input,
        url_path_prefix="toggle",
        url_name="toggle",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/toggle.html"
    ),
    "kbd": ComponentInfo(
        name="Kbd",
        category=ComponentCategory.data_display,
        url_path_prefix="kbd",
        url_name="kbd",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/kbd.html"
    ),
    "badge": ComponentInfo(
        name="Badge",
        category=ComponentCategory.data_display,
        url_path_prefix="badge",
        url_name="badge",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/badge.html"
    ),
    "status": ComponentInfo(
        name="Status",
        category=ComponentCategory.data_display,
        url_path_prefix="status",
        url_name="status",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/status.html"
    ),
    "table": ComponentInfo(
        name="Table",
        category=ComponentCategory.data_display,
        url_path_prefix="table",
        url_name="table",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/table.html"
    ),
    "mockup_browser": ComponentInfo(
        name="Mockup Browser",
        category=ComponentCategory.mockup,
        url_path_prefix="mockup-browser",
        url_name="mockup_browser",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/mockup-browser.html"
    ),
    "mockup_phone": ComponentInfo(
        name="Mockup Phone",
        category=ComponentCategory.mockup,
        url_path_prefix="mockup-phone",
        url_name="mockup_phone",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/mockup-phone.html"
    ),
    "mockup_code": ComponentInfo(
        name="Mockup Code",
        category=ComponentCategory.mockup,
        url_path_prefix="mockup-code",
        url_name="mockup_code",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/mockup-code.html"
    ),
    "mockup_window": ComponentInfo(
        name="Mockup Window",
        category=ComponentCategory.mockup,
        url_path_prefix="mockup-window",
        url_name="mockup_window",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/mockup-window.html"
    ),
    "modal": ComponentInfo(
        name="Modal",
        category=ComponentCategory.actions,
        url_path_prefix="modal",
        url_name="modal",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/modal.html"
    ),
    "theme_controller": ComponentInfo(
        name="Theme Controller",
        category=ComponentCategory.actions,
        url_path_prefix="theme-controller",
        url_name="theme_controller",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/theme-controller.html"
    ),
    "card": ComponentInfo(
        name="Card",
        category=ComponentCategory.data_display,
        url_path_prefix="card",
        url_name="card",
        showcase_template_path_str=f"{SHOWCASE_COMMON_PREFIX}/card.html"
    ),
}
