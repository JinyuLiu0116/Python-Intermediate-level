INSERT INTO EMPLOYEE VALUES('JOHN','B','SMITH','123456789','1965-01-09','731 FONDREN, HOUSTON, TX','M',30000,'333445555','5');
INSERT INTO EMPLOYEE VALUES('FRANKLIN','T','WONG','333445555','1955-12-08','638 VOSS, HOUSTON, TX','M',40000,'888665555','5');
INSERT INTO EMPLOYEE VALUES('ALICIA','J','ZELAYA','999887777','1968-07-19','3321 CASTLE, SPRING, TX','F',25000,'987654321','4');
INSERT INTO EMPLOYEE VALUES('JENNIFER','S','WALLACE','987654321','1941-06-20','291, BERRY, BELLAIRE, TX','F',43000,'888665555','4');
INSERT INTO EMPLOYEE VALUES('RAMESH','K','NARAYAH','666884444','1962-09-15','975 FIRE OAK, HUMBLE, TX','M',38000,'333445555','5');
INSERT INTO EMPLOYEE VALUES('JOYCE','A','ENGLISH','453453453','1972-07-31','5631, RICE, HOUSTON, TX','F',25000,'333445555','5');
INSERT INTO EMPLOYEE VALUES('AHMAD','V','JABBAR','987987987','1969-03-29','980, DALLAS, HOUSTON, TX','M',25000,'987654321','4');
INSERT INTO EMPLOYEE VALUES('JAMES','E','BORG','888665555','1937-11-10','450 STONE, HOUSTON, TX','M',55000,'','1');


INSERT INTO DEPARTMENT VALUES('RESEARCH','5','333445555','1988-05-22');
INSERT INTO DEPARTMENT VALUES('ADMINISTRATION','4','987654321','1995-01-01');
INSERT INTO DEPARTMENT VALUES('HEADQUARTERS','1','888665555','1981-06-19');



INSERT INTO DEPT_LOCATIONS VALUES('1','HOUSTON');
INSERT INTO DEPT_LOCATIONS VALUES('4','STAFFORD');
INSERT INTO DEPT_LOCATIONS VALUES('5','BELLAIRE');
INSERT INTO DEPT_LOCATIONS VALUES('5', 'SUGARFAND');
INSERT INTO DEPT_LOCATIONS VALUES('5', 'HOUSTON');



INSERT INTO PROJECT VALUES('PRODUCTX','1','BELLAIRE','5');
INSERT INTO PROJECT VALUES('PRODUCTY','2','SUGARFAND','5');
INSERT INTO PROJECT VALUES('PRODUCTZ','3','HOUSTON','5');
INSERT INTO PROJECT VALUES('COMPUTERIZATION','10','STAFFORD','4');
INSERT INTO PROJECT VALUES('REORGANIZATION','20','HOUSTON','1');
INSERT INTO PROJECT VALUES('NEWBENEFITS','30','STAFFORD','4');



INSERT INTO WORKS_ON VALUES('123456789','1',32.5);
INSERT INTO WORKS_ON VALUES('123456789','2',7.5);
INSERT INTO WORKS_ON VALUES('666884444','3',40.0);
INSERT INTO WORKS_ON VALUES('453453453','1',20.0);
INSERT INTO WORKS_ON VALUES('453453453','2',20.0);
INSERT INTO WORKS_ON VALUES('333445555','2',10.0);
INSERT INTO WORKS_ON VALUES('333445555','3',10.0);
INSERT INTO WORKS_ON VALUES('333445555','10',10.0);
INSERT INTO WORKS_ON VALUES('333445555','20',10.0);
INSERT INTO WORKS_ON VALUES('999887777','30',30.0);
INSERT INTO WORKS_ON VALUES('987987987','10',35.0);
INSERT INTO WORKS_ON VALUES('987987987','30',5.0);
INSERT INTO WORKS_ON VALUES('987654321','30',20.0);
INSERT INTO WORKS_ON VALUES('987654321','20',15.0);
INSERT INTO WORKS_ON VALUES('888665555','20',NULL);



INSERT INTO DEPENDENT VALUES('333445555','ALICE','F','1986-04-05','DAUGHTER');
INSERT INTO DEPENDENT VALUES('333445555','THEODORE','M','1983-10-25','SON');
INSERT INTO DEPENDENT VALUES('333445555','JOY','F','1958-05-03','SPOUSE');
INSERT INTO DEPENDENT VALUES('987654321','ABNER','M','1942-02-28','SPOUSE');
INSERT INTO DEPENDENT VALUES('123456789','MICHAEL','M','1988-01-04','SON');
INSERT INTO DEPENDENT VALUES('123456789','ALICE','F','1988-12-30','DAUGHTER');
INSERT INTO DEPENDENT VALUES('123456789','ELIZABETH','F','1967-05-05','SPOUSE');
