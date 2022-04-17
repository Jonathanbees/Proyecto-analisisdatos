import pandas as pd
import csv
import networkx as nx
import matplotlib.pyplot as plt
archivo = pd.read_csv('calles_de_medellin_con_acoso.csv', delimiter=";")
archivo.describe()    #saca datos generales, como el acoso promedio

#se crea el grafo leyendo cada una de las columnas y filas del archivo, para almacenarlas
grafo = nx.DiGraph()
for row in archivo.iterrows():
    grafo.add_edge(row[1]["origin"],
                      row[1]["destination"],
                      longitud=row[1]["length"],
                      risk=row[1]["harassmentRisk"])


#función que permite obtener el camino más corto
def obtenercamino(grafo, source, target, weight="length"):
    grafootro = grafo.subgraph(list(nx.astar_path(grafo, source=source, target=target, weight= "length")))
    nx.draw_spectral(grafootro, node_color="lightblue", font_size=3, width=0.1, with_labels=True, node_size=100)
    plt.show()

obtenercamino(grafo, source='(-75.5776257, 6.3071547)', target='(-75.5721946, 6.2861633)', weight="length")


def obtenercaminosinacoso(grafo, source, target, weight= "harassmentRisk"):
    grafootro = grafo.subgraph(list(nx.dijkstra_path(grafo, source=source, target=target, weight="harassmentRisk")))
    nx.draw_spectral(grafootro, node_color="lightgreen", font_size=5, width=0.1, with_labels=True, node_size=500)
    plt.show()

obtenercaminosinacoso(grafo,source='(-75.5776257, 6.3071547)', target='(-75.5721946, 6.2861633)', weight="harassmentRisk")