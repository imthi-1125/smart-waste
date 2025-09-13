# Smart-Waste

A Flask-based web application to **report and monitor waste bins** in real-time. Designed to showcase full-stack development skills with Python, HTML, CSS, JavaScript, and SQLite.

Features

- **Report Page**: Users can submit waste bin status with location and landmark.  
- **Admin Dashboard**: View all reports in a table, with visual charts for bin statuses.  
- **Minimal Elegant Design**: Clean UI for both report and admin pages.  
- **Geocoding & Map Integration** (Optional): Visualize bin locations on a map.  
- **Database**: Uses SQLite for lightweight storage of reports.
  
Technologies Used

- **Backend**: Python 3, Flask  
- **Frontend**: HTML5, CSS3, JavaScript  
- **Database**: SQLite  
- **Visualization**: Chart.js  
- **Geocoding (Optional)**: geopy  

Installation & Setup

1. Clone the repository

bash
git clone https://github.com/imthi-1125/smart-waste.git
cd smart-waste

create a virtual environment
python3 -m venv venv
source venv/bin/activate

install dependancies
pip install -r requirements.txt

run
python app.py

Open your browser at http://127.0.0.1:5000/report to submit reports and http://127.0.0.1:5000/admin to view admin dashboard.
