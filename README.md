# 📊 Student Performance Data Analytics  
*(MySQL + Python Project)*

## 📌 Project Overview
The **Student Performance Data Analytics** project is a data-driven application that analyzes student academic performance using **MySQL** as the database backend and **Python** for data processing and visualization.

The project retrieves student marks from a relational database, performs analytical operations using **Pandas**, and visualizes subject-wise performance using **Matplotlib**. This system helps in understanding academic trends and identifying subjects where students perform better or need improvement.

---

## 🛠️ Technologies Used
- **Database:** MySQL 8.0  
- **Programming Language:** Python 3  
- **Libraries:**  
  - mysql-connector-python  
  - pandas  
  - matplotlib  
- **Tools:**  
  - MySQL Workbench  
  - Visual Studio Code  
  - Git & GitHub  

---

## 📁 Project Structure
Student-Performance-Data-Analytics/
│
├── database/
│ └── student_schema.sql
│
├── src/
│ ├── db_connection.py
│ ├── analysis.py
│ └── main.py
│
├── output/
│ └── graphs.png (generated during execution)
│
├── .gitignore
├── LICENSE
└── README.md


---

## 🗄️ Database Schema
The database `student_analytics` contains a table named `students` with the following attributes:

| Column Name | Data Type | Description |
|------------|----------|-------------|
| student_id | INT (PK) | Unique student ID |
| name | VARCHAR(50) | Student name |
| department | VARCHAR(10) | Department |
| subject | VARCHAR(50) | Subject name |
| marks | INT | Marks obtained |

---



