def printTable(table):
    print( [0] * len(tableData))
    for list in table:
        for items in list:
            print(items)
            print(list)



tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
