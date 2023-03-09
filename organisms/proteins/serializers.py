from rest_framework import serializers
from .models import *

#create the Pfam serializers
class PfamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pfam
        fields = ['domain_id', 'domain_description']

class TaxonomySerializer(serializers.ModelSerializer):

    class Meta:
        model = Taxonomy
        fields = ['taxa_id', 'clade', 'genus', 'species']

class ProteinDomainLinkSerializer(serializers.ModelSerializer):

    pfam_id = PfamSerializer(many=False)
    class Meta:
        model = Protein_Domain_link
        fields = ['pfam_id', 'description', 'start', 'stop']

class ProteinSerializer(serializers.ModelSerializer):

    taxonomy = TaxonomySerializer()
    domains = ProteinDomainLinkSerializer(source='protein_linked', many=True)
    class Meta:
        model = Protein
        fields = ['protein_id', 'sequence', 'taxonomy', 'length', 'domains']


#helps to return protein id from taxa id
class ProteinTaxaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Protein
        fields = ['id', 'protein_id']

#helps to return pfam id from taxa id
class ProteinDomainSerializer(serializers.ModelSerializer):

    pfam_id = PfamSerializer(many=False)
    class Meta:
        model = Protein_Domain_link
        fields = ['id', 'pfam_id']