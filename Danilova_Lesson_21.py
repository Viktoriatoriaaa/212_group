# Задача 1:
# import sqlite3
#
# conn = sqlite3.connect('my_table1.db')
# cursor = conn.cursor()
# cursor.execute(
#     '''CREATE TABLE IF NOT EXISTS my_table1(
#                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
#                                            text1 TEXT,
#                                            text2 TEXT)'''
# )
# cursor.execute('''INSERT INTO my_table1(text1, text2) VALUES("HELLO", "WORLD")''')
# conn.commit()
# cursor.execute('''SELECT * FROM my_table1''')
# k = cursor.fetchall()
# cursor.execute('''DELETE FROM my_table1 WHERE id = ?''', (k[1][0],))
# conn.commit()
# cursor.execute('''UPDATE my_table1 SET text1 = 'hello1', text2 = 'world1' WHERE id = ?''', (k[1][0],))
# conn.commit()
# conn.close()

# Задача 2:
# cursor.execute('''SELECT * FROM my_table1''')
# n = cursor.fetchall()
# print(n)
# s = 0
# for i in n:
#     s += 1
#     if s <= (len(n)//2) and len(n) != 1:
#         cursor.execute('''DELETE FROM my_table1 WHERE id=?''', (i[0],))
#         conn.commit()
#     elif s > (len(n)//2):
#         cursor.execute('''UPDATE my_table1 SET text1 = 'h1', text2 = 'w1' WHERE id = ?''', (i[0],))
#         conn.commit()
# conn.close()
# Задача 3:
import sqlite3

conn = sqlite3.connect('my_table2.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS my_table2(id INTEGER PRIMARY KEY AUTOINCREMENT,text TEXT)''')
conn.commit()

conn1 = sqlite3.connect('my_table3.db')
cursor1 = conn1.cursor()
cursor1.execute('''CREATE TABLE IF NOT EXISTS my_table3(id INTEGER PRIMARY KEY AUTOINCREMENT,digit INTEGER)''')
conn1.commit()
my_list = ['Home', 'Work', 29, 9, 2022]
g = 'нечётное'
for i in my_list:
    if str(i).isalpha():
        cursor.execute('''INSERT INTO my_table2(text) VALUES(?)''', (i,))
        conn.commit()
        p = len(i)
        cursor1.execute('''INSERT INTO my_table3(digit) VALUES(?)''', (p,))
        conn1.commit()
    elif str(i).isdigit():
        if int(i)%2 == 0:
            cursor1.execute('''INSERT INTO my_table3(digit) VALUES(?)''', (i,))
            conn1.commit()
        else:
            cursor.execute('''INSERT INTO my_table2(text) VALUES(?)''', (g,))
            conn.commit()

cursor.execute('''SELECT * FROM my_table2''')
x = cursor.fetchall()
print(x)
cursor1.execute('''SELECT * FROM my_table3''')
y = cursor1.fetchall()
print(y)
if len(y) > 5:
    cursor.execute('''DELETE FROM my_table2 WHERE id = ?''', (x[0][0],))
    conn.commit()
elif len(y) < 5:
    cursor.execute('''UPDATE my_table2 SET text = 'hello' WHERE id = ?''', (x[0][0],))
    conn.commit()
# conn.close()
