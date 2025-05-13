# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
from consolemenu.prompt_utils import *
from colors import color
import pyfiglet
import pyodbc

#Host Wide World Importers Locally, check for the correct connection string and driver
#Only works with Windows Authentication and the ODBC Driver 17 for SQL Server
#Install the ODBC Driver 17 for SQL Server from https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server

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

#Install InvoiceLineMarginsView on Wide World Importers Database before running this
def importersView():
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

# Create the menu
#menu = ConsoleMenu("Stefans AB", "All Data Things")
menu = ConsoleMenu(pyfiglet.figlet_format("Stefans AB"), "All Data Things")

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected
#menu_item = MenuItem(color("Telefonlista",fg="green"))


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
submenu_item3 = SubmenuItem("Importers", ImportersActionSubMenu, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(submenu_item)
menu.append_item(submenu_item2)
menu.append_item(submenu_item3)



# Finally, we call show to show the menu and allow the user to interact

menu.show()