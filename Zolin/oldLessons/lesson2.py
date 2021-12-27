import sqlite3

test = {}
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''CREATE TABLE Good (Id integer PRIMARY KEY AUTOINCREMENT,Name string,ManufacturerId integer,Price float)''')
c.execute('''CREATE TABLE Storage (Id integer, Count integer)''')
c.execute('''CREATE TABLE Manufacturer (ManufacturerId integer PRIMARY KEY AUTOINCREMENT,PrName string,
Country string)''')
c.execute('''CREATE TABLE Size (Id integer,Size float)''')

while True:
    input1 = str(input('>'))
    if input1 == "add":
        name = str(input('>>'))
        brand = str(input('>>'))
        brandCountry = str(input('>>'))
        count = int(input('>>'))
        size = float(input('>>'))
        price = float(input('>>'))
        c.execute('insert into Manufacturer(PrName, Country) values(?,?)', (brand, brandCountry))
        c.execute('insert into Good(Name, ManufacturerId, Price) values (?,?,?)', (name, c.lastrowid, price))
        c.execute('insert into Storage(Id, Count) values(?,?)', (c.lastrowid, count))
        c.execute('insert into Size(Id, Size) values(?,?)', (c.lastrowid, size))

        # Save (commit) the changes
        conn.commit()
        test.update({name: {"brand": brand, "size": size, "price": price, "count": count}})
    elif input1 == "del":
        name = str(input('>>'))
        del test[name]
    elif input1 == "stat":
        brands = {}
        sizes = {}
        for name in test:
            brand = test[name]["brand"]
            size = test[name]["size"]

            if brands == brand:
                brands[brand] += test[name]["count"]
            else:
                brands[brand] = test[name]["count"]

            if sizes == size:
                sizes[size] += test[name]["count"]
            else:
                sizes[size] = test[name]["count"]
        print(sizes)
        print(brands)
    else:
        c.execute('select * from Good JOIN Storage ON Good.Id = Storage.Id')
        [print(row) for row in c.fetchall()]
