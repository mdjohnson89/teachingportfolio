

# script to SCRAPE the HTML at a URL and
# search for all hotlinks inside this file
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

URL = "https://hartford.craigslist.org/"

# snag the entire HTML markup at this URL
response = urllib.request.urlopen(URL)
html = response.read()

# convert to a string
html = str(html)

# dump some of the .html file (just to check for now)
print (html)

# find all the URLs

URLstart = html.find("content=")
while (URLstart != -1):
    
    #_____YOUR CODE HERE_______
    # 1) find the end of the URL
    URLend = html.find(">\n<link")
    URL = (html[html.index(str(URLstart))+len(str(URLstart)):html.index(str(URLend))])
    print(URL)
    
    URLstart = html.find("href=")
    
# end while loop

print("\nDone.\n")