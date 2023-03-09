from django.urls import include, path
from . import api

urlpatterns = [
    path('protein/<str:protein_id>', api.ProteinGet.as_view(), name='protein_get_api'),
    path('protein/', api.ProteinPost.as_view(), name='protein_post_api'),
    path('pfam/<str:domain_id>', api.PfamGet.as_view(), name='pfam_get_api'),
    path('proteins/<str:taxa_id>', api.ProteinTaxaGet.as_view(), name='protein_taxa_get_api'),
    path('pfams/<str:taxa_id>', api.DomainTaxaGet.as_view(), name='domain_taxa_get_api'),
    path('coverage/<str:protein_id>', api.ProteinCoverage.as_view(), name='protein_coverage_api'),
]
