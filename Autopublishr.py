import mysql.connector
def tabase():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="password",
      database="autopublishr"
    )
    return mydb
def create_user(mydb, username, password):
    mycursor = mydb.cursor()
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)
    mydb.commit()
def get_user(mydb, username):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM users WHERE username = %s"
    val = (username,)
    mycursor.execute(sql, val)
    return mycursor.fetchone()
def create_draft(mydb, user_id, title, content):
    mycursor = mydb.cursor()
    sql = "INSERT INTO drafts (user_id, title, content) VALUES (%s, %s, %s)"
    val = (user_id, title, content)
    mycursor.execute(sql, val)
    mydb.commit()
def get_draft(mydb, draft_id):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM drafts WHERE draft_id = %s"
    val = (draft_id,)
    mycursor.execute(sql, val)
    return mycursor.fetchone()
def update_draft(mydb, draft_id, title, content):
    mycursor = mydb.cursor()
    sql = "UPDATE drafts SET title = %s, content = %s WHERE draft_id = %s"
    val = (title, content, draft_id)
    mycursor.execute(sql, val)
    mydb.commit()
def delete_draft(mydb, draft_id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM drafts WHERE draft_id = %s"
    val = (draft_id,)
    mycursor.execute(sql, val)
    mydb.commit()
def create_feedback(mydb, draft_id, feedback):
    mycursor = mydb.cursor()
    sql = "INSERT INTO
