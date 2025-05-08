# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
from consolemenu.prompt_utils import *
from colors import color
import pyfiglet

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

# Once we're done creating them, we just add the items to the menu
menu.append_item(submenu_item)
menu.append_item(submenu_item2)



# Finally, we call show to show the menu and allow the user to interact

menu.show()