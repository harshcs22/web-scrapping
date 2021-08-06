import requests
from bs4 import BeautifulSoup as bts
url = "https://www.walmart.com/reviews/product/14898365"

#Get data from url
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

#PArse HTML data
soup = bts(htmlContent,'html.parser')
#print(soup)

#To scrape data
def scrap(tag,className):
    name= soup.find_all(tag, class_=className)
    #len(name)
    cust_list = []
    for i in range(0,len(name)):
        cust_list.append(name[i].get_text())
    return cust_list

name = scrap('span','review-footer-userNickname')   
title = scrap('h3','review-title font-bold')  
body = scrap('div','review-text')  
rating = scrap('span','average-rating')  
date = scrap('span','review-date-submissionTime')  

# load data in dataframe
import pandas as pd
data= pd.DataFrame()
data['customer_name']= name
data['Date']= date
data['description']= body
data['Rating']= rating[5:]
data1=pd.DataFrame({'Title':title})
data= pd.concat([data,data1], ignore_index=True, axis=1)


#to Save data in CSV file 
data.to_csv(r'C:\review.csv', index=True)