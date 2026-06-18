import csv
data=[{'MOUNTAIN':'Everest','HEIGHT':'8848'},
{'MOUNTAIN':'Anamudi','HEIGHT':'2695'},
{'MOUNTAIN':'Kanchenjunga','HEIGHT':'8586'}]
with open('C:\pyprg\ch13\peak.csv','w') as CF:
    fields=['MOUNTAIN','HEIGHT']
    w=csv.DictWriter(CF,fieldnames=fields)
    w.writeheader()
    w.writerows(data)
    print("writing completed")
CF.close()
