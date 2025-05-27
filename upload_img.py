from datetime import datetime
import os
import fnmatch

def CreateFileName():

    date = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    filename = f"{date}-CreateTableImages.sql"
    return filename

def CreateSQLFile():
    file_name = CreateFileName()

    with open(f"{file_name}", "w") as file:
        file.write("IF NOT EXISTS (\n")
        file.write("    SELECT 1 FROM INFORMATION_SCHEMA.TABLES\n")
        file.write("    WHERE TABLE_NAME = 'Images' AND TABLE_SCHEMA = 'Application'\n")
        file.write(")\n")
        file.write("BEGIN\n")
        file.write("    CREATE TABLE Images(\n")
        file.write("        ID INT PRIMARY KEY IDENTITY(1,1),\n")
        file.write("        Img_Name VARCHAR(20) NOT NULL,\n")
        file.write("        Img_Data VARBINARY(MAX) NOT NULL,\n")
        file.write("        Img_Hash NVARCHAR(64) NOT NULL,\n")
        file.write("        Created_At DATETIME DEFAULT GETDATE() NOT NULL,\n")
        file.write("	);\n")
        file.write("	PRINT 'Table created';\n")
        file.write("END\n")
        file.write("ELSE\n")
        file.write("BEGIN\n")
        file.write("	PRINT 'Something went wrong';\n")
        file.write("END\n")

for file in os.listdir("."):
    if fnmatch.fnmatch(file, "*-CreateTableImages.sql"):
        os.remove(file)

CreateSQLFile()