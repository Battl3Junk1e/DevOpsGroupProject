import pyodbc
from datetime import datetime

def create_new_person():
    try:
        print("\n--- Skapa en ny Person till Person-tabellen ---")

        # 1. Set up database connection
        conn_str = (
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'
            'DATABASE=WideWorldImporters;'
            'Trusted_Connection=yes;'
            'Encrypt=yes;'
            'TrustServerCertificate=yes;'
        )

        cnxn = pyodbc.connect(conn_str)
        cursor = cnxn.cursor()

        #  2. Check if Person table exists — create it if not
        cursor.execute("""
            IF NOT EXISTS (
                SELECT * FROM sys.tables 
                WHERE name = 'Person' AND schema_id = SCHEMA_ID('Application')
            )
            BEGIN
                EXEC('
                    CREATE TABLE Application.Person (
                        PersonID INT IDENTITY PRIMARY KEY,
                        FullName NVARCHAR(50) NOT NULL,
                        PreferredName NVARCHAR(50) NOT NULL,
                        EmailAddress NVARCHAR(256) NULL,
                        CreatedAt DATETIME2 DEFAULT SYSDATETIME()
                    )
                ')
            END
        """)

        # 3. If the table is empty, import initial data from Application.People
        cursor.execute("SELECT COUNT(*) FROM Application.Person")
        count = cursor.fetchone()[0]

        if count < 1:
            print(" Initializing test table with data from Application.People...")
            cursor.execute("""
                INSERT INTO Application.Person (FullName, PreferredName, EmailAddress)
                SELECT TOP 30 FullName, PreferredName, EmailAddress
                FROM Application.People
                WHERE EmailAddress IS NOT NULL
            """)
            cnxn.commit()
            print(" Test data has been imported.\n")

        #  4. Prompt for input and validate until all fields are filled
        while True:
            full_name = input("Fullständigt namn: ").strip()
            preferred_name = input("Tilltalsnamn: ").strip()
            email = input("E-postadress: ").strip()

            if not full_name or not preferred_name or not email:
                print(" All fields are required. Please try again.\n")
                continue
            break

        print('')
        print(" Attempting to save the person to Person...")

        #  5. Insert the new person
        cursor.execute("""
            INSERT INTO Application.Person (FullName, PreferredName, EmailAddress)
            VALUES (?, ?, ?)
        """, (full_name, preferred_name, email))
        cnxn.commit()
        print("The person has been saved successfully.")

        #  6. Confirm the new person was inserted
        cursor.execute("""
            SELECT TOP 1 PersonID, FullName, EmailAddress 
            FROM Application.Person
            ORDER BY PersonID DESC
        """)
        result = cursor.fetchone()
        if result:
            print(f"\n Confirmation: {result.FullName} | {result.EmailAddress} | ID = {result.PersonID}")
        else:
            print("Could not confirm inserted data.")

    except Exception as e:
        print(f"\n Error during insert: {e}")

    finally:
        #  7. Clean up
        try:
            cursor.close()
            cnxn.close()
        except:
            pass
        input("\n Press any key to return to the menu...")







def show_all_people():
    import pyodbc
    try:
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'
            'DATABASE=WideWorldImporters;'
            'Trusted_Connection=yes;'
            'Encrypt=yes;'
            'TrustServerCertificate=yes;'
        )
        cursor = cnxn.cursor()

        cursor.execute("""
            SELECT TOP 20 FullName, PreferredName, EmailAddress
            FROM Application.Person
            ORDER BY PersonID DESC;
        """)

        print("\n Alla personer i databasen (senaste först):")
        for row in cursor.fetchall():
            print(f"- {row.FullName} ({row.PreferredName}) | {row.EmailAddress}")

    except Exception as e:
        print(f" Fel vid hämtning: {e}")

    finally:
        try:
            cursor.close()
            cnxn.close()
        except:
            pass

    input("\n Tryck på valfri knapp för att gå tillbaka...")



'''
def show_person_table_columns():
    import pyodbc

    try:
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'
            'DATABASE=WideWorldImporters;'
            'Trusted_Connection=yes;'
            'Encrypt=yes;'
            'TrustServerCertificate=yes;'
        )
        cursor = cnxn.cursor()

        cursor.execute("SELECT TOP 1 * FROM Application.People")
        columns = [col[0] for col in cursor.description]

        print("\n📋 Kolumner i Application.People:")
        for col in columns:
            print(f" - {col}")

    except Exception as e:
        print(f"\n❌ Kunde inte läsa tabellstruktur: {e}")

    finally:
        try:
            cursor.close()
            cnxn.close()
        except Exception as ex:
            print(f"⚠️ Fel vid stängning av anslutning: {ex}")

    input("\n👉 Tryck på valfri knapp för att gå tillbaka till menyn...")
'''
