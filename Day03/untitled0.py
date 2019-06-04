with open(northwind, 'r') as f:
    wholefile = f.read()
    #or, you can initialize a list to store your data
    data = []
    for line in f:
        data.append(line)