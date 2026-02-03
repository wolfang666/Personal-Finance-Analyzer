# 💳 Adaptive ML-Based Transaction Categorization and Insight System

An **AI-assisted personal finance analysis system** for extracting, categorizing, and analyzing **Google Pay (GPay) transaction data** from PDF statements.  
The project combines **structured data processing**, **human-in-the-loop categorization**, and **local LLM-based insight generation** with an interactive dashboard.

---

## 📝 Project Description

This project implements an **end-to-end personal finance analysis pipeline** that converts unstructured GPay PDF statements into meaningful analytical insights.

Key highlights:
- Parses and structures transaction data from PDF statements
- Categorizes transactions using merchant-based logic
- Allows **human-in-the-loop corrections** to improve categorization accuracy
- Uses a **local Large Language Model (LLM)** to generate interpretable spending insights
- Designed to be **privacy-preserving**, with no external API dependency

---

## 📊 Data Source

- **Input:** Google Pay (GPay) PDF transaction statements  
- **Extracted Fields:**
  - Transaction date
  - Merchant name
  - Transaction amount
  - Transaction type

> No financial data is stored in this repository.  
> All data is processed and stored locally.

---

## 🧠 System Methodology

### 🔹 Transaction Extraction
- Parsed GPay PDF statements to extract transaction metadata
- Cleaned and normalized extracted records
- Stored structured data in a lightweight relational database

### 🔹 Transaction Categorization
- Implemented **merchant-based categorization**
- Built a **human-in-the-loop correction interface**
- Corrections are persisted for future analyses

### 🔹 LLM-Based Insight Generation
- Integrated a **local LLM using `llama.cpp`**
- Generated interpretable insights such as dominant categories and spending patterns
- All inference is performed **locally**, ensuring data privacy

### 🔹 Analytics & Aggregation
- Monthly spending trends
- Category-wise expenditure distribution
- Top merchant summaries

---

## 📈 Visualization & Dashboard

- Interactive **Streamlit dashboard**
- Monthly trend charts, category breakdowns, and KPIs
- Focus on interpretability over black-box recommendations

---

## 🚀 Key Features

✅ End-to-end personal finance analysis  
✅ Human-in-the-loop transaction categorization  
✅ Local LLM-based insight generation  
✅ Privacy-preserving design  
✅ Modular and extensible architecture  

---

## 📂 Project Structure

```
Personal-Finance-Analyzer/
├── app.py
├── api/
│   └── backend_client.py
├── components/
│   ├── charts.py
│   ├── insights.py
│   └── corrections.py
├── config.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🛠️ Setup & Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📜 License

MIT License

---

## 👤 Author

**Shuvrajyoti Nath Mohajohn**  
GitHub: https://github.com/wolfang666
