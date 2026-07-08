from django import template


register = template.Library()


@register.filter
def make_range(value):
    """
    Create a range list from a number for use in template loops.

    Usage: {% for i in max|make_range %}
    """
    try:
        return range(1, int(value) + 1)
    except (ValueError, TypeError):
        return range(1, 6)


@register.filter
def equals_half_range(current_val, user_val):
    """
    Checks if current_val plus 0.5 equals the user val.

    Used in the rating component.

    Usage: {% if i||equals_half_range:rate %}
        - i = "4"
        - rate = "4.5"
    """
    try:
        return str(int(current_val) + 0.5) == str(user_val)
    except:
        return False
