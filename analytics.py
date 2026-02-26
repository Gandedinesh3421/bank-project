from db_connection import db, cursor

print("\n1) Total Deposit and Withdrawal Summary:")
query1 = """
SELECT 
    SUM(CASE WHEN txn_type = 'CREDIT' THEN amount END) AS total_deposit,
    SUM(CASE WHEN txn_type = 'DEBIT' THEN amount END) AS total_withdrawal
FROM transactions;
"""
cursor.execute(query1)
print(cursor.fetchall())

print("\n2) Highest Spending Customers:")
query2 = """
SELECT c.name, SUM(t.amount) AS total_spent
FROM transactions t
JOIN accounts a ON t.account_id = a.account_id
JOIN customers c ON a.customer_id = c.customer_id
WHERE t.txn_type = 'DEBIT'
GROUP BY c.customer_id
ORDER BY total_spent DESC;
"""
cursor.execute(query2)
print(cursor.fetchall())

print("\n3) Customers with Most Deposits:")
query3 = """
SELECT c.name, SUM(t.amount) AS total_deposit
FROM transactions t
JOIN accounts a ON t.account_id = a.account_id
JOIN customers c ON a.customer_id = c.customer_id
WHERE t.txn_type = 'CREDIT'
GROUP BY c.customer_id
ORDER BY total_deposit DESC;
"""
cursor.execute(query3)
print(cursor.fetchall())

print("\n4) Monthly Transaction Volume:")
query4 = """
SELECT MONTH(txn_date) AS month, COUNT(*) AS total_transactions
FROM transactions
GROUP BY MONTH(txn_date)
ORDER BY month;
"""
cursor.execute(query4)
print(cursor.fetchall())

print("\n5) Suspicious Transactions (Above ₹20,000):")
query5 = """
SELECT txn_id, account_id, amount, txn_type, txn_date
FROM transactions
WHERE amount > 20000;
"""
cursor.execute(query5)
print(cursor.fetchall())

db.close()
