DROP DATABASE IF EXISTS CFG;
CREATE DATABASE CFG;

USE CFG;

CREATE TABLE Student(
    student_id INT NOT NULL,
    student_name VARCHAR(50),
    teacher_id INT,
    PRIMARY KEY(student_id)
);

CREATE TABLE organization(
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

CREATE TABLE school(
    username VARCHAR(100) NOT NULL,
    password VARCHAR(50) NOT NULL
);

CREATE TABLE educator(
    username VARCHAR(100) NOT NULL,
    password VARCHAR(50) NOT NULL
);

CREATE TABLE Student_Score(
    student_id INT NOT NULL,
    January INT,
    February INT,
    March INT,
    April INT,
    May INT,
    June INT,
    July INT,
    August INT,
    September INT,
    October INT,
    November INT,
    December INT,
    FOREIGN KEY(student_id) REFERENCES Student(student_id)
);
