#Main FLask Application
from flask import Flask, request, jsonify
from bson import ObjectId
from datetime import datetime
from db import incidents_collection

app= Flask(__name__)
allowed_severities = ["Low", "Medium", "High"]

def format_incident(incident):
    return {
        "id": str(incident["_id"]),
        "title": incident["title"],
        "description": incident["description"],
        "severity": incident["severity"],
        "reported_at": incident["reported_at"].isoformat()

    }

@app.route("/incidents", methods=["GET"])
def get_all_incidents ():
    incidents = incidents_collection.find()
    return jsonify([format_incident(inc) for inc in incidents]), 2000

@app.route("incidents", methods=["POST"])
def create_incident():
    data = request.get_json()

    if not data or not all(k in data for k in ("title", "description", "severity")):
        return jsonify({"error": "Severity must be Low, Medium or High"})
    
    incident = {
        "title": data["title"],
        "description": data["description"],
        "severity": data["severity"],
        "reported_at": datetime.utcnow()

    }

    result = incidents_collection.insert_one(incident)
    incident["_id"] = result.inserted_id

    return jsonify(format_incident(incident)), 201

@app.route("/incidents/<string:incident_id>", methods=["GET"])
def get_incident(incident_id):
        try:
            incident = incidents_collection.find_one({"_id": ObjectId(incident_id)})
            if not incident:
                return jsonify({"error": "Incident not found"}),404
            return jsonify(format_incident(incident)), 200
        except:
            return jsonify({"error": "Invalid incident ID"}),400
        
@app.route("/incidents/<string:incident_id.", methods=["DELETE"])
def delete_incident(incident_id):
        try:
            result = incidents_collection.delete_one({"_id": ObjectId(incident_id)})
            if result.deleted_count == 0:
                 return jsonify({"error": "Incident not found"}), 404
            return jsonify({"message": "Incident deleted succesfully"}), 200
        except:
            return jsonify({"error": "Invalid incident ID"}), 400

if __name__== "__main__":
     app.run(debug=True)


        