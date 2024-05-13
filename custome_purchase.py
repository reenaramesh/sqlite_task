import sqlite3

try:

  # Connect to DB and create a cursor
  sqlite_connection = sqlite3.connect('customer_order.db')
  cursor = sqlite_connection.cursor()
  print('DB initiated')


  
  query1 = 'CREATE TABLE IF NOT EXISTS customers (customer_id INTEGER PRIMARY KEY, name TEXT, age INTEGER);'
  cursor.execute(query1)
  print('Table1 created')

  query2 = 'CREATE TABLE IF NOT EXISTS items (item_id INTEGER PRIMARY KEY, item_name TEXT);'
  cursor.execute(query2)
  print('Table2 created')

  query3 = 'CREATE TABLE IF NOT EXISTS sales (sales_id INTEGER PRIMARY KEY, customer_id INTEGER);'
  cursor.execute(query3)
  print('Table3 created')

  query4 = 'CREATE TABLE IF NOT EXISTS orders (order_id INTEGER PRIMARY KEY, sales_id INTEGER, item_id INTEGER, quantity INTEGER,FOREIGN KEY (customer_id) REFERENCES customer(customer_id), FOREIGN KEY (item_id) REFERENCES item(item_id));'
  cursor.execute(query4) 
  print('Table4 created')


  cursor.execute( 
    """INSERT INTO customers (customer_id,name,age) VALUES ("1","a",25)""")
  print('inserted')
  cursor.execute( 
    """INSERT INTO customers (customer_id,name,age) VALUES ("2","b",22)""")
  print('inserted')
  cursor.execute( 
    """INSERT INTO customers (customer_id,name,age) VALUES ("3","c",20)""")
  print('inserted')
  cursor.execute( 
    """INSERT INTO customers (customer_id,name,age) VALUES ("4","d",12)""")
  print('inserted')

  cursor.execute( 
    """INSERT INTO items (item_id,item_name) VALUES ("1","coffee")""")
  print('inserted')


  cursor.execute( 
    """INSERT INTO items (item_id,item_name) VALUES ("2","tea")""")
  print('inserted')
  
  cursor.execute( 
    """INSERT INTO items (item_id,item_name) VALUES ("3","milk")""")
  print('inserted')

  cursor.execute( 
    """INSERT INTO items (item_id,item_name) VALUES ("4","juice")""")
  print('inserted')

  cursor.execute( 
    """INSERT INTO sales (sales_id,customer_id) VALUES ("1","2")""")
  print('inserted')

  cursor.execute( 
    """INSERT INTO sales (sales_id,customer_id) VALUES ("2","1")""")
  print('inserted')

 
  cursor.execute( 
    """INSERT INTO sales (sales_id,customer_id) VALUES ("3","1")""")
  print('inserted')

  cursor.execute( 
    """INSERT INTO sales (sales_id,customer_id) VALUES ("4","3")""")
  print('inserted')

  cursor.execute( 
    """INSERT INTO sales (sales_id,customer_id) VALUES ("5","1")""")
  print('inserted')

 
  cursor.execute( 
    """INSERT INTO sales (sales_id,customer_id) VALUES ("6","2")""")
  print('inserted')

  cursor.execute( 
    """INSERT INTO sales (sales_id,customer_id) VALUES ("7","4")""")
  print('inserted')

  cursor.execute( 
    """INSERT INTO orders (order_id,sales_id, item_id, quantity ) VALUES ("1","4","4","3")""")
  print('inserted')  

  cursor.execute( 
    """INSERT INTO orders (order_id,sales_id, item_id, quantity ) VALUES ("2","3","2","2")""")
  print('inserted')

  cursor.execute( 
    """INSERT INTO orders (order_id,sales_id, item_id, quantity ) VALUES ("3","2","3","7")""")
  print('inserted')

  cursor.execute( 
    """INSERT INTO orders (order_id,sales_id, item_id, quantity ) VALUES ("4","4","2","4")""")
  print('inserted')


  cursor.execute( 
    """INSERT INTO orders (order_id,sales_id, item_id, quantity ) VALUES ("5","1","4","2")""")
  print('inserted')

  cursor.execute( 
    """INSERT INTO orders (order_id,sales_id, item_id, quantity ) VALUES ("6","2","3","7")""")
  print('inserted')

  cursor.execute( 
    """INSERT INTO orders (order_id,sales_id, item_id, quantity ) VALUES ("7","4","4","4")""")
  

  show_data = '''select * from sales'''
  cursor.execute(show_data)
  print('data')
  
  show_data = cursor.fetchall()
  for x in show_data:
            print(x)


  total = """select customers.name, items.item_name, sum (orders.quantity), customers.age as sum_quantity from orders join customers on orders.order_id = customers.customer_id join items on orders.item_id = items.item_id where customers.age between 18 and 35 group by items.item_name"""         
  
  cursor.execute(total)
  print('data')
  
  show_data = cursor.fetchall()
  for y in show_data:
            print(y)


  

  cursor.close()


except sqlite3.Error as error:
  print('Error occurred - ', error)



finally:

  if sqlite_connection:
    sqlite_connection.close()
    print(" Connection closed")

    

