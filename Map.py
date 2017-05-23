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

def main():
	choiche = input("0 --> Display Norwegian counties map \n1 --> Display current input\n\n")
 	# Downloaded from http://biogeo.ucdavis.edu/data/gadm2.8/shp/NOR_adm_shp.zip
	fname = 'Datasets/NOR/NOR_adm1.shp'
	NOR_shapes = list(shpreader.Reader(fname).geometries())
	plt.figure()
	ax = plt.axes(projection=ccrs.Robinson())
	ax.coastlines(resolution='10m')
	ax.set_extent([4, 32, 57, 72], ccrs.Robinson())	

	# Rendering the sea
	#ax.stock_img()

	if(choiche==0):
		norway = add_geom(ax, NOR_shapes, "Norway", "gray")

		finnmark = add_geom(ax, NOR_shapes[4], "Finnmark", "red")
		troms = add_geom(ax, NOR_shapes[16], "Troms", "springgreen")
		nordland = add_geom(ax, NOR_shapes[9], "Nordland", "purple")
		nord_trondelag = add_geom(ax, NOR_shapes[8], "Nord Trondelag", "orange")
		sor_trondelag = add_geom(ax, NOR_shapes[13], "Sor Trondelag", "brown")
		more_og_romsdal = add_geom(ax, NOR_shapes[7], "More og Romsdal", "yellow")
		sogn_og_fjordane = add_geom(ax, NOR_shapes[14], "Sogn og Fjordane", "aqua")
		hordaland = add_geom(ax, NOR_shapes[6], "Hordaland", "blue")
		rogaland_og_agder = add_geom(ax, NOR_shapes[2], "Rogaland og Agder", "darkgreen")
		rogaland_og_agder = add_geom(ax, NOR_shapes[12], "Rogaland og Agder", "darkgreen")
		rogaland_og_agder = add_geom(ax, NOR_shapes[17], "Rogaland og Agder", "darkgreen")

		plt.title('Norway - Counties involved in Aquaculture business', fontsize=35)

	
	else:
		# Decide the range of colors of the colorsMap
		colorsMap='bwr'
		dataInput = sys.argv[1]
		inputSeries = pd.read_csv("Datasets/countiesAverages.csv")
		# Data input for each region
		inputValues = [inputSeries[dataInput][0], inputSeries[dataInput][1], inputSeries[dataInput][2], inputSeries[dataInput][3],
				inputSeries[dataInput][4], inputSeries[dataInput][5], inputSeries[dataInput][6], inputSeries[dataInput][7], inputSeries[dataInput][8]]

		cm = plt.get_cmap(colorsMap)
		mininputValues = min(inputValues)
		cNorm = matplotlib.colors.Normalize(vmin=mininputValues, vmax=max(inputValues))
		scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)	
		colors = scalarMap.to_rgba(inputValues)	

		# Colorbar displayed like a legend for the colors
		scalarMap.set_array(inputValues)
		plt.colorbar(scalarMap,label='Input Value')

		norway = add_geom(ax, NOR_shapes, "Norway", "gray")

		finnmark = add_geom(ax, NOR_shapes[4], "Finnmark", colors[0])
		troms = add_geom(ax, NOR_shapes[16], "Troms", colors[1])
		nordland = add_geom(ax, NOR_shapes[9], "Nordland", colors[2])
		nord_trondelag = add_geom(ax, NOR_shapes[8], "Nord Trondelag", colors[3])
		sor_trondelag = add_geom(ax, NOR_shapes[13], "Sor Trondelag", colors[4])
		more_og_romsdal = add_geom(ax, NOR_shapes[7], "More og Romsdal", colors[5])
		sogn_og_fjordane = add_geom(ax, NOR_shapes[14], "Sogn og Fjordane", colors[6])
		hordaland = add_geom(ax, NOR_shapes[6], "Hordaland", colors[7])
		rogaland_og_agder = add_geom(ax, NOR_shapes[2], "Rogaland og Agder", colors[8])
		rogaland_og_agder = add_geom(ax, NOR_shapes[12], "Rogaland og Agder", colors[8])
		rogaland_og_agder = add_geom(ax, NOR_shapes[17], "Rogaland og Agder", colors[8])

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
		labels, loc='lower right', fancybox=True)

	manager = plt.get_current_fig_manager()
	manager.resize(*manager.window.maxsize())

	plt.show()


if __name__ == '__main__':
   main()

   
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