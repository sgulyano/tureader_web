from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from readerapp.models import Reader, University, AcademicField

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('name_list', nargs='+',type=str)
        
    def handle(self, *args, **options):
        uni_list = 'res/universitylist.xlsx'
        field_list = 'res/academicfieldname.xlsx'

        print(options['name_list'][0])
        
        # read academic field name provided by MUA
        print('--- Reading Academic Field Name from ' + field_list + ' ---')
        acafield = pd.read_excel(field_list, dtype='str')
        acafield.dropna(how='all', inplace=True)
        acafield.fillna('', inplace=True)
        for index, row in acafield.iterrows():
            af = AcademicField(code=row['รหัส'],
                    name = row['ชื่อสาขา'],
                    engname = row['ชื่อสาขา (ภาษาอังกฤษ)'],
                    category = row['หมวดหมู่'])
            af.save()

        # read a list of university names from a dict we prepared
        print('--- Reading University Names from ' + uni_list + ' ---')
        unis = pd.read_excel(uni_list, dtype='str')
        unis.dropna(how='all', inplace=True)
        unis.fillna('', inplace=True)

        for index, row in unis.iterrows():
            u = University(name = row['ชื่อ'],
                    engname = row['ชื่ออังกฤษ'],
                    nameabbr = row['ชื่อย่อ'],
                    engnameabbr = row['ชื่อย่ออังกฤษ'])
            u.save()

        # read a list of readers
        print('--- Reading Reader List from ' + options['name_list'][0] + ' ---')
        a=pd.read_csv(options['name_list'][0])
        a.dropna(how='all', inplace=True)
        a=a.fillna('-')

        for i in range(len(a.index)):
            A=[]
            
            for j in a.loc[i]:
                A.append(j)


            

            try:
                uni_i = University.objects.get(name=A[5])
            except University.DoesNotExist:
                print(i)
                print(A[5])
                continue

            
            if uni_i == None:
                print(i)
                print(A[5])
                continue

            p = Reader(rank=A[0],
            phd=A[1],
            firstname=A[2],
            lastname=A[3],
            edu=A[4],
            spc=A[7],
            contact=A[8],
            uni=uni_i,#A[5],
            field=A[6],
            tel=A[9],
            email=A[10],
            status=A[11],
            source=A[12])
            p.save()
        










