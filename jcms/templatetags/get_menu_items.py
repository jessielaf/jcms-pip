from django import template
from jcms.config import AppInfo
from jcms.components import StaticFunctions
from jcms.models import GenericMenuItem

register = template.Library()


@register.simple_tag
def get_menu_items():
    """
    Gets the menu items from AppInfo and converts it to a json

    :return: Json string with menu item information
    """
    apps = AppInfo().JCMS_APPS
    menu_items = []

    for name, app in apps.items():
        if StaticFunctions.app_has_attr(name, app, 'menu_item', GenericMenuItem):
            menu_items.append(app.menu_item)

    return menu_items
