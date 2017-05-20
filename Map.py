import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.offsetbox import AnchoredText
import cartopy.io.shapereader as shpreader
import shapefile
import matplotlib
import matplotlib.patches as mpatches
import matplotlib.cm as cmx

def main():
	choiche = input("0 --> Display Norwegian counties map \n1 --> Display current input\n\n")
 # Downloaded from http://biogeo.ucdavis.edu/data/gadm2.8/shp/NOR_adm_shp.zip
	fname = 'NOR/NOR_adm1.shp'
	adm1_shapes = list(shpreader.Reader(fname).geometries())
	ax = plt.axes(projection=ccrs.Robinson())
	# Rendering the sea
	#ax.stock_img()
	ax.coastlines(resolution='10m')
	# adm1_shapes[0] -> Ostfold
	# adm1_shapes[1] -> Akershus
	# adm1_shapes[2] -> Aust Agder
	# adm1_shapes[3] -> Buskerud
	# adm1_shapes[4] -> Finnmark
	# adm1_shapes[5] -> Hedmark
	# adm1_shapes[6] -> Hordaland
	# adm1_shapes[7] -> More og Romsdal
	# adm1_shapes[8] -> Nord Trondelag
	# adm1_shapes[9] -> Nordland
	# adm1_shapes[10] -> Oppland
	# adm1_shapes[11] -> Oslo ?
	# adm1_shapes[12] -> Rogaland
	# adm1_shapes[13] -> Sor Trondelag
	# adm1_shapes[14] -> Sogn og Fjordane
	# adm1_shapes[15] -> Telemark 
	# adm1_shapes[16] -> Troms
	# adm1_shapes[17] -> Vest Agder
	# adm1_shapes[18] -> Vestfold

	if(choiche==0):
		ax.add_geometries(adm1_shapes, ccrs.Robinson(),
		                  edgecolor='black',label = "Norway", facecolor='gray', alpha=0.8)

		ax.add_geometries(adm1_shapes[4], ccrs.Robinson(),
		                  edgecolor='black',  label = "Finnmark", facecolor='red', alpha=0.8)

		ax.add_geometries(adm1_shapes[6], ccrs.Robinson(),
		                  edgecolor='black',  label = "Hordaland", facecolor='blue', alpha=0.8)

		ax.add_geometries(adm1_shapes[7], ccrs.Robinson(),
		                  edgecolor='black',  label = "More og Romsdal", facecolor='yellow', alpha=0.8)

		ax.add_geometries(adm1_shapes[8], ccrs.Robinson(),
		                  edgecolor='black',  label = "Nord Trondelag", facecolor='orange', alpha=0.8)

		ax.add_geometries(adm1_shapes[9], ccrs.Robinson(),
		                  edgecolor='black',  label = "Nordland", facecolor='purple', alpha=0.8)

		ax.add_geometries(adm1_shapes[13], ccrs.Robinson(),
		                  edgecolor='black',  label = "Sor Trondelag", facecolor='brown', alpha=0.8)

		ax.add_geometries(adm1_shapes[14], ccrs.Robinson(),
		                  edgecolor='black',  label = "Sogn og Fjordane", facecolor='aqua', alpha=0.8)

		ax.add_geometries(adm1_shapes[16], ccrs.Robinson(),
		                  edgecolor='black',  label = "Troms", facecolor='springgreen', alpha=0.8)

		ax.add_geometries(adm1_shapes[2], ccrs.Robinson(),
		                  edgecolor='black',  label = "Rogaland og Agder", facecolor='darkgreen', alpha=0.8)
		ax.add_geometries(adm1_shapes[12], ccrs.Robinson(),
		                  edgecolor='black',  label = "Rogaland og Agder", facecolor='darkgreen', alpha=0.8)
		ax.add_geometries(adm1_shapes[17], ccrs.Robinson(),
		                  edgecolor='black',  label = "Rogaland og Agder", facecolor='darkgreen', alpha=0.8)
		norway = mpatches.Rectangle((0, 0), 1, 1, facecolor="gray")
		finnmark = mpatches.Rectangle((0, 0), 1, 1, facecolor="red")
		hordaland = mpatches.Rectangle((0, 0), 1, 1, facecolor="blue")
		more_og_romsdal = mpatches.Rectangle((0, 0), 1, 1, facecolor="yellow")
		nord_trondelag = mpatches.Rectangle((0, 0), 1, 1, facecolor="orange")
		nordland = mpatches.Rectangle((0, 0), 1, 1, facecolor="purple")
		sor_trondelag = mpatches.Rectangle((0, 0), 1, 1, facecolor="brown")			
		sogn_og_fjordane = mpatches.Rectangle((0, 0), 1, 1, facecolor="aqua")
		troms = mpatches.Rectangle((0, 0), 1, 1, facecolor="springgreen")
		rogaland_og_agder = mpatches.Rectangle((0, 0), 1, 1, facecolor="darkgreen")
		plt.title('Norway - Counties involved in Aquaculture business', fontsize=35)

	
	else:
		colorsMap='bwr'
		cs = [6, 6.5 , 6.7 , 8 , 5 , 6.2, 5.8, 5.5, 6.9]
		cm = plt.get_cmap(colorsMap)
		minCs = min(cs)
		cNorm = matplotlib.colors.Normalize(vmin=minCs, vmax=max(cs))
		scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)	
		colors = scalarMap.to_rgba(cs)	

		scalarMap.set_array(cs)
		plt.colorbar(scalarMap,label='Input Value')

		ax.add_geometries(adm1_shapes, ccrs.Robinson(),
		                  edgecolor='black',label = "Norway", facecolor='gray', alpha=0.8)

		ax.add_geometries(adm1_shapes[4], ccrs.Robinson(),
		                  edgecolor='black',  label = "Finnmark", facecolor=colors[0], alpha=0.8)

		ax.add_geometries(adm1_shapes[6], ccrs.Robinson(),
		                  edgecolor='black',  label = "Hordaland", facecolor=colors[1], alpha=0.8)

		ax.add_geometries(adm1_shapes[7], ccrs.Robinson(),
		                  edgecolor='black',  label = "More og Romsdal", facecolor=colors[2], alpha=0.8)

		ax.add_geometries(adm1_shapes[8], ccrs.Robinson(),
		                  edgecolor='black',  label = "Nord Trondelag", facecolor=colors[3], alpha=0.8)

		ax.add_geometries(adm1_shapes[9], ccrs.Robinson(),
		                  edgecolor='black',  label = "Nordland", facecolor=colors[4], alpha=0.8)

		ax.add_geometries(adm1_shapes[13], ccrs.Robinson(),
		                  edgecolor='black',  label = "Sor Trondelag", facecolor=colors[5], alpha=0.8)

		ax.add_geometries(adm1_shapes[14], ccrs.Robinson(),
		                  edgecolor='black',  label = "Sogn og Fjordane", facecolor=colors[6], alpha=0.8)

		ax.add_geometries(adm1_shapes[16], ccrs.Robinson(),
		                  edgecolor='black',  label = "Troms", facecolor=colors[7], alpha=0.8)

		ax.add_geometries(adm1_shapes[2], ccrs.Robinson(),
		                  edgecolor='black',  label = "Rogaland og Agder", facecolor=colors[8], alpha=0.8)
		ax.add_geometries(adm1_shapes[12], ccrs.Robinson(),
		                  edgecolor='black',  label = "Rogaland og Agder", facecolor=colors[8], alpha=0.8)
		ax.add_geometries(adm1_shapes[17], ccrs.Robinson(),
		                  edgecolor='black',  label = "Rogaland og Agder", facecolor=colors[8], alpha=0.8)
		norway = mpatches.Rectangle((0, 0), 1, 1, facecolor="gray")
		finnmark = mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[0])
		hordaland = mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[1])
		more_og_romsdal = mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[2])
		nord_trondelag = mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[3])
		nordland = mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[4])
		sor_trondelag = mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[5])			
		sogn_og_fjordane = mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[6])
		troms = mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[7])
		rogaland_og_agder = mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[8])
		plt.title('Norway - Current Input ', fontsize=35)



	ax.set_extent([4, 32, 57, 72], ccrs.Robinson())	
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
	plt.show()

if __name__ == '__main__':
   main()