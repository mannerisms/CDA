import csv
from cda.models import Person
from callDataAnalyser import settings

with open('C:\Development\callDataAnalyser\TESTFILES\MOCK_Persons.csv') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)
    Person.objects.bulk_create([Person(first_name=row[1],last_name=row[2],date_of_birth=row[3],person_gender=row[4],person_type=row[5],Comment=row[6]) for row in reader])


