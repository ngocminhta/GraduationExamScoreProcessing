import requests
import json
import csv

with open("/Users/ngocminhta/CrawlDiemthiTHPTQG/1.csv", "w") as csvfile:
    fieldnames = ["Code", "DiaLi", "GDCD", "HoaHoc", "KHTN", "KHXH", "LichSu", "ListGroup", "NgoaiNgu", "NguVan", "Result", "SinhHoc", "Toan", "VatLi"]
    #fieldnames = ["message", "success", "result"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator="\n")
    
    writer.writeheader()
    
    provincecode = '64'
    for j in range(80000):
        try:
            sid = str(j).zfill(6)
            link = 'https://diemthi.vnanet.vn/Home/SearchBySobaodanhFile?code=' + provincecode + sid + '&nam=2022'
            response_API = requests.get(link)
            responsetext = str(response_API.text)[30:-1:]
            #print(responsetext)
            responsejson = json.loads(responsetext)
            
            #print(responsejson)
            
            for row in responsejson:
                writer.writerow(row)
                #print(row)
        except:
            pass