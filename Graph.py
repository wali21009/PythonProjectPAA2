# Muhammad Waliyuddin
# F55121009
import networkx as nx
import time

# Fungsi untuk menghitung shortest path menggunakan algoritma TSP
def tsp_shortest_path(graph, start_node):
    shortest_path = nx.approximation.traveling_salesman_problem(graph, weight='weight', cycle=True)
    shortest_distance = nx.approximation.traveling_salesman_problem(graph, weight='weight')
    return shortest_path, shortest_distance

# Fungsi untuk menghitung shortest path menggunakan algoritma Dijkstra
def dijkstra_shortest_path(graph, start_node):
    shortest_path = nx.shortest_path(graph, source=start_node, weight='weight')
    shortest_distance = nx.shortest_path_length(graph, source=start_node, weight='weight')
    return shortest_path, shortest_distance

# Fungsi untuk menampilkan hasil setiap iterasi
def display_iterations(iterations):
    print("Iterasi:")
    for i, iteration in enumerate(iterations, 1):
        print(f"Iterasi {i}: {iteration}")

# Fungsi untuk menampilkan waktu komputasi
def display_computation_time(time):
    print("Waktu Komputasi: %.6f detik" % time)

# Fungsi untuk menampilkan hasil akhir
def display_shortest_path(path, distance):
    print("Shortest Path:")
    print(path)
    print("Shortest Distance:", distance)

# Fungsi untuk melakukan analisis algoritma
def analyze_algorithm(graph, start_node, algorithm):
    if algorithm == 'TSP':
        print("Travelling Salesman Problem (TSP):")
        start_time = time.time()
        shortest_path, shortest_distance = tsp_shortest_path(graph, start_node)
        end_time = time.time()
        time_taken = end_time - start_time
        display_iterations(shortest_path)
        display_computation_time(time_taken)
        display_shortest_path(shortest_path, shortest_distance)
        print()

    elif algorithm == 'Dijkstra':
        print("Dijkstra Algorithm:")
        start_time = time.time()
        shortest_path, shortest_distance = dijkstra_shortest_path(graph, start_node)
        end_time = time.time()
        time_taken = end_time - start_time
        display_iterations(shortest_path)
        display_computation_time(time_taken)
        display_shortest_path(shortest_path, shortest_distance)
        print()
    else:
        print("Algoritma yang Anda pilih tidak valid.")

# Main program
if __name__ == '__main__':
    # Membangun graph
    graph = nx.Graph()

    edges = [
        ('a', 'b', {'weight': 12}),
        ('a', 'c', {'weight': 10}),
        ('a', 'g', {'weight': 12}),
        ('b', 'c', {'weight': 8}),
        ('b', 'd', {'weight': 12}),
        ('c', 'd', {'weight': 11}),
        ('c', 'e', {'weight': 3}),
        ('c', 'g', {'weight': 9}),
        ('g', 'e', {'weight': 7}),
        ('g', 'f', {'weight': 9}),
        ('d', 'e', {'weight': 11}),
        ('d', 'f', {'weight': 10}),
        ('e', 'f', {'weight': 6})
    ]

    graph.add_edges_from(edges)

    print()

    algorithm = input("Pilih algoritma (TSP atau Dijkstra) -Ketik TSP atau Dijkstra- : ")
    start_node = input("Pilih node awal: ")

    analyze_algorithm(graph, start_node, algorithm)
