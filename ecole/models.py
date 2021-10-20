from django.db import models

# Create your models here.
class Ecole(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Niveau(models.Model):
    ecole=models.ForeignKey(Ecole, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Classe(models.Model):
    name=models.CharField(max_length=50)
    niveau=models.ForeignKey(Niveau, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Description(models.Model):
    description=models.CharField(max_length=200)
    ecole=models.ForeignKey(Ecole, on_delete=models.SET_NULL, null=True)
    niveau=models.ForeignKey(Niveau, on_delete=models.SET_NULL, null=True)
    classe=models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.description
    

