from rest_framework import generics, serializers


# Creates the standard mixin for the general views of rest_framework
def standard_mixin(self):
    class StandardMixin:
        queryset = self.model.objects.all()
        serializer_class = self.serializer
        lookup_field = self.lookup_field

    return StandardMixin


# This returns the url that adds the api calls for a model that exists
# Options that can be returned are: retrieve, update and delete
def known_model(self):
    # Check which they should be extending
    if self.all or (self.retrieve and self.update and self.delete):
        extend_class = generics.RetrieveUpdateDestroyAPIView
    elif self.retrieve and self.update:
        extend_class = generics.RetrieveUpdateAPIView
    elif self.retrieve and self.delete:
        extend_class = generics.RetrieveDestroyAPIView
    elif self.update and self.delete:
        # There is no standard mixin for this
        class KnownModel(standard_mixin(self), generics.UpdateAPIView, generics.DestroyAPIView):
            pass

        return KnownModel
    elif self.retrieve:
        extend_class = generics.RetrieveAPIView
    elif self.update:
        extend_class = generics.UpdateAPIView
    elif self.delete:
        extend_class = generics.DestroyAPIView
    else:
        return None

    class KnownModel(standard_mixin(self), extend_class):
        pass

    return KnownModel


# This returns the url that adds the api calls for a model that does not exists
# Options that can be returned are: overview and create
def unknown_model(self):
    if self.all or (self.overview and self.create):
        extend_class = generics.ListCreateAPIView
    elif self.create:
        extend_class = generics.CreateAPIView
    elif self.overview:
        extend_class = generics.ListAPIView
    else:
        return None

    class UnknownModel(standard_mixin(self), extend_class):
        pass

    return UnknownModel


# Creates a standard serializer for a model
def create_serializer(self):
    class ModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = self.model
            fields = self.fields

    return ModelSerializer
