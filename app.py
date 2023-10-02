from flask import Flask

app = Flask(__name__)

doctors_list = [
    {
        "id": 23,
        "first_name": "Shaun",
        "last_name": "Murphy",
        "speciality": "Attending surgeon",
        "appointments": {},
    },
    {
        "id": 31,
        "first_name": "Neil",
        "last_name": "Melendez",
        "speciality": "Cardiothoracic Surgeon",
        "appointments": {},
    },
]


@app.route("/doctors", methods=["GET"])
def list_doctors():
    if request.method == "GET":
        doctors = ", ".join(
            f"{doc['first_name']} {doc['last_name']} (ID: {doc['id']})"
            for doc in doctors_list
        )
        return doctors


@app.route("/doctors/<int:id>", methods=["GET"])
def doctors_info(id):
    if request.method == "GET":
        for doc in doctors_list:
            if id == doc["id"]:
                return doc


@app.route("/book", methods=["POST"])
def get_appointment():
    if request.method == "POST":
        id = request.form["id"]
        day = request.form["day"]
        time = request.form["time"]
        for doc in doctors_list:
            if doc["id"] == int(id):
                if day not in [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                ]:
                    return (
                        "Invalid day selected. Please pick a day between Monday-Saturday.\n",
                        400,
                    )
                if time not in [
                    "15:00",
                    "16:00",
                    "17:00",
                    "18:00",
                    "19:00",
                    "20:00",
                    "21:00",
                ]:
                    return (
                        "Invalid time selected. Please pick an hour between 15:00-21:00. Thank you!",
                        400,
                    )
                doc["appointments"] = {day: time}
                return "Your appointment with Dr. {} for {} at {} has been successfully booked.".format(
                    doc["first_name"], day, time
                )
