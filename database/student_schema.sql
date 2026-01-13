CREATE DATABASE IF NOT EXISTS student_analytics;
USE student_analytics;

CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(10),
    subject VARCHAR(50),
    marks INT
);

INSERT INTO students VALUES
(1, 'Pavi', 'ISE', 'Operating Systems', 85),
(2, 'Anu', 'ISE', 'Operating Systems', 78),
(3, 'Meena', 'CSE', 'DBMS', 92),
(4, 'Kavya', 'ECE', 'Computer Networks', 68),
(5, 'Riya', 'ISE', 'DBMS', 88);
