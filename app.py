from flask import Flask, render_template, request
import pandas as pd
import psycopg2
import os
from sqlalchemy import create_engine

def abspathgen(path:str):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dir_name,path).replace('/','\\')

app = Flask(__name__, template_folder=abspathgen("templates"))

@app.route('/')
def home():
    return render_template("index.html")

# @app.route('/index.html',methods= ['GET','POST'])
# def file_upload():
#     if request.method == 'POST':
#         file = request.files['file']
#         file_name = file.filename
#         file_data = file.read()

#         if not file_name.endswith('.xlsx') and not file_name.endswith('.xls'):
#             return render_template("index.html", status = "The file you are uploaded is not a spreadsheet!")
        
if __name__ == "__main__":
    app.run(debug=True)
