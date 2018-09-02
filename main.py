import pygal
i = open('pets.txt','w')

piechart = pygal.Pie()
for line in i.read().splitlines():
  piechart.add(line.split()[0],int(line.split()[1]))

barchart = pygal.Bar()
for line in i.read().splitlines():
  barchart.add(line.split()[0],int(line.split()[1]))
  
piechart.render()
barchart.render()