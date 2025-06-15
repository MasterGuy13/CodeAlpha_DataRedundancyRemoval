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
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Flask App**

```bash
python app.py
```

4. **Test with Postman or CURL**

- Add data (POST request):
```json
POST http://127.0.0.1:5000/add
Body:
{
  "id": "101",
  "name": "Meer Imam"
}
```

- View all data (GET request):
```
GET http://127.0.0.1:5000/data
```

---

## 📁 Project Structure

```
CodeAlpha_DataRedundancyRemoval/
│
├── app.py               # Flask backend logic
├── database.json        # Simulated cloud storage
├── requirements.txt     # Dependencies
└── README.md            # Project description
```

---

## ✍️ Author

**Meer Imam**  
BTech CSE, Amity University  
Connect on [LinkedIn](https://www.linkedin.com/) *(add your actual link)*

---

## 📜 License

This project is for academic and learning purposes only, submitted as part of the CodeAlpha Internship.
