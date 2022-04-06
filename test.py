from db import query

query("INSERT INTO customers (surname, name, birthday) VALUES ('nick','hallo','2222-01-01')")
query("SELECT * FROM customers;")