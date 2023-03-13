import cartopy.crs as ccrs
import cartopy.feature as cf
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D

# Read data from files
airports = pd.read_csv('airports.dat')
flights20 = pd.read_csv('otselennud20.csv', sep=';')
flights23 = pd.read_csv('otselennud23.csv', sep=';')

# Merge 2020 and 2023 flights
merged_flights20 = pd.merge(flights20, airports, on='IATA')
merged_flights23 = pd.merge(flights23, airports, on='IATA')

# Set the size and projection of the map
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Miller())

# Set the extent of the map and add an underlay image to the map
ax.set_extent([-20, 45, 26, 69])
ax.stock_img()

# Add coastlines and borders
ax.add_feature(cf.COASTLINE, lw=0.5)
ax.add_feature(cf.BORDERS, lw=0.5)

# Set Tallinn's location on map
tln_latitude = 59.41329956049999
tln_longitude = 24.8327999115

# Iterate through 2020 year's flights and draw lines
for indx, row in merged_flights20.iterrows():
    plt.plot([tln_longitude, row['Longitude']], [tln_latitude, row['Latitude']],
             color='red', transform=ccrs.Geodetic(), marker='o', linewidth=1)
    plt.text(row['Longitude'], row['Latitude'], row['IATA'],
             horizontalalignment='right',
             transform=ccrs.Geodetic(), fontsize=8)

# Iterate through 2023 year's flights and draw lines
for indx, row in merged_flights23.iterrows():
    plt.plot([tln_longitude, row['Longitude']], [tln_latitude, row['Latitude']],
             color='green', transform=ccrs.Geodetic(), marker='o', linewidth=0.6)
    plt.text(row['Longitude'], row['Latitude'], row['IATA'],
             horizontalalignment='right',
             transform=ccrs.Geodetic(), fontsize=8)

# Set the title of map
plt.title("Tallinna Lennujaama lennud 2020 ja 2023\nAutor: Danyil Kurbatov")


# Add the legend
plt.legend([Line2D([], [], color='red', markersize=20), Line2D([], [], color='green', markersize=20)],
           ['2020', '2023'], loc="upper left", framealpha=1)

# Save an image as map.png
plt.savefig("map.png")

# Show an image
plt.show()
