USE [WideWorldImporters]
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
    JOIN Sales.Customers AS sc ON si.CustomerID = sc.CustomerID;