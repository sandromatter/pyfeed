from flask import Flask, render_template

# Flask app initialization
app = Flask(__name__, template_folder="frontend", static_url_path="/frontend/static", static_folder="frontend/static")

# Flask app logic
@app.route("/")
def index():
    # Home page
    return render_template("/pages/index.html", title="Pyfeed", description="The only feedburner you want in 2020.")

if __name__ == "__main__":
    app.run(debug=True)