from flask import Flask
from flask import render_template
import glob

app = Flask(__name__)

#path = r'templates/*.html'
files = glob.glob("./templates/*.html")
filenames=[]
for filestr in files:
    filenames.append("http://127.0.0.1:5000/"+filestr[filestr.replace("\\","/").rfind("/")+1:])
    #    filenames.append("<a href=\"http://127.0.0.1:5000/"+filestr[filestr.replace("\\","/").rfind("/")+1:]+"\">link</a>"
#print(filenames)

@app.route("/")
def index():
    return render_template("index.html", items=filenames)

@app.route("/<string:id>")
def page(id):
    if id=="index.html":
        return index()
    else:
        return render_template(id)

#@app.route("/post/<int:id>")
#def page(id):
#    return render_template("post"+ str(id)+".html")
#
#@app.route("/post1")
#def post1():
#    return render_template("post1.html")
