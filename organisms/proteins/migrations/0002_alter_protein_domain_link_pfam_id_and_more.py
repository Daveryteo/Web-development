# Generated by Django 4.1.7 on 2023-03-09 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proteins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protein_domain_link',
            name='pfam_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domain_linked', to='proteins.pfam'),
        ),
        migrations.AlterField(
            model_name='protein_domain_link',
            name='protein',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='protein_linked', to='proteins.protein'),
        ),
    ]