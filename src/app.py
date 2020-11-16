from flask import Flask, render_template, request, redirect, url_for

# Flask app initialization
app = Flask(__name__, template_folder="frontend", static_url_path="/frontend/static", static_folder="frontend/static")

# Flask app logic
@app.route("/")
def index():
    # Home page
    return render_template("/pages/index.html", title="Pyfeed", description="The only feedburner you want in 2020.")

@app.route("/submit-feed", methods=["GET", "POST"])
def submit_feed():
    # Form submit feed URL
    return render_template("/pages/form__submit-feed.html", title="Submit feed URL.", description="Submit the feed URL you'd like to optimize.")

@app.route("/optimize-feed", methods=["GET", "POST"])
def optimize_feed():
    # Checkbox submit feed URL
    if request.method == "POST":
        return render_template("/pages/form__optimize-feed.html", title="Optimize feed.", description="Choose which optimization you'd like to do on your URL.")
    else:
        return redirect(url_for("submit_feed"))

if __name__ == "__main__":
    app.run(debug=True)