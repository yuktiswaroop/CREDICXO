from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return (self.name)

class Branch(models.Model):
    
    ifsc = models.CharField(max_length=500, unique=True)
    bank_id =models.IntegerField()
    branch = models.CharField(max_length=256)  # branch     
    address = models.TextField()
    city = models.CharField(max_length=500)
    district = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    bank_name = models.ForeignKey(Bank, on_delete = models.CASCADE)

    class Meta:
        ordering = ('bank_name',)
        verbose_name = 'Branch'
        verbose_name_plural = 'Branch'
    
    def __str__(self):
    	return (self.name, self.city, self.bank)
        