import csv
from sys import argv
'''
with open('data.csv', 'w+') as csvfile:
    wri = csv.writer(csvfile)
    wri.writerow(['Subject', 'Description'])
    wri.writerow(['Prob', 'Im goint to be failed with high probability.'])
    wri.writerow(['Ckts', 'I need a huge amount of practice!'])
'''
if argv[1] is '1':
    with open('dict.csv', 'w+') as dictfile:
        fieldnames = ['title', 'eva', 'date']
        data_dict = [{'title': 'courage', 'eva': 10, 'date': '10/17'}, {'title': 'weakness', 'eva': 6, 'date': '8/13'}]
        w = csv.DictWriter(dictfile, fieldnames=fieldnames)
        w.writeheader()
        w.writerow({'title':'mit physics', 'eva':3, 'date':'3/11'})
        w.writerows(data_dict)

elif argv[1] is '2':
    with open('dict.csv', 'r') as dictfile:
        r = csv.DictReader(dictfile)
        for row in r:
            print (row)
