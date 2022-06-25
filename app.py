from flask import Flask
import requests

#Untuk menjelaskan nama modul yang digunakan, sehingga ketika folder lain memanggil folder app akan otomatis teridentifikasi.
app = Flask(__name__) 

# @app.route('/', methods=['GET', 'POST'])
# def parse_request():
#     data = request.data
#     if request.method == 'GET':
#         return 'Make get' + data
#     else:
#         return 'Make post' + data

    # use data here


@app.route("/")
def home():
    return "Hello, Flasks!"