from django.db import models

class Reader(models.Model):
    rank = models.CharField(max_length=100, default='-')
    phd = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    edu = models.TextField()  #คุณวุติ
    spc = models.TextField() #ความเชี่ยวชาญ
    contact = models.TextField()
    uni = models.CharField(max_length=200) #มหาลัย
    field = models.CharField(max_length=100)
    tel = models.TextField()
    email = models.EmailField()
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.firstname+' '+self.lastname

