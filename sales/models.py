from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sales(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.company.name} - {self.amount} on {self.date}"

