from db import incidents_collection
from datetime import datetime

sample_incidents = [
    {
        "title": "Drone malfunction",
        "description": "Drone lost control and fell down near crowd",
        "severity": "High",
        "reported_at": datetime.utcnow()
    },
    {
        "title": "Financial crisis",
        "description": "AI algorith causes financial issues at starbuckc",
        "severity": "Medium",
        "reported_at": datetime.utcnow()
    },
    {
        "title": "Humanoid Robot rests",
        "description": "Robot made errors and made unplanned breaks",
        "severity": "Low",
        "reported_at": datetime.utcnow()
    }
]

incidents_collection.insert_many(sample_incidents)
print("Inserted sample incidents.")
