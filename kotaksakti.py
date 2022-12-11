import mysql.connector

def func_sql(sql_statement):
    connection = mysql.connector.connect(host='localhost',
                                                database='test',
                                                user='root',
                                                password='306766@!#Aa')
    cursor = connection.cursor()
    cursor.execute(sql_statement)
    result = cursor.fetchall()
    return(result)

data1 = func_sql('SELECT customer_id FROM  invoices LEFT JOIN  invoice_lines  ON invoices.id = invoice_lines.invoice_id group by customer_id having (sum(quantity) >= 5)')
data2 = func_sql('SELECT name FROM test.customers WHERE NOT EXISTS ( SELECT customer_id from test.invoices WHERE test.invoices.customer_id = test.customers.id)')
data3 = func_sql('SELECT `description`, `name` FROM invoice_lines i INNER JOIN invoices j ON i.invoice_id = j.id INNER JOIN customers c ON j.customer_id = c.id ORDER BY `description`')

print('Number of customers purchasing more than 5 books : {}'.format(len(data1)))
print('\nList of customers who never purchased anything :')
for row in data2:
    print(row[0])
print('\nList of book purchased with the users :')
for row in data3:
    print(row[0],row[1])

