#for 404 testing and writing the data into excel file
import urllib.request
import ssl
import os, ssl
import xlwt
import requests
#To Supress the SSL Warning 
requests.packages.urllib3.disable_warnings()


	

#To ignore Http Errors/SSL Error
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context

#print ("Hello World")
#print ("Hitting all the extracted urls")
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def find_connection(url,count):
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE
	print ("Hitting all the extracted urls:",url,count)
	conn = requests.get(url,verify=False)
	print ("Final Code",conn.status_code)
	if conn.status_code ==404:
		style = xlwt.easyxf('font: color red ')
		sheet.write(count,1,url,style)
		sheet.write(count,0,conn.status_code,style)
	else:
		style = xlwt.easyxf('font: bold 1') 
		sheet.write(count,1,url,style)
		sheet.write(count,0, conn.status_code, style)
# Specifying column 
	workbook.save("url.xls") 

	
	

workbook = xlwt.Workbook() 
sheet = workbook.add_sheet("Sheet Name") 

# Specifying style 
style = xlwt.easyxf('font: bold 1') 

# Specifying column 
workbook.save("url.xls") 
