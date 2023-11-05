# pip install matplotlib basemap

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def plot_world_map():
    plt.figure(figsize=(8, 6))
    m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180)
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    plt.title("World Map")
    plt.show()

if __name__ == "__main__":
    plot_world_map()
