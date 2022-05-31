from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import CountrySerializer
from .models import Country

# Create your views here.

class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryGetOne(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

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

class CountryGetRange():
    pass
class CountryGetFrom():
    pass
class CountryStartWith():
    pass
class CountryEndWith():
    pass
