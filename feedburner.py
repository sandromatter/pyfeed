# ---------------------------------------------------------------------------------------
#
# feedburner.py
#
# Source, 10 ways to optimize your feed:
# https://blog.feedly.com/10-ways-to-optimize-your-feed-for-feedly/
# ---------------------------------------------------------------------------------------
# Import packages
# ---------------------------------------------------------------------------------------
import requests
import time
import json


# ---------------------------------------------------------------------------------------
# Global variables
# ---------------------------------------------------------------------------------------
content_type_id = "Content-Type"
json_filename = "submitted-urls.json"
file_path_json_file = "backend/json/"+json_filename


# ---------------------------------------------------------------------------------------
# Program
# ---------------------------------------------------------------------------------------

# Check if the requested URL is empty
def check_feedurl_empty(url):
    if url == "":
        return True


# Check if URL is not content-type RSS
def check_feedurl_invalid(url):
    # Check if the requested URL is valid XML
    source = requests.head(url)
    if "application/rss+xml" in source.headers[content_type_id]:
        return False
    elif "application/atom+xml" in source.headers[content_type_id]:
        return False
    elif "application/xml" in source.headers[content_type_id]:
        return False
    elif "text/xml" in source.headers[content_type_id]:
        return False
    else:
        return True


# Save feed URL and endpoint URL to JSON object
# https://github.com/fabod/pro2/blob/master/demo_snippets/10_Persistente_Daten/
def save_json(key, value):
    try:
        with open(file_path_json_file) as open_file:
            file_content = json.load(open_file)
    except FileNotFoundError:
        file_content = {}

    file_content[str(key)] = value

    with open(file_path_json_file, "w") as open_file:
        json.dump(file_content, open_file)


# Load file content from JSON object
def load_json():
    try:
        with open(file_path_json_file) as open_file:
            file_content = json.load(open_file)
    except FileNotFoundError:
        file_content = {}
    return file_content


# Save feed URL as XML
def save_xml(url):
    req = requests.get(url)
    timestr = time.strftime("%Y-%m-%d-%H%M%S")
    xml_filename = "endpoint-url-" + timestr + ".xml"
    file_path_xml_file = "backend/xml/"
    file_path_xml_file = file_path_xml_file + xml_filename
    if req.status_code == 200:
        with open(file_path_xml_file, "w") as f:
            f.write(req.text)
    return xml_filename
        

def optimize_xml_file():
    return None