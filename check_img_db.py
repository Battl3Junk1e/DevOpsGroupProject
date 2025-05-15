import pyodbc

def check_img_in_db():
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=WideWorldImporters;"
        "Trusted_Connection=yes;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )

    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()
    cursor.execute("select Img_hash from images")
    dbimg = [row[0] for row in cursor.fetchall()]
    return dbimg

if __name__ == '__main__':
    check_img_in_db()