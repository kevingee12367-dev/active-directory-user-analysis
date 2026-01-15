# 📊 Active Directory User Analysis with Python  
**Junior Data Analyst / IT Portfolio Project**

---

## 📌 Project Overview

This project simulates a real-world task commonly assigned to a **junior data analyst or entry-level IT professional** in an enterprise environment.

The objective was to:
- Work with **Active Directory (AD)** user accounts
- Export real AD user data using **PowerShell**
- Analyze that data using **Python**
- Answer **business-driven questions** using both technical analysis and human judgment

This project reflects practical tasks seen in:
- IT Support / Help Desk
- Identity & Access Management (IAM)
- Junior Data Analyst roles

---

## 🧠 Business Scenario

> *“Kevin, we want visibility into our Active Directory environment.  
Please export user account data, analyze it, and provide insights that help us understand account status and potential security concerns.”*

---

## 🏗️ Active Directory Setup

### Environment
- Windows Server (Domain Controller)
- Active Directory Users and Computers (ADUC)
- PowerShell
- Local virtual lab (no paid services)

### AD Work Completed
- Created Organizational Units (OUs)
- Created security groups
- Created and managed user accounts
- Verified account status (enabled/disabled)

### Users Included
- Administrator (enabled)
- Guest (disabled)
- krbtgt (disabled)
- John Carter (enabled)
- Sarah Lee (enabled)
- Additional test users

This mirrors a realistic enterprise AD environment.

---

## 🔁 Data Export (PowerShell)

User data was exported directly from Active Directory using PowerShell to ensure accuracy.

### Fields Exported
- Name
- SamAccountName
- Enabled (account status)

The CSV file was validated to ensure:
- Clean headers
- No metadata corruption
- All users properly included

---

## 🐍 Python Data Analysis

### Tools Used
- Python 3.12
- pandas
- VS Code

### Analysis Performed
The Python script:
- Loads AD user data from CSV
- Validates columns and row count
- Analyzes enabled vs disabled accounts
- Identifies disabled accounts
- Outputs human-readable insights

### Summary Results
- **Total users:** 7  
- **Enabled accounts:** 5 (71.43%)  
- **Disabled accounts:** 2 (28.57%)

Disabled accounts identified:
- Guest
- krbtgt

---

## 📈 Business Questions & Answers

### **Q1: How many active users are in Active Directory?**
**Answer:**  
There are **5 active (enabled) users** out of 7 total accounts.

**Why this matters:**  
Helps IT understand current access usage.

---

### **Q2: Are there any disabled accounts?**
**Answer:**  
Yes — `Guest` and `krbtgt`.

**Why this matters:**  
Both are expected system accounts and should remain disabled for security.

---

### **Q3: What percentage of accounts are disabled?**
**Answer:**  
Approximately **28.57%** of accounts.

**Why this matters:**  
Provides a high-level security and utilization metric for leadership.

---

### **Q4: Do any disabled accounts require action?**
**Answer:**  
No immediate action is required.

Human judgment was applied to distinguish between system accounts and user-created accounts.

---

### **Q5: What risks would exist if unexpected accounts were enabled?**
**Answer:**  
- Unauthorized access
- Orphaned accounts
- Audit and compliance failures

This analysis helps proactively detect such risks.

---

### **Q6: What would be the next steps in a real company?**
**Answer:**  
- Review enabled users against HR records
- Audit group memberships
- Identify stale or unused accounts
- Schedule recurring access reviews

---

## 🧠 Human-Centered Decision Making

This project emphasizes **judgment over blind automation**.

Instead of flagging accounts purely based on status:
- Account purpose was evaluated
- Security best practices were considered
- Business context was applied

---

## 🚀 Skills Demonstrated

### Technical Skills
- Active Directory fundamentals
- PowerShell data export
- Python data analysis
- pandas
- Data validation

### Analyst & IT Skills
- Troubleshooting
- Security awareness
- Business communication
- Documentation
- Critical thinking

---

## 📁 Repository Structure


