import geopandas
import matplotlib.pyplot as pt
import os
tme=os.getcwd()
l1=["Bangalore","Chennai","Gurgaon","Kolkata","Mumbai"]


#Function To plot Maps
def plots(x,b):
    global l1
    xt=l1[b]
	#Importing all required shapefiles
    nature= geopandas.read_file(x+"natural.shp")
    landuse= geopandas.read_file(x+"landuse.shp")
    buildings = geopandas.read_file(x+"buildings.shp")
    roads = geopandas.read_file(x+"roads.shp")
    railways= geopandas.read_file(x+"railways.shp")
    waterways= geopandas.read_file(x+"waterways.shp")

	#Plotting All the features by superimposing
    fig, ax = pt.subplots(1)
    nature.plot(ax=ax,color='green')
    landuse.plot(ax=ax,color='yellow')
    buildings.plot(ax=ax,color='brown')
    roads.plot(ax=ax,color='grey',linewidth=0.2)
    railways.plot(ax=ax,color='red',linewidth=0.4)
    waterways.plot(ax=ax,color='blue',linewidth=0.4)
    pt.title(xt)
    pt.show()
    print(xt+" Done!")


#User gets the choice to plot graph	
while True:
    print("Get a map from the following cities:\n1)Bangalore\n2)Chennai\n3)Gurgaon\n4)Kolkata\n5)Mumbai")
    a=int(input("Enter Your Choice:"))
    if a==1:
    	x=tme+"/Bangalore/"
    	plots(x,0)
    if a==2:
    	x=tme+"/Chennai/"
    	plots(x,1)
    if a==3:
    	x=tme+"/Gurgaon/"
    	plots(x,2)
    if a==4:
    	x=tme+"/Kolkata/"
    	plots(x,3)
    if a==5:
    	x=tme+"/Mumbai/"
    	plots(x,4)
    if a>5:
        print("Closing...")
        break

