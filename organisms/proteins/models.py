from django.db import models

# Create your models here.

#pfam model
class Pfam(models.Model):
    domain_id = models.CharField(max_length=25, null=False, blank=False)
    domain_description = models.CharField(max_length=256, null=False, blank=False)
    def __str__(self):
        return self.domain_id

#taxonomy model
class Taxonomy(models.Model):
    taxa_id = models.CharField(max_length=15, null=False, blank=False)
    clade = models.CharField(max_length=1, default='E')
    genus = models.CharField(max_length=256, null=False, blank=False)
    species = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.taxa_id

#protein model
class Protein(models.Model):
    protein_id = models.CharField(max_length=30, null=False, blank=False)
    sequence = models.CharField(max_length=256, null=False, blank=False)
    #making taxonomy class a foreign key
    taxonomy = models.ForeignKey(Taxonomy, on_delete=models.CASCADE)
    length = models.IntegerField(null=False, blank=True)
    #use a protein-domain table to link
    domains = models.ManyToManyField(Pfam, through='Protein_Domain_link')

#protein-domain link model
class Protein_Domain_link(models.Model):
    #making protein class and pfam a foreign key
    protein = models.ForeignKey(Protein, on_delete=models.CASCADE, related_name='protein_linked')
    pfam_id = models.ForeignKey(Pfam, on_delete=models.CASCADE, related_name='domain_linked')
    description = models.CharField(max_length=256, null=False, blank=False)
    start = models.IntegerField(null=False, blank=False)
    stop = models.IntegerField(null=False, blank=False)

