#test to extract the url

import xml.etree.ElementTree as ET
import writefile as c

tree = ET.parse('sitemap.xml')  
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
print ("All loc Indexed, Please find the file named sample.xls")