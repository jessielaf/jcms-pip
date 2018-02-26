from jcms.helpers.api_views import known_model, unknown_model, create_serializer
from django.urls import path


class JcmsApi:
    def __init__(self, model, fields, lookup_field='pk', create=False, retrieve=False, update=False, delete=False, overview=False, all=False):
        self.model = model
        self.fields = fields
        self.lookup_field = lookup_field

        # Crud variables
        self.create = create
        self.retrieve = retrieve
        self.update = update
        self.delete = delete
        self.overview = overview
        self.all = all

        # Variables that are used very often
        self.serializer = create_serializer(self)
        self.model_name = model.__name__.lower()

    # makes the urls
    def get_urls(self):
        known_model_views = self.known_model()
        unknown_model_views = self.unknown_model()

        urls = []

        if known_model_views:
            urls.append(path('api/' + self.model_name + '/<' + self.lookup_field + '>/', known_model_views.as_view(), name=self.model_name + 'ApiKnown'))

        if unknown_model_views:
            urls.append(path('api/' + self.model_name + '/', unknown_model_views.as_view(), name=self.model_name + 'ApiUnknown'))

        return urls

    # So it can be overwritten
    def known_model(self):
        return known_model(self)

    # So it can be overwritten
    def unknown_model(self):
        return unknown_model(self)
