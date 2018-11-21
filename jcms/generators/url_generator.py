from abc import ABCMeta, abstractmethod


class UrlGenerator:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_urls(self):
        pass
