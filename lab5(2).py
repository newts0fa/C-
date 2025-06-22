import osmnx as ox
from shapely.geometry import Polygon

# Получаем полигон Стокгольма
gdf = ox.geocode_to_gdf('Stockholm, Sweden')
polygon = gdf.geometry.iloc[0]

# Скачиваем граф
G = ox.graph_from_place('Stockholm, Sweden', network_type='drive')
ox.save_graphml(G, 'stockholm_road_network.graphml')

G = ox.graph_from_point((59.3293, 18.0686), dist=5000, network_type='drive')

# Вариант 2: По адресу
G = ox.graph_from_address("Stockholm, Sweden", dist=5000, network_type='drive')

ox.save_graphml(G, 'stockholm_road_network.graphml')
