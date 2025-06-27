# 🛡️ Cyber Threat Intelligence Dashboard

A sleek and powerful dashboard that allows users to scan IP addresses using **VirusTotal** and **AbuseIPDB** APIs. Built with Flask and MongoDB, it provides real-time threat intelligence with visual charts and dark/light theme toggle.

---

## 📸 Screenshots

### 🔹 Home Page – IP Threat Scanner
![Home Page](./index.jpg)

### 🔹 Threat Analysis Result
![Result Page](./results.jpg)

> _These images show the clean dark-mode UI, IP lookup form, and threat analysis summary using VirusTotal & AbuseIPDB APIs._

---

## 🚀 Features

- 🔍 **IP Lookup** using VirusTotal and AbuseIPDB APIs
- 📊 **Visual Report** with Abuse Confidence Scores
- 💡 **Dark/Light Mode Toggle**
- 💾 **MongoDB Storage**
- 📁 **CSV Export Option**
- ⏳ **Loading Spinner on Submit**
- 🎯 Responsive and Minimal UI

---

## 🧠 Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript, Chart.js  
- **Backend**: Python (Flask)  
- **Database**: MongoDB  
- **APIs**: VirusTotal, AbuseIPDB  

---

## 🛠️ Installation

```bash
# Clone the repo
git clone https://github.com/your-username/cyber-threat-intel-dashboard.git
cd cyber-threat-intel-dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add your API keys in app.py

# Run the app
python app.py
```

Open your browser and visit: `http://127.0.0.1:5000`

---

## 📁 Project Structure

```
cyber-threat-intel-dashboard/
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── visuals.html
│   └── export.html
├── static/
│   └── styles.css
├── screenshots/
│   ├── home.png
│   └── result.png
├── app.py
├── requirements.txt
└── README.md
```

---

## ✍️ Author

**Krathan N Shetty**  
🎓 BCA Cybersecurity | Developer | NSS Volunteer  
🔗 [LinkedIn](https://www.linkedin.com/in/shettykrathan)

---

## 📄 License

This project is licensed under the MIT License.
