from flask import Flask

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return "Starding Machine Learning Project"

if __name__=="__main":
    app.run(debug=True)