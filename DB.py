import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

#====== CREATE ========
# cur.execute("CREATE TABLE users (login TEXT);")
# connection.commit()


#===== INSERT =========
# log = input("Login : ")
# cur.execute(f"INSERT INTO users (login) VALUES ('{log}');")
# connection.commit()
# print("Users added!")


#===== SELECT ========
# cur.execute(f"SELECT * FROM users WHERE login='admin';")
# connection.commit()
# res = cur.fetchall()
# print(res)


#===== UPDATE ========
# cur.execute(f"UPDATE users SET login='vlad' WHERE rowid=4;")
# connection.commit()


#===== DELETE =======
cur.execute(f"DELETE FROM users WHERE login='anna';")
connection.commit()



connection.close()