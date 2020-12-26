# ---------------------------------------------------------------------------------------
#
# feedburner.py
#
# Source, 10 ways to optimize your feed:
# https://blog.feedly.com/10-ways-to-optimize-your-feed-for-feedly/
# ---------------------------------------------------------------------------------------
# Import packages
# ---------------------------------------------------------------------------------------
from flask import session
import lxml.etree as etree
import requests
import time
import json


# ---------------------------------------------------------------------------------------
# Global variables
# ---------------------------------------------------------------------------------------
content_type_id = "Content-Type"
json_filename = "submitted-urls.json"
file_path_json_file = "backend/json/" + json_filename
session_property_xml_filename = "xml_filename"
session_property_file_path_xml_file = "file_path_xml_file"
image = "image"
channel = "channel"

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


# Remove www. from URL to prevent double entries in json
def remove_www_feedurl(input_url):
    stripped_url = input_url
    if "http://www." in input_url:
        stripped_url = stripped_url.replace("http://www.","http://")
    elif "https://www." in input_url:
        stripped_url = stripped_url.replace("https://www.","https://")
    return stripped_url


# Save feed URL and endpoint URL to JSON object, accessed from
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
    xml_filename = timestr + ".xml"
    session[session_property_xml_filename] = xml_filename
    file_path_xml_file = "backend/xml/"
    file_path_xml_file = file_path_xml_file + xml_filename
    session[session_property_file_path_xml_file] = file_path_xml_file
    if req.status_code == 200:
        with open(file_path_xml_file, "w") as f:
            f.write(req.text)
    return xml_filename
        

# Optimize XML feed
def optimize_xml_file(feed_title, feed_description, feed_analytics_ua, feed_accentColor, feed_icon):  

    # Optimize XML feed with:
        # 1. Replace title
        # 2. Replace description
        # 3. Add webfeeds:analytics
        # 4. Add webfeeds:accentColor
        # 5. Add webfeeds:icon
        # 6. Add webfeeds:related
        # 7. Add atom:link
        # 8. Save XML with pretty_printed

    parser = etree.XMLParser(remove_blank_text = True)
    tree = etree.parse(session[session_property_file_path_xml_file], parser)
    root = tree.getroot()

    # Replace title
    title = root.xpath("//rss/channel/title")
    if title:
        # Replaces <title> text
        title[0].text = feed_title
   
    # Replace description
    description = root.xpath("//rss/channel/description")
    if description:
        # Replaces <description> text
        description[0].text = feed_description
    
    # Add webfeeds:analytics plus additional arguments
    ns = "http://webfeeds.org/rss/1.0"
    etree.register_namespace("webfeeds", ns)
    etree.Element("rss")
    find_channel = tree.find(channel)
    webfeeds = etree.SubElement(find_channel, "{http://webfeeds.org/rss/1.0}analytics")
    find_channel.insert(0, webfeeds)
    ns = {"webfeeds": "http://webfeeds.org/rss/1.0"}
    webfeeds_analytics = root.xpath("//rss/channel/webfeeds:analytics", namespaces = ns)
    for el in webfeeds_analytics:
        el.attrib["id"] = feed_analytics_ua
        el.attrib["engine"] = "GoogleAnalytics"

    # Add webfeeds:accentColor plus additional arguments
    ns = "http://webfeeds.org/rss/1.0"
    etree.register_namespace("webfeeds", ns)
    etree.Element("rss")
    find_channel = tree.find(channel)
    webfeeds = etree.SubElement(find_channel, "{http://webfeeds.org/rss/1.0}accentColor")
    find_channel.insert(0, webfeeds)
    ns = {"webfeeds": "http://webfeeds.org/rss/1.0"}
    webfeeds_accentColor = root.xpath("//rss/channel/webfeeds:accentColor", namespaces = ns)
    if webfeeds_accentColor:
        # Replaces <webfeeds:accentColor> text
        webfeeds_accentColor[0].text = feed_accentColor
        
    # Add webfeeds:icon plus additional arguments
    ns = "http://webfeeds.org/rss/1.0"
    etree.register_namespace("webfeeds", ns)
    etree.Element("rss")
    find_channel = tree.find(channel)
    webfeeds = etree.SubElement(find_channel, "{http://webfeeds.org/rss/1.0}icon")
    find_channel.insert(0, webfeeds)
    ns = {"webfeeds": "http://webfeeds.org/rss/1.0"}
    webfeeds_icon = root.xpath("//rss/channel/webfeeds:icon", namespaces = ns)
    if webfeeds_icon:
        # Replaces <webfeeds:icon> text
        webfeeds_icon[0].text = feed_icon

    # Add webfeeds:related plus additional arguments
    ns = "http://webfeeds.org/rss/1.0"
    etree.register_namespace("webfeeds", ns)
    etree.Element("rss")
    find_channel = tree.find(channel)
    webfeeds = etree.SubElement(find_channel, "{http://webfeeds.org/rss/1.0}related")
    find_channel.insert(0, webfeeds)
    ns = {"webfeeds": "http://webfeeds.org/rss/1.0"}
    webfeeds_related = root.xpath("//rss/channel/webfeeds:related", namespaces = ns)
    for el in webfeeds_related:
        el.attrib["layout"] = "card"
        el.attrib["target"] = "browser"

    # Replace atom:link
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    atom_link = root.xpath("//rss/channel/atom:link[@href]", namespaces = ns)
    for el in atom_link:
        el.attrib["href"] = "{XXXXXXXXXXXXXXXXXX}"

    # Save XML file with pretty print
    def pretty_print_write_xml(xml):
        tree.write(xml, encoding="UTF-8", pretty_print=True, xml_declaration=True)
    pretty_print_write_xml(session[session_property_file_path_xml_file])