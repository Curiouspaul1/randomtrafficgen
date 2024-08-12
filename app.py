from flask import Flask
import random

app = Flask(__name__)


speed_values = [
    "NORMAL", "SLOW", "HEAVY"
]

listMap = [
    {
        "beforeT": [
            {
                "startPolylinePointIndex": 0,
                "endPolylinePointIndex": 2,
                "speed": random.choice(speed_values)
            }
        ],
        "afterT": [
            {
                "startPolylinePointIndex": 0,
                "endPolylinePointIndex": 2,
                "speed": random.choice(speed_values)
            }
        ]
    }
]


@app.route('/')
def gen_data():
    resp = {
        "beforeT": [
            {
                "startPolylinePointIndex": 0,
                "endPolylinePointIndex": 2,
                "speed": random.choice(speed_values)
            }
        ],
        "afterT": [
            {
                "startPolylinePointIndex": 0,
                "endPolylinePointIndex": 2,
                "speed": random.choice(speed_values)
            }
        ]
    }
    response = {
        "routes": [
            {
                "travelAdvisory": {
                    "speedReadingIntervals": resp
                }
            }
        ]
    }
    return response, 200
