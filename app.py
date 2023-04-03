from flask import Flask, render_template, request
import pandas as pd
import psycopg2
import os
import io
import xlrd
import openpyxl
from sqlalchemy import create_engine

def abspathgen(path:str):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dir_name,path).replace('/','\\')

app = Flask(__name__, template_folder=abspathgen("templates"))

@app.route('/', methods = ['GET','POST'])
def home():

    if request.method == 'POST':
        file = request.files['file']
        file_name = file.filename
        file_data = file.read()

        if file_name == None:
            return render_template("index.html", message='No file selected')
        elif not file_name.endswith('.xlsx') and not file_name.endswith('.xls'):
            return render_template("index.html", message='Invalid file format. Please upload an Excel file.')
        else:
            data = pd.read_excel(io.BytesIO(file_data), engine='xlrd')
            print(data)
            return render_template("index.html", success_message='File Uplaoded Successfully!')
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
