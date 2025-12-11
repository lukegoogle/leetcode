## 🐍 LeetCode Journey: VS Code Workspace & Notebook Solutions

This repository features my comprehensive solutions to LeetCode problems, organized into focused Jupyter Notebooks for detailed analysis. The entire structure is optimized for an efficient workflow within **Visual Studio Code (VS Code)**, leveraging its native support for Python and Jupyter files.

-----

### 📂 Repository Structure

All solutions are grouped into sequential notebooks, with each file covering **10 consecutive problems**. The files are kept in the root directory for easy access within the VS Code explorer.

| File Name | Description | Focus |
| :--- | :--- | :--- |
| `leetcode1to10.ipynb` | Detailed solutions for LeetCode Problems 1 through 10. | Arrays, Hashing, Two Pointers |
| `leetcode11to20.ipynb` | Detailed solutions for LeetCode Problems 11 through 20. | Linked Lists, Binary Search |
| `leetcode21to30.ipynb` | Detailed solutions for LeetCode Problems 21 through 30, and so on. | Stacks, Queues, String Manipulation |
| `README.md` | This file. | |

### 💡 Notebook Content & VS Code Workflow

Each notebook adheres to a strict format designed for learning and rapid review, best viewed using the **Jupyter Extension** within VS Code:

1.  **Problem Statement:** The original problem description.
2.  **Brute-Force Analysis:** An implementation of the naive solution, including its $O(N^2)$ or worse complexity analysis.
3.  **Optimal Algorithm Explanation:** A detailed explanation of the efficient technique (e.g., Hash Maps, Kadane's Algorithm, BFS/DFS).
4.  **Code Implementation:** The final, clean, $O(N)$ or optimal complexity solution in Python.
5.  **Complexity Breakdown:** Clear sections for **Time ($O$)** and **Space ($\Omega$)** complexity.
6.  **Inline Testing:** Cells demonstrating input and output, allowing for immediate execution and validation within the VS Code notebook viewer.

### 🛠️ Prerequisites and Setup

To run and interact with the notebooks within VS Code, you need the following:

1.  **Visual Studio Code** installed.
2.  **Python 3.x** installed and configured in your system path.
3.  **VS Code Extensions:**
      * **Python Extension** (Microsoft)
      * **Jupyter Extension** (Microsoft)

### 🚀 Getting Started (Optimized for VS Code)

1.  **Clone the Repository:**
    ```bash
    git clone [Your Repository URL]
    ```
2.  **Open the Folder in VS Code:**
      * Launch VS Code.
      * Go to `File` \> `Open Folder...` and select the cloned repository directory.
3.  **Install Dependencies:**
      * Open the integrated Terminal (\`Ctrl + \`\`).
      * Run the recommended installation command:
        ```bash
        pip install jupyter pandas numpy
        ```
4.  **Explore Solutions:**
      * Click on any `.ipynb` file in the VS Code Explorer (e.g., `leetcode1to10.ipynb`).
      * VS Code will open the notebook viewer, allowing you to read the explanations and execute the code cells directly.

-----

### ⭐ Key Algorithmic Concepts Covered

The notebooks are designed to systematically cover core computer science topics:

| Concept Block | Example Notebooks | Focus Techniques |
| :--- | :--- | :--- |
| **Foundations** | 1-20 | Arrays, Hash Maps, Two Pointers, Linked Lists |
| **Advanced Data Structures** | 21-40 | Stacks, Queues, Priority Queues (Heaps), Trees (BSTs) |
| **Optimization** | 41-60 | Dynamic Programming (DP), Greedy Algorithms |
| **Graphs** | 61+ | BFS, DFS, Topological Sort, Union-Find |

### 🤝 Feedback and Contributions

While this is primarily a personal learning repository, feedback on the code and explanations is welcome. Please open an issue if you find a more optimal solution or encounter any issues when viewing the notebooks in VS Code.