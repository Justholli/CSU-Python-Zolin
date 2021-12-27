test = {}

def readfileonstart():
    f = open("filename.txt", "r")
    lines = f.readlines()

    for line in lines:
        linesplit = line.split(" ")
        name = linesplit[0]
        brand = linesplit[1]
        count = linesplit[2]
        size = linesplit[3]
        price = linesplit[4]
        test.update()

while True:
    input1 = str(input('>'))
    if input1 == "add":
        name = str(input('>>'))
        brand = str(input('>>'))
        count = int(input('>>'))
        size = int(input('>>'))
        price = int(input('>>'))
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

            if (brands.has_key(brand)):
                brands[brand] += test[name]["count"]
            else:
                brands[brand] = test[name]["count"]

            if (sizes.has_key(size)):
                sizes[size] += test[name]["count"]
            else:
                sizes[size] = test[name]["count"]
        print(sizes)
        print(brands)
    else:
        print(test)
