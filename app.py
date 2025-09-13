from flask import Flask, render_template, request, redirect
import sqlite3, datetime
from geopy.geocoders import Nominatim

app = Flask(__name__)
geolocator = Nominatim(user_agent="smart_waste_app")

# --- Database Setup ---
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    # Create table with landmark, pincode, coordinates
    c.execute('''CREATE TABLE IF NOT EXISTS reports
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  location TEXT,
                  landmark TEXT,
                  pincode TEXT,
                  status TEXT,
                  latitude REAL,
                  longitude REAL,
                  timestamp TEXT)''')
    conn.commit()
    conn.close()

init_db()

# --- Routes ---
@app.route("/report", methods=["GET", "POST"])
def report():
    if request.method == "POST":
        location = request.form["location"]
        landmark = request.form.get("landmark", "")
        pincode = request.form["pincode"]
        status = request.form["status"]
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Geocode pincode to coordinates
        try:
            loc = geolocator.geocode(pincode)
            if loc:
                latitude = loc.latitude
                longitude = loc.longitude
            else:
                latitude = 20.5937  # fallback: center of India
                longitude = 78.9629
        except:
            latitude = 20.5937
            longitude = 78.9629

        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("""INSERT INTO reports 
                     (location, landmark, pincode, status, latitude, longitude, timestamp)
                     VALUES (?, ?, ?, ?, ?, ?, ?)""",
                  (location, landmark, pincode, status, latitude, longitude, timestamp))
        conn.commit()
        conn.close()
        return redirect("/report")
    return render_template("report.html")

@app.route("/admin")
def admin():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM reports ORDER BY id DESC")
    data = c.fetchall()
    conn.close()
    return render_template("admin.html", reports=data)

if __name__ == "__main__":
    app.run(debug=True)
