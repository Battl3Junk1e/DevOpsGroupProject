USE WideWorldImporters
GO

-- This code replaces area codes '415' to '515'
UPDATE Application.People
SET PhoneNumber = STUFF(PhoneNumber, CHARINDEX('415', PhoneNumber), 3, '515'),
	FaxNumber = STUFF(FaxNumber, CHARINDEX('415', FaxNumber), 3, '515')
WHERE PhoneNumber LIKE '%415%' or FaxNumber LIKE '%415%';

-- This code replaces area codes '252' to '992'
UPDATE Application.People
SET PhoneNumber = STUFF(PhoneNumber, CHARINDEX('252', PhoneNumber), 3, '992'),
	FaxNumber = STUFF(FaxNumber, CHARINDEX('252', FaxNumber), 3, '992')
WHERE PhoneNumber LIKE '%252%' or FaxNumber LIKE '%252%';

-- This code replaces area codes '314' to '316'
UPDATE Application.People
SET PhoneNumber = STUFF(PhoneNumber, CHARINDEX('314', PhoneNumber), 3, '316'),
	FaxNumber = STUFF(FaxNumber, CHARINDEX('314', FaxNumber), 3, '316')
WHERE PhoneNumber LIKE '%314%' or FaxNumber LIKE '%314%';

/* Use these SELECT-Statements to check if the update codes has gone through and if changes were made correctly.
This SELECT-Statement shows you the PhoneNumber and/or FaxNumber with the area codes 252, 415 and/or 314.
SELECT PhoneNumber, FaxNumber
FROM Application.People
WHERE PhoneNumber LIKE '%252%'
	OR PhoneNumber LIKE '%415%'
	OR PhoneNumber LIKE '%314%'
	OR FaxNumber LIKE '%252%'
	OR FaxNumber LIKE'%415%'
	OR FaxNumber LIKE '%314%';

This SELECT-Statement shows you the PhoneNumber and/or FaxNumber with the new area codes 992, 515 and/or 316.
SELECT PhoneNumber, FaxNumber
FROM Application.People
WHERE PhoneNumber LIKE '%992%'
	OR PhoneNumber LIKE '%515%'
	OR PhoneNumber LIKE '%316%'
	OR FaxNumber LIKE '%992%'
	OR FaxNumber LIKE'%515%'
	OR FaxNumber LIKE '%316%'; 
	*/