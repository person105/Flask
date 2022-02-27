# import sqlite3


# print("Setting up DB")
# con = sqlite3.connect('CTF.db')

# con.execute("CREATE TABLE IF NOT EXISTS SuperSecretTable(flag text)")

# con.execute("""INSERT INTO users (username, password) 
#                     VALUES (?, ?)""", ("dontlookforthesupersecrettable","https://www.youtube.com/watch?v=DYLDG_2Vs3E"))


# con.execute("""INSERT INTO SuperSecretTable (flag) 
#                     VALUES (?)""", ("FLAAAGGG: CLEARED",))
                    
# con.commit()