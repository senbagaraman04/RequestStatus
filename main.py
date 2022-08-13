'''
Program Name: Request Status.

Author: Senbagaraman M.

GitHubLink : https://github.com/senbagaraman04/RequestStatus

Problem: Sitemap.xml may contains url, which might be pointing to some error pages. Find the urls which is not valid.

'''
import xml.etree.ElementTree as ET
import writefile as c


xmlFileName = 'sitemap.xml'

tree = ET.parse(xmlFileName)  
print ("Process Started")

root = tree.getroot()
print ("********************")
count = 0
#print (tree.getroot())
print(root.tag)
print (root.findall('url'))


#Iterate through each <url> tag and find the <loc> tag data
for item in root.findall('url'):
	urlloc = item.find('loc').text
	print ("The Url is ",urlloc)
	count = count + 1
	print("moving to next file")
	c.find_connection(urlloc,count)


	
print ("Thank you for using Request Status for your work.")
print ("********************")	
print ("All loc Indexed in "+xmlFileName+",Please find the file named",c.excelFileName)