from flask import Flask , jsonify
from flask.globals import request
from flask.helpers import send_file
import numpy as np
import pandas as pd
import ast
import json
import requests
from matplotlib import pyplot as plt

app= Flask(__name__)

@app.route('/NL_Question', methods= ['POST'])
    #recieve the NL Question and forward it to the model
def parse_Question():
    NL_Question = request.form.get('NL_Question')
    print(NL_Question)
    url = 'http://509ff9514fa1.ngrok.io/question'
    r = requests.post(url, data= {'nl_question': NL_Question})
    return r.json()

@app.route('/barChart', methods= ['POST'])
def bar_req():
    req_data = eval(request.form.get('data'))
    axesOrder = eval(request.form.get('axesOrder'))
    acol1 =[]
    acol2 =[]
    for x in req_data:
         acol1.append(x[0])
         acol2.append(x[1])
    if(axesOrder==1):
        Bchart = barChart(acol1, acol2)
    else:
        Bchart = barChart(acol2, acol1)
    return Bchart

@app.route('/pieChart', methods=['POST'])
def pie_req():
    req_data = eval(request.form.get('data'))
    axesOrder = eval(request.form.get('axesOrder'))
    print(type(req_data))
    acol1 =[]
    acol2 =[]
    for x in req_data:
         acol1.append(x[0])
         acol2.append(x[1])
    if(axesOrder == 1): 
        PChart = pieChart(acol1, acol2)
    else: 
        PChart = pieChart(acol2, acol1)
    return PChart
    

@app.route('/lineChart', methods= ['POST'])
def line_req():
    req_data = eval(request.form.get('data'))
    axesOrder = eval(request.form.get('axesOrder'))
    print(type(req_data))
    acol1 =[]
    acol2 =[]
    for x in req_data:
         acol1.append(x[0])
         acol2.append(x[1])
    if(axesOrder == 1): 
        lChart = lineChart(acol1, acol2)
    else: 
        lChart = lineChart(acol2, acol1)
    return lChart    

def barChart(columns , data):
    plt.bar(columns, data)
    plt.savefig('barfoo.png')
    plt.clf()
    return send_file('barfoo.png')

def pieChart(columns, data):
    plt.pie(data,labels =columns, autopct ='%1.1f%%')
    plt.savefig('piefoo.png')
    plt.clf()
    return send_file('piefoo.png')

def lineChart(columns, data): 
    plt.plot(columns, data)
    plt.savefig('lineFoo.png')
    plt.clf()
    return send_file('lineFoo.png')