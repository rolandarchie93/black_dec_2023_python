#list collection of multiple elements
number = [1, 2, 3, 4]
countries = ['UK', 2, 'US']
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
cells[0]
cells[0][1]

cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    print('Element:', x)
    
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    for y in x:
        print('Element:', y)