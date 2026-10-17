# Algorithms Content Module for GATE 2027 CSE
# Weightage: 8-10 Marks

SUBJECT_META = {
    "id": "ALGO",
    "name": "Algorithms",
    "folder": "05_Algorithms",
    "weightage": "8 Marks",
    "topics": [
        "Asymptotic worst-case time and space complexity, Master Theorem, recurrences",
        "Searching, sorting, and hashing: Comparison vs linear sorting, hash functions, collision resolution",
        "Algorithm design techniques: Greedy algorithms, dynamic programming, divide-and-conquer",
        "Graph traversals, minimum spanning trees (Prim, Kruskal), shortest paths (Dijkstra, Bellman-Ford, Floyd-Warshall)"
    ]
}

CHAPTERS = [
    {
        "title": "Asymptotic Analysis & Recurrence Relations",
        "hinglish": "Complexity analysis me Master Theorem aur function growth rates (log n &lt; sqrt(n) &lt; n &lt; n log n &lt; n^2 &lt; 2^n &lt; n!) direct compare karne aate hain.",
        "theory": (
            "<b>1. Asymptotic Notations:</b><br/>"
            "• <b>Big-O (Upper Bound):</b> f(n) = O(g(n)) iff ∃ c &gt; 0, n0 &gt; 0 such that f(n) ≤ c * g(n) for all n ≥ n0.<br/>"
            "• <b>Big-Omega (Lower Bound):</b> f(n) = Ω(g(n)) iff ∃ c &gt; 0, n0 &gt; 0 such that f(n) ≥ c * g(n) for all n ≥ n0.<br/>"
            "• <b>Big-Theta (Tight Bound):</b> f(n) = Θ(g(n)) iff f(n) = O(g(n)) AND f(n) = Ω(g(n)).<br/>"
            "• <b>Little-o (Strict Upper Bound):</b> lim (n->∞) [f(n) / g(n)] = 0.<br/>"
            "• <b>Little-omega (Strict Lower Bound):</b> lim (n->∞) [f(n) / g(n)] = ∞.<br/><br/>"
            "<b>2. Master Theorem for Divide-and-Conquer:</b><br/>"
            "Recurrence: T(n) = a * T(n/b) + Θ(n^k * log^p(n)) where a ≥ 1, b &gt; 1, k ≥ 0, p real.<br/>"
            "• <b>Case 1:</b> If log_b(a) &gt; k => T(n) = Θ(n^(log_b(a))).<br/>"
            "• <b>Case 2:</b> If log_b(a) == k:<br/>"
            "  - If p &gt; -1 => T(n) = Θ(n^k * log^(p+1)(n)).<br/>"
            "  - If p == -1 => T(n) = Θ(n^k * log(log n)).<br/>"
            "  - If p &lt; -1 => T(n) = Θ(n^k).<br/>"
            "• <b>Case 3:</b> If log_b(a) &lt; k:<br/>"
            "  - If p ≥ 0 => T(n) = Θ(n^k * log^p(n)).<br/>"
            "  - If p &lt; 0 => T(n) = O(n^k)."
        ),
        "callouts": [
            ("Master Theorem Gap Trap", "Master Theorem CANNOT be applied if a is not constant (e.g. T(n) = 2^n T(n/2)), if b is not constant, or if f(n) is not polynomial (e.g. T(n) = 2T(n/2) + n!). Use recursion tree in those cases!", "warn"),
            ("Asymptotic Ranking", "Standard growth hierarchy: 1 &lt; log(log n) &lt; log n &lt; (log n)^2 &lt; sqrt(n) &lt; n &lt; n log n &lt; n^2 &lt; n^3 &lt; 2^n &lt; e^n &lt; n! &lt; n^n.", "formula")
        ],
        "tables": []
    },
    {
        "title": "Sorting, Searching & Hashing",
        "hinglish": "Sorting algorithms me stability, in-place property, aur worst-case vs average-case complexities standard tables hain jo har aspirant ko memorized honi chahiye.",
        "theory": (
            "<b>1. Comparison-Based Sorting Lower Bound:</b><br/>"
            "• Any comparison-based sorting algorithm requires at least Ω(n log n) comparisons in the worst case (derived from decision tree of height ⌈log2(n!)⌉ ≥ n log2(n) - n log2(e)).<br/><br/>"
            "<b>2. Sorting Algorithms Summary:</b><br/>"
            "• <b>Merge Sort:</b> Divide-and-Conquer. Worst/Avg/Best = Θ(n log n). Stable. Not in-place (requires O(n) auxiliary space).<br/>"
            "• <b>Quick Sort:</b> Partition based. Avg/Best = Θ(n log n), Worst = Θ(n^2) (when array already sorted with first/last element as pivot). Unstable. In-place (O(log n) stack space).<br/>"
            "• <b>Heap Sort:</b> Heap based. Worst/Avg/Best = Θ(n log n). Unstable. In-place O(1) auxiliary space.<br/>"
            "• <b>Counting Sort:</b> Non-comparison. Time = O(n + k), Space = O(k). Stable. Linear time when range k = O(n).<br/><br/>"
            "<b>3. Hashing & Collision Resolution:</b><br/>"
            "• <b>Chaining:</b> Linked lists at each bucket. Successful search = 1 + α/2, Unsuccessful = 1 + α (where load factor α = n/m).<br/>"
            "• <b>Open Addressing (No pointers):</b> All elements stored directly in hash table (α ≤ 1).<br/>"
            "  - Linear Probing: h(k, i) = (h'(k) + i) mod m. Suffers from Primary Clustering.<br/>"
            "  - Quadratic Probing: h(k, i) = (h'(k) + c1*i + c2*i^2) mod m. Suffers from Secondary Clustering.<br/>"
            "  - Double Hashing: h(k, i) = (h1(k) + i * h2(k)) mod m. Eliminates clustering (h2(k) must be relatively prime to m)."
        ),
        "callouts": [
            ("QuickSort Worst Case Avoidance", "Randomized QuickSort (or picking median-of-three pivot) yields expected time O(n log n) on all inputs, eliminating the deterministic sorted array worst-case trap!", "tip"),
            ("Chaining vs Open Addressing", "In Open Addressing, load factor α CANNOT exceed 1. In Chaining, load factor α can be any positive value &gt; 1.", "formula")
        ],
        "tables": [
            {
                "header": ["Algorithm", "Best Time", "Average Time", "Worst Time", "Aux Space", "Stable?"],
                "rows": [
                    ["Merge Sort", "O(n log n)", "O(n log n)", "O(n log n)", "O(n)", "Yes"],
                    ["Quick Sort", "O(n log n)", "O(n log n)", "O(n^2)", "O(log n)", "No"],
                    ["Heap Sort", "O(n log n)", "O(n log n)", "O(n log n)", "O(1)", "No"],
                    ["Insertion Sort", "O(n)", "O(n^2)", "O(n^2)", "O(1)", "Yes"],
                    ["Counting Sort", "O(n+k)", "O(n+k)", "O(n+k)", "O(k)", "Yes"]
                ]
            }
        ]
    },
    {
        "title": "Design Techniques - Greedy & Dynamic Programming",
        "hinglish": "Greedy me locally optimal choice globally optimal result deti hai (Matroid property). DP me Overlapping Subproblems aur Optimal Substructure zaroori hote hain.",
        "theory": (
            "<b>1. Greedy Strategy:</b><br/>"
            "• <b>Fractional Knapsack:</b> Greedy by value-to-weight ratio (v_i / w_i). Solved in O(n log n). Works because items can be split.<br/>"
            "• <b>Activity Selection:</b> Sort by finish time, greedily pick next compatible activity. O(n log n).<br/>"
            "• <b>Huffman Coding:</b> Prefix code tree built using min-heap in O(n log n). Generates optimal variable-length codes.<br/><br/>"
            "<b>2. Dynamic Programming (DP):</b><br/>"
            "• <b>0/1 Knapsack:</b> Items cannot be split. Greedy fails! DP recurrence:<br/>"
            "  dp[i][w] = max(dp[i-1][w], v_i + dp[i-1][w - w_i]) if w ≥ w_i else dp[i-1][w].<br/>"
            "  Time = O(n * W) (Pseudo-polynomial). Space = O(W).<br/>"
            "• <b>Matrix Chain Multiplication (MCM):</b> Order of multiplying A1 * A2 * ... * An.<br/>"
            "  Recurrence: m[i, j] = min_{i ≤ k &lt; j} { m[i, k] + m[k+1, j] + p_{i-1} * p_k * p_j }.<br/>"
            "  Time = O(n^3), Space = O(n^2).<br/>"
            "• <b>Longest Common Subsequence (LCS):</b><br/>"
            "  If X[i] == Y[j] => 1 + c[i-1, j-1]; else max(c[i-1, j], c[i, j-1]). Time = O(m * n)."
        ),
        "callouts": [
            ("0/1 Knapsack Greedy Failure", "Never apply greedy value-to-weight ratio to 0/1 Knapsack! It can produce arbitrarily poor results. Always use dynamic programming table.", "warn"),
            ("Huffman Optimal Path Length", "The average number of bits per character in Huffman coding equals the Weighted External Path Length of the Huffman tree divided by total frequency.", "formula")
        ],
        "tables": []
    },
    {
        "title": "Graph Algorithms - Traversals, MST & Shortest Paths",
        "hinglish": "Dijkstra negative edge weights handle nahi kar sakta! Bellman-Ford negative cycles detect karta hai aur Floyd-Warshall all-pairs shortest path O(V^3) deta hai.",
        "theory": (
            "<b>1. Traversals:</b><br/>"
            "• <b>BFS (Queue):</b> Finds shortest paths in unweighted graphs. Time = O(V + E).<br/>"
            "• <b>DFS (Stack/Recursion):</b> Classifies edges into Tree, Back (detects cycles!), Forward, and Cross edges. Time = O(V + E).<br/>"
            "• <b>Topological Sort:</b> Linear ordering of vertices in Directed Acyclic Graph (DAG). If cycle exists, topological sort is impossible! Time = O(V + E).<br/><br/>"
            "<b>2. Minimum Spanning Trees (MST):</b> Connected undirected weighted graph G.<br/>"
            "• Number of edges in MST = |V| - 1.<br/>"
            "• <b>Kruskal's Algorithm:</b> Sort edges, greedily pick smallest edge that does not form a cycle (using Disjoint Set Union - DSU with union by rank and path compression). Time = O(E log E) = O(E log V).<br/>"
            "• <b>Prim's Algorithm:</b> Grow tree from a source vertex using Min-Heap. Time = O((V + E) log V).<br/>"
            "• Cut Property: For any cut in G, the minimum weight edge crossing the cut is in every MST.<br/><br/>"
            "<b>3. Shortest Path Algorithms:</b><br/>"
            "• <b>Dijkstra's Algorithm (Single Source):</b> Works ONLY with non-negative edge weights. Time = O((V + E) log V) with binary heap, O(V^2) with array.<br/>"
            "• <b>Bellman-Ford Algorithm (Single Source):</b> Handles negative edge weights. Relaxes all edges |V| - 1 times. On |V|-th iteration, if relaxation is still possible, a NEGATIVE WEIGHT CYCLE exists! Time = O(V * E).<br/>"
            "• <b>Floyd-Warshall Algorithm (All Pairs):</b> Dynamic programming. d_k[i, j] = min(d_{k-1}[i, j], d_{k-1}[i, k] + d_{k-1}[k, j]). Time = O(V^3), Space = O(V^2)."
        ),
        "callouts": [
            ("Dijkstra Negative Edge Trap", "If a graph has negative edges, Dijkstra's algorithm CAN give incorrect results because it assumes that visiting a node permanently determines its shortest path!", "warn"),
            ("Unique MST Condition", "If all edge weights in a connected undirected graph are strictly DISTINCT, then the graph has a strictly UNIQUE Minimum Spanning Tree!", "tip")
        ],
        "tables": []
    }
]

PRACTICE_QUESTIONS = [
    {
        "id": "ALGO-Q01",
        "type": "NAT",
        "marks": 2,
        "text": "What is the solution to the recurrence relation T(n) = 4 T(n/2) + n^2 log n? If T(n) = Θ(n^k * log^p n), what is the value of k + p?",
        "answer": "4",
        "explanation": "Here a = 4, b = 2, f(n) = n^2 log n.<br/>log_b(a) = log_2(4) = 2.<br/>Since f(n) = n^2 log^1 n, we have log_b(a) = k = 2 and p = 1.<br/>By Case 2 of Master Theorem with p = 1 > -1:<br/>T(n) = Θ(n^k * log^(p+1) n) = Θ(n^2 * log^2 n).<br/>Here k = 2, power of log is p' = 2.<br/>Hence k + p' = 2 + 2 = 4.",
        "is_pyq": True,
        "year": 2022,
        "difficulty": "Medium"
    },
    {
        "id": "ALGO-Q02",
        "type": "MCQ",
        "marks": 2,
        "text": "An undirected graph has 8 vertices and 14 edges. The weights of the edges are 1, 2, 3, ..., 14. What is the total weight of the Minimum Spanning Tree?",
        "options": {
            "A": "28",
            "B": "29",
            "C": "30",
            "D": "Cannot be determined without graph topology"
        },
        "answer": "D",
        "explanation": "Even though edge weights are distinct, the MST depends on the topology of which edges form cycles and connect the 8 vertices. If the smallest 7 edges (weights 1 to 7) form cycles, larger edges must be chosen. Without the adjacency structure, the exact weight cannot be determined uniquely.",
        "is_pyq": True,
        "year": 2021,
        "difficulty": "GATE-Level"
    },
    {
        "id": "ALGO-Q03",
        "type": "MSQ",
        "marks": 2,
        "text": "Which of the following problems can be solved in POLYNOMIAL TIME on a directed graph G = (V, E)?",
        "options": {
            "A": "Finding topological ordering if G is a DAG",
            "B": "Determining whether G has a negative weight cycle",
            "C": "Finding the longest simple path between two vertices in general graph",
            "D": "Finding strongly connected components"
        },
        "answer": "A, B, D",
        "explanation": "A: Topological sort takes O(V + E) using DFS or Kahn's algorithm (Polynomial).<br/>B: Bellman-Ford detects negative weight cycles in O(V * E) time (Polynomial).<br/>C: Finding the longest simple path in a general graph is NP-Hard! (Not polynomial).<br/>D: Kosaraju's or Tarjan's algorithm finds SCCs in O(V + E) time (Polynomial).<br/>Hence A, B, D are polynomial.",
        "is_pyq": False,
        "year": None,
        "difficulty": "GATE-Level"
    },
    {
        "id": "ALGO-Q04",
        "type": "NAT",
        "marks": 2,
        "text": "In a 0/1 knapsack problem with capacity W = 10, there are 4 items with weights w = [2, 3, 4, 5] and values v = [3, 4, 5, 8]. What is the maximum value that can be accommodated in the knapsack?",
        "answer": "16",
        "explanation": "Possible combinations within weight ≤ 10:<br/>• Items 1, 2, 4: weight = 2 + 3 + 5 = 10. Value = 3 + 4 + 8 = 15.<br/>• Items 1, 3, 4: weight = 2 + 4 + 5 = 11 (>10 invalid).<br/>• Items 2, 3, 4: weight = 3 + 4 + 5 = 12 (>10 invalid).<br/>• Items 1, 2, 3: weight = 2 + 3 + 4 = 9. Value = 3 + 4 + 5 = 12.<br/>Wait! Check combination with Item 4 (w=5, v=8):<br/>Remaining capacity = 5. Best items from {1, 2, 3} with weight ≤ 5 are Items 1 and 2: w = 2 + 3 = 5, v = 3 + 4 = 7. Total value = 8 + 7 = 15.<br/>Can we take {3, 4}? w = 4 + 5 = 9, v = 5 + 8 = 13.<br/>Can we take {1, 2, 3}? w = 9, v = 12.<br/>Therefore, maximum value = 15.",
        "is_pyq": False,
        "year": None,
        "difficulty": "Medium"
    },
    {
        "id": "ALGO-Q05",
        "type": "MCQ",
        "marks": 1,
        "text": "What is the tightest upper bound on the number of comparisons performed during the execution of QuickSort on an array of n elements when the pivot is chosen as the median element in O(n) time?",
        "options": {
            "A": "O(n)",
            "B": "O(n log n)",
            "C": "O(n^2)",
            "D": "O(n^1.5)"
        },
        "answer": "B",
        "explanation": "If the pivot is guaranteed to be the exact median, the array is partitioned into two equal halves of size n/2 each. The recurrence becomes T(n) = 2T(n/2) + O(n), which solves by Master Theorem to strictly O(n log n) even in the worst case.",
        "is_pyq": True,
        "year": 2019,
        "difficulty": "Easy"
    }
]
