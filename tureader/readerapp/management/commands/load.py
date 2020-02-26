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

        cnt = 0
        for index, row in acafield.iterrows():
            _, created = AcademicField.objects.update_or_create(
                code=row['รหัส'],
                name = row['ชื่อสาขา'],
                engname = row['ชื่อสาขา (ภาษาอังกฤษ)'],
                category = row['หมวดหมู่'])
            if not created:
                print(row['ชื่อสาขา'])
            cnt += created
        print(f'Add new {cnt}/{len(acafield.index)} academica fields')

        # read a list of university names from a dict we prepared
        print('--- Reading University Names from ' + uni_list + ' ---')
        unis = pd.read_excel(uni_list, dtype='str')
        unis.dropna(how='all', inplace=True)
        unis.fillna('', inplace=True)

        cnt = 0
        for index, row in unis.iterrows():
            _, created = University.objects.update_or_create(
                name = row['ชื่อ'],
                engname = row['ชื่ออังกฤษ'],
                nameabbr = row['ชื่อย่อ'],
                engnameabbr = row['ชื่อย่ออังกฤษ'])
            cnt += created
        print(f'Add new {cnt}/{len(unis.index)} universities')

        # read a list of readers
        print('--- Reading Reader List from ' + options['name_list'][0] + ' ---')
        readers = pd.read_csv(options['name_list'][0])
        readers.dropna(how='all', inplace=True)
        readers.fillna('-', inplace=True)

        cnt = 0
        for index, row in readers.iterrows():
            try:
                uni_i = University.objects.get(name=row['มหาวิทยาลัย'])
            except University.DoesNotExist:
                print(index)
                print(row['มหาวิทยาลัย'])
                continue

            if uni_i == None:
                print('A')
                print(index)
                print(row['มหาวิทยาลัย'])
                continue

            _, created = Reader.objects.update_or_create(
                rank=row['ตำแหน่ง'],
                phd=row['ตำแหน่ง ป.เอก'],
                title=row['คำนำหน้านาม'],
                firstname=row['ชื่อ'],
                lastname=row['นามสกุล'],
                edu=row['คุณวุฒิ'],
                field=row['สาขาวิชา'],
                spc=row['ความเชี่ยวชาญ'],
                contact=row['สถานที่ติดต่อ'],
                uni=uni_i,#A[5],
                tel=row['โทร'],
                email=row['email'],
                status=row['สถานะ'],
                source=row['แหล่งที่มา'])

            cnt += created
        print(f'Add new {cnt}/{len(readers.index)} records')
        










