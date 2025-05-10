# Floyd-Warshall Path Finder

A Python console application that demonstrates the Floyd-Warshall algorithm for finding the shortest paths between all pairs of vertices in a directed weighted graph.

This project allows users to:
- Generate a random graph as an adjacency matrix
- View the matrix in a readable format
- Query the shortest path between any two vertices
- Display the route and total cost of the path

---

## 🔧 Features

- Random graph generation with weights and "infinite" distances (unreachable paths)
- Floyd-Warshall implementation with intermediate vertex tracking
- Recursive shortest path reconstruction
- User-friendly text interface with menus
- Handles edge cases like no direct/indirect paths

---

## 🧠 Algorithm Used

This project implements the **Floyd-Warshall algorithm**, which is a dynamic programming method for solving the All-Pairs Shortest Paths (APSP) problem in weighted graphs.

- **Time Complexity:** O(n³)
- **Handles:** Positive weights and unreachable paths (using `float('inf')`)
- **Intermediate Path Tracking:** Uses a matrix `P[i][j]` to store intermediate vertices for path reconstruction

---

## ▶️ How to Run

Make sure you have **Python 3.x** and **NumPy** installed.

1. Clone or download the project.
2. Run the main file:

```bash
python pathfinder.py
