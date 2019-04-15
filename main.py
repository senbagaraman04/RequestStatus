'''
Program Name: Request Status.

Author: Senbagaraman M.

Problem: Sitemap.xml may contains url, which might be pointing to some error pages. Find the urls which is not valid.

'''
import xml.etree.ElementTree as ET
import writefile as c


xmlFileName = 'sitemap.xml'

tree = ET.parse(xmlFileName)  
print ("Process Started")
#print (tree)

root = tree.getroot()
print ("********************")
count = 0

#Iterate through each <url> tag and find the <loc> tag data
for item in tree.findall('url'):
	urlloc = item.find('loc').text
	#print ("The Url is ",urlloc)
	count = count + 1
	#print("moving to next file")
	c.find_connection(urlloc,count)


	
print ("********************")	
print ("All loc Indexed in "+xmlFileName+",Please find the file named",c.excelFileName)