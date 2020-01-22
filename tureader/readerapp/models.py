from django.db import models

class Reader(models.Model):
    rank = models.CharField('ตำแหน่งทางวิชาการ', max_length=100, default='-')
    phd = models.CharField('ตำแหน่ง ป.เอก', max_length=100)
    firstname = models.CharField('ชื่อ', max_length=100)
    lastname = models.CharField('สกุล', max_length=100)
    edu = models.TextField('คุณวุฒิ')
    spc = models.TextField('ความเชี่ยวชาญ')
    contact = models.TextField('สถานที่ติดต่อ')
    uni = models.CharField('มหาวิทยาลัย', max_length=200) #มหาลัย
    field = models.CharField('สาขาวิชา', max_length=100)
    tel = models.TextField('โทร.')
    email = models.EmailField('อีเมล')
    status = models.CharField('สถานะ', max_length=100)
    spc_field = models.TextField('สาขาวิชาตาม ก.พ.อ.')
    source = models.CharField('แหล่งที่มา', max_length=100)
    def __str__(self):
        return self.firstname+' '+self.lastname