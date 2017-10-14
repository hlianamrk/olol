import requests
import json
import numpy as np

City1 =input("First City: ")
Country1=input("First Country: ")
City2 =input("Second City: ")
Country2=input("Second Country: ")


url = "https://api.openaq.org/v1/latest"

City1="Omaha-Council Bluffs"
Country1="US"
City2="Flanders"
Country2="BE"

querystring1 = {"city":[City1],"country":[Country1],"limit":"1"}
response1 = requests.request("GET", url,params=querystring1)
json_data1 = response1.json()

querystring2 = {"city":[City2],"country":[Country2],"limit":"1"}
response2 = requests.request("GET", url,params=querystring2)
json_data2=response2.json()

pinakas=[]

for i in range(0,len(json_data1['results'][0]['measurements'])):
 pin=(json_data1['results'][0]['measurements'][i]['parameter'])
 akas=(json_data1['results'][0]['measurements'][i]['value'])
 pinakas.append([pin,akas])

pinakas2=[]
for i in range(0,len(json_data2['results'][0]['measurements'])):
 pin2=(json_data2['results'][0]['measurements'][i]['parameter'])
 akas2=(json_data2['results'][0]['measurements'][i]['value'])
 pinakas2.append([pin2,akas2])

a=([i[0] for i in pinakas])
b=([i[0] for i in pinakas2])

main_list = [item for item in a if item in b]

if not main_list:
  print("Not enough elements to compare")
else:
	for i in pop:
		
		for y in lol:
			
			if (i[0]==y[0]):
				if(i[1]>y[1]):
					c+=1
					fp1=(i[0])
				else:
					c2+=1
					fp2=(i[0])
	if (c>c2):
		print (City1,"has better air quality in",fp1)
	else:
		print(City2,"has better air quality",fp2)