#---------------------------------------------------------------------------------------
# 
# feedburner.py
# 
#---------------------------------------------------------------------------------------
# Import packages
#---------------------------------------------------------------------------------------
import requests


#---------------------------------------------------------------------------------------
# Program
#---------------------------------------------------------------------------------------

# check if the requested URL is empty
def check_feedurl_empty(url):
    if url == "":
        # return to login page
        return False

# Check if URL had content-type rss.
def check_feedurl_valid(url):
    # check if the requested URL is valid XML
    source = requests.head(url)
    if source.headers["Content-Type"] != "":
        if "application/rss+xml" in source.headers["Content-Type"]:
            return True
        if "application/atom+xml" in source.headers["Content-Type"]:
            return True
        if "application/xml" in source.headers["Content-Type"]:
            return True
        if "text/xml" in source.headers["Content-Type"]:
            return True
        else:
            return False

# Save feedurl as XML
def saveXML(url):
    req = requests.get(url)
    if req.status_code == 200:
        with open("backend/xml_raw_data/endpoint__feed-url-xml.xml", "w") as f:
            f.write(req.text)