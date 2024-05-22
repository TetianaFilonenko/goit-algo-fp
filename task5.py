import networkx as nx
import matplotlib.pyplot as plt


def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next_node in set(graph.neighbors(start)) - set(path):
        yield from dfs_paths(graph, next_node, goal, path + [next_node])


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


# Create an empty graph
G = nx.Graph()

# Add nodes (people)
people = ["Олег", "Марія", "Андрій", "Наталія", "Іван", "Оксана"]
G.add_nodes_from(people)

# Add edges (friendships without weights)
friendships = [
    ("Олег", "Марія"),
    ("Олег", "Андрій"),
    ("Олег", "Наталія"),
    ("Марія", "Наталія"),
    ("Наталія", "Іван"),
    ("Іван", "Оксана"),
    ("Марія", "Оксана"),
    ("Андрій", "Оксана"),
]
G.add_edges_from(friendships)

# Find paths from Олег to Іван
dfs_result = list(dfs_paths(G, "Олег", "Іван"))[0]
bfs_result = list(bfs_paths(G, "Олег", "Іван"))[0]

# Visualization of the graph
pos = nx.spring_layout(G)

fig, ax = plt.subplots(1, 2, figsize=(15, 5))  # Create a figure with two subplots


# Helper function to create a color gradient
def create_color_gradient(n):
    return [
        (0.8 - 0.8 * (i / (n - 1)), 0.8 - 0.8 * (i / (n - 1)), 1.0) for i in range(n)
    ]


# Subplot 1: DFS path visualization
dfs_colors = create_color_gradient(len(dfs_result))
node_colors_dfs = {node: dfs_colors[i] for i, node in enumerate(dfs_result)}

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=[node_colors_dfs.get(node, "lightblue") for node in G.nodes()],
    edge_color="gray",
    width=2,
    node_size=2000,
    ax=ax[0],
)
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=[(dfs_result[i], dfs_result[i + 1]) for i in range(len(dfs_result) - 1)],
    width=3,
    edge_color="red",
    ax=ax[0],
)
ax[0].set_title("Шлях DFS від Олега до Івана")

# Subplot 2: BFS path visualization
bfs_colors = create_color_gradient(len(bfs_result))
node_colors_bfs = {node: bfs_colors[i] for i, node in enumerate(bfs_result)}

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=[node_colors_bfs.get(node, "lightblue") for node in G.nodes()],
    node_size=2000,
    edge_color="gray",
    width=2,
    ax=ax[1],
)
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=[(bfs_result[i], bfs_result[i + 1]) for i in range(len(bfs_result) - 1)],
    width=3,
    edge_color="blue",
    ax=ax[1],
)
ax[1].set_title("Шлях BFS від Олега до Івана")

plt.tight_layout()
plt.show()
