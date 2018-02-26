from django.test import TestCase
from jcms.mixins.jcms_api import JcmsApi
from django.contrib.auth.models import User

from rest_framework import generics


class TestJcmsApi(TestCase):
    def subclasses(self, jcms_api, unknown_class, known_class):
        unknown_api_class = jcms_api.unknown_model()
        known_api_class = jcms_api.known_model()

        if unknown_class is None:
            self.assertEqual(unknown_api_class, None)
        else:
            self.assertTrue(issubclass(unknown_api_class, unknown_class))

        if known_class is None:
            self.assertEqual(known_api_class, None)
        else:
            self.assertTrue(issubclass(known_api_class, known_class))

    def test_jcms_api_none(self):
        jcms_api = JcmsApi(User, ['username'])
        self.subclasses(jcms_api, None, None)

    def test_jcms_api_all(self):
        jcms_api = JcmsApi(User, ['username'], all=True)
        self.subclasses(jcms_api, generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView)

    def test_jcms_api_overview(self):
        jcms_api = JcmsApi(User, ['username'], overview=True)
        self.subclasses(jcms_api, generics.ListAPIView, None)

    def test_jcms_api_create(self):
        jcms_api = JcmsApi(User, ['username'], create=True)
        self.subclasses(jcms_api, generics.CreateAPIView, None)

    def test_jcms_api_retrieve(self):
        jcms_api = JcmsApi(User, ['username'], retrieve=True)
        self.subclasses(jcms_api, None, generics.RetrieveAPIView)

    def test_jcms_api_update(self):
        jcms_api = JcmsApi(User, ['username'], update=True)
        self.subclasses(jcms_api, None, generics.UpdateAPIView)

    def test_jcms_api_delete(self):
        jcms_api = JcmsApi(User, ['username'], delete=True)
        self.subclasses(jcms_api, None, generics.DestroyAPIView)

    def test_jcms_api_overview_create(self):
        jcms_api = JcmsApi(User, ['username'], overview=True, create=True)
        self.subclasses(jcms_api, generics.ListCreateAPIView, None)

    def test_jcms_api_overview_create_retrieve(self):
        jcms_api = JcmsApi(User, ['username'], overview=True, create=True, retrieve=True)
        self.subclasses(jcms_api, generics.ListCreateAPIView, generics.RetrieveAPIView)

    def test_jcms_api_overview_create_retrieve_update(self):
        jcms_api = JcmsApi(User, ['username'], overview=True, create=True, retrieve=True, update=True)
        self.subclasses(jcms_api, generics.ListCreateAPIView, generics.RetrieveUpdateAPIView)

    def test_jcms_api_overview_create_retrieve_update_delete(self):
        jcms_api = JcmsApi(User, ['username'], overview=True, create=True, retrieve=True, update=True, delete=True)
        self.subclasses(jcms_api, generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView)

    def test_jcms_api_overview_create_retrieve_delete(self):
        jcms_api = JcmsApi(User, ['username'], overview=True, create=True, retrieve=True, delete=True)
        self.subclasses(jcms_api, generics.ListCreateAPIView, generics.RetrieveDestroyAPIView)

    def test_jcms_api_overview_create_update(self):
        jcms_api = JcmsApi(User, ['username'], overview=True, create=True, update=True)
        self.subclasses(jcms_api, generics.ListCreateAPIView, generics.UpdateAPIView)

    def test_jcms_api_overview_create_delete(self):
        jcms_api = JcmsApi(User, ['username'], overview=True, create=True, delete=True)
        self.subclasses(jcms_api, generics.ListCreateAPIView, generics.DestroyAPIView)

    def test_jcms_api_overview_create_update_delete(self):
        jcms_api = JcmsApi(User, ['username'], overview=True, create=True, update=True, delete=True)
        self.subclasses(jcms_api, generics.ListCreateAPIView, generics.DestroyAPIView)
        self.subclasses(jcms_api, generics.ListCreateAPIView, generics.UpdateAPIView)

    def test_jcms_api_overview_retrieve(self):
        jcms_api = JcmsApi(User, ['username'], overview=True, retrieve=True)
        self.subclasses(jcms_api, generics.ListAPIView, generics.RetrieveAPIView)

    def test_jcms_api_overview_retrieve_update(self):
        jcms_api = JcmsApi(User, ['username'], overview=True, retrieve=True, update=True)
        self.subclasses(jcms_api, generics.ListAPIView, generics.RetrieveUpdateAPIView)

    def test_jcms_api_overview_retrieve_delete(self):
        jcms_api = JcmsApi(User, ['username'], overview=True, retrieve=True, delete=True)
        self.subclasses(jcms_api, generics.ListAPIView, generics.RetrieveDestroyAPIView)

    def test_jcms_api_overview_retrieve_update_delete(self):
        jcms_api = JcmsApi(User, ['username'], overview=True, retrieve=True, update=True, delete=True)
        self.subclasses(jcms_api, generics.ListAPIView, generics.RetrieveUpdateDestroyAPIView)

    def test_jcms_api_overview_update(self):
        jcms_api = JcmsApi(User, ['username'], overview=True, update=True)
        self.subclasses(jcms_api, generics.ListAPIView, generics.UpdateAPIView)

    def test_jcms_api_overview_update_delete(self):
        jcms_api = JcmsApi(User, ['username'], overview=True, update=True, delete=True)
        self.subclasses(jcms_api, generics.ListAPIView, generics.UpdateAPIView)
        self.subclasses(jcms_api, generics.ListAPIView, generics.DestroyAPIView)

    def test_jcms_api_overview_delete(self):
        jcms_api = JcmsApi(User, ['username'], overview=True, delete=True)
        self.subclasses(jcms_api, generics.ListAPIView, generics.DestroyAPIView)

    def test_jcms_api_create_retrieve(self):
        jcms_api = JcmsApi(User, ['username'], create=True, retrieve=True)
        self.subclasses(jcms_api, generics.CreateAPIView, generics.RetrieveAPIView)

    def test_jcms_api_create_retrieve_update(self):
        jcms_api = JcmsApi(User, ['username'], create=True, retrieve=True, update=True)
        self.subclasses(jcms_api, generics.CreateAPIView, generics.RetrieveUpdateAPIView)

    def test_jcms_api_create_retrieve_update_delete(self):
        jcms_api = JcmsApi(User, ['username'], create=True, retrieve=True, update=True, delete=True)
        self.subclasses(jcms_api, generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView)

    def test_jcms_api_create_retrieve_delete(self):
        jcms_api = JcmsApi(User, ['username'], create=True, retrieve=True, delete=True)
        self.subclasses(jcms_api, generics.CreateAPIView, generics.RetrieveDestroyAPIView)

    def test_jcms_api_create_update(self):
        jcms_api = JcmsApi(User, ['username'], create=True, update=True)
        self.subclasses(jcms_api, generics.CreateAPIView, generics.UpdateAPIView)

    def test_jcms_api_create_update_delete(self):
        jcms_api = JcmsApi(User, ['username'], create=True, update=True, delete=True)
        self.subclasses(jcms_api, generics.CreateAPIView, generics.UpdateAPIView)
        self.subclasses(jcms_api, generics.CreateAPIView, generics.DestroyAPIView)

    def test_jcms_api_create_delete(self):
        jcms_api = JcmsApi(User, ['username'], create=True, delete=True)
        self.subclasses(jcms_api, generics.CreateAPIView, generics.DestroyAPIView)

    def test_jcms_api_retrieve_update(self):
        jcms_api = JcmsApi(User, ['username'], retrieve=True, update=True)
        self.subclasses(jcms_api, None, generics.RetrieveUpdateAPIView)

    def test_jcms_api_retrieve_update_delete(self):
        jcms_api = JcmsApi(User, ['username'], retrieve=True, update=True, delete=True)
        self.subclasses(jcms_api, None, generics.RetrieveUpdateDestroyAPIView)

    def test_jcms_api_retrieve_delete(self):
        jcms_api = JcmsApi(User, ['username'], retrieve=True, delete=True)
        self.subclasses(jcms_api, None, generics.RetrieveDestroyAPIView)

    def test_jcms_api_update_delete(self):
        jcms_api = JcmsApi(User, ['username'], update=True, delete=True)
        self.subclasses(jcms_api, None, generics.UpdateAPIView)
        self.subclasses(jcms_api, None, generics.DestroyAPIView)
