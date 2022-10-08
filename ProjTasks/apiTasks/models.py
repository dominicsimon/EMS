from pickle import TRUE
from django.db import models

# Create your models here.
class Task(models.Model):
    owner=models.PositiveBigIntegerField(null=False, blank=False)
    parent=models.PositiveBigIntegerField(null=True,blank=True)
    title= models.TextField(null=True, blank=True)
    body= models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    progress=models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    budget_labor=models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    budget_material=models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    budget_money=models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    spent_labor=models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    spent_material=models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    spent_money=models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)


    def _str(self):
        return self.body
