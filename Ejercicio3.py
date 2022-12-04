import matplotlib.pyplot as plt
import networkx as nx

def camino_mas_corto(G, origen, destino):
    return nx.shortest_path(G, origen, destino)

G = nx.Graph()

G.add_node('King\'s Cross', tipo='estacion')
G.add_node('Waterloo', tipo='estacion')
G.add_node('Victoria Train Station', tipo='estacion')
G.add_node('Liverpool Street Station', tipo='estacion')
G.add_node('St. Pancras', tipo='estacion')
G.add_node('1', tipo='desvio')
G.add_node('2', tipo='desvio')
G.add_node('3', tipo='desvio')
G.add_node('4', tipo='desvio')
G.add_node('5', tipo='desvio')
G.add_node('6', tipo='desvio')

G.add_edge('King\'s Cross', '1')
G.add_edge('1', '2')
G.add_edge('2', '3')
G.add_edge('3', '4')
G.add_edge('4', '5')
G.add_edge('5', '6')
G.add_edge('6', 'Waterloo')
G.add_edge('Victoria Train Station', '1')
G.add_edge('1', 'Liverpool Street Station')
G.add_edge('St. Pancras', '2')

camino_mas_corto_king_waterloo = camino_mas_corto(G, 'King\'s Cross', 'Waterloo')
camino_mas_corto_victoria_liverpool = camino_mas_corto(G, 'Victoria Train Station', 'Liverpool Street Station')
camino_mas_corto_st_king = camino_mas_corto(G, 'St. Pancras', 'King\'s Cross')

print('Camino mas corto desde King\'s Cross hasta Waterloo: ', camino_mas_corto_king_waterloo)
print('Camino mas corto desde Victoria Train Station hasta Liverpool Street Station: ', camino_mas_corto_victoria_liverpool)
print('Camino mas corto desde St. Pancras hasta King\'s Cross: ', camino_mas_corto_st_king)

nx.draw(G, with_labels=True)
plt.show()

nx.draw(G, with_labels=True)
nx.draw_networkx_nodes(G, pos=nx.spring_layout(G), nodelist=camino_mas_corto_king_waterloo, node_color='r')
nx.draw_networkx_nodes(G, pos=nx.spring_layout(G), nodelist=camino_mas_corto_victoria_liverpool, node_color='r')
nx.draw_networkx_nodes(G, pos=nx.spring_layout(G), nodelist=camino_mas_corto_st_king, node_color='r')
plt.show()

nx.draw(G, with_labels=True)
nx.draw_networkx_nodes(G, pos=nx.spring_layout(G), nodelist=camino_mas_corto_king_waterloo, node_color='r')
nx.draw_networkx_nodes(G, pos=nx.spring_layout(G), nodelist=camino_mas_corto_victoria_liverpool, node_color='r')
nx.draw_networkx_nodes(G, pos=nx.spring_layout(G), nodelist=camino_mas_corto_st_king, node_color='r')

plt.show()

nx.draw(G, with_labels=True)
nx.draw_networkx_nodes(G, pos=nx.spring_layout(G), nodelist=camino_mas_corto_king_waterloo, node_color='r')
nx.draw_networkx_nodes(G, pos=nx.spring_layout(G), nodelist=camino_mas_corto_victoria_liverpool, node_color='r')
nx.draw_networkx_nodes(G, pos=nx.spring_layout(G), nodelist=camino_mas_corto_st_king, node_color='r')
nx.draw_networkx_edges(G, pos=nx.spring_layout(G), edgelist=camino_mas_corto_king_waterloo, edge_color='r')
nx.draw_networkx_edges(G, pos=nx.spring_layout(G), edgelist=camino_mas_corto_victoria_liverpool, edge_color='r')
nx.draw_networkx_edges(G, pos=nx.spring_layout(G), edgelist=camino_mas_corto_st_king, edge_color='r')

plt.show()