from django.db import models

class Patient(models.Model):
    male = 1
    female = 2
    GENDER = (
        (male, 'male'),
        (female, 'female'),
    )

    name= models.CharField(max_length=100, unique=True)
    age= models.IntegerField()
    mobileNUM= models.IntegerField()
    diagonisis= models.CharField(max_length=2000)
    gender = models.PositiveSmallIntegerField(choices=GENDER, null=True, blank=True, default=male)

    def __str__(self):
        return self.name

class Sample(models.Model):
    sampleID=models.IntegerField()
    refregator= models.IntegerField()
    rackNUM=models.IntegerField()
    lineNum=models.IntegerField()
    patient= models.ForeignKey(Patient,on_delete=models.CASCADE)




