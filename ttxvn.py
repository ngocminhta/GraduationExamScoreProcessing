import requests
import json
import csv
import threading
import time

def getdata1():
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

def getdata2():
    with open("/Users/ngocminhta/CrawlDiemthiTHPTQG/2.csv", "w") as csvfile:
        fieldnames = ["Code", "DiaLi", "GDCD", "HoaHoc", "KHTN", "KHXH", "LichSu", "ListGroup", "NgoaiNgu", "NguVan", "Result", "SinhHoc", "Toan", "VatLi"]
        #fieldnames = ["message", "success", "result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator="\n")
        
        writer.writeheader()
        
        provincecode = '63'
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

def getdata3():
    with open("/Users/ngocminhta/CrawlDiemthiTHPTQG/3.csv", "w") as csvfile:
        fieldnames = ["Code", "DiaLi", "GDCD", "HoaHoc", "KHTN", "KHXH", "LichSu", "ListGroup", "NgoaiNgu", "NguVan", "Result", "SinhHoc", "Toan", "VatLi"]
        #fieldnames = ["message", "success", "result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator="\n")
        
        writer.writeheader()
        
        provincecode = '62'
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
                
def getdata4():
    with open("/Users/ngocminhta/CrawlDiemthiTHPTQG/4.csv", "w") as csvfile:
        fieldnames = ["Code", "DiaLi", "GDCD", "HoaHoc", "KHTN", "KHXH", "LichSu", "ListGroup", "NgoaiNgu", "NguVan", "Result", "SinhHoc", "Toan", "VatLi"]
        #fieldnames = ["message", "success", "result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator="\n")
        
        writer.writeheader()
        
        provincecode = '61'
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

def getdata5():
    with open("/Users/ngocminhta/CrawlDiemthiTHPTQG/5.csv", "w") as csvfile:
        fieldnames = ["Code", "DiaLi", "GDCD", "HoaHoc", "KHTN", "KHXH", "LichSu", "ListGroup", "NgoaiNgu", "NguVan", "Result", "SinhHoc", "Toan", "VatLi"]
        #fieldnames = ["message", "success", "result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator="\n")
        
        writer.writeheader()
        
        provincecode = '60'
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

def getdata6():
    with open("/Users/ngocminhta/CrawlDiemthiTHPTQG/6.csv", "w") as csvfile:
        fieldnames = ["Code", "DiaLi", "GDCD", "HoaHoc", "KHTN", "KHXH", "LichSu", "ListGroup", "NgoaiNgu", "NguVan", "Result", "SinhHoc", "Toan", "VatLi"]
        #fieldnames = ["message", "success", "result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator="\n")
        
        writer.writeheader()
        
        provincecode = '59'
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

def getdata7():
    with open("/Users/ngocminhta/CrawlDiemthiTHPTQG/7.csv", "w") as csvfile:
        fieldnames = ["Code", "DiaLi", "GDCD", "HoaHoc", "KHTN", "KHXH", "LichSu", "ListGroup", "NgoaiNgu", "NguVan", "Result", "SinhHoc", "Toan", "VatLi"]
        #fieldnames = ["message", "success", "result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator="\n")
        
        writer.writeheader()
        
        provincecode = '58'
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

def getdata8():
    with open("/Users/ngocminhta/CrawlDiemthiTHPTQG/8.csv", "w") as csvfile:
        fieldnames = ["Code", "DiaLi", "GDCD", "HoaHoc", "KHTN", "KHXH", "LichSu", "ListGroup", "NgoaiNgu", "NguVan", "Result", "SinhHoc", "Toan", "VatLi"]
        #fieldnames = ["message", "success", "result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator="\n")
        
        writer.writeheader()
        
        provincecode = '57'
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

def getdata9():
    with open("/Users/ngocminhta/CrawlDiemthiTHPTQG/9.csv", "w") as csvfile:
        fieldnames = ["Code", "DiaLi", "GDCD", "HoaHoc", "KHTN", "KHXH", "LichSu", "ListGroup", "NgoaiNgu", "NguVan", "Result", "SinhHoc", "Toan", "VatLi"]
        #fieldnames = ["message", "success", "result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator="\n")
        
        writer.writeheader()
        
        provincecode = '56'
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

def getdata10():
    with open("/Users/ngocminhta/CrawlDiemthiTHPTQG/10csv", "w") as csvfile:
        fieldnames = ["Code", "DiaLi", "GDCD", "HoaHoc", "KHTN", "KHXH", "LichSu", "ListGroup", "NgoaiNgu", "NguVan", "Result", "SinhHoc", "Toan", "VatLi"]
        #fieldnames = ["message", "success", "result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator="\n")
        
        writer.writeheader()
        
        provincecode = '55'
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

def getdata11():
    with open("/Users/ngocminhta/CrawlDiemthiTHPTQG/11.csv", "w") as csvfile:
        fieldnames = ["Code", "DiaLi", "GDCD", "HoaHoc", "KHTN", "KHXH", "LichSu", "ListGroup", "NgoaiNgu", "NguVan", "Result", "SinhHoc", "Toan", "VatLi"]
        #fieldnames = ["message", "success", "result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator="\n")
        
        writer.writeheader()
        
        provincecode = '54'
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

def getdata12():
    with open("/Users/ngocminhta/CrawlDiemthiTHPTQG/12.csv", "w") as csvfile:
        fieldnames = ["Code", "DiaLi", "GDCD", "HoaHoc", "KHTN", "KHXH", "LichSu", "ListGroup", "NgoaiNgu", "NguVan", "Result", "SinhHoc", "Toan", "VatLi"]
        #fieldnames = ["message", "success", "result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator="\n")
        
        writer.writeheader()
        
        provincecode = '53'
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

def getdata13():
    with open("/Users/ngocminhta/CrawlDiemthiTHPTQG/13.csv", "w") as csvfile:
        fieldnames = ["Code", "DiaLi", "GDCD", "HoaHoc", "KHTN", "KHXH", "LichSu", "ListGroup", "NgoaiNgu", "NguVan", "Result", "SinhHoc", "Toan", "VatLi"]
        #fieldnames = ["message", "success", "result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator="\n")
        
        writer.writeheader()
        
        provincecode = '52'
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

def getdata14():
    with open("/Users/ngocminhta/CrawlDiemthiTHPTQG/14.csv", "w") as csvfile:
        fieldnames = ["Code", "DiaLi", "GDCD", "HoaHoc", "KHTN", "KHXH", "LichSu", "ListGroup", "NgoaiNgu", "NguVan", "Result", "SinhHoc", "Toan", "VatLi"]
        #fieldnames = ["message", "success", "result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator="\n")
        
        writer.writeheader()
        
        provincecode = '51'
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

t = time.time()

t1 = threading.Thread(target=getdata1)

t2 = threading.Thread(target=getdata2)

t3 = threading.Thread(target=getdata3)

t4 = threading.Thread(target=getdata4)

t5 = threading.Thread(target=getdata5)

t6 = threading.Thread(target=getdata6)

t7 = threading.Thread(target=getdata7)

t8 = threading.Thread(target=getdata8)

t9 = threading.Thread(target=getdata9)

t10 = threading.Thread(target=getdata10)

t11 = threading.Thread(target=getdata11)

t12 = threading.Thread(target=getdata12)

t13 = threading.Thread(target=getdata13)

t14 = threading.Thread(target=getdata14)

t1.start()

t2.start()

t3.start()

t4.start()

t5.start()

t6.start()

t7.start()

t8.start()

t9.start()

t10.start()

t11.start()

t12.start()

t13.start()

t14.start()

t1.join()

t2.join()

t3.join()

t4.join()

t5.join()

t6.join()

t7.join()

t8.join()

t9.join()

t10.join()

t11.join()

t12.join()

t13.join()

t14.join()



print ("done in ", time.time()- t)
