from email.headerregistry import Address
from flask import Flask, jsonify, render_template
from service import service

app = Flask(__name__)

service = service.Service

@app.route("/")
def main():
    hostname, ip = service.fetchSystemDetails()
    return render_template("index.html", HOSTNAME=hostname, IP = ip)

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/details")
def details():
    hostname, host_ip = service.fetchSystemDetails()
    return jsonify(
        hostname=hostname,
        IP_Address = host_ip 
    )    

if __name__ == '__main__':
    app.run(debug=True, port=5000)