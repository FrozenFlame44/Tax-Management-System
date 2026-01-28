# 💰 Automated Tax Management System

A full-stack Django web application designed to automate Indian Income Tax calculations (New Regime FY 2025-26), manage tax profiles, and generate instant PDF receipts. This system streamlines the tax filing process with real-time analytics and audit tracking.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple.svg)


## 📌 Key Features

* **🇮🇳 New Tax Regime Logic:** Automates tax calculation based on the latest FY 2025-26 slabs (0%, 5%, 10%, etc.).
* **📊 Interactive Dashboard:** Visualizes income vs. tax liability using **Chart.js**.
* **📄 PDF Receipt Generation:** Instantly downloads official-looking tax receipts using `xhtml2pdf`.
* **🔔 Alerts & Notifications:** Notifies users about due dates and filing status updates.
* **💳 Payment Simulation:** Integrated dummy payment gateway flow for tax payments.
* **🔒 Security:** Role-based access and **Audit Logs** to track every user action (Login, Filing, Payment).
* **📂 Document Management:** (Optional) Support for uploading proofs like W-2/Form-16.

## 🛠️ Tech Stack

* **Backend:** Python, Django 5.x
* **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript (Chart.js)
* **Database:** SQLite (Default for Development) / PostgreSQL (Compatible)
* **PDF Engine:** xhtml2pdf
* **Version Control:** Git & GitHub

## 🚀 Installation & Setup Guide

Follow these steps to run the project locally on your machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/Tax-Management-System.git](https://github.com/YOUR_USERNAME/Tax-Management-System.git)
cd Tax-Management-System

2. Create & Activate Virtual Environment (Recommended)
Bash
# Windows
python -m venv env
env\Scripts\activate

# Mac/Linux
python3 -m venv env
source env/bin/activate
3. Install Dependencies
Bash
pip install -r requirements.txt
(If requirements.txt is missing, install manually: pip install django xhtml2pdf)

4. Apply Database Migrations
Initialize the database tables:

Bash
python manage.py makemigrations
python manage.py migrate
5. Create an Admin User
To access the backend admin panel:

Bash
python manage.py createsuperuser
# Follow the prompts to set a username (e.g., admin) and password.
6. Run the Server
Bash
python manage.py runserver
Open your browser and go to: http://127.0.0.1:8000/

📖 How to Use
Register/Login: Create a new user account on the login page.

File a Return: Click "File New Return", enter your Salary and Other Income.

View Logic: The system automatically calculates Gross Income and Tax based on the New Regime slabs.

Pay Tax: On the dashboard, click "Pay Now" (Simulated). The status changes to "Approved".

Download: Click "Receipt" to download your Tax Acknowledgement PDF.

Admin Panel: Go to /admin/ to view Audit Logs and manage users.

📂 Project Structure
Tax-Management-System/
├── tax_project/          # Main Django settings & URL configuration
├── tax_app/              # Core application logic
│   ├── models.py         # Database Tables (Returns, Profiles, Logs)
│   ├── views.py          # Business Logic (Calc, PDF, Auth)
│   ├── urls.py           # App routing
│   ├── utils.py          # Tax Calculation Algorithm
│   └── forms.py          # Input forms
├── templates/            # HTML Files (Dashboard, Login, Receipt)
├── static/               # CSS, JS, Images
├── manage.py             # Django command-line utility
└── db.sqlite3            # Database file
📸 Screenshots
(Optional: Add screenshots of your Dashboard and PDF Receipt here)

🤝 Contributing
Fork the repo.

Create a feature branch: git checkout -b new-feature

Commit changes: git commit -m "Added feature"

Push to branch: git push origin new-feature

Submit a Pull Request.

Developed by [Sagar Marale]
```
# Deployement Link:
  admin: https://sagar7821.pythonanywhere.com/admin/
  user: https://sagar7821.pythonanywhere.com/ 
