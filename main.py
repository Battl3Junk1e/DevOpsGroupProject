from consolemenu import *
from consolemenu.items import *
from consolemenu.prompt_utils import *
from colors import color
from fetch_phone_list import fetch_file
import pyfiglet
from importers import *
from Phone_Rensa import *
import os
import hashlib
import check_img_db
import SwedishPhoneNumbers

import pyodbc

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=WideWorldImporters;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

def bildRapport():
    print("Report")
    input("Press key to continue")
    return 

def bildStorleksKontroll():
    print("Size")
    input("Press key to continue")
    return 

def bildCopyToBackup():
    print(" Copy")
    input("Press key to continue")
    return

def phoneGetFile():
    message = fetch_file()
    print(message)
    input("Press key to continue")
    return

def phoneCleanData():
    from Phone_Rensa import clean_phone_data
    print("=" * 50)
    print("Cleaning data in phonelists.csv ...\n")
    
    result = clean_phone_data()

    print(result)  # Print result
    print("\nRensning completed. Press any key to return to menu.")
    input()
    
    
def phoneCleanUp():
    print(" ")
    input("Press key to continue")
    return

def bildtilldb():

    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()
    folder_path = "./images"

    current_imgs = check_img_db.check_img_in_db()

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        with open(file_path, "rb") as f:
            binary = f.read()
            hashed = hashlib.sha256(binary).hexdigest()
            
        if hashed in current_imgs:
            print("Skipping, image already in db")
        else:
            cursor.execute("INSERT INTO Images( Img_Name, Img_Data, Img_Hash, Created_At) VALUES (?,?,?,GETDATE())", (file, binary, hashed))

    cnxn.commit()
    cursor.close()
    cnxn.close()           

def SwedishPhoneList():
    print("Swedish telephone numbers:")
    SwedishPhoneNumbers.SwedishPhoneList()
    input("Press key to continue")
    return

def importersView():
    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()
    print("Wide World Importers - Invoice Informations")
    input("Press key to continue")
    cursor.execute("SELECT TOP 200 * FROM dbo.InvoiceLineMargins ORDER BY InvoiceID ASC")
    headers = [col[0] for col in cursor.description]
    print(headers)
    for row in cursor:
        print(row.InvoiceID, row.CustomerName, row.InvoiceDate, row.Description, row.LineProfit)
    input("Top 200 Orderlines - Press key to continue")       
    cursor.close()
    cnxn.close()
    return

menu = ConsoleMenu(pyfiglet.figlet_format("Stefans AB"), "All Data Things")

telefonListaActionSubMenu = ConsoleMenu(pyfiglet.figlet_format("Telefonlista"), "Actions",exit_option_text="Back")
telefonListaActionSubMenu.append_item( FunctionItem("Hämta grundfil", phoneGetFile) )
telefonListaActionSubMenu.append_item( FunctionItem("Rensa data", phoneCleanData) )
telefonListaActionSubMenu.append_item( FunctionItem("Clean up", phoneCleanUp) )
telefonListaActionSubMenu.append_item( FunctionItem("Swedish Phone Numbers", SwedishPhoneList) )
submenu_item = SubmenuItem("Telefonlista", telefonListaActionSubMenu, menu)

bilderActionSubMenu = ConsoleMenu(pyfiglet.figlet_format("Bilder"), "Actions",exit_option_text="Back")
bilderActionSubMenu.append_item( FunctionItem("Generera thumbnails", bildRapport) )
bilderActionSubMenu.append_item( FunctionItem("Bildrapport", bildRapport) )
bilderActionSubMenu.append_item( FunctionItem("Storlekskontroll", bildStorleksKontroll) )
bilderActionSubMenu.append_item( FunctionItem("Kopiera till backup", bildCopyToBackup) )
bilderActionSubMenu.append_item( FunctionItem("Ladda upp bilder till DB", bildtilldb) ) 
submenu_item2 = SubmenuItem("Bilder", bilderActionSubMenu, menu)

ImportersActionSubMenu = ConsoleMenu(pyfiglet.figlet_format("Importers"), "Actions",exit_option_text="Back")
ImportersActionSubMenu.append_item( FunctionItem("Hämta fakturasiffror", importersView) )
ImportersActionSubMenu.append_item(FunctionItem("Skapa ny Person", create_new_person))
ImportersActionSubMenu.append_item(FunctionItem("Visa alla personer", show_all_people))
submenu_item3 = SubmenuItem("Importers", ImportersActionSubMenu, menu)

menu.append_item(submenu_item)
menu.append_item(submenu_item2)
menu.append_item(submenu_item3)


menu.show()
