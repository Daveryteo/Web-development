import factory
from django.test import TestCase
from django.conf import settings
from django.core.files import File

from .models import *

class PfamFactory(factory.django.DjangoModelFactory):

    domain_id = "PF01650"
    domain_description = "PeptidaseC13family"

    class Meta:
        model = Pfam

class TaxonomyFactory(factory.django.DjangoModelFactory):
    taxa_id = "53326"
    clade = "E"
    genus = "Ancylostoma"
    species = "ceylanicum"

    class Meta:
        model = Taxonomy

class ProteinFactory(factory.django.DjangoModelFactory):
    protein_id = "A0A016S8J7"
    sequence = "MVIGVGFLLVLFSSSVLGILNAGVQLRIEELFDTPGHTNNWAVLVCTSRFWFNYRHVSNVLALYHTVKRLGIPDSNIILMLAEDVPCNPRNPRPEAAVLSA"
    taxonomy = factory.SubFactory(TaxonomyFactory)
    length = 101

    class Meta:
        model = Protein

class ProteinDomainLinkFactory(factory.django.DjangoModelFactory):
    protein_id = factory.SubFactory(ProteinFactory)
    pfam_id = factory.SubFactory(PfamFactory)
    description = "Peptidase C13 legumain"
    start = 40
    stop = 94

    class Meta:
        model = Protein_Domain_link