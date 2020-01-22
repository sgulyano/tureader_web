from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from readerapp.models import Reader

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('name', nargs='+',type=str)
        
    def handle(self, *args, **options):
        a=pd.read_csv(options['name'][0])
        a=a.fillna('-')

        for i in range(len(a.index)):
            A=[]
            
            for j in a.loc[i]:
                A.append(j)
            p=Reader(rank=A[0],
            phd=A[1],
            firstname=A[2],
            lastname=A[3],
            edu=A[4],
            spc=A[7],
            contact=A[8],
            uni=A[5],
            field=A[6],
            tel=A[9],
            email=A[10],
            status=A[11])
            p.save()










