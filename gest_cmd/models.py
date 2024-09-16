from django.db import models

from django.db import models

class Client(models.Model):
    code_client = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Commande(models.Model):
    num_cmd = models.AutoField(primary_key=True)
    date_cmd = models.DateField()
    design_cmd = models.CharField(max_length=255)
    code_client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.design_cmd


class Produit(models.Model):
    code_prod = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    TVA = models.DecimalField(max_digits=5, decimal_places=2)
    Prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom


class Ligne_cmd(models.Model):
    num_cmd = models.ForeignKey(Commande, on_delete=models.CASCADE)
    code_prod = models.ForeignKey(Produit, on_delete=models.CASCADE)
    Qte = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = (('num_cmd', 'code_prod'),)

    def __str__(self):
        return f"Commande {self.num_cmd} - Produit {self.code_prod}"

