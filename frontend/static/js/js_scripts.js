var xml_filename = {{ xml_filename }}

function replaceUrl() {
    document.getElementById("xml_redirect").onclick = function () {
        var theUrl = "http://127.0.0.1:5000/project/" + e;
        window.location.replace(theUrl);
    };
}
