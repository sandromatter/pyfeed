#---------------------------------------------------------------------------------------
# 
# app.py
# 
#---------------------------------------------------------------------------------------
# Import packages
#---------------------------------------------------------------------------------------
from flask import Flask, render_template, request, redirect, url_for, send_file, flash, session
import feedburner

#---------------------------------------------------------------------------------------
# Flask env and app initialization / configuration
#---------------------------------------------------------------------------------------
app = Flask(__name__, template_folder="frontend", static_url_path="/frontend/static", static_folder="frontend/static")
app.config.from_object("config.DevelopmentConfig")


#---------------------------------------------------------------------------------------
# Flask app routes
#---------------------------------------------------------------------------------------

# 1. Home page
# 2. Introduction page
# 3. Form submit feed URL page
# 4. Form Optimize feed page
# 5. Form enter custom URL


# Home page
@app.route("/")
def index():
    return render_template("/pages/index.html", title="Pyfeed", description="The modern 2020 python feedburner.")


# Introduction page
@app.route("/introduction")
def introduction():
    return render_template("/pages/introduction.html", title="Introduction", description="An hommage to RSS feeds and the original google feedburner.")


# Form submit feed URL page
@app.route("/submit-feed", methods=["GET", "POST"])
def submit_feed():
    if request.method == "POST":
        source_feedurl = request.form["source_feedurl"]
        submit_visit = "visited"
        session["submit_visit"] = submit_visit

        # Test if submitted URL is empty or valid.
        if feedburner.check_feedurl_empty(source_feedurl) == False:
            flash("Please submit an RSS feed URL.", "warning")
            return redirect(url_for("submit_feed"))
        else:
            if feedburner.check_feedurl_valid(source_feedurl) == False:
                flash("Please submit a valid RSS feed URL.", "danger")
                return redirect(url_for("submit_feed"))
            else:
                # Save RSS feed as XML
                feedburner.saveXML(source_feedurl)
                return redirect(url_for("optimize_feed"))

    return render_template("/pages/form__submit-feed.html", title="Submit", description="Submit your RSS feed URL you'd like to optimize for feedreaders.")


# Form Optimize feed page
@app.route("/optimize-feed", methods=["GET", "POST"])
def optimize_feed():

    if session["submit_visit"] == "visited":
        if request.method == "POST":
            # Checkbox submit feed URL
            return redirect(url_for("get_endpoint_url"))
    else:
        flash("Please submit an RSS feed URL first.", "warning")
        return redirect(url_for("submit_feed"))

    return render_template("/pages/form__optimize-feed.html", title="Optimize", description="Choose which optimization you'd like to do on your URL.")


# Form enter custom URL
@app.route("/get-endpoint-url", methods=["GET", "POST"])
def get_endpoint_url():
    if request.method == "POST":
        return render_template("/pages/endpoint__feed-url.html", title="Get URL", description="Get your custom endpoint URL of your customized feed.")
    else:
        flash("Please submit an RSS feed URL first.", "warning")
        return redirect(url_for("submit_feed"))


@app.route("/endpoint-url")
def endpoint_url():
    return send_file("frontend/pages/endpoint__feed-url-xml.xml", mimetype='text/xml')

if __name__ == "__main__":
    app.run(debug=True)