import os
import sys
import matplotlib
import pandas as pd
import cartopy.crs as ccrs
import matplotlib.cm as cmx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import cartopy.io.shapereader as shpreader

def add_geom(axes, shapeInput, labelInput, colorInput):
	axes.add_geometries(shapeInput, ccrs.Robinson(), edgecolor='black',label = labelInput, facecolor=colorInput, alpha=0.8)
	return mpatches.Rectangle((0, 0), 1, 1, facecolor=colorInput)

# Downloaded from http://biogeo.ucdavis.edu/data/gadm2.8/shp/NOR_adm_shp.zip
fname = 'Datasets/NOR/NOR_adm1.shp'
NOR_shapes = list(shpreader.Reader(fname).geometries())

# Rendering the sea
#ax.stock_img()

dataInput = sys.argv[1]
inputSeries = pd.read_csv("Datasets/countiesAverages.csv")
# Data input for each region
inputValues = [inputSeries[dataInput][0], inputSeries[dataInput][1], inputSeries[dataInput][2], inputSeries[dataInput][3],
inputSeries[dataInput][4], inputSeries[dataInput][5], inputSeries[dataInput][6], inputSeries[dataInput][7], inputSeries[dataInput][8]]

# Decide the range of col of the colMap
colMap='bwr'
cm = plt.get_cmap(colMap)
minValues = min(inputValues)
maxValues = max(inputValues)
cNorm = matplotlib.colors.Normalize(vmin=minValues, vmax=maxValues)
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)	
col = scalarMap.to_rgba(inputValues)	
# Colorbar displayed like a legend for the col
scalarMap.set_array(inputValues)
plt.colorbar(scalarMap,label='Input Value')

ax = plt.axes(projection=ccrs.Robinson())
ax.coastlines(resolution='10m')
ax.set_extent([4, 32, 57, 72], ccrs.Robinson())	

norway = add_geom(ax, NOR_shapes, "Norway", "gray")
finnmark = add_geom(ax, NOR_shapes[4], "Finnmark", col[0])
troms = add_geom(ax, NOR_shapes[16], "Troms", col[1])
nordland = add_geom(ax, NOR_shapes[9], "Nordland", col[2])
nord_trondelag = add_geom(ax, NOR_shapes[8], "Nord Trondelag", col[3])
sor_trondelag = add_geom(ax, NOR_shapes[13], "Sor Trondelag", col[4])
more_og_romsdal = add_geom(ax, NOR_shapes[7], "More og Romsdal", col[5])
sogn_og_fjordane = add_geom(ax, NOR_shapes[14], "Sogn og Fjordane", col[6])
hordaland = add_geom(ax, NOR_shapes[6], "Hordaland", col[7])
rogaland_og_agder = add_geom(ax, NOR_shapes[2], "Rogaland og Agder", col[8])
rogaland_og_agder = add_geom(ax, NOR_shapes[12], "Rogaland og Agder", col[8])
rogaland_og_agder = add_geom(ax, NOR_shapes[17], "Rogaland og Agder", col[8])

plt.title('Norway - '+sys.argv[1] , fontsize=35)

labels = [
	'Finnmark', 
	'Troms', 	
	'Nordland', 
	'Nord Trondelag', 
	'Sor Trondelag', 
	'More og Romsdal', 
	'Sogn og Fjordane', 
	'Hordaland', 	
	'Rogaland og Agder',
	'Other counties', 
	]

plt.legend([finnmark, troms, nordland, nord_trondelag, sor_trondelag, 
		more_og_romsdal, sogn_og_fjordane, hordaland, rogaland_og_agder, norway], 
		labels, loc='lower right', fancybox=True, fontsize=20)

manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

plt.show()

   
	# NOR_shapes[0] -> Ostfold
	# NOR_shapes[1] -> Akershus
	# NOR_shapes[2] -> Aust Agder
	# NOR_shapes[3] -> Buskerud
	# NOR_shapes[4] -> Finnmark
	# NOR_shapes[5] -> Hedmark
	# NOR_shapes[6] -> Hordaland
	# NOR_shapes[7] -> More og Romsdal
	# NOR_shapes[8] -> Nord Trondelag
	# NOR_shapes[9] -> Nordland
	# NOR_shapes[10] -> Oppland
	# NOR_shapes[11] -> Oslo ?
	# NOR_shapes[12] -> Rogaland
	# NOR_shapes[13] -> Sor Trondelag
	# NOR_shapes[14] -> Sogn og Fjordane
	# NOR_shapes[15] -> Telemark 
	# NOR_shapes[16] -> Troms
	# NOR_shapes[17] -> Vest Agder
	# NOR_shapes[18] -> Vestfold