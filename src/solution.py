import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def solve_network_optimization():
    try:
        data = pd.read_csv('../data/network_data.csv')
    except FileNotFoundError:
        data = pd.read_csv('data/network_data.csv')

    G = nx.DiGraph()

    for index, row in data.iterrows():
        G.add_edge(row['source'], row['target'], weight=row['weight'], label=row['description'])

    source_node = 'Employee_PC'
    target_node = 'Domain_Controller'
    
    shortest_path = nx.shortest_path(G, source=source_node, target=target_node, weight='weight')
    path_length = nx.shortest_path_length(G, source=source_node, target=target_node, weight='weight')

    print("--- Analysis Results ---")
    print(f"Identified Critical Attack Path: {' -> '.join(shortest_path)}")
    print(f"Total Risk Score (Cost): {path_length}")

    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)
    
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    path_edges = list(zip(shortest_path, shortest_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

    plt.title("Cybersecurity Attack Path Analysis (Critical Route Highlighted in Red)")
    plt.savefig('../results/network_visualization.png')
    plt.show()

    with open('../results/solution_output.txt', 'w', encoding='utf-8') as f:
        f.write(f"Analyzed Starting Point: {source_node}\n")
        f.write(f"Target Asset: {target_node}\n")
        f.write(f"Critical Route: {' -> '.join(shortest_path)}\n")
        f.write(f"Total Path Cost: {path_length}\n")

if __name__ == "__main__":
    solve_network_optimization()
