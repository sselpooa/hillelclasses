import sqlite3

connection = sqlite3.connect('articles.db')
cursor = connection.cursor()

def create_table():
    abc= """
    CREATE TABLE IF NOT EXISTS articles(
        id = INTEGER PRIMARY KEY AUTOINCREMENT,
        title = VARCHAR(40) DEFAULT 'NO NAME',
        text = VARCHAR(111111),
        created_at = CURRENT_DATE 
    )
    """
    cursor.execute(abc)
    connection.commit()

def update_article(id,title,text):
    cursor.execute(f'update articles set title = "{title}" set text = "{text}" where id = "{id}")
    connection.commit()

def get_article(search):
    cursor.execute(f"select * from articles where title or text like '{search}'")

def delete_article(id):
    cursor.execute(f"delete from articles where id = '{id}'")