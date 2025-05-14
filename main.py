from consolemenu import *
from consolemenu.items import *
from consolemenu.prompt_utils import *
#from colors import color
import pyfiglet
import pyodbc
from importers import *


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
    print(" Getting the file")
    input("Press key to continue")
    return

def phoneCleanData():
    print(" ")
    input("Press key to continue")
    return
    
    
def phoneCleanUp():
    print(" ")
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
submenu_item = SubmenuItem("Telefonlista", telefonListaActionSubMenu, menu)


bilderActionSubMenu = ConsoleMenu(pyfiglet.figlet_format("Bilder"), "Actions",exit_option_text="Back")
bilderActionSubMenu.append_item( FunctionItem("Generera thumbnails", bildRapport) )
bilderActionSubMenu.append_item( FunctionItem("Bildrapport", bildRapport) )
bilderActionSubMenu.append_item( FunctionItem("Storlekskontroll", bildStorleksKontroll) )
bilderActionSubMenu.append_item( FunctionItem("Kopiera till backup", bildCopyToBackup) )
submenu_item2 = SubmenuItem("Bilder", bilderActionSubMenu, menu)

ImportersActionSubMenu = ConsoleMenu(pyfiglet.figlet_format("Importers"), "Actions",exit_option_text="Back")
ImportersActionSubMenu.append_item( FunctionItem("Hämta fakturasiffror", importersView) )
#ImportersActionSubMenu.append_item(FunctionItem("Visa kolumner i People-tabellen", show_person_table_columns))
ImportersActionSubMenu.append_item(FunctionItem("Skapa ny Person", create_new_person))
ImportersActionSubMenu.append_item(FunctionItem("Visa alla personer", show_all_people))
submenu_item3 = SubmenuItem("Importers", ImportersActionSubMenu, menu)


menu.append_item(submenu_item)
menu.append_item(submenu_item2)
menu.append_item(submenu_item3)


menu.show()
