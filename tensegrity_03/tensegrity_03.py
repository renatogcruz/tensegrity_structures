import rhinoscriptsyntax as rs
import Rhino as rh
import math

#setup array para manter vértices e variáveis de círculo ou polígono para rastrear angular
#incremento em torno dos lados dos círculos ou polígono
pointList = []
curAngle = 0
delAngle = 360/numberSides

print('Tensegrity simple')

# while loop se move ao redor do perímetro do círculo e determina
while (curAngle <= 360):
    x = centerPt.X + math.cos(math.radians(curAngle)) * radius
    y = centerPt.Y + math.sin(math.radians(curAngle)) * radius
    z = centerPt.Z
    pt = rh.Geometry.Point3d(x, y, z)
    pt2 = rh.Geometry.Point3d(x, y, altura) 
    curAngle += delAngle
    pointList.append(pt)
    pointList.append(pt2)


# criar as barras
bars = []
numPoint = (len(pointList) - 2)
cont = 0

while cont < numPoint:
    bar = rs.AddLine(pointList[cont], pointList[cont + 3])
    bars.append(bar)
    cont += 2

# cria linhas verticais
lineV = []
numPoint2 = (len(pointList) - 2)
cont2 = 0

while cont2 < numPoint2:
    lv = rs.AddLine(pointList[cont2], pointList[cont2 + 1])
    lineV.append(lv)
    cont2 += 2

# cria linhas verticais
superior = polyline = rs.AddPolyline(pointList[:7:2])
inferior = polyline = rs.AddPolyline(pointList[1:8:2])



#print(pointList)
b = bars
c = [superior,inferior]
d = lineV