from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import CountrySerializer
from .models import Country

class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryGetOne(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryInContinent(generics.ListAPIView):
    serializer_class = CountrySerializer
    def get_queryset(self):
        continent = self.kwargs['continent']
        return Country.objects.filter(continent=continent)

class CountryGetRange(generics.ListAPIView):
    serializer_class = CountrySerializer
    def get_queryset(self):
        start = self.kwargs['start'] - 1
        end = self.kwargs['end']
        return Country.objects.all()[start:end]

class CountryGetFrom(generics.ListAPIView):
    serializer_class = CountrySerializer
    def get_queryset(self):
        start = self.kwargs['start'] - 1
        return Country.objects.all()[start:]

class CountryCreate(generics.CreateAPIView):
    serializer_class = CountrySerializer
    permission_classes = [IsAdminUser]

class CountryUpdate(generics.UpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminUser]

class CountryDelete(generics.DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminUser]
