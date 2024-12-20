import os
from datetime import date
from pathlib import Path

from dbfpy3 import dbf

# # create DBF
# db = dbf.Dbf('Y:/new.dbf', new=True)
# db.header.code_page = 0x78
# db.add_field(
#     ('C', 'NAME', 15),
#     ('C', 'SURNAME', 25),
#     ('D', 'BIRTHDATE'),
# )

# for (name, surname, birthdate) in (
#         ('John', 'Miller', (1981, 1, 2)),
#         ('Andy', 'Larkin', (1982, 3, 4)),
#         ('Bill', 'Clinth', (1983, 5, 6)),
#         ('Bobb', 'McNail', (1984, 7, 8)),
#         ('毛', '仁愛', (1984, 7, 8)),
#         ('吳', '開深', (1984, 7, 8)),
# ):
#     rec = db.new()
#     rec['NAME'] = name
#     rec['SURNAME'] = surname
#     rec['BIRTHDATE'] = birthdate
#     db.write(rec)

# print(db, '\n\n')
# db.close()

# # read and update DBF

# print("Windows console can't print unicode characters, "
#       'so this may raise error')


# Use `with` statement
with dbf.Dbf('Y:/ZYHG0002_20240422.dbf') as db:
    print(db, '\n')
    for record in db:
        print(record, '\n')
        record[b'ZJYTMS'] = 'yaoyaoyaoyaoyaoyaoyao'
        record[b'LYBZBL'] = 888.88
        db.write(record)