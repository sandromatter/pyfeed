# ---------------------------------------------------------------------------------------
#
# app.py
#
# ---------------------------------------------------------------------------------------
# Import packages
# ---------------------------------------------------------------------------------------
from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
import feedburner


# ---------------------------------------------------------------------------------------
# Flask env and app initialization / configuration
# ---------------------------------------------------------------------------------------
app = Flask(__name__, template_folder="frontend",
            static_url_path="/frontend/static", static_folder="frontend/static")
app.config.from_object("config.ProductionConfig")


# ---------------------------------------------------------------------------------------
# Global variables
# ---------------------------------------------------------------------------------------

# If run in local environment change variable to: 
# webapp_url = "http://127.0.0.1:5000/"
webapp_url = "https://pyfeed.herokuapp.com/"

method_get = "GET"
method_post = "POST"

session_key_url_submitted = "url_submitted"
session_key_feed_optimized = "feed_optimized"
session_key_feedurl = "feedurl"
session_key_xml_filename = "xml_filename"

message_type_warning = "warning"
message_type_danger = "danger"
message_type_success = "success"

app_function_index = "index"
app_function_introduction = "introduction"
app_function_submit_feed = "submit_feed"
app_function_optimize_feed = "optimize_feed"
app_function_get_endpoint_url = "get_endpoint_url"

page_path_index = "/pages/index.html"
page_path_introduction = "/pages/introduction.html"
page_path_submit_feed = "/pages/form__submit-feed.html"
page_path_optimize_feed = "/pages/form__optimize-feed.html"
page_path_get_endpoint_url = "/pages/endpoint__feed-url.html"


# ---------------------------------------------------------------------------------------
# Flask app routes
# ---------------------------------------------------------------------------------------

# 1. Home page = /index
# 2. Introduction page = /introduction
# 3. Form submit feed URL page = /submit-feed
# 4. Form Optimize feed page = /optimize-feed
# 5. Form enter custom URL = /get-endpoint-url


# Home page
@app.route("/")
def index():
    session[session_key_url_submitted] = False
    session[session_key_feed_optimized] = False
    return render_template(page_path_index, title="Pyfeed", description="The modern 2020 python feedburner.")


# Custom error page for 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template("/pages/404.html"), 404


# Custom error page for 500
@app.errorhandler(500)
def internal_error(error):
    return render_template("/pages/500.html"),500


# Introduction page
@app.route("/introduction")
def introduction():
    return render_template(page_path_introduction, title="Introduction", description="An hommage to RSS feeds and the original Google Feedburner.")


# Form submit feed URL page
@app.route("/submit-feed", methods=[method_get, method_post])
def submit_feed():
    if request.method == method_post:
        feedurl = request.form["input_feedurl"]
        session[session_key_feedurl] = feedurl

        # Test if submitted URL is empty or valid.
        if feedburner.check_input_empty(feedurl):
            flash("Please submit an RSS feed URL.", message_type_warning)
            return redirect(url_for(app_function_submit_feed))
        elif feedburner.check_feedurl_invalid(feedurl):
            flash("Please submit a valid RSS feed URL.", message_type_danger)
            return redirect(url_for(app_function_submit_feed))
        # Therefore this is a valid RSS URL
        else:
            # Save RSS feed as XML and stripped URL into dict
            feedurl = session[session_key_feedurl]
            stripped_feedurl = feedburner.remove_www_feedurl(feedurl)
            feedburner.delete_old_xml(stripped_feedurl)
            xml_filename = feedburner.save_xml(feedurl)
            session[session_key_xml_filename] = xml_filename
            feedburner.save_json(stripped_feedurl, xml_filename)
            session[session_key_url_submitted] = True
            return redirect(url_for(app_function_optimize_feed))

    # Therefore request method must be get
    else:
        return render_template(page_path_submit_feed, title="Submit", description="Submit your RSS feed URL you'd like to optimize for feedreaders.")


# Form optimize feed page
@app.route("/optimize-feed", methods=[method_get, method_post])
def optimize_feed():
    if session[session_key_url_submitted]:
        
        # Optimize feed URL
        if request.method == method_get:
            return render_template("/pages/form__optimize-feed.html", title="Optimize", description="Choose which optimization you'd like to do on your URL. Please leave the input empty if none is required.")
        # Therefore request method must be post
        else:
            feed_title = request.form["input_title"]
            feed_description = request.form["input_description"]
            feed_analytics_ua = request.form["input_analytics_ua"]
            feed_accentColor = request.form["input_accentColor"]
            feed_icon = request.form["input_icon"]

            # Check if inputs are valid
            if feedburner.check_analytics_invalid(feed_analytics_ua):
                flash("Please submit a valid Google Analytics 3 property (UA-XXXXXX-X) or leave input empty.", message_type_danger)
                return redirect(url_for(app_function_optimize_feed))
            elif feedburner.check_image_invalid(feed_icon):
                flash("Please submit a valid URL to your icon as image or leave input empty.", message_type_danger)
                return redirect(url_for(app_function_optimize_feed))
            else:
                feedburner.optimize_xml_file(feed_title, feed_description, feed_analytics_ua, feed_accentColor, feed_icon)
                session[session_key_feed_optimized] = True
                return redirect(url_for("get_endpoint_url"))
            
    # Therefore no RSS feed URL is submitted
    else:  
        flash("Please submit an RSS feed URL first.", "warning")
        return redirect(url_for("submit_feed"))


# Form enter custom URL
@app.route("/endpoint-url")
def get_endpoint_url():
    if session[session_key_feed_optimized]:
        xml_file_endpoint_url = webapp_url + "endpoint-url/" + session[session_key_xml_filename]
        return render_template(page_path_get_endpoint_url, title="Get URL", description="Get the endpoint URL of your optimized feed.", endpoint_url = xml_file_endpoint_url)
    # Therefore no RSS feed URL is submitted and optimized
    else:
        flash("You can't get your endpoint URL without submitting a RSS feed URL first.", message_type_warning)
        return redirect(url_for(app_function_submit_feed))


# Send optimized XML file to endpoint URL
@app.route("/endpoint-url/<xml_filename>")
def xml_file_endpoint_url(xml_filename):
    file_path_xml_file = "backend/xml/"
    return send_from_directory(file_path_xml_file, xml_filename, mimetype="text/xml")


if __name__ == "__main__":
    app.run(debug=True)
