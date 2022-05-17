import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from geopy import distance
import geopandas as gpd
from shapely import wkt

archivo = pd.read_csv('calles_de_medellin_con_acoso.csv', delimiter=";")
print(archivo.describe())    #saca datos generales, como el acoso promedio

#Load area
area = pd.read_csv('poligono_de_medellin.csv',sep=';')
area['geometry'] = area['geometry'].apply(wkt.loads)
area = gpd.GeoDataFrame(area)

#Load streets
edges = pd.read_csv('calles_de_medellin_con_acoso.csv',sep=';')
edges['geometry'] = edges['geometry'].apply(wkt.loads)
edges = gpd.GeoDataFrame(edges)

#se crea el grafo leyendo cada una de las columnas y filas del archivo, para almacenarlas
grafo = nx.DiGraph()
for row in archivo.iterrows():
    grafo.add_edge(row[1]["origin"],
                      row[1]["destination"],
                      longitud=row[1]["length"],
                      risk=row[1]["harassmentRisk"])

geocoder=Nominatim(user_agent="i know python")
location1= input("Escriba el lugar de inicio ")
location2= input("Escriba el destino")
coordinates1=geocoder.geocode(location1)
coordinates2=geocoder.geocode(location2)
lat1,long1=(coordinates1.latitude), (coordinates1.longitude)
lat2,long2=(coordinates2.latitude),(coordinates2.longitude)
place1=(lat1, long1)
place2=(lat2, long2)
print(distance.distance(place1,place2))

#función que permite obtener el camino más corto
def obtenercaminocorto(grafo, source, target, weight="length"):
    caminocorto = nx.astar_path(grafo, source=source, target=target, weight= "length")
    #nx.draw(caminocorto, node_color="lightblue", font_size=3, width=0.1, with_labels=True, node_size=100)

    listacaminocortoorigen = [] #lista con los caminos que manda el grafo de astar
    for i in range(len(caminocorto) -2):
        listacaminocortoorigen.append(caminocorto[i])

    listacaminocortodestinos = []
    for i in range(1, len(caminocorto) -1):
        listacaminocortodestinos.append(caminocorto[i])

    fig,ax = plt.subplots(figsize = (30,18))

    area.plot(ax=ax, facecolor= 'lightcyan')
    edges.plot(ax=ax, linewidth=1, edgecolor= 'black')
    longitud = 0
    for i in range(len(listacaminocortoorigen)):
        distancia = edges[(edges['origin'] == listacaminocortoorigen[i]) & (edges['destination'] == listacaminocortodestinos[i])]
        distancia.plot(ax = ax, linewidth=4, edgecolor= 'mediumvioletred')
        #longitud += distancia['length'].values
    '''
    longitud = 0
    arreglolongitud = []
    for i in range(len(listacaminocortoorigen)- 1):
        arreglolongitud.append(edges[(edges['length'])])
    b = 0
    for i in range(len(arreglolongitud)):
        b = b + int(arreglolongitud[i])
    print(b)
    '''
    print("la longitud de la ruta es: ")
    print(int(longitud))
    plt.tight_layout()
    plt.show()

obtenercaminocorto(grafo, source='(-75.5778046, 6.2029412)', target='(-75.6101004, 6.2312125)', weight="length")


def obtenercaminosinacoso(grafo, source, target, weight= "harassmentRisk"):
    caminomenosacoso = nx.astar_path(grafo, source=source, target=target, weight="harassmentRisk")
    #nx.draw_spectral(grafootro, node_color="lightgreen", font_size=5, width=0.1, with_labels=True, node_size=500)

    listacaminoacosoorigen = [] #lista con los caminos que manda el grafo de astar
    for i in range(len(caminomenosacoso) -2):
        listacaminoacosoorigen.append(caminomenosacoso[i])

    listacaminoacosodestinos = []
    for i in range(1, len(caminomenosacoso) -1):
        listacaminoacosodestinos.append(caminomenosacoso[i])

    fig,ax = plt.subplots(figsize = (30,18))

    area.plot(ax=ax, facecolor='lightcyan')
    edges.plot(ax=ax, linewidth=1, edgecolor='black')

    for i in range(len(listacaminoacosoorigen)):
        distancia = edges[(edges['origin'] == listacaminoacosoorigen[i]) & (edges['destination'] == listacaminoacosodestinos[i])]
        distancia.plot(ax = ax, linewidth=4, edgecolor= 'red')

    plt.tight_layout()
    plt.show()

#obtenercaminosinacoso(grafo,source='(-75.5778046, 6.2029412)', target='(-75.6101004, 6.2312125)', weight="harassmentRisk")

