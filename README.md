# Aegis AI-IDS: AI-Enhanced Intrusion Detection System

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.14-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Library](https://img.shields.io/badge/library-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

In an increasingly interconnected digital landscape, the security of organizational networks and sensitive data is of paramount importance. **Aegis AI-IDS** is a modern, AI-powered Intrusion Detection System that leverages machine learning to detect, classify, and respond to network intrusions with high accuracy. 

The convergence of cutting-edge machine learning algorithms and cybersecurity expertise empowers organizations to fortify their cybersecurity defenses in the face of evolving cyber threats.

---

## 🛡️ Key Features

- **Optimized AI Engine**: Utilizes a highly trained **Random Forest Classifier** optimized down to **4 critical network flow features** from the standard 78. This reduces evaluation latency to under a millisecond, making real-time analysis viable.
- **Class-Balanced Training**: Trained on the industry-standard **CICIDS2017 Dataset**, with severe class imbalances handled using **SMOTE** (Synthetic Minority Over-sampling Technique) to ensure highly accurate detection of minority attack profiles.
- **Premium Cybersecurity Dashboard**: A clean, responsive, human-crafted dashboard that replaces generic neon templates with slate UI components:
  - **Live Threat Log**: Displays a simulated real-time stream of incoming network packet flows.
  - **On-Demand Scanner**: Submit custom network flow characteristics or load presets to perform instant security assessments.
  - **Interactive Presets**: One-click test profiles (Benign, Brute Force, SQL Injection, and XSS) loaded with actual dataset traffic characteristics.
  - **Developer API Docs**: Integration blueprints and code templates.
- **Dual-Interface (Web & REST API)**: Supports traditional HTML form submissions for administrative scans, and raw JSON inputs for programmatic API integrations.

---

## 📁 Repository Structure

```text
├── app.py                      # Flask web server and prediction API route
├── requirements.txt            # Flexible dependency configuration
├── requirements-frozen.txt     # Frozen package versions for exact replication
├── random_forest_model_4_features.joblib # Serialized Random Forest model
├── web_attacks_balanced.csv    # Balanced web attack packet data for reference
├── templates/
│   └── index.html              # Redesigned premium slate dashboard interface
└── Untitled.ipynb              # Jupyter notebook detailing model training steps
```

---

## 🔬 How the Model Works

To classify traffic efficiently inside network hardware, the model focuses on **4 key traffic flow metrics**:

1. **Flow Duration**: The total time of the packet flow in microseconds. This helps separate fast single-transaction events from slow brute force lockouts.
2. **Total Forward Packets**: Total number of packets sent from source to destination.
3. **Total Backward Packets**: Total number of packets returned from destination to source.
4. **Total Length of Fwd Packets**: Sum of payload byte sizes of forward packets. High lengths indicate payload injection attempts (e.g. SQLi).

### Performance Metrics
The Random Forest model balances accuracy and execution speed:
- **Accuracy**: $\approx 98.9\%$
- **Verdict Classes**:
  - `BENIGN` (Normal safe traffic)
  - `Web Attack – Brute Force`
  - `Web Attack – Sql Injection`
  - `Web Attack – XSS` (Cross-Site Scripting)

---

## 🚀 Setup & Installation

Follow these steps to run the application locally on your machine.

### Prerequisites
- Python 3.10 or higher (Fully tested on Python 3.14.3)
- Pip (Python Package Installer)

### 1. Clone the Project
```bash
git clone https://github.com/your-username/AI_Enhanced_Intrusion_Detection_System.git
cd AI_Enhanced_Intrusion_Detection_System/Project code
```

### 2. Set Up a Virtual Environment (Recommended)
Creating an isolated environment prevents library version conflicts:

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Choose between flexible installation (recommended for new OS/Python builds) or the frozen environment.

**For flexible, compatible installation:**
```bash
pip install -r requirements.txt
```

**For exact frozen environment replication:**
```bash
pip install -r requirements-frozen.txt
```

### 4. Run the Web Server
Launch the Flask development server:
```bash
python app.py
```
*Note: The server will run on `http://127.0.0.1:5000/` by default.*

---

## 💻 Usage & Verification

1. Open your browser and navigate to `http://127.0.0.1:5000/`.
2. View system health and live traffic streams on the **Dashboard**.
3. Navigate to **On-Demand Scanner**.
4. Click one of the quick autofill buttons under **Quick Test Presets** (e.g., *SQL Injection Attack*).
5. Press **Execute Threat Scan** to run the prediction and view the detailed analyst security report.

---

## 🔌 API Integration

You can integrate Aegis AI-IDS with custom proxies or Web Application Firewalls (WAF) using JSON payloads.

### request
- **Method**: `POST`
- **Route**: `/predict`
- **Headers**: `Content-Type: application/json`
- **Body**:
```json
{
  "flow_duration": 5006127.0,
  "total_fwd_packets": 4.0,
  "total_backward_packets": 4.0,
  "total_length_fwd_packets": 447.0
}
```

### Response (200 OK)
```json
{
  "status": "success",
  "prediction": "Web Attack - Sql Injection",
  "inputs": {
    "flow_duration": 5006127.0,
    "total_fwd_packets": 4.0,
    "total_backward_packets": 4.0,
    "total_length_fwd_packets": 447.0
  }
}
```

### Querying with cURL
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"flow_duration":76978.0,"total_fwd_packets":2.0,"total_backward_packets":2.0,"total_length_fwd_packets":78.0}'
```

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for details.

## 🤝 Acknowledgments
- Canadian Institute for Cybersecurity (CIC) for the CICIDS2017 Dataset.
- Scikit-Learn developers for the classifier framework.
