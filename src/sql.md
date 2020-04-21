### SQL Statements 

- 1.Create a table T_Salesman 
a.SalesMan_Id - Primary key
b.Name
c.City
d.Commission

- 2.Create a table T_Customer
a.Customer_Id - Primary Key
b.Cust_Name
c.City
d.Grade
e.SalesMan_Id 

- 3.Create a table T_Orders
a.Ord_num - Primary Key
b.Purchase_Amt
c.Ord_Date
d.Customer_Id - Foreign Key (T_Customer)
e.SalesMan_Id - Foreign Key (T_Salesman)

```
CREATE TABLE T_Salesman (SalesMan_ID numeric(5) primary key,
Name varchar(30),
City varchar(15),
Commission decimal(5,2));

CREATE TABLE T_Customer (Customer_ID numeric(5) primary key,
Cust_Name varchar(30),
City varchar(15),
Grade numeric(3),
SalesMan_ID numeric(5));

create table T_Orders(Ord_No numeric(5) primary key,
Purchase_Amt decimal(8,2),
Ord_Date date,
Customer_ID numeric(5) 
references T_Customer(Customer_ID),
SalesMan_ID numeric(5) references T_SalesMan(SalesMan_ID));

```
- Inserting data into each table 

```
insert into  T_Customer values(3002,'Nick Rimando','New York',100,5001);

insert into T_Salesman values(5001,'James Hoog','New York',0.15);

insert into T_Orders values(70001,       150.5      ,      '2012-10-05 ',   3005    ,          5002);

```

### Retriving Data from Tables

- 1.Write a sql statement to display all the information of all salesmen. 
- 2.Write a sql statement to display a string "This is SQL Exercise, Practice and Solution".
- 3.Write a query to display three numbers (5,10,15) in three columns.
- 4.Write a query to display the sum of two numbers 10 and 15.
- 5.Write a query to display the result of an arithmetic expression. 10+15-5*2
- 6.Write a sql statement to display specific columns like name and commission for all the salesmen.
- 7.Write a query to display the columns in a specific order like order date, salesman id, order number and purchase amount from for all the orders.
- 8.Write a query which will retrieve the value of salesman id of all salesmen, getting orders from the customers in orders table without any repeats.
- 9.Write a sql statement to display names and city of salesman, who belongs to the city of Paris.
- 10.Write a sql statement to display all the information for those customers with a grade of 200.
- 11.Write a sql query to display the order number followed by order date and the purchase amount for each order which will be delivered by the salesman who is holding the ID 5001.

```
select * from T_Salesman;
SELECT 'This is SQL Exercise, Practice and Solution';
select 5,10,15;
select 10+15;
select 10+15-5*2;

select Name ,Commission from T_Salesman;

select Ord_Date, SalesMan_ID,Ord_Date,Purchase_Amt from T_Orders;

select Distinct	SalesMan_ID from T_Orders; 	

select Name ,City from T_Salesman where City='Paris';

select * from T_Customer where Grade=200;

select Ord_No,Purchase_Amt,Ord_Date from T_Orders where SalesMan_ID=5001;

```

### Using Boolean and Relational operators

- 1.Write a query to display all customers with a grade above 100.
- 2.Write a query statement to display all customers in New York who have a grade value above 100.
- 3.Write a SQL statement to display all customers, who are either belongs to the city New York or had a grade above 100.
- 4.Write a SQL statement to display all the customers, who are either belongs to the city New York or not had a grade above 100.
- 5.Write a SQL query to display those customers who are neither belongs to the city New York nor grade value is more than 100.
- 6.Write a SQL statement to display either those orders which is not issued on date 2012-09-10 and issued by the salesman whose ID is 505 and below or those orders which purchase amount is 1000.00 and below.
- 7.Write a SQL statement to display salesman_id, name, city and commission who gets the commission within the range more than 0.10% and less than 0.12%.
- 8.Write a SQL statement to display all information where purchase amount less than a specified amount or order date is less than a specified date and customer id greater than or equal to a specified number, then display the output in descending order of order date.
- 9.Write a SQL query to display all orders where purchase amount less than a specified amount or orders in a specified date and customer ID less than a specified number, then display the output in descending order of order date
- 10.Display all in descending order of order date where order dates equal to a specified date or customer id greater than a specified number and purchase amount less than a specified amount.

```
select * from T_Customer where Grade>100;
select * from T_Customer where Grade>100 AND City='New York' ;
select * from T_Customer where  NOT  Grade>100  or City='New York'   ;
select * from T_Customer where  NOT  Grade>100  or  not City='New York'   ;
select * from T_Customer where  NOT  Grade>100  or  not City='New York'   ;
select * from T_Orders Where (Not Ord_Date='2012-09-10' and SalesMan_ID=505) or Purchase_Amt<=1000.0; 
select * from T_Salesman where Commission>0.10 and Commission<0.12;
select * from  T_Orders where (Purchase_Amt<300.0 or Ord_Date>='2012-09-10') and Customer_ID<3009  order by Ord_Date desc;
select * from T_Orders where ((Purchase_Amt<300	or Ord_Date>='2012-09-10') and Customer_ID<3009 )order by Ord_Date desc ;
select * from T_Orders where Ord_Date>='2012-09-10' or Customer_ID>3009 order by Ord_Date desc;
```

### Wild Card and Special Operators

- 1.Write a SQL statement to find those salesmen with all information who come from the city either Paris or Rome.
- 2.Write a query to filter those salesmen with all information who comes from any of the cities Paris and Rome.
- 3.Write a query to filter those salesmen with all information who likes to leave other cities than Paris and Rome. 
- 4.Write a query to sort out those customers with all information whose ID value is within any of 3007, 3008 and 3009. 
- 5.Write a SQL statement to find those salesmen with all information who gets the commission within a range of 0.12 and 0.14.
- 6.Write a query to filter all those orders with all information which purchase amount value is within the range 500 and 4000 except those orders of purchase amount value 948.50 and 1983.43.  
- 7.Write a SQL statement to find those salesmen with all other information and name started with any letter 'A' and 'L'. 
- 8.Write a SQL statement to find those salesmen with all other information and name started with other than any letter within 'A' and 'L'. 
- 9.Write a SQL statement to find those customer with all information whose name begin with the letter 'B'.
- 10.Write a SQL statement to find all those customer with all information whose names are ending with the letter 'n'. 
11.Write a SQL statement to find those salesmen with all information whose name contain only four characters, in which 1st character must be 'N' and 4th character is l and rests may be any character.

```
select * from T_Salesman where City='Rome' or CITY='Paris';
select * from  T_Salesman where City in('Rome','Paris');
select * from  T_Salesman where City not in('Rome','Paris');
select * from T_Customer where Customer_ID in  (3007,3008,3009);
select * from  T_Salesman where Commission between 0.12 and 0.14;
select * from T_Orders where  (Purchase_Amt between 500 and  4000) and (Purchase_Amt not in (948.50,1983.43)) ;
select * from T_Salesman where  Name between 'A' and 'L';  
select * from T_Salesman where  Name not  between 'A' and 'L';
select * from T_Customer where Cust_Name like 'B%';
select * from T_Customer where Cust_Name like'%n'; 
select * from  T_Salesman where  Name like 'N__l%'

```
### Special Characters

Sample Data - ‘Test Table’
col1
--------------------------
```A001/DJ-402\44_/100/2015
A001_\DJ-402\44_/100/2015
A001_DJ-402-2014-2015
A002_DJ-401-2014-2015
A001/DJ_401
A001/DJ_402\44
A001/DJ_402\44\2015
A001/DJ-402%45\2015/200
A001/DJ_402\45\2015%100
A001/DJ_402%45\2015/300
A001/DJ-402\44
```
- 12.Write a SQL statement to find those rows from the table test table which contain the escape character underscore ( _ ) in its column 'col1'.
- 13.Write a SQL statement to find those rows from the table test table which does not contain the character underscore ( _ ) in its column 'col1'. 
- 14.Write a SQL statement to find those rows from the table test table which contain the escape character ( / ) in its column 'col1'.
- 15.Write a SQL statement to find those rows from the table test table which does not contain the escape character ( / ) in its column 'col1'.
- 16.Write a SQL statement to find those rows from the table test table which contain the string ( _/ ) in its column 'col1'.
- 17.Write a SQL statement to find those rows from the table test table which does not contain the string ( _/ ) in its column 'col1'.
- 18.Write a SQL statement to find those rows from the table test table which contain the character ( % ) in its column 'col1'. 
- 19.Write a SQL statement to find those rows from the table test table which does not contain the character ( % ) in its column 'col1'.
- 20.Write a SQL statement to find those customer with all information who does not get any grade except NULL.
21.Write a SQL statement to find those customer with all information who gets a grade except NULL value.

```
select	* from  TestTable where col1 like '%/_%' escape '/' ;
select	* from  TestTable where col1 not  like '%/_%' escape '/' ;
select	* from  TestTable where col1 like '%//%' escape '/' ;
select	* from  TestTable where col1  not like '%//%' escape '/' ;
select	* from  TestTable where col1   like '%/_//%' escape '/' ;
select	* from  TestTable where col1  not  like '%/_//%' escape '/' ;
select * from  TestTable where col1 like '%/%%'  escape '/';
select * from  TestTable where col1 not like '%/%%'  escape '/';
select * from T_Customer where Grade is  null;
select * from T_Customer where Grade is not null;
```
### Aggregate Functions  

- 1.Write a SQL statement to find the total purchase amount of all orders.
- 2.Write a SQL statement to find the average purchase amount of an order
- 3.Write a SQL statement to find the number of salesmen currently listing for all of their customers. 
- 4.Write a SQL statement know how many customer have listed their names with other information. 
- 5.Write a SQL statement find the number of customers who gets at least a gradation for his/her performance. 
- 6.Write a SQL statement to get the maximum purchase amount of all the orders. 
- 7.Write a SQL statement to get the minimum purchase amount of all the orders.
- 8.Write a SQL statement which selects the highest grade for each of the cities of the customers. 
- 9.Write a SQL statement to find the highest purchase amount ordered by the each customer with their ID and highest purchase amount.
- 10.Write a SQL statement to find the highest purchase amount ordered by the each customer on a particular date with their ID, order date and highest purchase amount.
- 11.Write a SQL statement to find the highest purchase amount in a date '2012-08-17' for each salesman with their ID.
- 12.Write a SQL statement to find the highest purchase amount with their ID and order date, for only those customers who have highest purchase amount in a day is more than 2000. 
- 13.Write a SQL statement to find the highest purchase amount with their ID and order date, for those customers who have a higher purchase amount in a day is within the range 2000 and 6000.
- 14.Write a SQL statement to find the highest purchase amount with their ID and order date, for only those customers who have a higher purchase amount in a day is within the list 2000, 3000, 5760 and 6000.
- 15.Write a SQL statement to find the highest purchase amount with their ID, for only those customers whose ID is within the range 3002 and 3007. 
- 16.Write a SQL statement to display customer details (ID and purchase amount) whose IDs are within the range 3002 and 3007 and highest purchase amount is more than 1000. 
- 17.Write a SQL statement to find the highest purchase amount with their ID, for only those salesmen whose ID is within the range 5003 and 5008.
- 18.Write a SQL statement that counts all orders for a date August 17th, 2012.
- 19.Write a SQL statement that counts the number of different non NULL city values for salesmen. 
- 20.Write a query that counts the number of salesmen with their order date and ID registering orders for each day.

```
select sum(Purchase_Amt) from T_Orders;

select avg(Purchase_Amt) from T_Orders ;

select count(distinct SalesMan_ID )  from T_Orders;

select count(distinct Customer_ID )from	 T_Customer;

select count(ALL Grade) from T_Customer;

select MAX(Purchase_Amt)from T_Orders;

select MIN(Purchase_Amt)from T_Orders;

Select City , Max(Grade) from T_Customer group by City;

select Max(Purchase_Amt) ,Customer_ID from T_Orders group by Customer_ID;

select Customer_ID,Ord_Date ,max(Purchase_Amt) from T_Orders group by Ord_Date,Customer_ID;

select SalesMan_ID,Max(Purchase_Amt) from T_Orders where Ord_Date='2012-08-17'  group  by SalesMan_ID;

select Customer_ID,Ord_Date, max(Purchase_Amt) from T_Orders group by Customer_ID, Ord_Date having max(Purchase_Amt)>2000;

select Customer_ID,Ord_date,max(Purchase_Amt) from T_Orders group by Customer_ID, Ord_Date having MAX(Purchase_Amt) between 2000 and 6000;

--select Customer_ID,Ord_Date,max(Purchase_Amt) from T_Orders GROUP BY Customer_ID,Ord_Date having MAX(Purchase_Amt) like  '2___.%'

select Customer_ID,Ord_Date,max(Purchase_Amt) from T_Orders GROUP BY Customer_ID,Ord_Date having MAX(Purchase_Amt) in (2000,3000,5760,6000)

select Customer_ID,MAX(Purchase_Amt)  from T_Orders	group by Customer_ID having Customer_ID between 3002 and 3007

select Customer_ID,  max(Purchase_Amt) from  T_Orders where Customer_ID between 3002 and  3007 group by  Customer_ID having   MAX(Purchase_Amt)>1000

select SalesMan_ID, MAX(Purchase_Amt) from  T_Orders   group by  SalesMan_ID having   SalesMan_ID between  5003 and  5008

select count(*) from T_Orders where  Ord_Date='2012-08-17'

select SalesMan_ID, Ord_Date,COUNT(*) from  T_Orders group by  Ord_Date, SalesMan_ID
```

### Formatting Output 
- 1.Write a SQL statement to find out the number of orders booked for each day and display it in such a format like "For 2001-10-10 there are 15 orders".
- 2.Write a query to display the orders according to the order number arranged by ascending order. 
- 3.Write a SQL statement to arrange the orders according to the order date in such a manner that the latest date will come first then previous dates.
- 4.Write a SQL statement to display the orders with all information in such a manner that the latest order date with highest purchase amount will come first.
- 5.Write a SQL statement to display the customer name, city and grade etc. and smallest customer ID will comes first.
- 6.Write a SQL statement to make a report with salesman ID, order date in such an arrangement that, the smallest salesman ID will come first along with their smallest order date and highest purchase amount. 
- 7.Write a SQL statement to display customer name, city and grade in such a manner that, the customer holding highest grade will comes first.
- 8.Write a SQL statement make a report with customer ID in such a manner that, the largest number of orders booked by the customer will comes first along with their highest purchase amount.
- 9.Write a SQL statement to make a report with order date in such a manner that, the latest order date will comes first along with the total purchase amount and total commission (15% for all salesmen) for that date.

```

select 'FOR' ,Ord_Date,'there are' ,COUNT(distinct Ord_No), 'Orders' from  T_Orders group  by  Ord_Date

select * from T_orders	order by Ord_No asc

select * from  T_Orders order by  Ord_Date desc

select * from T_Orders order by  Ord_Date,Purchase_Amt desc

select Cust_Name, City, Grade from T_Customer order by Customer_ID asc

select SalesMan_ID, Ord_Date , max(Purchase_Amt) from T_Orders group by SalesMan_ID, Ord_Date order by SalesMan_ID , Ord_Date

select Cust_Name, City, Grade from  T_Customer order by  Grade desc

select Customer_ID,count(distinct Ord_No),MAX(Purchase_Amt) from  T_Orders group by  Customer_ID  order by MAX(Purchase_Amt) DESC 

select Ord_Date	,sum(Purchase_Amt),sum(Purchase_Amt)*.15 from T_Orders group by Ord_Date  order by Ord_Date

```

### Queries on Multiple Table

- 1.Write a query to find those customers with their name and those salesmen with their name and city who lives in the same city. 
- 2.Write a SQL statement to find the names of all customers along with the salesmen who works for them.
- 3.Write a SQL statement to display all those orders by the customers not located in the same cities where their salesmen lives.
- 4.Write a SQL statement that find out each order number followed by the name of the customers who made the order. 
- 5.Write a SQL statement that short out the customer and their grade who made an order. Each of the customer must have a grade and served by at least a salesman, who belongs to a city.
- 6.Write a query that produces all customers with their name, city, salesman and commission, who served by a salesman and the salesman works at a rate of commission within 12% to 14%.
- 7.Write a SQL statement that produces all orders with order number, customer name, commission rate and earned commission amount for those customers who carry their grade more than 200 and served by an existing salesman.

```

select T_Customer.Cust_Name , T_Salesman.Name ,T_Customer.City from T_Customer, T_Salesman where T_Customer.City=T_Salesman.City
select	T_Customer.Cust_Name, T_Salesman.Name from T_Salesman,T_Customer where T_Customer.SalesMan_ID=T_Salesman.SalesMan_ID 
select Ord_No,T_Orders.Customer_ID,T_Orders.SalesMan_ID  from  T_Salesman , T_Customer,T_Orders where	T_Customer.City!=T_Salesman.City AND T_Orders.Customer_ID=T_Customer.Customer_ID AND T_Orders.SalesMan_ID= T_Salesman.SalesMan_ID; 
select Ord_No, T_Customer.Cust_Name from T_Orders , T_Customer where T_Orders.Customer_ID=T_Customer.Customer_ID
select T_Customer.Cust_Name, T_Customer.Grade from  T_Orders, T_Customer, T_Salesman where T_Orders.Customer_ID=T_Customer.Customer_ID and T_Orders.SalesMan_ID=T_Salesman.SalesMan_ID and T_Customer.Grade is not null and  T_Salesman.city is not null
select T_Customer.Customer_ID, T_Customer.Cust_Name ,T_Customer.City ,T_Salesman.SalesMan_ID, T_Salesman.Commission from T_Salesman , T_Customer where  T_Customer.SalesMan_ID=T_Salesman.SalesMan_ID and T_Salesman.Commission between 0.12 and 0.14
select T_Orders.Ord_No ,Cust_Name, T_Orders.Purchase_Amt*T_Salesman.Commission from T_Customer , T_Salesman, T_Orders where T_Orders.Customer_ID=T_Customer.Customer_ID and T_Orders.SalesMan_ID=T_Salesman.SalesMan_ID and  T_Customer.Grade>200 
```

### Joins  

- 1.Write a SQL statement to prepare a list with salesman name, customer name and their cities for the salesmen and customer who belongs to same city.
- 2.Write a SQL statement to make a list with order no, purchase amount, customer name and their cities for those orders which order amount between 500 and 2000.
- 3.Write a SQL statement to know which salesman are working for which customer.  
- 4.Write a SQL statement to find the list of customers who appointed a salesman for their jobs who gets a commission from the company is more than 12%.
- 5.Write a SQL statement to find the list of customers who appointed a salesman for their jobs who does not live in same city where there customer lives, and gets a commission is above 12% .
- 6.Write a SQL statement to find the details of a order i.e. order number, order date, amount of order, which customer gives the order and which salesman works for that customer and how much commission he gets for an order.
- 7.Write a SQL statement to make a join within the tables salesman, customer and orders in such a form that the same column of each table will appear once and only the relational rows will come. 
- 8.Write a SQL statement to make a list in ascending order for the customer who works either through a salesman or by own.
- 9.Write a SQL statement to make a list in ascending order for the customer who holds a grade less than 300 and works either through a salesman or by own. 
- 10.Write a SQL statement to make a report with customer name, city, order number, order date and order amount in ascending order according to the order date to find that either any of the existing customer have placed no order or placed one or more orders.
- 11.Write a SQL statement to make a report with customer name, city, order number, order date, order amount salesman name and commission to find that either any of the existing customer have placed no order or placed one or more orders by their salesman or by own.
- 12.Write a SQL statement to make a list in ascending order for the salesmen who works either for one or more customer or not yet join under any of the customer.  
- 13.Write a SQL statement to make a list for the salesmen who works either for one or more customer or not yet join under any of the customer who placed either one or more orders or no order to their supplier. 
- 14.Write a SQL statement to make a list for the salesmen who either work for one or more customer or yet to join any of the customer. The customer, may have placed, either one or more orders on or above order amount 2000 and must have a grade, or he may not have placed any order to the associated supplier.
- 15.Write a SQL statement to make a report with customer name, city, order no. order date, purchase amount for those customers from the existing list who placed one or more orders or which order(s) have been placed by the customer who are not in the list. 
- 16. Write a SQL statement to make a report with customer name, city, order no. order date, purchase amount for only those customers in the list who must have a grade and placed one or more orders or which order(s) have been placed by the customer who are neither in the list not have a grade.
- 17.Write a SQL statement to make a cartesian product between salesman and customer i.e. each salesman will appear for all customer and vice versa. 
- 18.Write a SQL statement to make a cartesian product between salesman and customer i.e. each salesman will appear for all customer and vice versa for those customer who belongs to a city. 
- 19. Write a SQL statement to make a cartesian product between salesman and customer i.e. each salesman will appear for all customer and vice versa for those salesmen who belongs to a city and the customers who must have a grade.
- 20.Write a SQL statement to make a cartesian product between salesman and customer i.e. each salesman will appear for all customer and vice versa for those salesmen who must belongs a city which is not the same as his customer and the customers should have a own grade.

```
select T_Salesman.Name, T_Customer.Cust_Name,T_Salesman.City from  T_Customer,T_Salesman where  T_Customer.City=T_Salesman.City

select T_Orders.Ord_No , T_Orders.Purchase_Amt, T_Customer.Cust_Name ,T_Customer.City from  T_Orders , T_Customer where T_Customer.Customer_ID=T_Orders.Customer_ID and T_Orders.Purchase_Amt between 500 and  2000 

--select  T_Salesman.Name, T_Customer.Cust_Name from  T_Salesman , T_Customer where T_Customer.SalesMan_ID=T_Salesman.SalesMan_ID 

select  b.Name, a.Cust_Name from  T_Customer a inner join T_Salesman b on a.SalesMan_ID=b.SalesMan_ID

select  a.Cust_Name, b.Name,b.Commission from T_Customer a inner join T_Salesman b on a.SalesMan_ID=b.SalesMan_ID where b.Commission>.12

select  a.Cust_Name, b.Name,b.Commission from T_Customer a inner join T_Salesman b on a.SalesMan_ID=b.SalesMan_ID where b.Commission>.12 and a.City<>b.City

select a.Ord_No ,a.Ord_Date, a.Purchase_Amt,b.Cust_Name,c.Name,c.Commission from  T_Orders a inner join T_Customer b on a.Customer_ID=b.Customer_ID inner join T_Salesman c on a.SalesMan_ID=c.SalesMan_ID 

--  doubt in  7  
select  * from T_Customer a  left join T_Salesman b on a.SalesMan_ID=b.SalesMan_ID order by Customer_ID asc

select  * from T_Customer a  left join T_Salesman b on a.SalesMan_ID=b.SalesMan_ID where  a.Grade<300  order by Customer_ID asc

select a.Cust_Name ,a.City,b.Ord_No,b.Ord_Date,b.Purchase_Amt from T_Customer a left join T_Orders b on a.Customer_ID=b.Customer_ID order by  b.Ord_Date asc

select a.Cust_Name ,a.City,b.Ord_No,b.Ord_Date,b.Purchase_Amt , c.Commission   from T_Customer a left join T_Orders b on a.Customer_ID=b.Customer_ID left  join T_Salesman c on b.SalesMan_ID=c.SalesMan_ID order by  b.Ord_Date asc

select  * from T_Customer a left join T_Salesman b  on a.SalesMan_ID=b.SalesMan_ID order by  Customer_ID asc

--select * from  T_Salesman a left join  T_Customer b on a.SalesMan_ID=b.SalesMan_ID left join  T_Orders c on b.Customer_ID=c.Customer_ID 

select * from  T_Salesman a right join  T_Customer b on a.SalesMan_ID=b.SalesMan_ID right join  T_Orders c on b.Customer_ID=c.Customer_ID

select a.SalesMan_ID	 from  T_Salesman a right join  T_Customer b on a.SalesMan_ID=b.SalesMan_ID right join  T_Orders c on b.Customer_ID=c.Customer_ID where c.Purchase_Amt>2000 and b.Grade is not null

select b.Cust_Name,b.City,c.Ord_No,Ord_Date, c.Purchase_Amt	 from  T_Salesman a right join  T_Customer b on a.SalesMan_ID=b.SalesMan_ID right join  T_Orders c on b.Customer_ID=c.Customer_ID 

select b.Cust_Name,b.City,c.Ord_No,Ord_Date, c.Purchase_Amt	 from  T_Salesman a right join  T_Customer b on a.SalesMan_ID=b.SalesMan_ID right join  T_Orders c on b.Customer_ID=c.Customer_ID where b.Grade is not null

select * from  T_Customer a cross join T_Salesman

select * from T_Salesman a cross join T_Customer b where a.City is not null 

select * from T_Salesman a cross join T_Customer b where a.City is not null and b.Grade is not null and a.City<>b.City

```

### Subqueries

- 1.Write a query to display all the orders from the orders table issued by the salesman 'Paul Adam'. 
- 2.Write a query to display all the orders for the salesman who belongs to the city New York.
- 3.Write a query to find all the orders issued against the salesman who works for customer whose id is 3007.
- 4.Write a query to display all the orders which values are greater than the average order value for 10th October 2012. 
- 5.Write a query to find all orders attributed to salesman in New york.
- 6.Write a query to display the commission of all the salesmen servicing customers in Paris.
- 7.Write a query to display all the customers whose id is 2001 bellow the salesman ID of Mc Lyon. 
- 8.Write a query to counts the customers with grades above New York's average. 
- 9.Write a query to display all customers with orders on October 5, 2012.
- 10.Write a query to display all the customers with orders issued on date 17th August, 2012.
- 11.Write a query to find the name and numbers of all salesmen who had more than one customer
- 12.Write a queries to find all orders with order amounts which is above-average amounts for their customers.
- 13.Write a queries to find all orders with order amounts which is on or above-average amounts for their customers. 
- 14.Write a query to find the sums of the amounts from the orders table, grouped by date, eliminating all those dates where the sum was not at least 1000.00 above the maximum amount. 
- 15.Write a query to extract the data from the customer table if and only if one or more of the customers in the customer table are located in London.
- 16.Write a query to display the name of salesmen who have multiple customers. 
- 17.Write a query to find the all salesmen name with only one customer. 
- 18.Write a query that are extracts the rows of all salesmen who have customers with more than one current order.
- 19.Write a query to find salesman with customers located in their cities.
- 20.Write a query to find all the salesmen for whom there are customers that follow them.
- 21.Write a query to display the salesmen which name are alphabetically lower than the name of the customers.
- 22.Write a query to display the customers who have a greater gradation than any customer who belongs to the alphabetically lower than the city New York.
- 23.Write a query to display all the orders that had amounts that were greater than at least one of the orders from October 9th 2012.
- 24.Write a query to find all orders with amount smaller than any amount for a customer in London.
- 25.Write a query to display all orders with amount smaller than any amount for a customer in London.
- 26.Write a query to display only those customers whose grade are, in fact, higher than every customer in New York.
- 27.Write a query to find only those customers whose grade are, higher than every customer to the city New York.
- 28.Write a query to find all grade for those customers who belongs to the city Rome. 
- 29.Write a query to find all those customers whose grade are not as the grade, belongs to the city Paris.
- 30.Write a query to find all those customers who holds a different grade than any customer of the city Dallas.

```
select * from T_Orders where SalesMan_ID=(select SalesMan_ID from T_Salesman where Name='Paul Adam');

select * from T_Orders where SalesMan_ID=(select SalesMan_ID from T_Salesman  where City='New York')

select * from T_Orders where SalesMan_ID=(select SalesMan_ID from T_Orders where Customer_ID=3007)

select  * from T_Orders where Purchase_Amt>(select AVG(Purchase_Amt) from T_Orders where Ord_Date='2012-10-10')

select * from T_Orders where SalesMan_ID=(select SalesMan_ID from T_Salesman where  City='New York')

select * from T_Salesman where SalesMan_ID=(select SalesMan_ID from T_Customer where City='Paris')

select  * from T_Customer where Customer_ID=(select SalesMan_ID-2001  from T_Salesman where Name='Mc Lyon') 

select COUNT(*) from T_Customer where Grade>(select AVG(Grade) from T_Customer where City='New York')

select * FROM T_CUSTOMER where Customer_Id IN(select Customer_Id FROM T_ORDERS where Ord_Date='10/05/2012');

select * from T_CUSTOMER where Customer_Id IN(select Customer_Id FROM T_ORDERS where Ord_Date='08/17/2012');

select Salesman_Id, Name FROM T_SALESMAN where Salesman_Id IN(select Salesman_Id FROM T_ORDERS GROUP BY Salesman_Id HAVING COUNT(DISTINCT(Customer_id))>1);

select * FROM T_ORDERS Torm where Purchase_Amt >(select AVG(Purchase_Amt) FROM T_ORDERS Tori  where Torm.Customer_id=Tori.Customer_id );

select * FROM T_ORDERS Torm where Purchase_Amt >=(select AVG(Purchase_Amt) FROM T_ORDERS Tori  where Torm.Customer_id=Tori.Customer_id );

select SUM(Purchase_Amt)AS 'Total Purchase ' ,Ord_Date FROM T_ORDERS Torm  GROUP BY Ord_Date HAVING SUM(Purchase_Amt) >(select MAX(Purchase_Amt)+1000 FROM T_ORDERS Tori where Tori.Ord_Date=Torm.Ord_Date);

select * FROM T_CUSTOMER where EXISTS (select Customer_Id FROM T_CUSTOMER where City='London'); 

select Salesman_Id, Name FROM T_SALESMAN where Salesman_Id IN(select Salesman_Id FROM T_ORDERS GROUP BY Salesman_Id HAVING COUNT(DISTINCT(Customer_id))>1);

select Salesman_Id, Name FROM T_SALESMAN where Salesman_Id IN(select Salesman_Id FROM T_ORDERS GROUP BY Salesman_Id HAVING COUNT(DISTINCT(Customer_id))=1);

select Salesman_Id, Name FROM T_SALESMAN where Salesman_Id IN(select Ord_No FROM T_ORDERS GROUP BY Customer_id,Salesman_Id HAVING COUNT(Ord_No)>1);--/ Pending

select * FROM T_SALESMAN where CITY IN(select DISTINCT(CITY) FROM T_CUSTOMER) 

select * FROM T_SALESMAN where CITY IN(select DISTINCT(CITY) FROM T_CUSTOMER) ;

select * FROM T_SALESMAN Ts where EXISTS(select Customer_Id FROM T_CUSTOMER where Cust_name>Ts.Name); 

select * FROM T_CUSTOMER Tc where Grade >ANY (select Grade FROM T_CUSTOMER where  City <'New York' );

select * FROM T_ORDERS where Purchase_Amt > ANY(select Purchase_Amt FROM T_ORDERS where Ord_Date='10/09/2012');

select * FROM T_ORDERS where Purchase_Amt < ANY(select Purchase_amt FROM T_ORDERS where Customer_id IN(select Customer_id FROM T_CUSTOMER where City='lONDON'));

select * FROM T_ORDERS where Purchase_Amt < ANY(select Purchase_amt FROM T_ORDERS where Customer_id IN(select Customer_id FROM T_CUSTOMER where City='lONDON'));

select * FROM T_CUSTOMER where Grade > ALL(select Grade FROM T_CUSTOMER where City='New York' );

select * FROM T_CUSTOMER where Grade > ALL(select Grade FROM T_CUSTOMER where City='New York' );

select * FROM T_CUSTOMER where City='Rome';

select * FROM T_CUSTOMER where GRADE NOT IN(select Grade 
FROM T_CUSTOMER where CITY='Paris');

select * FROM T_CUSTOMER where GRADE NOT IN(select Grade FROM T_CUSTOMER where CITY='Dallas');

```

### Union 

- 1.Write a query to display all salesmen and customer located in California.
- 2.Write a query to display distinct salesman and their cities.
- 3.Write a query to display all the salesmen and customer.
- 4.Write a query to make a report of which salesman produce the largest and smallest orders on each date.
- 5.Write a query to make a report of which salesman produce the largest and smallest orders on each date and arranged the orders number in smallest to largest number.
- 6.Write a query to list all the salesmen, and indicate those who do not have customers in their cities, as well as those who do.
- 7.Write a query to that appends strings to the selected fields, indicating whether or not a specified salesman was matched to a customer in his city.
- 8.Create a union of two queries that shows the names, cities, and ratings of all customers. Those with a rating of 200 or greater will also have the words "High Rating", while the others will have the words "Low Rating".
- 9.Write a command that produces the name and number of each salesman and each customer with more than one current order. Put the results in alphabetical order.

```
--1
select Cust_name,City from T_CUSTOMER where City='California'
UNION 
select Name,City from T_SALESMAN where City='California';
--2
select  Distinct Cust_Name from  T_Customer
UNION
select Distinct Name from  T_Salesman
--3
select  Cust_Name from  T_Customer
UNION
select  Name from  T_Salesman
--4
select 'Highest',Ts.Salesman_id,Ts.Name,Purchase_Amt,Ord_No,Ord_Date from T_ORDERS Tor,T_SALESMAN Ts where Tor.Salesman_id=Ts.Salesman_Id AND Purchase_Amt = (select MAX(Purchase_Amt) from T_orders Tori where Tori.Ord_Date=Tor.Ord_Date) 
UNION
select 'Lowest',Ts.Salesman_id,Ts.Name,Purchase_Amt,Ord_No,Ord_Date from T_ORDERS Tor,T_SALESMAN Ts where Tor.Salesman_id=Ts.Salesman_Id AND Purchase_Amt = (select MIN(Purchase_Amt) from T_orders Tori where Tori.Ord_Date=Tor.Ord_Date) 

--5
select 'Highest',Ts.Salesman_id,Ts.Name,Purchase_Amt,Ord_No,Ord_Date from T_ORDERS Tor,T_SALESMAN Ts where Tor.Salesman_id=Ts.Salesman_Id AND Purchase_Amt = (select MAX(Purchase_Amt) from T_orders Tori where Tori.Ord_Date=Tor.Ord_Date) 
UNION
select 'Lowest',Ts.Salesman_id,Ts.Name,Purchase_Amt,Ord_No,Ord_Date from T_ORDERS Tor,T_SALESMAN Ts where Tor.Salesman_id=Ts.Salesman_Id AND Purchase_Amt = (select MIN(Purchase_Amt) from T_orders Tori where Tori.Ord_Date=Tor.Ord_Date) 
order by Ord_No

--6
select * from T_SALESMAN where City NOT IN (select City from T_CUSTOMER )
UNION 
select * from T_SALESMAN where City IN(select CITY from T_CUSTOMER )

--7
select Ts.Salesman_Id,Name,Ts.City, 'Match' from T_SALESMAN Ts,T_CUSTOMER Tc where Ts.City=Tc.City
UNION
select Salesman_id ,Ts.Name, Ts.City ,'No Match' from T_SALESMAN  Ts where Ts.City NOT IN(select City from T_CUSTOMER)

--8
select Cust_Name,City,Grade,'High Rating' from T_CUSTOMER where Grade >=200
UNION
select Cust_Name,City,Grade,'Low Rating' from T_CUSTOMER where Grade <200

--9
select Customer_Id,Cust_Name from T_CUSTOMER Tc where 1< (select COUNT(*) from T_ORDERS Tor where Tc.Customer_Id=Tor.Customer_id )
UNION
select Salesman_id,Name from T_SALESMAN Ts where 1< (select COUNT(*) from T_ORDERS Tor where Ts.Salesman_Id=Tor.Salesman_id )
ORDER BY Cust_name
```
### Views

- 1.Write a query to create a view for all salesmen with columns salesman_id, name and city. 
- 2.Write a query to create a view for all salesmen with columns salesman_id, name and city. 
- 3.Write a query to find the salesmen of the city New York who achieved the commission more than 13%. 
- 4.Write a query to create a view to get a count of how many customers we have at each level of grade.  
- 5.Write a query to create a view to keep track the number of customers ordering, number of salesmen attached, average amount of orders and total amount of orders in a day. 
- 6.Write a query to create a view that shows for each order the salesman and customer by name. 
- 7.Write a query to create a view that find the salesman who has the customer with the highest order on a day. 
- 8.Write a query to create a view that find the salesman who has the customer with the highest order at least 3 times on a day. 
- 9.Write a query to create a view that shows all of the customers who have the highest grade.
- 10.Write a query to create a view that shows the number of salesman in each city.
- 11.Write a query to create a view that shows the average and total orders for each salesman after his or her name. (Assume all names are unique)
- 12.Write a query to create a view that shows each salesman with more than one customers.
- 13.Write a query to create a view that shows all matches of customers with salesman such that at least one customer in the city of customer served by a salesman in the city of salesman.
- 14.Write a query to create a view that shows the number of orders in each day.
- 15.Write a query to create a view that find the salesmen who issued orders on October 10th, 2012.
- 16.Write a query to create a view that find the salesmen who issued orders on either August 17th, 2012 or October 10th, 2012.

```
--1
CREATE VIEW SALESMAN_INFO  AS select Salesman_id,Name,City from T_SALESMAN
--2
CREATE VIEW SALESMAN_INFO  AS select Salesman_id,Name,City from T_SALESMAN
--3
CREATE VIEW SALES_COM_NEW AS SELECT * FROM T_SALESMAN WHERE City='New York'AND Commission>.13;
--4
CREATE VIEW CUST_SAME_LEVEL AS (SELECT Grade,COUNT(* ) AS 'COunt ' FROM T_CUSTOMER GROUP BY Grade); 
--5
CREATE VIEW TRACKDATA AS SELECT Ord_Date,COUNT( DISTINCT Customer_id)'Customers',AVG(Purchase_Amt)'Avg Purchase',SUM(Purchase_Amt) 'Total Purchase'FROM T_ORDERS GROUP BY ord_date;
SELECT * FROM TRACKDATA;
--6
CREATE VIEW ORD_SAL_CUST AS (SELECT Ord_Num,Cust_Name,Name FROM T_ORDERS Tor,T_CUSTOMER Tc,T_SALESMAN Ts WHERE Tor.salesman_id=Ts.Salesman_Id AND Tor.Customer_id=Tc.Customer_Id );
SELECT * FROM ORD_SAL_CUST;
--7
CREATE VIEW HIGHEST_ORDER AS SELECT Ord_No,Ts.Salesman_Id,Ts.Name FROM T_ORDERS Tor,T_SALESMAN Ts WHERE  Tor.Salesman_id=Ts.Salesman_Id AND Tor.Purchase_Amt =(SELECT MAX(purchase_amt) FROM T_ORDERS Tori WHERE Tor.ord_date=tori.ord_date);
SELECT * FROM HIGHEST_ORDER;
--8
CREATE VIEW hIGHEST3 AS SELECT Salesman_id,Name FROM T_SALESMAN Ts WHERE 3<=(SELECT COUNT(*) FROM T_SALESMAN TsI WHERE TsI.Salesman_Id=Ts.Salesman_Id);
SELECT * FROM hIGHEST3
--9
CREATE VIEW HIGHEST_GRADE AS SELECT MAX(GRADE)AS 'GRADE' FROM T_CUSTOMER; 
SELECT * FROM HIGHEST_GRADE;
--10
CREATE VIEW CITYWISE_SALESMAN AS SELECT CITY,COUNT(CITY)AS 'COUNT' FROM T_SALESMAN GROUP BY City
SELECT * FROM CITYWISE_SALESMAN
--11
CREATE VIEW AVGORD_SALESMAN AS SELECT Ts.Name,AVG(Purchase_Amt)AS 'AVG ORDER',COUNT(Purchase_Amt)AS 'TOTAL ORDER' FROM T_ORDERS Tor,T_SALESMAN Ts WHERE Tor.salesman_id=TS.Salesman_Id GROUP BY Ts.Name
SELECT * FROM AVGORD_SALESMAN
--12
CREATE VIEW SALESCUST1GREAT AS SELECT *  FROM T_SALESMAN Ts WHERE 1 < (SELECT COUNT(*) FROM T_CUSTOMER Tc WHERE Tc.salesman_id=Ts.Salesman_Id);
SELECT * FROM SALESCUST1GREAT;
--13
CREATE VIEW citymatch(custcity, salescity) AS SELECT DISTINCT a.City, b.City FROM T_Customer a, T_Salesman b
WHERE a.SalesMan_ID = b.SalesMan_ID
--14
CREATE VIEW ORDEREACHDAY AS SELECT Ord_Date,COUNT(*)AS 'On DAte Order' FROM T_ORDERS GROUP BY Ord_Date;
SELECT * FROM ORDEREACHDAY;
--15
CREATE VIEW ORDERONDATE10TH AS SELECT * FROM T_Salesman WHERE Salesman_Id IN(SELECT Salesman_Id FROM T_ORDERS WHERE Ord_Date='10/10/2012')
SELECT * FROM ORDERONDATE10TH;
--16
CREATE VIEW ORDERONDATE12TH AS SELECT * FROM T_Salesman WHERE Salesman_Id IN(SELECT Salesman_Id FROM T_ORDERS WHERE Ord_Date='10/10/2012' OR Ord_Date='08/17/2012');
SELECT * FROM ORDERONDATE12TH;

```
 










