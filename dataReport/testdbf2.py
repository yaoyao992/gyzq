import dbf

# Define the structure of the DBF table and create it

table = dbf.Table('Y:/newfile.dbf', 'name C(25); age N(3,0)')
table.open(dbf.READ_WRITE)

# Add records to the table
table.append(('Alice',30))
print(table.first_record)

# Commit changes and close the table
table.close()