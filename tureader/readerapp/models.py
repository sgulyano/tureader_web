from django.db import models

class University(models.Model):
    name = models.CharField('ชื่อสถาบัน', max_length=300)
    engname = models.CharField('ชื่อสถาบันภาษาอังกฤษ', max_length=300)
    nameabbr = models.CharField('ชื่อย่อสถาบัน', max_length=50)
    engnameabbr = models.CharField('ชื่อย่อสถาบันภาษาอังกฤษ', max_length=50)
    def __str__(self):
        return self.name

class AcademicField(models.Model):
    code = models.CharField('รหัสวิชา', max_length=50)
    name = models.CharField('ชื่อสาขา', max_length=300)
    engname = models.CharField('ชื่อสาขา (ภาษาอังกฤษ)', max_length=300)
    category = models.CharField('หมวดหมู่', max_length=200)
    def __str__(self):
        return self.code+' '+self.name

class Reader(models.Model):

    RANK_CHOICES = [
        ('อาจารย์', 'อาจารย์'),
        ('อาจารย์ (พิเศษ)', 'อาจารย์ (พิเศษ)'),
        ('ผู้ช่วยศาสตราจารย์', 'ผู้ช่วยศาสตราจารย์'), 
        ('ผู้ช่วยศาสตราจารย์ (พิเศษ)', 'ผู้ช่วยศาสตราจารย์ (พิเศษ)'), 
        ('รองศาสตราจารย์', 'รองศาสตราจารย์'),
        ('รองศาสตราจารย์ (พิเศษ)', 'รองศาสตราจารย์ (พิเศษ)'), 
        ('ศาสตราจารย์', 'ศาสตราจารย์'),
        ('ศาสตราจารย์ (พิเศษ)', 'ศาสตราจารย์ (พิเศษ)'),
        ('ศาสตราจารย์กิตติคุณ', 'ศาสตราจารย์กิตติคุณ'),
        ('ศาสตราจารย์เกียรติคุณ', 'ศาสตราจารย์เกียรติคุณ'), 
        ('ศาสตราจารย์ ระดับ 11', 'ศาสตราจารย์ ระดับ 11'), 
        ('ศาสตราจารย์ (มทส.)', 'ศาสตราจารย์ (มทส.)'), 
        ('ศาสตราจารย์ (มจธ.)', 'ศาสตราจารย์ (มจธ.)'), 
        ('ศาสตราจารย์ (AIT)', 'ศาสตราจารย์ (AIT)'),
        ('ศาสตราจารย์ (มทม.)', 'ศาสตราจารย์ (มทม.)'), 
        ('ศาสตราจารย์ (มวล.)', 'ศาสตราจารย์ (มวล.)'),
        ('-', '-'),
        ]



    PHD_CHOICES = [
        ('ดร.', 'ดร.'), 
        ('-', '-'),
    ]

    rank = models.CharField('ตำแหน่งทางวิชาการ', max_length=100, default='-', choices=RANK_CHOICES)
    phd = models.CharField('ตำแหน่ง ป.เอก', max_length=100, default='-', choices=PHD_CHOICES)
    title = models.CharField('คำนำหน้านาม', max_length=100, default='-')
    firstname = models.CharField('ชื่อ', max_length=100)
    lastname = models.CharField('สกุล', max_length=100)
    edu = models.TextField('คุณวุฒิ')
    spc = models.TextField('ความเชี่ยวชาญ')
    contact = models.TextField('สถานที่ติดต่อ')
    uni = models.ForeignKey(University, on_delete=models.DO_NOTHING, verbose_name='มหาวิทยาลัย') #'มหาวิทยาลัย'
    field = models.CharField('สาขาวิชา', max_length=100)
    tel = models.TextField('โทร.')
    email = models.EmailField('อีเมล')
    status = models.CharField('สถานะ', max_length=100)
    spc_field = models.ManyToManyField(AcademicField, verbose_name='สาขาวิชาตาม ก.พ.อ.') #'สาขาวิชาตาม ก.พ.อ.'
    source = models.CharField('แหล่งที่มา', max_length=100)
    def __str__(self):
        return self.firstname+' '+self.lastname