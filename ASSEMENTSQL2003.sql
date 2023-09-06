CREATE DATABASE ASSIMEET ;
USE ASSIMEET ;

CREATE TABLE MEETCO 
(
WORKER_ID INT  ,
FIRST_NAME VARCHAR (25) ,
LAST_NAME VARCHAR (18) ,
SALARY INT ,
JOINING_DATE VARCHAR(50) ,
DEPARTMENT VARCHAR (20)

) ;

INSERT INTO MEETCO (WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT) 
VALUES (01,"MONIKA","VERMA",100000, "2/20/2014"  ,"HR" ) ;

INSERT INTO MEETCO VALUES
(02,"NIHARIKA","VERMA",80000,"6/112014","ADMIN"),
(03,"VISHAL","SINGHAL",300000,"2/20/2014","HR"),
(04,"AMITABH","SINGH",500000,"2/20/2014","ADMIN"),
(05,"VIVEK","BHATI",500000,"6/11/2014","ADMIN"),
(06,"VIPUL","DIWAN",200000,"6/11/2014","ACCOUNT"),
(07,"SATISH","KUMAR",75000,"1/20/2014","ACCOUNT"),
(08,"GEETIKA","CHAUHAN",90000,"4/11/2014","ADMIN") ;

/*1. Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME
Ascending and DEPARTMENT Descending. */

SELECT * FROM MEETCO ORDER BY  FIRST_NAME ASC , DEPARTMENT DESC ;

/*2.Write an SQL query to print details for Workers with the first names “Vipul” and “Satish”
from the Worker table. */

SELECT * FROM MEETCO WHERE FIRST_NAME = 'VIPUL' OR  FIRST_NAME = 'SATISH' ;

/*3. Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and
contains six alphabets. */

SELECT * FROM MEETCO WHERE FIRST_NAME LIKE "_%_%_%_%_%_%H" ;

/*4. Write an SQL query to print details of the Workers whose SALARY lies between 1. */

SELECT * FROM MEETCO WHERE SALARY BETWEEN 0 AND 100000 ;

/*5. Write an SQL query to fetch duplicate records having matching data in some fields of a table. */

/*6. Write an SQL query to show the top 6 records of a table. */

SELECT * FROM MEETCO LIMIT  6 ;

/*7. Write an SQL query to fetch the departments that have less than five people in them. */

SELECT COUNT(WORKER_ID), DEPARTMENT FROM MEETCO  GROUP BY DEPARTMENT having  COUNT(WORKER_ID) < 5 ;

/*8. Write an SQL query to show all departments along with the number of people in there. */

SELECT COUNT(WORKER_ID), DEPARTMENT FROM MEETCO  GROUP BY DEPARTMENT having  COUNT(WORKER_ID) ;

/*9. Write an SQL query to print the name of employees having the highest salary in each
department. */

SELECT MAX(SALARY) FROM MEETCO ; 


CREATE TABLE GUJRATCOLLAGE 
(
 STDID INT primary KEY auto_increment ,
 STD_NAME VARCHAR(25),
 SEX VARCHAR (10) ,
 PERCENTAGE INT ,
 CLASS INT ,
 SEC VARCHAR (5) ,
 STREAMS varchar (20) ,
 DOB VARCHAR (30) 
 
) ;

/* 1>  To display all the records form STUDENT table.*/ 
SELECT * FROM GUJRATCOLLAGE   ;

/* 2. To display any name and date of birth from the table STUDENT. */

SELECT STD_NAME , DOB FROM GUJRATCOLLAGE ;

/*3. To display all students record where percentage is greater of equal to 80 FROM student table.*/ 

SELECT * FROM  GUJRATCOLLAGE WHERE PERCENTAGE >=80 ;

/*4. To display student name, stream and percentage where percentage of student is more than 80*/

 SELECT  STD_NAME,STREAMS,PERCENTAGE FROM GUJRATCOLLAGE WHERE PERCENTAGE >80 ;
 
 /*5. To display all records of science students whose percentage is more than 75 form student table*/
 
 SELECT * FROM GUJRATCOLLAGE WHERE STREAMS= "SCIENCE" AND PERCENTAGE>70 ;