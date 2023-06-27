#!/usr/bin/env python
# coding: utf-8

# # Lab Session

# ## <font color='blue'> Table Of Contents </font>
# - Problem Statement 
# - Load required libraries
# - Connect to DB using mysql-connector-python package
# - Create database named `e_commerce`
# - Create tables and insert data into tables as specified in the question
# - Read all the questions and write sql queries to meet the objective 

# ## <font color='blue'> Problem Statement </font>
# ###  An E-commerce website manages its data in the form of various tables.
# You need to create a Database called `e_commerce` and various tables in it. The tables needed and attributes which need to be in every table are given before hand. All you have to do is create tables with data in it and answer some of the questions that follows.

# ### e_commerce Schema:

# ![e_commerce%20_schema.png](attachment:e_commerce%20_schema.png)

# ### Load Required Libraries

# In[1]:


import mysql.connector
import pandas as pd


# ### Connect to DB using Mysql-connector-python package

# In[2]:


connection = mysql.connector.connect(host = "localhost",
                                     user = "root",
                                     passwd ="prachi2525")

cursorObject = connection.cursor() 


# ### You are required to create a database named 'e_commerce'

# In[14]:


connection = mysql.connector.connect(host = "localhost",
                                     user = "root",
                                     passwd ="prachi2525")

cursorObject = connection.cursor() 
cursorObject.execute("CREATE DATABASE if not exists e_commerce")
connection.close()


# In[19]:


connection = mysql.connector.connect(host ="localhost",
                                     user ="root",
                                     passwd ="prachi2525",
                                     database = "e_commerce")

cursorObject = connection.cursor()


# ### Q1. Create tables for supplier, customer, category, product, productDetails, order, rating to store the data for the E-commerce with the schema definition given below.
# 
# 
# - **`supplier`**(SUPP_ID int primary key, SUPP_NAME varchar(50), SUPP_CITY varchar(50), SUPP_PHONE varchar(10))
# 
# 
# - **`customer`** (CUS_ID INT NOT NULL, CUS_NAME VARCHAR(20) NULL DEFAULT NULL, CUS_PHONE VARCHAR(10), CUS_CITY varchar(30) ,CUS_GENDER CHAR,PRIMARY KEY (CUS_ID))
# 
# 
# - **`category`** (CAT_ID INT NOT NULL, CAT_NAME VARCHAR(20) NULL DEFAULT NULL,PRIMARY KEY (CAT_ID))
# 
# 
# - **`product`** (PRO_ID INT NOT NULL, PRO_NAME VARCHAR(20) NULL DEFAULT NULL, PRO_DESC VARCHAR(60) NULL DEFAULT NULL, CAT_ID INT NOT NULL,PRIMARY KEY (PRO_ID),FOREIGN KEY (CAT_ID) REFERENCES CATEGORY (CAT_ID))
# 
# 
# - **`product_details`** (PROD_ID INT NOT NULL, PRO_ID INT NOT NULL, SUPP_ID INT NOT NULL, PROD_PRICE INT NOT NULL,
#   PRIMARY KEY (PROD_ID),FOREIGN KEY (PRO_ID) REFERENCES PRODUCT (PRO_ID), FOREIGN KEY (SUPP_ID) REFERENCES SUPPLIER(SUPP_ID))
#   
#   
# - **`order`** (ORD_ID INT NOT NULL, ORD_AMOUNT INT NOT NULL, ORD_DATE DATE, CUS_ID INT NOT NULL, PROD_ID INT NOT NULL,PRIMARY KEY (ORD_ID),FOREIGN KEY (CUS_ID) REFERENCES CUSTOMER(CUS_ID),FOREIGN KEY (PROD_ID) REFERENCES PRODUCT_DETAILS(PROD_ID))
# 
# 
# - **`rating`** (RAT_ID INT NOT NULL, CUS_ID INT NOT NULL, SUPP_ID INT NOT NULL, RAT_RATSTARS INT NOT NULL,PRIMARY KEY (RAT_ID),FOREIGN KEY (SUPP_ID) REFERENCES SUPPLIER (SUPP_ID),FOREIGN KEY (CUS_ID) REFERENCES CUSTOMER(CUS_ID))

# In[20]:


table_creation_query =  """ CREATE TABLE supplier(SUPP_ID int primary key, SUPP_NAME varchar(50), SUPP_CITY varchar(50), 
                        SUPP_PHONE varchar(10));
                       
                       CREATE TABLE customer(CUS_ID INT NOT NULL, CUS_NAME VARCHAR(20) NULL DEFAULT NULL,
                       CUS_PHONE VARCHAR(10), CUS_CITY varchar(30) ,CUS_GENDER CHAR,PRIMARY KEY (CUS_ID));

                       CREATE TABLE category(CAT_ID INT NOT NULL, CAT_NAME VARCHAR(20) NULL DEFAULT NULL,PRIMARY KEY (CAT_ID));

                       CREATE TABLE product(PRO_ID INT NOT NULL, PRO_NAME VARCHAR(20) NULL DEFAULT NULL, 
                       PRO_DESC VARCHAR(60) NULL DEFAULT NULL,CAT_ID INT NOT NULL,
                       PRIMARY KEY (PRO_ID),FOREIGN KEY (CAT_ID) REFERENCES CATEGORY (CAT_ID));

                       CREATE TABLE product_details(PROD_ID INT NOT NULL, PRO_ID INT NOT NULL, SUPP_ID INT NOT NULL, 
                       PROD_PRICE INT NOT NULL,PRIMARY KEY (PROD_ID),FOREIGN KEY (PRO_ID) REFERENCES PRODUCT (PRO_ID), 
                       FOREIGN KEY (SUPP_ID) REFERENCES SUPPLIER(SUPP_ID));

                       CREATE TABLE `orders`(ORD_ID INT NOT NULL, ORD_AMOUNT INT NOT NULL, ORD_DATE DATE, CUS_ID INT NOT NULL,
                       PROD_ID INT NOT NULL,PRIMARY KEY (ORD_ID),FOREIGN KEY (CUS_ID) REFERENCES CUSTOMER(CUS_ID),
                       FOREIGN KEY (PROD_ID) REFERENCES PRODUCT_DETAILS(PROD_ID));

                       CREATE TABLE rating(RAT_ID INT NOT NULL, CUS_ID INT NOT NULL, SUPP_ID INT NOT NULL, 
                       RAT_RATSTARS INT NOT NULL, PRIMARY KEY (RAT_ID), FOREIGN KEY (SUPP_ID) REFERENCES SUPPLIER (SUPP_ID),
                       FOREIGN KEY (CUS_ID) REFERENCES CUSTOMER(CUS_ID));"""

# Executing the query
cursorObject.execute(table_creation_query)


# ### Q2. Insert the following data in the table created above
# #### `Note:` If you are getting any error while inserting the data into tables, Kindly close the connection and reconnect
# 
# #### Table:  supplier
# | SUPP_ID | SUPP_NAME | SUPP_CITY | SUPP_PHONE |
# | --- | --- | --- | --- | 
# | 1 | Rajesh Retails | Delhi | 1234567890 |
# | 2 | Appario Ltd. | Mumbai | 258963147032 | 
# | 3 | Knome products | Bangalore | 9785462315 |
# | 4 | Bansal Retails | Kochi | 8975463285 |
# | 5 | Mittal Ltd. | Lucknow | 7898456532 |

# In[36]:


connection = mysql.connector.connect(host ="localhost",
                                     user ="root",
                                     passwd ="prachi2525",
                                     database = 'e_commerce')
cursorobject = connection.cursor()
# insert into "supplier" table
insert_into_supplier = """INSERT INTO supplier (SUPP_ID, SUPP_NAME, SUPP_CITY, SUPP_PHONE) VALUES (%s, %s, %s, %s);"""

val = [(1, 'Rajesh Retails', 'Delhi', '1234567890'),(2, 'Appario Ltd.', 'Mumbai', '8963147032'),
      (3, 'Knome products', 'Bangalore', '9785462315'),(4, 'Bansal Retails', 'Kochi', '8975463285'),
      (5, 'Mittal Ltd.', 'Lucknow', '7898456532')]

cursorobject.executemany(insert_into_supplier, val)
connection.commit()


# #### Table:  customer
# | CUS_ID | CUS_NAME | SUPP_PHONE | CUS_CITY | CUS_GENDER
# | --- | --- | --- | --- | --- |
# | 1 | AAKASH | 9999999999 | DELHI | M |
# | 2 | AMAN | 9785463215 | NOIDA | M |
# | 3 | NEHA | 9999999998 | MUMBAI | F |
# | 4 | MEGHA | 9994562399 | KOLKATA | F |
# | 5 | PULKIT | 7895999999 | LUCKNOW | M |

# In[38]:


# insert into "category" table
insert_into_category = """INSERT INTO category (CAT_ID, CAT_NAME) VALUES (%s, %s);"""

val = [(1, 'BOOKS'),
       (2, 'GAMES'),
       (3, 'GROCERIES'),
       (4, 'ELECTRONICS'),
       (5, 'CLOTHES')]

cursorobject.executemany(insert_into_category, val)
connection.commit()


# #### Table:  category
# | CAT_ID | CAT_NAME | 
# | --- | --- |  
# | 1 | BOOKS |
# | 2 | GAMES |  
# | 3 | GROCERIES | 
# | 4 | ELECTRONICS | 
# | 5 | CLOTHES | 

# In[37]:


# insert into "customer" table
insert_into_customer = """INSERT INTO customer (CUS_ID, CUS_NAME, CUS_PHONE, CUS_CITY, CUS_GENDER) 
                            VALUES (%s, %s, %s, %s, %s);"""

val = [(1, 'AAKASH', '9999999999', 'DELHI','M'),
       (2, 'AMAN', '9785463215', 'NOIDA','M'),
       (3, 'NEHA', '9999999998', 'MUMBAI','F'),
       (4, 'MEGHA', '9994562399', 'KOLKATA','F'),
       (5, 'PULKIT', '7895999999', 'LUCKNOW','M')]

cursorobject.executemany(insert_into_customer, val)
connection.commit()


# #### Table:  product
# | PRO_ID | PRO_NAME | PRO_DESC | CAT_ID |
# | --- | --- | --- | --- | 
# | 1 | GTA V | DFJDJFDJFDJFDJFJF | 2 |
# | 2 | TSHIRT | DFDFJDFJDKFD | 5 | 
# | 3 | ROG LAPTOP | DFNTTNTNTERND | 4 |
# | 4 | OATS | REURENTBTOTH | 3 |
# | 5 | HARRY POTTER | NBEMCTHTJTH | 1 |
# 

# In[39]:


# insert into "product" table
insert_into_product = """INSERT INTO product (PRO_ID, PRO_NAME, PRO_DESC, CAT_ID)  VALUES (%s, %s, %s, %s);"""

val = [(1, 'GTA V', 'DFJDJFDJFDJFDJFJF', 2),
       (2, 'TSHIRT', 'DFDFJDFJDKFD', 5),
       (3, 'ROG LAPTOP', 'DFNTTNTNTERND', 4),
       (4, 'OATS', 'REURENTBTOTH', 3),
       (5, 'HARRY POTTER', 'NBEMCTHTJTH', 1)]

cursorobject.executemany(insert_into_product, val)
connection.commit()


# #### Table:  product_details
# | PROD_ID | PRO_ID | SUPP_ID | PROD_PRICE |
# | --- | --- | --- | --- | 
# | 1 | 1 | 2 | 1500 |
# | 2 | 3 | 5 | 30000 | 
# | 3 | 5 | 1 | 3000 |
# | 4 | 2 | 3 | 2500 |
# | 5 | 4 | 1 | 1000 |

# In[40]:


# insert into "product_details" table
insert_into_prod_dtls = """INSERT INTO product_details (PROD_ID, PRO_ID, SUPP_ID, PROD_PRICE)  VALUES (%s, %s, %s, %s);"""

val = [(1, 1, 2, 1500),
       (2, 3, 5, 30000),
       (3, 5, 1, 3000),
       (4, 2, 3, 2500),
       (5, 4, 1, 1000)]

cursorobject.executemany(insert_into_prod_dtls, val)
connection.commit()


# #### Table:  orders
# | ORD_ID | ORD_AMOUNT | ORD_DATE | CUS_ID | PROD_ID
# | --- | --- | --- | --- | --- |
# | 20 | 1500 | 2021-10-12 | 3 | 5 |
# | 25 | 30500 | 2021-09-16 | 5 | 2 |
# | 26 | 2000 | 2021-10-05 | 1 | 1 |
# | 30 | 3500 | 2021-08-16 | 4 | 3 |
# | 50 | 2000 | 2021-10-06 | 2 | 1 |

# In[41]:


# insert into "orders" table
insert_into_order = """INSERT INTO `orders` (ORD_ID, ORD_AMOUNT, ORD_DATE, CUS_ID, PROD_ID)   VALUES (%s, %s, %s, %s, %s);"""

val = [(20, 1500, '2021-10-12', 3, 5),
       (2, 30500, '2021-09-16', 5, 2),
       (3, 2000, '2021-10-05', 1, 1),
       (4, 3500, '2021-08-16', 4, 3),
       (5, 2000, '2021-10-06', 2, 1)]

cursorobject.executemany(insert_into_order, val)
connection.commit()


# #### Table: rating
# | RAT_ID | CUS_ID | SUPP_ID | RAT_RATSTARS |
# | --- | --- | --- | --- | 
# | 1 | 2 | 2 | 4 |
# | 2 | 3 | 4 | 3 | 
# | 3 | 5 | 1 | 5 |
# | 4 | 1 | 3 | 2 |
# | 5 | 4 | 5 | 4 |

# In[42]:


# insert into "rating" table
insert_into_rating = """INSERT INTO rating (RAT_ID, CUS_ID, SUPP_ID, RAT_RATSTARS)  VALUES (%s, %s, %s, %s);"""

val = [(1, 2, 2, 4),
       (2, 3, 4, 3),
       (3, 5, 1, 5),
       (4, 1, 3, 2),
       (5, 4, 5, 4)]

cursorobject.executemany(insert_into_rating, val)
connection.commit()


# ### Q3) Display the number of the customer group by their genders who have placed any order of amount greater than or equal to Rs.3000.

# In[45]:


connection = mysql.connector.connect(host ="localhost",
                                     user ="root",
                                     passwd ="prachi2525",
                                     database = 'e_commerce')
cursorobject = connection.cursor()
q3_query="""select t.cus_gender,count(t.cus_gender) as count from
            (select customer.* from customer,`orders` where
            `orders`.cus_id=customer.cus_id  and `orders`.ord_amount>=3000) as t 
            group by t.cus_gender;"""

cursorobject.execute(q3_query)
output=cursorobject.fetchall()
output_panda= pd.DataFrame(output,columns=['CUS_GENDER','COUNT'])    
output_panda


# ### Q4) Display all the order along with product name ordered by a customer having Customer_Id=2;

# In[46]:


q4_query = """  select `orders`.* ,product.pro_name from `orders`,product,product_details where `orders`.cus_id=2 and
                product.pro_id = product_details.pro_id and `orders`.prod_id=product_details.prod_id;  
            """
cursorobject.execute(q4_query) 
#Assigning value to a variale
q4_output=cursorobject.fetchall()

#Data is set to datafram
q4_panda=pd.DataFrame(q4_output,columns=['ORDER_ID','AMOUNT','ORDER_DATE','CUSTOMER_ID','PRODUCT_ID','PRODUCT_NAME'])
#Datafram output display
q4_panda


# ### Q5) Display the Supplier details who can supply more than one product.

# In[47]:


q5_query = """select supplier.* from supplier where supp_id in
            (select supp_id from product_details group by supp_id having count(supp_id)>1 );"""
#Executing the query
cursorobject.execute(q5_query)
#Assign entire value into an output variable
q5_output = cursorobject.fetchall()

#Dataframe to display the values in tabular structure
pd.DataFrame(q5_output,columns=['SUPPLIER_ID','SUPPLIER_NAME','CITY','PHONE'])


# ### Q6) Find the category of the product whose order amount is minimum.

# In[48]:


q6_query="""select category.* from category, product,product_details where product_details.prod_price
            in(select min(prod_price) from product_details) and 
            category.cat_id=product.cat_id and product.pro_id=product_details.pro_id;"""

#Execute the query
cursorobject.execute(q6_query)            
#Fetch the data from the query
q6_output=cursorobject.fetchall()
#Display the table using dataframes
pd.DataFrame(q6_output,columns=['CATEGORY_ID','NAME'])


# ### Q7) Display the Id and Name of the Product ordered after “2021-10-05”.

# In[50]:


q7_query="""select product.pro_id, product.pro_name, `orders`.ord_date from product,`orders`,product_details 
            where `orders`.ord_date='2021-10-05' and
            product.pro_id=product_details.pro_id and
           `orders`.prod_id=product_details.prod_id;"""
#Execute the query           
cursorobject.execute(q7_query)
#Fetch the query data
q7_output=cursorobject.fetchall()
#Display the data through dataframe
pd.DataFrame(q7_output,columns=['Product_Id','Product_Name','Date'])


# ### Q8) Print the top 3 supplier name and id and rating on the basis of their rating along with the customer name who has given the rating.

# In[51]:


q8_query = """SELECT SUPPLIER.SUPP_ID, SUPPLIER.SUPP_NAME, CUSTOMER.CUS_ID, CUSTOMER.CUS_NAME, RATING.RAT_RATSTARS FROM RATING 
              INNER JOIN SUPPLIER ON RATING.SUPP_ID = SUPPLIER.SUPP_ID 
              INNER JOIN CUSTOMER ON RATING.CUS_ID = CUSTOMER.CUS_ID 
              ORDER BY RATING.RAT_RATSTARS DESC LIMIT 3;"""

cursorobject.execute(q8_query)

q8_output = cursorobject.fetchall()

## Lets put the output of this query in pandas DataFrame 
output_df = pd.DataFrame(q8_output, columns=['SUPP_ID','SUPP_NAME','CUS_ID','CUS_NAME','RAT_RATSTARS'])
output_df


# ### Q9) Display customer name and gender whose names start or end with character 'A'.

# In[52]:


q9_query="""select cus_name as Name,cus_gender as Gender from customer
            where cus_name like 'A%' or cus_name like '%A' """
#Execute the query
cursorobject.execute(q9_query)   
#Fetch the query data         
q9_output=cursorobject.fetchall()
#Use Panda Dataframe to visually arange the values
pd.DataFrame(q9_output,columns=['Customer Name','Gender'])


# ### Q10) Display the total order amount of the male customers.

# In[53]:


q10_query="""select sum(`orders`.ord_amount) as Total_Amount from `orders` 
             where cus_id in(select cus_id from customer where cus_gender='M');"""

#Execute the query
cursorobject.execute(q10_query)             
#Fetch the data in the query
q10_output=cursorobject.fetchall()
#Create dataframe to display the table
pd.DataFrame(q10_output,columns=['Total Amount'])


# ### Q11) Display all the Customers left outer join with  the orders

# In[54]:


q11_query="""select customer.*,`orders`.ord_id,`orders`.ord_amount,`orders`.ord_date,`orders`.prod_id from 
             customer left join `orders` on
            `orders`.cus_id=customer.cus_id"""
#Eecute the query
cursorobject.execute(q11_query)
#getting the data from the query
q11_output=cursorobject.fetchall()            
#Enabling dataframe to adapt the tabular columns
pd.DataFrame(q11_output,columns=['CUS_ID','CUS_NAME','CUS_PHONE','CUS_CITY','CUS_GENDER',
                                          'ORD_ID','ORD_AMOUNT','ORD_DATE','PROD_ID'])


# **NOTE:** Always close an open connection once you are done with the database operations

# ## Happy Learning:)
