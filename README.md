# 🗃️ Data Redundancy Removal System

This project is built as part of the **CodeAlpha Cloud Computing Internship**. It is a cloud-enabled system that removes redundant or duplicate data from a database to ensure accuracy and consistency.

---

## ✅ Objective

To develop a backend system that:
- Identifies and prevents redundant data entries.
- Validates new data before storing it.
- Maintains a clean and accurate database using JSON as a simulated cloud storage.

---

## 🔧 Features

- 🔄 **Redundant Data Check**: Detects if a data entry already exists.
- ✅ **Validation Mechanism**: Adds only unique entries.
- 💾 **JSON-Based Cloud Storage**: Simulates a cloud database.
- 📡 **API Endpoints**:
  - `POST /add` → Add a new entry
  - `GET /data` → View all stored entries

---

## 🛠️ Tech Stack

- **Backend**: Python + Flask
- **Data Storage**: JSON File (acts as cloud simulation)
- **Deployment Ready**: Render / Heroku / Any cloud provider

---

## 🚀 How to Run Locally

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/CodeAlpha_DataRedundancyRemoval.git
cd CodeAlpha_DataRedundancyRemoval
