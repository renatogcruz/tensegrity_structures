import rhinoscriptsyntax as rs
import Rhino as rh
import math

#setup array to maintain vertices and circle or polygon variables for angular tracking
#increment around the sides of the circles or polygon
pointList = []
curAngle = 0
delAngle = 360/numberSides

print('Tensegrity simple')

# while loop moves around the perimeter of the circle and determines
while (curAngle <= 360):
    x = centerPt.X + math.cos(math.radians(curAngle)) * radius
    y = centerPt.Y + math.sin(math.radians(curAngle)) * radius
    z = centerPt.Z
    pt = rh.Geometry.Point3d(x, y, z)
    pt2 = rh.Geometry.Point3d(x, y, altura) 
    curAngle += delAngle
    pointList.append(pt)
    pointList.append(pt2)

a = pointList
print(a)

# create the bars
bar1 = rs.AddLine(pointList[0], pointList[9])
bar2 = rs.AddLine(pointList[2], pointList[11])
bar3 = rs.AddLine(pointList[4], pointList[1])
bar4 = rs.AddLine(pointList[6], pointList[3])
bar5 = rs.AddLine(pointList[8], pointList[5])
bar6 = rs.AddLine(pointList[10], pointList[7])



# create the interstitial tendons
interstitials = []
numPoint = (len(pointList) - 2)
cont = 0

while cont < numPoint:
    interstitial = rs.AddLine(pointList[cont], pointList[cont + 3])
    interstitials.append(interstitial )
    cont += 2

# cria linhas verticais
inferior = polyline = rs.AddPolyline(pointList[:13:2])
superior = polyline = rs.AddPolyline(pointList[1:14:2])

#print(pointList)
a = interstitials
b = [bar1, bar2, bar3, bar4, bar5, bar6]
c = pointList
d = [superior, inferior]