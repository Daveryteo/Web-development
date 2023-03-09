from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from .models import *
from .serializers import *
from django.db.models import Sum

#get the protein sequence and all data based on the protein id
class ProteinGet(generics.RetrieveAPIView):
    lookup_field = 'protein_id'
    queryset = Protein.objects.all()
    serializer_class = ProteinSerializer

#add a new record
class ProteinPost(generics.CreateAPIView):
    queryset = Protein.objects.all()
    serializer_class = ProteinSerializer

#return domain and description
class PfamGet(generics.RetrieveAPIView):
    lookup_field = 'domain_id'
    queryset = Pfam.objects.all()
    serializer_class = PfamSerializer

#return protein id based on taxa id
class ProteinTaxaGet(generics.ListAPIView):
    queryset = Protein.objects.all()
    serializer_class = ProteinTaxaSerializer
    def filter_queryset(self, queryset):
        results = queryset.filter(taxonomy__taxa_id=self.kwargs.get('taxa_id'))
        return results

#get domains from taxa id
class DomainTaxaGet(generics.ListAPIView):
    queryset = Protein_Domain_link.objects.all()
    serializer_class = ProteinDomainSerializer
    def filter_queryset(self, queryset):
        results = queryset.filter(protein__taxonomy__taxa_id=self.kwargs.get('taxa_id'))
        return results

#protein coverage
class ProteinCoverage(generics.GenericAPIView):
    def get(self, request, protein_id):
        protein = Protein.objects.get(protein_id=protein_id)
        start = Protein_Domain_link.objects.filter(protein__protein_id=protein_id).aggregate(Sum('start'))['start__sum']
        stop = Protein_Domain_link.objects.filter(protein__protein_id=protein_id).aggregate(Sum('stop'))['stop__sum']
        length = protein.length
        diff = start - stop
        coverage = diff/length
        return Response(abs(coverage))
