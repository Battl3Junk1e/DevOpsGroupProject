from datetime import datetime
import os, fnmatch

SQL_VIEW = (

"""USE [WideWorldImporters]
GO

DROP VIEW IF EXISTS dbo.InvoiceLineMargins;
GO

CREATE VIEW dbo.InvoiceLineMargins
AS
    SELECT 
        si.InvoiceID, 
        sc.CustomerName, 
        si.InvoiceDate, 
        sil.Description, 
        sil.LineProfit
    FROM Sales.Invoices AS si
    JOIN Sales.InvoiceLines AS sil ON si.InvoiceID = sil.InvoiceID
    JOIN Sales.Customers AS sc ON si.CustomerID = sc.CustomerID;"""
)

def filename():    
    date = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))    
    return (date + "-CreateInvoiceLineMargins.sql")

def main():
    FOLDER = "sqlscripts"
    try:
        os.makedirs(FOLDER, exist_ok=True)
    except OSError as e:
        print(f"Error creating folder '{FOLDER}': {e}")
        return
    
    pattern = "*-CreateInvoiceLineMargins.sql"
    for file in os.listdir(FOLDER):
        if fnmatch.fnmatch(file, pattern):
            old_file = os.path.join(FOLDER, file)
            os.remove(old_file)
            print(f"Removed old file: {old_file}")
    
    file_path = os.path.join(FOLDER, filename())
    with open(file_path, 'w') as f:
        f.write(SQL_VIEW)
    print(f"File '{file_path}' created successfully.")

if __name__ == "__main__":
    main()
