# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 16:32:18 2015

@author: NAGDEV
"""

"""
This script retrieves the urls that correspond to user profiles on freelancer.com
Here is an example url:
    https://www.freelancer.com/u/zhj11651.html
    
On the website, freelancers are viewed in pages (10 per page). For example, 
page 1 is https://www.freelancer.com/freelancers/skills/all/1
page 2 is https://www.freelancer.com/freelancers/skills/all/2
etc.

Open a web browser (e.g. chrome) and go to page 1: https://www.freelancer.com/freelancers/skills/all/1.
Right click on the username of the 1st freelancer and click 'Copy Link Address'. If you do this for username 'calciustech',
the link https://www.freelancer.com/u/calciustech.html is copied. This is the link to the person's full profile. We want to get
all this link of multiple freelancers and store them in a file.

Our script will browse page by page, and retrieve the links of the 10 freelancers in each page.
"""

Links_FILE = 'freelancers.txt'

def loadLinks(wordFile):
    """Returns a set of words from a file"""
    return list(line.strip() for line in open(wordFile))

# Let's load the default links 
linksList = loadLinks(Links_FILE)

#import the two libraries we will be using in this script




import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from numpy.random import randn
import urllib



#number of pages you want to retrieve (remember: 10 freelancers per page)
#pagesToGet=10

#create a new file, which we will use to store the links to the freelancers. The 'w' parameter signifies that the file will be used for writing.
#fileWriter=open('freelancers.txt','w')

i=0 

with open("test.txt", "wt") as out_file:

  
    while i<len(linksList):
        htmlfile = urllib.request.urlopen(linksList[i]).read()
        soup = BeautifulSoup(htmlfile)
#    #[int(span.text) for span in soup.find_all("span", class_="hourly-rate-value")]
        j='\n'.join([p.get_text(strip=True) for p in soup.find_all("span", class_="review-total")])
        k='\n'.join([p.get_text(strip=True) for p in soup.find_all("h1", class_="profile-intro-username")])
        h='\n'.join([p.get_text(strip=True) for p in soup.find_all("div", class_="profile-location")])
        m='\n'.join([p.get_text(strip=True) for p in soup.find_all("div", class_="profile-membership-length")])
        n='\n'.join([p.get_text(strip=True) for p in soup.find_all("span", class_="user-earnings-total")])
        l='\n'.join([p.get_text(strip=True) for p in soup.find_all("h1", class_="profile-experience-item")])
        p='\n'.join([p.get_text(strip=True) for p in soup.find_all('div', class_='profile-recommendation')])
        q='\n'.join([p.get_text(strip=True) for p in soup.find_all('div', class_='pprofile-hourly-rate')]) 
        i+=1
        out_file.write('%s   %s   %s    %s    %s    %s    %s   %s\n'%(k, n, j, h, m, l, p, q))

    out_file.close()
#>>>>>>>You will check some interesting correlations via correlation plots in Seaborn (e.g. number of skills vs billing rate)
with open("test.txt") as f:
    data = f.read()

data = data.split('\n')

x = [row.split(' ')[0] for row in data] #Will result in error but if we correation between two parameters 
y = [row.split(' ')[1] for row in data] #the code runs perfectly fine and plots correlation between two parameters

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Review Vs Rating")    
ax1.set_xlabel('Review')
ax1.set_ylabel('Rating')

ax1.plot(x,y, c='r', label='Ploting Example')

leg = ax1.legend()

plt.show()

#>>>>>>>>>>>>>>>>>You will do visualizations of interesting metrics using Seaborn ( charts of distributions).
plt.hist(j, m, n, p)
plt.xlabel("Plotting user Parameters")
plt.ylabel("User Profile")

    
#Google
#stack overflow
#seaborn Api ref
#Python the hard way

# Write a file
    

"""for page in range(1,pagesToGet+1):
    
    print('processing page :', page)

    
    #make the full page url by appending the page num to the end of the standard prefix
    #we use the str() function because we cannot concatenate strings with numbers. We need
    #to convert the number to a string first.
    url='https://www.freelancer.com/freelancers/skills/all/'+str(page)

    #use the browser to get the url.
    with urllib.request.urlopen(url) as response:
       myHTML = response.read()

    unique=set() #remember unique usernames

    users=re.finditer('<a href="/u/(.*?)"',str(myHTML)) #get all the matches

    for user in users:
        username=user.group(1) # get the username
        if username.find('%')==-1:unique.add(username) #check to avoid adding the <%- username %>.html construct

    #write the results
    for username in unique:
        fileWriter.write('https://www.freelancer.com/u/'+username+'\n')


#close the file. File that are opened must always be closed to make sure everything is actually written and finalized.
fileWriter.close()"""