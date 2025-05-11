import numpy as np

def create_random_graph(n): 
    """Create a random adjacency matrix with random values"""

    graph = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0)  # Main diagonal is always 0
            else:
                value = np.random.randint(0, 20)
                row.append(float('inf') if value == 0 else value)
        graph.append(row)
    return graph


def print_matrix_with_indices(matrix, n): 
    """Print the matrix with row and column indices in a formatted way"""

    print("\nAdjacency Matrix:")
    
    # Print & format each column with column indices
    print("\n     ", end="")
    for j in range(n):
        print("{:^8}".format(f"[{j}]"), end="")
    print("\n")
    
    # Print & format each row with row index
    for i in range(n):
        print(f"[{i}] ", end="")
        for j in range(n):
            if matrix[i][j] == float('inf'):
                print("{:^8}".format("∞"), end="")
            else:
                print("{:^8}".format(str(matrix[i][j])), end="")
        print()


def floyd_warshall(graph, n):
    """Floyd-Warshall with intermediate matrix P"""
    
    # Copy the graph into dist
    dist = []
    for i in range(n):
        dist.append(graph[i][:])  

    # Initialize P matrix with -1
    # Later, if a shorter path via vertex k is found, P[i][j] will be updated to k.
    P = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(-1)
        P.append(row)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j] # Update dist[i][j] with the new shorter distance.
                        P[i][j] = k # Record k as the intermediate vertex on the shortest path from i to j.
    return dist, P


def construct_path(P, start, end):
    """Recursive path reconstruction that returns a list"""

    if P[start][end] == -1:
        return []
    mid = P[start][end]
    return construct_path(P, start, mid) + [mid] + construct_path(P, mid, end)


def display_menu(): 
    print("\n" + "-" * 43)
    print("MENU OPTIONS:")
    print("1. Find shortest path between two vertices")
    print("2. Exit program")
    print("-" * 43)


def display_results(start, end, direct_weight, dist_matrix, P): 
    print("\n" + "-" * 40)
    print("PATH ANALYSIS RESULTS:")

    print("\n1. Direct Path:")
    if direct_weight == float('inf'):
        print("   No direct connection exists")
    else:
        print(f"   Weight: {direct_weight}")

    print("\n2. Shortest Path:")
    if dist_matrix[start][end] == float('inf'):
        print("   No path exists between these vertices")
    else:
        path = [start] + construct_path(P, start, end) + [end]
        path_str = " -> ".join(f"v{node}" for node in path)
        print(f"   Route: {path_str}")
        print(f"   Total distance: {dist_matrix[start][end]}")


def setup_graph(): 
    print("\nWelcome to Floyd-Warshall Algorithm Path Finder")
    print("------------------------------------------------")
    while True:
        try:
            n = int(input("\nEnter n for the dimension of the n x n matrix: "))
            if n > 0:
                break
            print("Error: Please enter a positive number.")
        except ValueError:
            print("Error: Please enter a valid number.")
    graph = create_random_graph(n)
    print_matrix_with_indices(graph, n)
    return graph, n


def handle_user_interaction(graph, dist_matrix, P, n): 
    while True:
        display_menu()
        try:
            choice = input("\nEnter your choice (1-2): ")

            if choice == '2':
                print("\nThank you for using Path Finder!\n")
                break

            elif choice == '1':
                print("\nEnter vertex numbers:")
                start = int(input(f"From vertex (0-{n-1}): "))
                if not (0 <= start < n):
                    print(f"Error: Please enter a number between 0 and {n-1}")
                    continue

                end = int(input(f"To vertex (0-{n-1}): "))
                if not (0 <= end < n):
                    print(f"Error: Please enter a number between 0 and {n-1}")
                    continue

                direct_weight = graph[start][end]
                display_results(start, end, direct_weight, dist_matrix, P)

            else:
                print("Error: Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Error: Please enter valid numbers.")


def main(): 
    graph, n = setup_graph()
    dist_matrix, P = floyd_warshall(graph, n)
    handle_user_interaction(graph, dist_matrix, P, n)


if __name__ == "__main__":
    main()
