import sqlite3
conn = sqlite3.connect('my_table.db')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS my_table
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT, overview TEXT, status TEXT)'''
)
cursor.execute(
    '''INSERT INTO my_table
    (task, overview, status)
    VALUES('task_1', 'addition', 'completed')'''
)
conn.commit()
cursor.execute(
    '''INSERT INTO my_table
    (task, overview, status)
    VALUES('task_2', 'multiplication', 'not completed')''')
conn.commit()
cursor.execute(
    '''INSERT INTO my_table
    (task, overview, status)
    VALUES('task_3', 'division', 'not completed')''')
conn.commit()
cursor.execute('''SELECT * FROM my_table''')
k = cursor.fetchmany(3)
print(k)
conn.close()