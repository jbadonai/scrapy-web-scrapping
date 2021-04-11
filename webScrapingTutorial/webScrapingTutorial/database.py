import sqlite3

conn = sqlite3.connect("mydatabase1.db")
curr = conn.cursor()

def createTable(tableName, conn, curr):
    statement = f"""
    create table {tableName}(
        winename text,
        volume text,
        price text,
        category text
    )
    """
    curr.execute(statement)
    conn.commit()
    conn.close()

def insertData(tableName, conn, curr):
    statement = f"""
    insert into {tableName} values('eva', '75ml', 'N30.54', 'non alcoholic')
    """
    curr.execute(statement)
    conn.commit()
    conn.close()

# createTable('wine_tb',conn,curr)
# insertData('wine_tb',conn,curr)
