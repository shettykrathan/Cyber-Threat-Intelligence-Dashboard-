from flask import Flask, render_template, request, redirect, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from bson import ObjectId
from utils.vt_api import check_ip_virustotal
from utils.abuse_api import check_ip_abuse
from flask import Response
import csv
import io

load_dotenv()
app = Flask(__name__)

client = MongoClient(os.getenv("MONGO_URI"))
db = client.cti_dashboard
threats_collection = db["threats"]  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lookup', methods=['POST'])
def lookup():
    ip = request.form['ip']
    vt_data = check_ip_virustotal(ip)
    abuse_data = check_ip_abuse(ip)

    result = {
        "ip": ip,
        "virustotal": vt_data,
        "abuseipdb": abuse_data
    }

    db.threats.insert_one(result)
    return render_template('result.html', result=result)

@app.route("/visuals")
def visuals():
    raw_threats = list(db.threats.find()) 
    for t in raw_threats:
        if '_id' in t:
            t['_id'] = str(t['_id']) 
    return render_template("visuals.html", threats=raw_threats)

@app.route("/export")
def export():
    data = list(threats_collection.find({}, {'_id': 0}))  

    if not data:
        return "No data to export."

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

    return Response(
        output.getvalue(),
        mimetype='text/csv',
        headers={"Content-Disposition": "attachment;filename=cti_export.csv"}
    )

if __name__ == '__main__':
    app.run(debug=True)
