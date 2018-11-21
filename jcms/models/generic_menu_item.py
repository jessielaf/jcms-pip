from typing import List
from jcms.models.single_menu_item import SingleMenuItem
from django.urls import path


class GenericMenuItem:
    """
    Generic menu item that can be seen in the left bar in the cms
    """

    def __init__(self, slug: str, title: str, single_menu_items: List[SingleMenuItem]):
        """
        :param slug: The slug the single menu items will have in front of them
        :type slug: str
        :param title: Display name for the MenuItem
        :type title: str
        :param single_menu_items: SingleMenuItems that are shown as children
        :type single_menu_items: List[SingleMenuItem]
        """
        self.slug = slug
        self.title = title
        self.single_menu_items = single_menu_items
