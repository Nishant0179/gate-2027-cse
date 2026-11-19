# Master Textbook Module: COA, PDS & Algorithms (11 Chapters)
# Auto-generated comprehensive ChatGPT-style point-form guide

CHAPTERS_COA_PDS_ALGO = { ('ALGO', 0): { 'chapter_number': 16,
                 'exam_traps': [ { 'title': 'Master Theorem Non-Polynomial Difference Trap',
                                   'warning': "For T(n) = 2T(n/2) + n log n: here a=2, b=2, k=1, p=1. Many think it's "
                                              'Case 3 because of log n, but a = bᵏ is Case 2, giving Θ(n log² n).'}],
                 'foundations': [ { 'content': '• <b>The 5 Formal Asymptotic Notations:</b><br/>\n'
                                               '&nbsp;&nbsp;• <b>Big-O (O):</b> Asymptotic Upper Bound: <code>f(n) ≤ c '
                                               '· g(n)</code> for all n ≥ n₀.<br/>\n'
                                               '&nbsp;&nbsp;• <b>Big-Omega (Ω):</b> Asymptotic Lower Bound: <code>f(n) '
                                               '≥ c · g(n)</code> for all n ≥ n₀.<br/>\n'
                                               '&nbsp;&nbsp;• <b>Big-Theta (Θ):</b> Tight Bound: <code>c₁ · g(n) ≤ '
                                               'f(n) ≤ c₂ · g(n)</code> (Both O and Ω hold).<br/>\n'
                                               '&nbsp;&nbsp;• <b>Little-o (o):</b> Strict upper bound: <code>lim [f(n) '
                                               '/ g(n)] = 0</code> as n → ∞.<br/>\n'
                                               '&nbsp;&nbsp;• <b>Little-omega (ω):</b> Strict lower bound: <code>lim '
                                               '[f(n) / g(n)] = ∞</code> as n → ∞.<br/><br/>\n'
                                               '\n'
                                               '• <b>Master Growth Rate Hierarchy (Slowest to Fastest):</b><br/>\n'
                                               '&nbsp;&nbsp;<code>O(1) < O(log log n) < O(log n) < O(√n) < O(n) < O(n '
                                               'log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!) < O(nⁿ)</code><br/><br/>\n'
                                               '\n'
                                               '• <b>Limit Comparison Test:</b><br/>\n'
                                               '&nbsp;&nbsp;To compare f(n) and g(n), evaluate <code>L = lim [f(n) / '
                                               'g(n)]</code> as n → ∞:<br/>\n'
                                               '&nbsp;&nbsp;- If L = 0: f(n) = o(g(n)).<br/>\n'
                                               '&nbsp;&nbsp;- If 0 < L < ∞: f(n) = Θ(g(n)).<br/>\n'
                                               '&nbsp;&nbsp;- If L = ∞: f(n) = ω(g(n)).',
                                    'crucial_rule': '🎯 GOLDEN RULE FOR GATE: n^(1/log n) = 2^(log n / log n) = 2¹ = '
                                                    'Constant O(1)! (log n)! is polynomial (Θ(n^(log log n))), whereas '
                                                    '2^(log n) = n.',
                                    'number': '16.1',
                                    'title': 'Asymptotic Growth Hierarchy & Big-O Definitions'},
                                  { 'content': '• <b>Standard Form:</b> <code>T(n) = a T(n / b) + f(n)</code> (where a '
                                               '≥ 1, b > 1, f(n) = Θ(nᵏ logᵖ n)).<br/><br/>\n'
                                               '\n'
                                               '• <b>Comparison: Compare a with bᵏ:</b><br/>\n'
                                               "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 "
                                               "rounded-xl my-2 leading-relaxed overflow-x-auto'>\n"
                                               'Condition               │ Recurrence Result T(n)\n'
                                               '─────────────────────────────────────────────────────────────────\n'
                                               'a > bᵏ (log_b(a) > k)   │ T(n) = Θ(n^(log_b a))\n'
                                               'a = bᵏ (log_b(a) = k)   │ \n'
                                               '  - If p > -1           │ T(n) = Θ(nᵏ log^(p+1) n)\n'
                                               '  - If p = -1           │ T(n) = Θ(nᵏ log(log n))\n'
                                               '  - If p < -1           │ T(n) = Θ(nᵏ)\n'
                                               'a < bᵏ (log_b(a) < k)   │\n'
                                               '  - If p ≥ 0            │ T(n) = Θ(nᵏ logᵖ n)\n'
                                               '  - If p < 0            │ T(n) = Θ(nᵏ)\n'
                                               '</div>',
                                    'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Master theorem FAILS if: (1) a is not '
                                                    'constant (e.g. 2ⁿ T(n/2)), (2) b < 1, or (3) f(n) is not '
                                                    'polynomially larger/smaller (e.g. T(n) = 2T(n/2) + n/log n).',
                                    'number': '16.2',
                                    'title': 'Master Theorem for Divide & Conquer Recurrences'}],
                 'real_life_examples': [ { 'text': 'A quadtree map splits into 4 sub-tiles each time you zoom in. '
                                                   'Master theorem calculates the exact rendering time required to '
                                                   'draw millions of map tiles at any zoom level.',
                                           'title': 'Real-Life Analogy: The Zoomable Digital Map'}],
                 'title': 'Asymptotic Analysis & Recurrence Relations',
                 'worked_examples': [ { 'answer': 'T(n) = Θ(n² log² n)',
                                        'problem': 'Solve the recurrence relation: T(n) = 4 T(n / 2) + n² log n.',
                                        'steps': [ 'Step 1: Identify parameters: a = 4, b = 2, f(n) = n² log n.',
                                                   'Step 2: Compare a with bᵏ: here k = 2, p = 1. So bᵏ = 2² = 4.',
                                                   'Step 3: Since a = bᵏ (4 = 4), we are in Case 2.',
                                                   'Step 4: Check power p of log: p = 1 > -1.',
                                                   'Step 5: Apply formula: T(n) = Θ(nᵏ log^(p+1) n) = Θ(n² log² n).'],
                                        'title': 'Worked Example: Solving Recurrence using Master Theorem'}]},
  ('ALGO', 1): { 'chapter_number': 17,
                 'exam_traps': [ { 'title': 'The Selection Sort Stability Trap',
                                   'warning': 'Selection sort is NOT stable because swapping elements over long '
                                              'distances can flip the relative order of identical elements (e.g. '
                                              'sorting [4a, 4b, 1] swaps 4a with 1, placing 4a after 4b).'}],
                 'foundations': [ { 'content': '• <b>Comprehensive Comparison Table:</b><br/>\n'
                                               "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 "
                                               "rounded-xl my-2 leading-relaxed overflow-x-auto'>\n"
                                               'Algorithm      │ Best Time     │ Average Time  │ Worst Time    │ Aux '
                                               'Space │ Stable? │ In-Place?\n'
                                               '───────────────────────────────────────────────────────────────────────────────────────────────\n'
                                               'Bubble Sort    │ O(n)          │ O(n²)         │ O(n²)         │ '
                                               'O(1)      │ YES     │ YES\n'
                                               'Insertion Sort │ O(n)          │ O(n²)         │ O(n²)         │ '
                                               'O(1)      │ YES     │ YES\n'
                                               'Selection Sort │ O(n²)         │ O(n²)         │ O(n²)         │ '
                                               'O(1)      │ NO      │ YES\n'
                                               'Merge Sort     │ O(n log n)    │ O(n log n)    │ O(n log n)    │ '
                                               'O(n)      │ YES     │ NO\n'
                                               'Quick Sort     │ O(n log n)    │ O(n log n)    │ O(n²)         │ O(log '
                                               'n)  │ NO      │ YES\n'
                                               'Heap Sort      │ O(n log n)    │ O(n log n)    │ O(n log n)    │ '
                                               'O(1)      │ NO      │ YES\n'
                                               'Counting Sort  │ O(n + k)      │ O(n + k)      │ O(n + k)      │ O(n + '
                                               'k)  │ YES     │ NO\n'
                                               'Radix Sort     │ O(d(n + k))   │ O(d(n + k))   │ O(d(n + k))   │ O(n + '
                                               'k)  │ YES     │ NO\n'
                                               '</div>\n'
                                               '\n'
                                               '• <b>Comparison-Based Sorting Lower Bound:</b><br/>\n'
                                               '&nbsp;&nbsp;Any comparison-based sorting algorithm requires at least '
                                               '<b>Ω(n log n) comparisons</b> in the worst case (proven via Decision '
                                               'Tree model of height ⌈log₂(n!)⌉).',
                                    'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Insertion Sort is optimal for nearly '
                                                    'sorted arrays (runs in O(n) time). Quick Sort worst case occurs '
                                                    'when pivot is always extreme (already sorted array with '
                                                    'first/last element as pivot).',
                                    'number': '17.1',
                                    'title': 'Master Summary Table of Sorting Algorithms'},
                                  { 'content': '• <b>Collision Resolution Techniques:</b><br/>\n'
                                               '&nbsp;&nbsp;1. <b>Separate Chaining (Open Hashing):</b> Linked list at '
                                               'each hash bucket. Load factor <code>α = n / m</code> can exceed 1. '
                                               'Search time = <code>O(1 + α)</code>.<br/>\n'
                                               '&nbsp;&nbsp;2. <b>Open Addressing (Closed Hashing):</b> All elements '
                                               'stored in the hash table itself (α ≤ 1):<br/>\n'
                                               '&nbsp;&nbsp;&nbsp;&nbsp;• <b>Linear Probing:</b> <code>h(k, i) = '
                                               "(h'(k) + i) mod m</code>. Suffers from <b>Primary Clustering</b> (long "
                                               'runs of occupied slots).<br/>\n'
                                               '&nbsp;&nbsp;&nbsp;&nbsp;• <b>Quadratic Probing:</b> <code>h(k, i) = '
                                               "(h'(k) + c₁i + c₂i²) mod m</code>. Eliminates primary clustering, but "
                                               'suffers from <b>Secondary Clustering</b>.<br/>\n'
                                               '&nbsp;&nbsp;&nbsp;&nbsp;• <b>Double Hashing:</b> <code>h(k, i) = '
                                               '(h₁(k) + i · h₂(k)) mod m</code>. Eliminates all clustering! '
                                               '<code>h₂(k)</code> must be relatively prime to m.',
                                    'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In Double Hashing, h₂(k) must NEVER '
                                                    'evaluate to 0! If h₂(k) = 0, the probe sequence remains trapped '
                                                    'in an infinite loop at the initial slot.',
                                    'number': '17.2',
                                    'title': 'Hashing, Collision Resolution & Open Addressing'}],
                 'real_life_examples': [ { 'text': 'A hash table is a coat check room where your receipt number '
                                                   'directly points to your coat hanger slot. Separate chaining hangs '
                                                   'multiple coats on the same hook.',
                                           'title': 'Real-Life Analogy: Coat Rack in a Restaurant'}],
                 'title': 'Sorting, Searching & Hashing',
                 'worked_examples': [ { 'answer': 'Final Table: [Slot 0: 42, Slot 3: 101, Slot 4: 25, Slot 5: 96, Slot '
                                                  '6: 102]',
                                        'problem': 'Insert keys [25, 42, 96, 101, 102] into a hash table of size 7 '
                                                   'using hash function h(k) = k mod 7 and Linear Probing.',
                                        'steps': [ 'Step 1: Table size m = 7 (slots 0 to 6).',
                                                   'Step 2: Key 25: 25 mod 7 = 4. Slot 4 is empty ⇒ Insert 25 at Slot '
                                                   '4.',
                                                   'Step 3: Key 42: 42 mod 7 = 0. Slot 0 is empty ⇒ Insert 42 at Slot '
                                                   '0.',
                                                   'Step 4: Key 96: 96 mod 7 = 5. Slot 5 is empty ⇒ Insert 96 at Slot '
                                                   '5.',
                                                   'Step 5: Key 101: 101 mod 7 = 3. Slot 3 is empty ⇒ Insert 101 at '
                                                   'Slot 3.',
                                                   'Step 6: Key 102: 102 mod 7 = 4. Slot 4 is occupied (collision!). '
                                                   'Probe slot (4+1)%7 = 5 (occupied!). Probe slot (4+2)%7 = 6 '
                                                   '(empty!) ⇒ Insert 102 at Slot 6.'],
                                        'title': 'Worked Example: Linear Probing Hash Table Insertion'}]},
  ('ALGO', 2): { 'chapter_number': 18,
                 'exam_traps': [ { 'title': '0/1 Knapsack Greedy Trap',
                                   'warning': 'Never use the Value/Weight ratio for 0/1 Knapsack! Greedy only '
                                              'guarantees optimal solution for Fractional Knapsack, not 0/1 '
                                              'Knapsack.'}],
                 'foundations': [ { 'content': '• <b>Greedy Choice Property:</b> Makes the locally optimal choice at '
                                               'each step with the hope that this leads to a globally optimal '
                                               'solution.<br/><br/>\n'
                                               '\n'
                                               '• <b>Activity Selection Problem:</b><br/>\n'
                                               '&nbsp;&nbsp;- Maximize number of non-overlapping activities.<br/>\n'
                                               '&nbsp;&nbsp;- <b>Greedy Strategy:</b> Sort activities in ascending '
                                               'order of their <b>FINISH TIMES</b>! Always pick the next compatible '
                                               'activity that finishes earliest. Runs in <code>O(n log '
                                               'n)</code>.<br/><br/>\n'
                                               '\n'
                                               '• <b>Huffman Coding (Optimal Prefix Codes):</b><br/>\n'
                                               '&nbsp;&nbsp;1. Place all characters in a Min-Priority Queue keyed by '
                                               'frequency.<br/>\n'
                                               '&nbsp;&nbsp;2. Repeatedly extract two smallest nodes, merge them into '
                                               'a new internal node with frequency = sum, and reinsert.<br/>\n'
                                               '&nbsp;&nbsp;3. Cost of tree: <code>L_avg = ∑ (frequencyᵢ × '
                                               'depthᵢ)</code>.<br/>\n'
                                               '&nbsp;&nbsp;4. Generates a <b>Full Binary Tree</b>: exactly <code>2n - '
                                               '1</code> total nodes for n characters!',
                                    'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In Huffman Coding, if all character '
                                                    'frequencies are Fibonacci numbers (1, 1, 2, 3, 5, 8...), the '
                                                    'generated tree is completely skewed, yielding maximum variance in '
                                                    'codeword lengths!',
                                    'number': '18.1',
                                    'title': 'Greedy Method: Activity Selection & Huffman Coding'},
                                  { 'content': '• <b>When to use DP?</b> Problems with (1) <b>Overlapping '
                                               'Subproblems</b> and (2) <b>Optimal Substructure</b>.<br/><br/>\n'
                                               '\n'
                                               '• <b>Fractional Knapsack (Greedy) vs 0/1 Knapsack (DP):</b><br/>\n'
                                               '&nbsp;&nbsp;• <b>Fractional Knapsack:</b> Items can be broken. Greedy '
                                               'by <code>Value / Weight</code> ratio works! O(n log n).<br/>\n'
                                               '&nbsp;&nbsp;• <b>0/1 Knapsack:</b> Items cannot be split. Greedy '
                                               'fails! Solved via DP in <code>O(n · W)</code> time (Pseudo-polynomial; '
                                               'NP-Complete).<br/><br/>\n'
                                               '\n'
                                               '• <b>Longest Common Subsequence (LCS):</b><br/>\n'
                                               '&nbsp;&nbsp;Given strings X of length m and Y of length n:<br/>\n'
                                               '&nbsp;&nbsp;• If <code>X[i] == Y[j]</code>: <code>LCS[i, j] = 1 + '
                                               'LCS[i-1, j-1]</code>.<br/>\n'
                                               '&nbsp;&nbsp;• If <code>X[i] != Y[j]</code>: <code>LCS[i, j] = '
                                               'max(LCS[i-1, j], LCS[i, j-1])</code>.<br/>\n'
                                               '&nbsp;&nbsp;• Table size: (m + 1) × (n + 1). Time and space: <code>O(m '
                                               '· n)</code>.',
                                    'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Matrix Chain Multiplication: Multiplying '
                                                    'matrices A₁ (d₀×d₁) ... Aₙ (dₙ₋₁×dₙ) has recurrence m[i, j] = '
                                                    'min_{k} { m[i,k] + m[k+1,j] + d_{i-1} d_k d_j } where i ≤ k < j. '
                                                    'Number of ways to parenthesize n matrices = Catalan number '
                                                    'C_{n-1}.',
                                    'number': '18.2',
                                    'title': 'Dynamic Programming: 0/1 Knapsack & LCS'}],
                 'real_life_examples': [ { 'text': 'Dynamic programming avoids re-calculating routes. If the optimal '
                                                   'path from Delhi to Mumbai passes through Jaipur, the optimal route '
                                                   'from Jaipur to Mumbai is already stored and reused.',
                                           'title': 'Real-Life Analogy: GPS Route Planning'}],
                 'title': 'Design Techniques - Greedy & Dynamic Programming',
                 'worked_examples': [ { 'answer': 'Average codeword length is 1.9 bits.',
                                        'problem': 'Given characters A, B, C, D with frequencies 0.4, 0.3, 0.2, 0.1, '
                                                   'find the average codeword length of the optimal Huffman code.',
                                        'steps': [ 'Step 1: Merge lowest two frequencies: C (0.2) + D (0.1) = Node CD '
                                                   '(0.3).',
                                                   'Step 2: Remaining: A (0.4), B (0.3), CD (0.3). Merge lowest two: B '
                                                   '(0.3) + CD (0.3) = Node BCD (0.6).',
                                                   'Step 3: Merge remaining two: A (0.4) + BCD (0.6) = Root (1.0).',
                                                   'Step 4: Compute codeword lengths (depth in tree):',
                                                   '  - A is at depth 1: length = 1 bit.',
                                                   '  - B is at depth 2: length = 2 bits.',
                                                   '  - C and D are at depth 3: length = 3 bits each.',
                                                   'Step 5: Average length L = (0.4 × 1) + (0.3 × 2) + (0.2 × 3) + '
                                                   '(0.1 × 3) = 0.4 + 0.6 + 0.6 + 0.3 = 1.9 bits/char.'],
                                        'title': 'Worked Example: Huffman Code Length Calculation'}]},
  ('ALGO', 3): { 'chapter_number': 19,
                 'exam_traps': [ { 'title': 'Adding Constant to Edge Weights Trap',
                                   'warning': 'Adding a positive constant c to ALL edge weights changes the shortest '
                                              'path (paths with more edges are penalized more!), but DOES NOT change '
                                              'the Minimum Spanning Tree!'}],
                 'foundations': [ { 'content': '• <b>Traversals Comparison:</b><br/>\n'
                                               '&nbsp;&nbsp;• <b>BFS (Breadth-First Search):</b> Uses a <b>Queue</b>. '
                                               'Finds the <b>shortest path in unweighted graphs</b>! Edge types: Tree '
                                               'edges and Cross edges.<br/>\n'
                                               '&nbsp;&nbsp;• <b>DFS (Depth-First Search):</b> Uses a <b>Stack</b> (or '
                                               'recursion). Edge types: Tree, Back, Forward, Cross edges.<br/>\n'
                                               '&nbsp;&nbsp;• Both run in <code>O(V + E)</code> time using adjacency '
                                               'list.<br/><br/>\n'
                                               '\n'
                                               '• <b>Cycle Detection Rules:</b><br/>\n'
                                               '&nbsp;&nbsp;• <b>Undirected Graph:</b> Cycle exists iff BFS/DFS '
                                               'encounters a visited node that is NOT the parent.<br/>\n'
                                               '&nbsp;&nbsp;• <b>Directed Graph:</b> Cycle exists iff DFS discovers a '
                                               '<b>BACK EDGE</b> (pointing to an active ancestor on the recursion '
                                               'stack)!<br/><br/>\n'
                                               '\n'
                                               '• <b>Topological Sort (for Directed Acyclic Graphs - DAGs):</b><br/>\n'
                                               '&nbsp;&nbsp;- Linear ordering where for every directed edge u → v, '
                                               'vertex u appears before v.<br/>\n'
                                               '&nbsp;&nbsp;- Possible if and only if the graph has <b>NO CYCLES</b> '
                                               '(is a DAG).<br/>\n'
                                               "&nbsp;&nbsp;- Kahn's Algorithm: Repeatedly remove vertices with "
                                               'in-degree 0.',
                                    'crucial_rule': '🎯 GOLDEN RULE FOR GATE: A directed graph has a unique topological '
                                                    'sort if and only if there exists a Hamiltonian path in the DAG.',
                                    'number': '19.1',
                                    'title': 'BFS vs DFS Traversals & Edge Classifications'},
                                  { 'content': '• <b>What is a Spanning Tree?</b> A subgraph that connects all V '
                                               'vertices with exactly <code>V - 1</code> edges and no '
                                               'cycles.<br/><br/>\n'
                                               '\n'
                                               "• <b>Kruskal's vs Prim's Algorithms:</b><br/>\n"
                                               "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 "
                                               "rounded-xl my-2 leading-relaxed overflow-x-auto'>\n"
                                               'Algorithm │ Data Structure Used                │ Time Complexity │ '
                                               'Better Suited For\n'
                                               '──────────────────────────────────────────────────────────────────────────────────────\n'
                                               'Kruskal   │ Disjoint Set Union (DSU / Find-Union)│ O(E log E)      │ '
                                               'Sparse Graphs (E ≈ V)\n'
                                               'Prim      │ Min-Heap (Priority Queue)          │ O(E log V)      │ '
                                               'Dense Graphs (E ≈ V²)\n'
                                               '</div>\n'
                                               '\n'
                                               '• <b>Cut Property & Uniqueness of MST:</b><br/>\n'
                                               '&nbsp;&nbsp;• <b>Cut Property:</b> For any cut in the graph, the '
                                               'minimum weight crossing edge MUST be in the MST.<br/>\n'
                                               '&nbsp;&nbsp;• <b>Uniqueness:</b> If all edge weights in a connected '
                                               'graph are <b>DISTINCT</b>, the graph has a <b>UNIQUE Minimum Spanning '
                                               'Tree</b>!',
                                    'crucial_rule': '🎯 GOLDEN RULE FOR GATE: If all edge weights are distinct, MST is '
                                                    'strictly unique! If edge weights are not distinct, multiple MSTs '
                                                    'may exist, but all MSTs have the EXACT SAME total weight.',
                                    'number': '19.2',
                                    'title': 'Minimum Spanning Tree (Kruskal & Prim)'},
                                  { 'content': '• <b>Master Shortest Path Decision Matrix:</b><br/>\n'
                                               "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 "
                                               "rounded-xl my-2 leading-relaxed overflow-x-auto'>\n"
                                               'Algorithm       │ Strategy │ Works with Negative Weights? │ Detects '
                                               'Negative Cycles? │ Time Complexity\n'
                                               '──────────────────────────────────────────────────────────────────────────────────────────────────\n'
                                               'Dijkstra        │ Greedy   │ NO (Fails with negative wts) │ '
                                               'NO                       │ O((V + E) log V)\n'
                                               'Bellman-Ford    │ DP       │ YES                          │ '
                                               'YES                      │ O(V · E)\n'
                                               'Floyd-Warshall  │ DP (All) │ YES (No negative cycles)     │ '
                                               'YES                      │ O(V³)\n'
                                               '</div>',
                                    'crucial_rule': "🎯 GOLDEN RULE FOR GATE: Dijkstra's algorithm FAILS with negative "
                                                    'weight edges because it greedily assumes that adding more edges '
                                                    'to an already finalized vertex can never decrease its distance!',
                                    'number': '19.3',
                                    'title': 'Shortest Paths (Dijkstra, Bellman-Ford, Floyd-Warshall)'}],
                 'real_life_examples': [ { 'text': 'An electrical power grid uses an MST to connect every town to the '
                                                   'power station with minimum total copper wire, ensuring zero '
                                                   'redundant circular loops.',
                                           'title': 'Real-Life Analogy: Power Grid & Fiber Optic Cabling'}],
                 'title': 'Graph Algorithms - Traversals, MST & Shortest Paths',
                 'worked_examples': [ { 'answer': 'Total MST weight is 11.',
                                        'problem': 'Given a graph with vertices {A, B, C, D, E} and edges with '
                                                   'weights: (A-B: 1), (B-C: 2), (A-C: 2), (C-D: 3), (B-D: 4), (D-E: '
                                                   "5), (C-E: 6). Find the total weight of the MST using Kruskal's "
                                                   'algorithm.',
                                        'steps': [ 'Step 1: Total vertices V = 5. An MST must contain exactly V - 1 = '
                                                   '4 edges.',
                                                   'Step 2: Sort edges by weight: (A-B: 1), (B-C: 2), (A-C: 2), (C-D: '
                                                   '3), (B-D: 4), (D-E: 5), (C-E: 6).',
                                                   'Step 3: Select (A-B: 1) ⇒ No cycle. Edge count = 1.',
                                                   'Step 4: Select (B-C: 2) ⇒ No cycle. Edge count = 2.',
                                                   'Step 5: Inspect (A-C: 2) ⇒ A, B, C are already connected! Adding '
                                                   'A-C creates cycle A-B-C-A. REJECT A-C.',
                                                   'Step 6: Select (C-D: 3) ⇒ Connects D to {A, B, C}. No cycle. Edge '
                                                   'count = 3.',
                                                   'Step 7: Inspect (B-D: 4) ⇒ Creates cycle B-C-D-B. REJECT B-D.',
                                                   'Step 8: Select (D-E: 5) ⇒ Connects E. No cycle. Edge count = 4. '
                                                   'Stop!',
                                                   'Step 9: Total MST weight = 1 + 2 + 3 + 5 = 11.'],
                                        'title': "Worked Example: Kruskal's MST Edge Selection"}]},
  ('COA', 0): { 'chapter_number': 9,
                'exam_traps': [ { 'title': 'The PC-Relative Pre-Increment Trap',
                                  'warning': 'Students frequently forget to update PC before calculating target '
                                             'address. In a 2-byte instruction at address 1000 with offset +20, PC '
                                             'becomes 1002, so Target = 1002 + 20 = 1022, NOT 1020!'}],
                'foundations': [ { 'content': '• <b>What is the Machine Instruction Cycle?</b><br/>\n'
                                              '&nbsp;&nbsp;The sequence of operations the CPU performs to execute a '
                                              'single machine instruction:<br/>\n'
                                              '&nbsp;&nbsp;1. <b>Fetch:</b> Program Counter (PC) places address on '
                                              'Memory Address Register (MAR). Instruction read into Memory Data '
                                              'Register (MDR) then to Instruction Register (IR). PC increments to '
                                              'point to next instruction.<br/>\n'
                                              '&nbsp;&nbsp;2. <b>Decode:</b> Control Unit decodes the opcode and '
                                              'determines addressing modes and required operands.<br/>\n'
                                              '&nbsp;&nbsp;3. <b>Execute:</b> ALU carries out the operation (e.g., '
                                              'addition, logical AND, branch condition evaluation).<br/>\n'
                                              '&nbsp;&nbsp;4. <b>Store (Write-back):</b> Result written to destination '
                                              'register or memory location.<br/><br/>\n'
                                              '\n'
                                              '• <b>Instruction Formats by Number of Addresses:</b><br/>\n'
                                              '&nbsp;&nbsp;• <b>3-Address Format:</b> <code>ADD R1, R2, R3</code> (R1 '
                                              '← R2 + R3). Expressive, but needs large instruction word length.<br/>\n'
                                              '&nbsp;&nbsp;• <b>2-Address Format:</b> <code>ADD R1, R2</code> (R1 ← R1 '
                                              '+ R2). One operand acts as both source and destination.<br/>\n'
                                              '&nbsp;&nbsp;• <b>1-Address Format:</b> <code>ADD X</code> (AC ← AC + '
                                              'M[X]). Uses an implicit <b>Accumulator (AC)</b> register.<br/>\n'
                                              '&nbsp;&nbsp;• <b>0-Address Format:</b> <code>ADD</code> (TOS ← TOS + '
                                              'SOS). Uses an implicit evaluation <b>Stack</b> (Push/Pop '
                                              'operations).<br/><br/>\n'
                                              '\n'
                                              '• <b>Expanding Opcode Technique:</b><br/>\n'
                                              '&nbsp;&nbsp;- Allows instructions with different numbers of addresses '
                                              'to coexist within a fixed-length instruction word.<br/>\n'
                                              '&nbsp;&nbsp;- If an n-bit opcode field has unused patterns, those '
                                              'unused bit combinations are extended into adjacent operand address '
                                              'fields to encode instructions with fewer operands!',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In expanding opcode calculation: Unused '
                                                   'opcodes at level k = (Total possible opcodes) - (Used opcodes). '
                                                   'Each unused opcode expands into 2^m opcodes at the next level!',
                                   'number': '9.1',
                                   'title': 'Instruction Cycle, Formats & Expanding Opcodes'},
                                 { 'content': '• <b>What is Effective Address (EA)?</b> The physical or logical '
                                              'address of the actual data operand in main memory.<br/><br/>\n'
                                              '\n'
                                              '• <b>Comprehensive Master Addressing Modes Guide:</b><br/>\n'
                                              "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 "
                                              "rounded-xl my-2 leading-relaxed overflow-x-auto'>\n"
                                              'Addressing Mode    │ Effective Address (EA) Formula │ Memory References '
                                              'to Fetch Operand │ Primary Exam Use Case\n'
                                              '───────────────────────────────────────────────────────────────────────────────────────────────────────────\n'
                                              'Immediate          │ Operand is inside instruction  │ 0 (Fastest! No '
                                              'memory lookup)      │ Loading constants (e.g. R1 ← 5)\n'
                                              'Direct (Absolute)  │ EA = Address field (A)         │ 1 memory '
                                              'read                      │ Global static variables\n'
                                              'Indirect           │ EA = M[A] (Pointer to pointer) │ 2 memory reads '
                                              '(Dereferencing)     │ Passing pointers / parameters\n'
                                              'Register           │ Operand is inside register R   │ 0 memory reads '
                                              '(Register file)     │ High-speed local variables\n'
                                              'Register Indirect  │ EA = [R]                       │ 1 memory '
                                              'read                      │ Array / pointer traversals\n'
                                              'PC-Relative        │ EA = PC + Offset (Displacement)│ 1 memory read (if '
                                              'in memory)       │ Relocatable branch jumps (if/else)\n'
                                              'Indexed            │ EA = Base (A) + Index Reg (R)  │ 1 memory '
                                              'read                      │ Array subscript access A[i]\n'
                                              'Base Register      │ EA = Base Reg (R) + Offset (A) │ 1 memory '
                                              'read                      │ Program relocation in memory\n'
                                              'Auto-Increment     │ EA = [R], then R ← R + d       │ 1 memory '
                                              'read                      │ Step through array elements\n'
                                              '</div>',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In PC-Relative addressing, when '
                                                   'calculating EA = PC + Offset, remember that the PC has ALREADY '
                                                   'BEEN INCREMENTED to point to the NEXT instruction! Never use the '
                                                   'address of the current instruction.',
                                   'number': '9.2',
                                   'title': 'Addressing Modes & Effective Address (EA) Mechanics'},
                                 { 'content': '• <b>Hardwired Control Unit:</b><br/>\n'
                                              '&nbsp;&nbsp;- Implemented as fixed combinational logic circuits '
                                              '(Decoders, Multiplexers, Logic Gates).<br/>\n'
                                              '&nbsp;&nbsp;- <b>Pros:</b> Extremely fast; minimal delay.<br/>\n'
                                              '&nbsp;&nbsp;- <b>Cons:</b> Rigid and inflexible; changing an '
                                              'instruction requires redesigning silicon chip layout.<br/>\n'
                                              '&nbsp;&nbsp;- <b>Used in:</b> RISC architectures.<br/><br/>\n'
                                              '\n'
                                              '• <b>Microprogrammed Control Unit:</b><br/>\n'
                                              '&nbsp;&nbsp;- Control signals generated by reading micro-instructions '
                                              'stored in a special high-speed memory called <b>Control ROM (Control '
                                              'Store)</b>.<br/>\n'
                                              '&nbsp;&nbsp;- <b>Pros:</b> Highly flexible; adding new instructions is '
                                              'just writing new micro-code in ROM.<br/>\n'
                                              '&nbsp;&nbsp;- <b>Cons:</b> Slower than hardwired due to ROM memory '
                                              'access time.<br/>\n'
                                              '&nbsp;&nbsp;- <b>Used in:</b> CISC architectures.<br/><br/>\n'
                                              '\n'
                                              '• <b>Horizontal vs Vertical Micro-instructions:</b><br/>\n'
                                              '&nbsp;&nbsp;• <b>Horizontal (Unencoded):</b> 1 bit per control signal. '
                                              'Fast, allows parallel control signals, but very wide word size (wastes '
                                              'memory).<br/>\n'
                                              '&nbsp;&nbsp;• <b>Vertical (Encoded):</b> Control signals grouped into n '
                                              'fields. An m-bit field decodes into 2ᵐ signals via decoders. Narrow '
                                              'word size, but slightly slower due to decoder delay.',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In vertical microprogramming, if k '
                                                   'mutually exclusive control signals need to be generated, the '
                                                   'minimum control field size is ⌈log₂(k + 1)⌉ bits (the +1 is for '
                                                   "the 'no operation' state).",
                                   'number': '9.3',
                                   'title': 'Control Unit Design: Hardwired vs Microprogrammed'}],
                'real_life_examples': [ { 'text': 'Immediate mode is cash handed directly to you. Direct mode is going '
                                                  'to a street address written on a card. Indirect mode is finding a '
                                                  'locker key at that address with instructions leading to another '
                                                  'locker.',
                                          'title': 'Real-Life Analogy: Mailing Addresses & Addressing Modes'}],
                'title': 'Machine Instructions & Addressing Modes',
                'worked_examples': [ { 'answer': '(a) Immediate: 0 operand reads, value=400; (b) Direct: 1 operand '
                                                 'read, value=500; (c) Indirect: 2 operand reads, value=600.',
                                       'problem': 'An instruction is stored at memory location 300 with its address '
                                                  'field holding value 400. The value stored at location 400 is 500, '
                                                  'and value at location 500 is 600. How many memory accesses are '
                                                  'required and what operand value is fetched if the addressing mode '
                                                  'is: (a) Immediate, (b) Direct, (c) Indirect?',
                                       'steps': [ 'Step 1: In all cases, 1 memory fetch is initially needed to read '
                                                  'the instruction itself from location 300.',
                                                  'Step 2: (a) Immediate Mode: The operand is 400 directly from the '
                                                  'instruction register. Additional memory accesses = 0. Operand = '
                                                  '400.',
                                                  'Step 3: (b) Direct Mode: Effective address EA = 400. Fetch M[400] = '
                                                  '500. Additional memory accesses = 1. Operand = 500.',
                                                  'Step 4: (c) Indirect Mode: Read location 400 to get address 500 '
                                                  '(1st memory access), then read location 500 to fetch operand 600 '
                                                  '(2nd memory access). Total additional memory accesses = 2. Operand '
                                                  '= 600.'],
                                       'title': 'Worked Example: Memory References in Addressing Modes'}]},
  ('COA', 1): { 'chapter_number': 10,
                'exam_traps': [ { 'title': 'Implicit Q₋₁ = 0 Omission Trap',
                                  'warning': "When counting Booth's operations, students often forget that Q₋₁ is "
                                             'initialized to 0! If the LSB of Q is 1, the first pair is (1, 0) which '
                                             'triggers a subtraction.'}],
                'foundations': [ { 'content': "• <b>Why Booth's Algorithm?</b><br/>\n"
                                              "&nbsp;&nbsp;- Multiplies two signed 2's complement numbers without "
                                              'requiring sign-magnitude conversion!<br/>\n'
                                              '&nbsp;&nbsp;- Replaces long strings of consecutive 1s with a single '
                                              'addition and subtraction (e.g. 7 in binary is 0111 = 8 - 1 = 2³ - '
                                              '2⁰).<br/><br/>\n'
                                              '\n'
                                              "• <b>Step-by-Step Booth's Execution Rules:</b><br/>\n"
                                              '&nbsp;&nbsp;Initialize: Accumulator AC = 0, Multiplier in Q, Q₋₁ = 0, '
                                              'Count = n.<br/>\n'
                                              '&nbsp;&nbsp;At each step, inspect the pair (Q₀, Q₋₁):<br/>\n'
                                              "<div class='font-mono text-xs p-3 bg-slate-900 text-emerald-400 "
                                              "rounded-xl my-2 leading-relaxed'>\n"
                                              '(Q₀, Q₋₁) Pair │ Action Performed\n'
                                              '─────────────────────────────────────────────────────────────\n'
                                              '0  0           │ No arithmetic operation (Just Shift)\n'
                                              '0  1           │ AC ← AC + M (End of a string of 1s)\n'
                                              '1  0           │ AC ← AC - M (Beginning of a string of 1s)\n'
                                              '1  1           │ No arithmetic operation (Middle of a string of 1s)\n'
                                              '</div>\n'
                                              '&nbsp;&nbsp;After arithmetic operation: <b>Arithmetic Right Shift [AC, '
                                              'Q, Q₋₁]</b> by 1 bit (preserving MSB of AC). Decrement count until '
                                              '0.<br/><br/>\n'
                                              '\n'
                                              '• <b>Performance Analysis (GATE Favorite):</b><br/>\n'
                                              '&nbsp;&nbsp;• <b>Best Case (Fewest Operations):</b> Multiplier with '
                                              'alternating blocks of all 0s or all 1s (e.g. 00001111).<br/>\n'
                                              '&nbsp;&nbsp;• <b>Worst Case (Maximum Operations):</b> Multiplier with '
                                              'alternating 0s and 1s (e.g. 01010101), where every cycle requires an '
                                              'add or subtract!',
                                   'crucial_rule': "🎯 GOLDEN RULE FOR GATE: In Booth's algorithm, the number of "
                                                   'arithmetic additions and subtractions equals the number of '
                                                   'transitions (0→1 and 1→0) between adjacent bits of the multiplier '
                                                   '(including implicit Q₋₁ = 0)!',
                                   'number': '10.1',
                                   'title': "Booth's Multiplication Algorithm for Signed 2's Complement"},
                                 { 'content': '• <b>Restoring Division:</b><br/>\n'
                                              '&nbsp;&nbsp;- Left shift [A, Q]. Subtract Divisor M: <code>A ← A - '
                                              'M</code>.<br/>\n'
                                              '&nbsp;&nbsp;- If result A is negative: Set Q₀ = 0 and <b>Restore A</b>: '
                                              '<code>A ← A + M</code>.<br/>\n'
                                              '&nbsp;&nbsp;- If result A is positive: Set Q₀ = 1 (no restoration '
                                              'needed).<br/><br/>\n'
                                              '\n'
                                              '• <b>Non-Restoring Division (Faster Hardware):</b><br/>\n'
                                              '&nbsp;&nbsp;- Avoids restoring addition when sign is negative!<br/>\n'
                                              '&nbsp;&nbsp;- If previous A was positive: Shift left, then <b>Subtract '
                                              'M</b> (A ← 2A - M).<br/>\n'
                                              '&nbsp;&nbsp;- If previous A was negative: Shift left, then <b>Add M</b> '
                                              '(A ← 2A + M).<br/>\n'
                                              '&nbsp;&nbsp;- Saves clock cycles because every step does exactly 1 '
                                              'shift and 1 arithmetic operation.',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Non-restoring division takes exactly n '
                                                   'cycles for n-bit numbers, whereas restoring division may take up '
                                                   'to 2n operations in worst-case.',
                                   'number': '10.2',
                                   'title': 'Restoring vs Non-Restoring Integer Division'}],
                'real_life_examples': [ { 'text': "Booth's multiplication is like paying $99: instead of handing over "
                                                  '99 individual $1 bills, you hand over a $100 bill and take back $1 '
                                                  'in change (100 - 1).',
                                          'title': 'Real-Life Analogy: Cashier Change Shortcut'}],
                'title': 'ALU, Control Unit & Memory Interfacing',
                'worked_examples': [ { 'answer': 'Exactly 2 arithmetic operations (1 addition, 1 subtraction).',
                                       'problem': 'How many additions and subtractions are performed when multiplying '
                                                  "by 00111100 using Booth's algorithm?",
                                       'steps': [ 'Step 1: Write down the multiplier with Q₋₁ = 0 appended at the end: '
                                                  'Q = 0 0 1 1 1 1 0 0, Q₋₁ = 0.',
                                                  'Step 2: Inspect adjacent bit pairs from right to left (Qᵢ, Qᵢ₋₁):',
                                                  '  - Pair 1 (Bit 0, Q₋₁): (0, 0) ⇒ No operation.',
                                                  '  - Pair 2 (Bit 1, Bit 0): (0, 0) ⇒ No operation.',
                                                  '  - Pair 3 (Bit 2, Bit 1): (1, 0) ⇒ SUBTRACTION.',
                                                  '  - Pair 4 (Bit 3, Bit 2): (1, 1) ⇒ No operation.',
                                                  '  - Pair 5 (Bit 4, Bit 3): (1, 1) ⇒ No operation.',
                                                  '  - Pair 6 (Bit 5, Bit 4): (1, 1) ⇒ No operation.',
                                                  '  - Pair 7 (Bit 6, Bit 5): (0, 1) ⇒ ADDITION.',
                                                  '  - Pair 8 (Bit 7, Bit 6): (0, 0) ⇒ No operation.',
                                                  'Step 3: Total operations = 1 Addition + 1 Subtraction = 2 '
                                                  'arithmetic operations.'],
                                       'title': "Worked Example: Counting Operations in Booth's Algorithm"}]},
  ('COA', 2): { 'chapter_number': 11,
                'exam_traps': [ { 'title': 'Byte-Addressable vs Word-Addressable Trap',
                                  'warning': 'If memory is 4-byte Word-Addressable, the block offset identifies the '
                                             'WORD within the block, NOT the byte! Students lose marks by calculating '
                                             'byte offsets for word-addressed machines.'}],
                'foundations': [ { 'content': '• <b>Main Memory Address Breakdown Formulas:</b><br/>\n'
                                              '&nbsp;&nbsp;Given: Main Memory Size = 2ᴹ bytes (M-bit address), Cache '
                                              'Size = C bytes, Block/Line Size = B = 2ᵇ bytes.<br/>\n'
                                              '&nbsp;&nbsp;• <b>Block Offset bits (w):</b> <code>w = log₂(Block Size '
                                              'B)</code> (Identifies the exact byte inside the cache '
                                              'block).<br/><br/>\n'
                                              '\n'
                                              '• <b>The Three Cache Mapping Schemes:</b><br/>\n'
                                              "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 "
                                              "rounded-xl my-2 leading-relaxed overflow-x-auto'>\n"
                                              'Mapping Scheme          │ Address Field Partitioning                   '
                                              '│ Cache Index Formula\n'
                                              '──────────────────────────────────────────────────────────────────────────────────────────────\n'
                                              'Direct Mapping          │ [ Tag (M - c) ] [ Line Index (c - w) ] [ Word '
                                              '(w) ] │ Line = (Block Address) mod (Total Lines)\n'
                                              'Fully Associative       │ [ Tag (M - w) ] [ Word Offset (w) ]          '
                                              '│ Block can go in ANY line (No index bits!)\n'
                                              'K-Way Set Associative   │ [ Tag (M - s - w) ] [ Set Index (s) ] [ Word '
                                              '(w) ]   │ Set = (Block Address) mod (Number of Sets)\n'
                                              '</div>\n'
                                              '\n'
                                              '• <b>K-Way Set Associative Details:</b><br/>\n'
                                              '&nbsp;&nbsp;• <b>Number of Sets:</b> <code>S = (Total Cache Lines) / K '
                                              '= Cache Size / (K × Block Size)</code>.<br/>\n'
                                              '&nbsp;&nbsp;• <b>Set Index bits (s):</b> <code>s = '
                                              'log₂(S)</code>.<br/>\n'
                                              '&nbsp;&nbsp;• <b>Tag bits:</b> <code>Tag = M - s - w</code>.<br/>\n'
                                              '&nbsp;&nbsp;• <b>Comparators Required:</b> Exactly <b>K comparators</b> '
                                              'operating in parallel, each comparing Tag bits with the stored tag in '
                                              'that set.',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Total Cache Directory / Tag Memory Size = '
                                                   '(Number of Lines) × (Tag bits + Valid bit + Dirty bit). GATE '
                                                   'questions often ask for Tag overhead in bits or KB!',
                                   'number': '11.1',
                                   'title': 'Cache Address Partitioning (Direct, Associative, Set-Associative)'},
                                 { 'content': '• <b>Cache Write Policies:</b><br/>\n'
                                              '&nbsp;&nbsp;• <b>Write-Through:</b> Updates both Cache and Main Memory '
                                              'simultaneously on every write. Always consistent, but slower writes '
                                              '(solved with Write Buffers).<br/>\n'
                                              '&nbsp;&nbsp;• <b>Write-Back:</b> Updates ONLY the Cache block. Sets a '
                                              '<b>Dirty Bit = 1</b>. Main memory is updated only when the block is '
                                              'evicted! Much faster writes.<br/>\n'
                                              '&nbsp;&nbsp;• <b>Write-Allocate vs No-Write-Allocate (on Write '
                                              'Miss):</b><br/>\n'
                                              '&nbsp;&nbsp;&nbsp;&nbsp;- Write-Allocate: Fetch missed block into cache '
                                              'then write (typically paired with Write-Back).<br/>\n'
                                              '&nbsp;&nbsp;&nbsp;&nbsp;- No-Write-Allocate: Write directly to main '
                                              'memory without loading into cache (paired with '
                                              'Write-Through).<br/><br/>\n'
                                              '\n'
                                              '• <b>Replacement Algorithms (used on cache miss when set is '
                                              'full):</b><br/>\n'
                                              '&nbsp;&nbsp;• <b>LRU (Least Recently Used):</b> Evicts block untouched '
                                              'for the longest time. Hardware tracking: K-way set associative requires '
                                              '⌈log₂(K!)⌉ or K(K-1)/2 bits per set.<br/>\n'
                                              '&nbsp;&nbsp;• <b>FIFO (First-In, First-Out):</b> Evicts oldest loaded '
                                              'block (ignores recency of access).<br/>\n'
                                              '&nbsp;&nbsp;• <b>Random:</b> Evicts a pseudo-random block (very cheap '
                                              'hardware, surprisingly good performance).',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Fully Associative cache has 0 conflict '
                                                   'misses (only cold and capacity misses). Direct-mapped cache '
                                                   'suffers heavily from conflict misses!',
                                   'number': '11.2',
                                   'title': 'Cache Write Policies & Replacement Algorithms'},
                                 { 'content': '• <b>Single-Level AMAT Formula:</b><br/>\n'
                                              '&nbsp;&nbsp;<code>AMAT = H₁ × T₁ + (1 - H₁) × Tₘₑₘ</code><br/>\n'
                                              '&nbsp;&nbsp;• Alternative (Add Hit Time to Miss Penalty): <code>AMAT = '
                                              'T₁ + (1 - H₁) × Miss_Penalty</code>.<br/><br/>\n'
                                              '\n'
                                              '• <b>Two-Level Cache Hierarchy (L1 and L2):</b><br/>\n'
                                              '&nbsp;&nbsp;<code>AMAT = T₁ + (1 - H₁) × [T₂ + (1 - H₂_local) × '
                                              'Tₘₑₘ]</code><br/>\n'
                                              '&nbsp;&nbsp;• <b>Local Hit Rate (H_local):</b> Hits in L2 divided by '
                                              'total accesses that reached L2.<br/>\n'
                                              '&nbsp;&nbsp;• <b>Global Hit Rate (H_global):</b> Hits in L2 divided by '
                                              'total CPU memory requests.<br/>\n'
                                              '&nbsp;&nbsp;• Relationship: <code>H₂_global = (1 - H₁) × '
                                              'H₂_local</code>.',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In simultaneous access memory, all levels '
                                                   'are searched together: AMAT = H₁T₁ + (H₂ - H₁)T₂ + ... In '
                                                   'hierarchical access, L2 is searched ONLY AFTER L1 misses!',
                                   'number': '11.3',
                                   'title': 'Average Memory Access Time (AMAT) & Multi-Level Caches'}],
                'real_life_examples': [ { 'text': 'CPU registers are the pens in your hand. L1 cache is the textbook '
                                                  'open on your desk. L2 is your backpack. Main memory is the '
                                                  'bookshelf across the room. Disk is the city public library!',
                                          'title': "Real-Life Analogy: The Student's Study Desk"}],
                'title': 'Memory Hierarchy, Cache Mapping & AMAT',
                'worked_examples': [ { 'answer': 'Tag = 18 bits, Set Index = 10 bits, Word Offset = 4 bits.',
                                       'problem': 'A computer system has 32-bit byte-addressable main memory. The '
                                                  'cache is 64 KB, 4-way set associative with 16-byte cache blocks. '
                                                  'Determine the size of the Tag, Set Index, and Word Offset fields.',
                                       'steps': [ 'Step 1: Total address bits M = 32 bits.',
                                                  'Step 2: Block size B = 16 bytes = 2⁴ bytes ⇒ Word Offset bits w = 4 '
                                                  'bits.',
                                                  'Step 3: Total cache lines = Cache Size / Block Size = 64 KB / 16 '
                                                  'bytes = 65,536 / 16 = 4096 lines.',
                                                  'Step 4: Number of Sets S = Total lines / K = 4096 / 4 = 1024 sets = '
                                                  '2¹⁰ sets ⇒ Set Index bits s = 10 bits.',
                                                  'Step 5: Tag bits = Total bits - Set bits - Word bits = 32 - 10 - 4 '
                                                  '= 18 bits.'],
                                       'title': 'Worked Example: Calculating Tag, Set and Word Bits'}]},
  ('COA', 3): { 'chapter_number': 12,
                'exam_traps': [ { 'title': 'Branch Resolved in ID vs EX Stage Trap',
                                  'warning': 'Read carefully whether the branch condition and target address are '
                                             'resolved in the ID stage (causes 1 stall) or the EX stage (causes 2 '
                                             'stalls).'}],
                'foundations': [ { 'content': '• <b>The 5 Pipeline Stages:</b><br/>\n'
                                              '&nbsp;&nbsp;1. <b>IF (Instruction Fetch):</b> Read instruction from '
                                              'I-cache using PC. Increment PC.<br/>\n'
                                              '&nbsp;&nbsp;2. <b>ID (Instruction Decode / Register Fetch):</b> Decode '
                                              'opcode and read source registers.<br/>\n'
                                              '&nbsp;&nbsp;3. <b>EX (Execution / Effective Address):</b> ALU executes '
                                              'arithmetic/logic operation or computes EA for load/store.<br/>\n'
                                              '&nbsp;&nbsp;4. <b>MEM (Memory Access):</b> Read from or write to '
                                              'D-cache for Load/Store instructions. Other instructions are idle.<br/>\n'
                                              '&nbsp;&nbsp;5. <b>WB (Write Back):</b> Write result from ALU or memory '
                                              'into destination register.<br/><br/>\n'
                                              '\n'
                                              '• <b>Cycle Time & Speedup Formula:</b><br/>\n'
                                              '&nbsp;&nbsp;• <b>Clock Cycle Time (τ):</b> <code>τ = max(Stage Delays) '
                                              '+ Register Delay</code>.<br/>\n'
                                              '&nbsp;&nbsp;• Time to execute n instructions on a k-stage pipeline: '
                                              '<code>T_pipe = [k + (n - 1)] × τ</code>.<br/>\n'
                                              '&nbsp;&nbsp;• Ideal Speedup over non-pipelined execution: <code>Speedup '
                                              'S = (n × k) / (k + n - 1)</code>.<br/>\n'
                                              '&nbsp;&nbsp;• For large n (as n → ∞): <b>Maximum Theoretical Speedup = '
                                              'k</b> (the number of stages)!',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: The pipeline clock frequency is strictly '
                                                   'determined by the SLOWEST stage! Speeding up non-bottleneck stages '
                                                   'gives zero improvement to the clock cycle.',
                                   'number': '12.1',
                                   'title': 'The 5-Stage Classic RISC Pipeline & Clock Cycle'},
                                 { 'content': '• <b>1. Structural Hazards (Hardware Resource Conflicts):</b><br/>\n'
                                              '&nbsp;&nbsp;- Occurs when two instructions compete for the same '
                                              'hardware unit in the same clock cycle.<br/>\n'
                                              '&nbsp;&nbsp;- <i>Classic example:</i> Memory conflict if instruction '
                                              'fetch (IF) and data access (MEM) share a single unified memory.<br/>\n'
                                              '&nbsp;&nbsp;- <i>Solution:</i> Harvard architecture (Separate I-Cache '
                                              'and D-Cache).<br/><br/>\n'
                                              '\n'
                                              '• <b>2. Data Hazards (Data Dependencies):</b><br/>\n'
                                              '&nbsp;&nbsp;• <b>RAW (Read After Write - True Dependency):</b> '
                                              'Instruction J tries to read register before Instruction I writes it! '
                                              'Most common hazard in GATE.<br/>\n'
                                              '&nbsp;&nbsp;• <b>WAR (Write After Read - Anti-Dependency):</b> '
                                              'Instruction J tries to write before Instruction I reads.<br/>\n'
                                              '&nbsp;&nbsp;• <b>WAW (Write After Write - Output Dependency):</b> '
                                              'Instruction J writes before Instruction I writes.<br/>\n'
                                              '&nbsp;&nbsp;• <i>Solutions for RAW:</i><br/>\n'
                                              '&nbsp;&nbsp;&nbsp;&nbsp;1. <b>Operand Forwarding (Bypassing):</b> Route '
                                              'ALU output directly from EX/MEM buffer to EX stage input of next cycle '
                                              '(eliminates stalls for ALU-to-ALU).<br/>\n'
                                              '&nbsp;&nbsp;&nbsp;&nbsp;2. <b>Load-Use Delay:</b> A Load instruction '
                                              'followed immediately by an instruction that uses its result ALWAYS '
                                              'requires <b>1 stall cycle</b> even with forwarding!<br/><br/>\n'
                                              '\n'
                                              '• <b>3. Control Hazards (Branch Penalty):</b><br/>\n'
                                              '&nbsp;&nbsp;- Target PC is not known until branch condition is '
                                              'evaluated in ID or EX stage.<br/>\n'
                                              '&nbsp;&nbsp;- <i>Solutions:</i> Branch prediction (Static: predict '
                                              'taken/not taken; Dynamic: 2-bit saturating counter), Branch delay '
                                              'slots.',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: With full operand forwarding: ALU-to-ALU '
                                                   'instructions cause 0 stalls! Load-to-ALU instructions cause '
                                                   'exactly 1 stall cycle.',
                                   'number': '12.2',
                                   'title': 'Pipeline Hazards: Structural, Data & Control'}],
                'real_life_examples': [ { 'text': 'Pipelining is like doing laundry: while load 2 is in the washer, '
                                                  'load 1 is in the dryer, and load 0 is being folded. You finish a '
                                                  'load every 30 minutes instead of waiting 90 minutes per load!',
                                          'title': 'Real-Life Analogy: The Industrial Laundromat Pipeline'}],
                'title': 'Instruction Pipelining, Hazards & Performance',
                'worked_examples': [ { 'answer': 'Total execution time is 20.8 ns.',
                                       'problem': 'A 5-stage pipeline has stage delays of 150 ps, 120 ps, 180 ps, 160 '
                                                  'ps, and 100 ps. The pipeline register delay is 20 ps. How long does '
                                                  'it take to execute 100 independent instructions?',
                                       'steps': [ 'Step 1: Find the bottleneck stage delay = max(150, 120, 180, 160, '
                                                  '100) = 180 ps.',
                                                  'Step 2: Calculate clock cycle time τ = max stage delay + register '
                                                  'delay = 180 ps + 20 ps = 200 ps.',
                                                  'Step 3: Number of stages k = 5, number of instructions n = 100.',
                                                  'Step 4: Total clock cycles required = k + n - 1 = 5 + 100 - 1 = 104 '
                                                  'cycles.',
                                                  'Step 5: Total execution time = 104 × 200 ps = 20,800 ps = 20.8 ns.'],
                                       'title': 'Worked Example: Pipeline Execution Time and Stalls'}]},
  ('PDS', 0): { 'chapter_number': 13,
                'exam_traps': [ { 'title': 'The Sequence Point & Undefined Behavior Trap',
                                  'warning': "Expressions like 'i = i++ + ++i' modify variable i multiple times "
                                             'without an intervening sequence point. In C standard, this is strictly '
                                             'UNDEFINED BEHAVIOR! GATE questions frequently ask if such code is valid '
                                             'or undefined.'}],
                'foundations': [ { 'content': '• <b>1. What is a Pointer? (Basic Definition & Memory Model):</b><br/>\n'
                                              '&nbsp;&nbsp;- A normal variable stores a data value: <code>int x = '
                                              '25;</code> (stores 25 at some address, say 1000).<br/>\n'
                                              '&nbsp;&nbsp;- A pointer variable stores the <b>memory address</b> of '
                                              'another variable: <code>int *p = &x;</code> (stores address '
                                              '1000).<br/>\n'
                                              '&nbsp;&nbsp;- The dereference operator (<code>*p</code>) reads or '
                                              'writes the value located at that stored address (<code>*p = 50</code> '
                                              'changes x to 50).<br/><br/>\n'
                                              '\n'
                                              '• <b>2. What is an Array in Memory?</b><br/>\n'
                                              '&nbsp;&nbsp;Suppose you declare: <code>int arr[4] = {10, 20, 30, '
                                              '40};</code> (assuming 4 bytes per integer):<br/>\n'
                                              "<div class='font-mono text-xs p-3 bg-slate-900 text-emerald-400 "
                                              "rounded-xl my-2 leading-relaxed'>\n"
                                              'Array Element:   arr[0]      arr[1]      arr[2]      arr[3]\n'
                                              'Stored Value:      10          20          30          40\n'
                                              'Memory Address:  [1000]      [1004]      [1008]      [1012]\n'
                                              '                    ↑\n'
                                              '                   arr (points here)\n'
                                              '</div>\n'
                                              '&nbsp;&nbsp;• <b>The array name <code>arr</code> is a CONSTANT '
                                              'POINTER:</b> It holds the base address: <code>arr == &arr[0] == '
                                              '1000</code>.<br/>\n'
                                              '&nbsp;&nbsp;• Because it is constant, you <b>CANNOT reassign it</b>: '
                                              '<code>arr++</code> or <code>arr = p</code> causes a compilation '
                                              'error!<br/><br/>\n'
                                              '\n'
                                              '• <b>3. Why does <code>3[arr] == arr[3]</code> work? (The Subscript '
                                              'Rule):</b><br/>\n'
                                              '&nbsp;&nbsp;• The C compiler does NOT know what square brackets '
                                              '<code>[]</code> mean in assembly language!<br/>\n'
                                              '&nbsp;&nbsp;• Every time you write <code>arr[i]</code>, the compiler '
                                              'literally rewrites it as:<br/>\n'
                                              '&nbsp;&nbsp;&nbsp;&nbsp;<code>arr[i] ≡ *(arr + i)</code><br/>\n'
                                              '&nbsp;&nbsp;• Since addition is commutative (<code>a + b == b + '
                                              'a</code>), <code>*(arr + i)</code> is identical to <code>*(i + '
                                              'arr)</code>.<br/>\n'
                                              '&nbsp;&nbsp;• But <code>*(i + arr)</code> can be written back into '
                                              'bracket notation as <code>i[arr]</code>!<br/>\n'
                                              '&nbsp;&nbsp;• <b>Therefore:</b> <code>arr[i] == *(arr + i) == *(i + '
                                              'arr) == i[arr]</code>! In C, writing <code>3[arr]</code> evaluates to '
                                              '40!<br/><br/>\n'
                                              '\n'
                                              '• <b>4. Pointer Arithmetic & Scaling Rule:</b><br/>\n'
                                              '&nbsp;&nbsp;- Adding 1 to a pointer does NOT add 1 byte! It adds '
                                              '<code>1 × sizeof(*p)</code> bytes.<br/>\n'
                                              '&nbsp;&nbsp;- If <code>p = 1000</code> (pointer to 4-byte int): <code>p '
                                              '+ 1 = 1004</code>, <code>p + 2 = 1008</code>.<br/>\n'
                                              '&nbsp;&nbsp;- If <code>char *cp = 1000</code>: <code>cp + 1 = '
                                              '1001</code>.<br/>\n'
                                              '&nbsp;&nbsp;- If <code>double *dp = 1000</code>: <code>dp + 1 = '
                                              '1008</code>.<br/><br/>\n'
                                              '\n'
                                              '• <b>5. Pointer Increment Nuances (*p++ vs (*p)++ vs *++p):</b><br/>\n'
                                              "<div class='font-mono text-xs p-3 bg-slate-900 text-slate-100 "
                                              "rounded-xl my-2 leading-relaxed overflow-x-auto'>\n"
                                              'Expression   │ Precedence & Step-by-Step '
                                              'Execution                             │ Value Returned │ Effect on '
                                              'Pointer / Memory\n'
                                              '─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n'
                                              '*p++         │ Postfix ++ has higher precedence than *. Reads *p '
                                              'first;        │ Original *p    │ Pointer p moves to next slot!\n'
                                              '             │ then increments pointer '
                                              'p.                                      │                │\n'
                                              '(*p)++       │ Parentheses force *p first. Fetches current value; '
                                              'then         │ Original *p    │ Value in memory incremented!\n'
                                              '             │ increments the INTEGER in memory by '
                                              '1.                          │                │ Pointer p DOES NOT '
                                              'MOVE!\n'
                                              '*++p         │ Prefix ++ increments pointer p to next slot '
                                              'first;              │ Value at new   │ Pointer p moves to next slot!\n'
                                              '             │ then dereferences that new '
                                              'address.                             │ address        │\n'
                                              '++*p         │ Dereferences *p to get value; then increments that '
                                              'integer      │ Incremented    │ Value in memory incremented!\n'
                                              '             │ before using '
                                              'it.                                                │ new value      │ '
                                              'Pointer p DOES NOT MOVE!\n'
                                              '</div>\n'
                                              '\n'
                                              '• <b>6. The Giant Trap: <code>arr + 1</code> vs <code>&arr + '
                                              '1</code>:</b><br/>\n'
                                              '&nbsp;&nbsp;• <code>arr</code> has type <code>int*</code>: Pointer to '
                                              'first element. <code>arr + 1</code> jumps <b>4 bytes</b> to '
                                              '<code>&arr[1]</code> (1004).<br/>\n'
                                              '&nbsp;&nbsp;• <code>&arr</code> has type <code>int (*)[4]</code>: '
                                              'Pointer to the ENTIRE array of 4 integers!<br/>\n'
                                              '&nbsp;&nbsp;• Therefore, <code>&arr + 1</code> jumps the <b>ENTIRE '
                                              'ARRAY of 4 ints (16 bytes)</b> to 1016!',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: When an array is passed into a function '
                                                   '(like void solve(int arr[])), the array automatically DECAYS into '
                                                   'a simple pointer (int *arr)! Inside that function, sizeof(arr) '
                                                   'returns the size of a POINTER (8 bytes on 64-bit systems), NOT the '
                                                   'size of the array!',
                                   'number': '13.1',
                                   'title': 'Pointers & Array Equivalence in C (Complete Conceptual Breakdown)'},
                                 { 'content': '• <b>Operator Precedence Hierarchy in C (Top to Bottom):</b><br/>\n'
                                              '&nbsp;&nbsp;1. Postfix operators: <code>() [] -> . ++ --</code> '
                                              '(Left-to-Right)<br/>\n'
                                              '&nbsp;&nbsp;2. Unary prefix operators: <code>! ~ ++ -- + - * & (type) '
                                              'sizeof</code> (Right-to-Left)<br/>\n'
                                              '&nbsp;&nbsp;3. Multiplicative: <code>* / %</code> (Left-to-Right)<br/>\n'
                                              '&nbsp;&nbsp;4. Additive: <code>+ -</code> (Left-to-Right)<br/>\n'
                                              '&nbsp;&nbsp;5. Relational: <code>< <= > >=</code> (Left-to-Right)<br/>\n'
                                              '&nbsp;&nbsp;6. Equality: <code>== !=</code> (Left-to-Right)<br/>\n'
                                              '&nbsp;&nbsp;7. Logical AND: <code>&&</code> (Left-to-Right - '
                                              'Short-circuit)<br/>\n'
                                              '&nbsp;&nbsp;8. Logical OR: <code>||</code> (Left-to-Right - '
                                              'Short-circuit)<br/>\n'
                                              '&nbsp;&nbsp;9. Conditional ternary: <code>? :</code> '
                                              '(Right-to-Left)<br/>\n'
                                              '&nbsp;&nbsp;10. Assignment: <code>= += -= *= ...</code> '
                                              '(Right-to-Left)<br/>\n'
                                              '&nbsp;&nbsp;11. Comma operator: <code>,</code> (Left-to-Right - Lowest '
                                              'precedence)<br/><br/>\n'
                                              '\n'
                                              '• <b>Short-Circuit Evaluation Mechanics:</b><br/>\n'
                                              '&nbsp;&nbsp;• <b>In Logical AND (expr1 && expr2):</b><br/>\n'
                                              '&nbsp;&nbsp;&nbsp;&nbsp;- If <code>expr1 == 0 (False)</code>, the whole '
                                              'result MUST be False.<br/>\n'
                                              '&nbsp;&nbsp;&nbsp;&nbsp;- <b>expr2 IS NEVER EVALUATED!</b> Any side '
                                              'effects (like <code>i++</code>) inside expr2 are completely '
                                              'skipped!<br/>\n'
                                              '&nbsp;&nbsp;• <b>In Logical OR (expr1 || expr2):</b><br/>\n'
                                              '&nbsp;&nbsp;&nbsp;&nbsp;- If <code>expr1 != 0 (True)</code>, the whole '
                                              'result MUST be True.<br/>\n'
                                              '&nbsp;&nbsp;&nbsp;&nbsp;- <b>expr2 IS NEVER EVALUATED!</b> Any side '
                                              'effects inside expr2 are completely skipped!',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In expression: int a=0, b=5; if (a++ && '
                                                   '++b) ..., a++ evaluates to 0 (post-increment), so && '
                                                   'short-circuits! ++b is NEVER executed. At the end, a = 1, b = 5.',
                                   'number': '13.2',
                                   'title': 'Short-Circuit Evaluation & Operator Precedence'},
                                 { 'content': '• <b>The Anatomy of a Recursive Call Stack Frame:</b><br/>\n'
                                              '&nbsp;&nbsp;Every function call pushes an <b>Activation Record (Stack '
                                              'Frame)</b> containing:<br/>\n'
                                              '&nbsp;&nbsp;1. Function parameters.<br/>\n'
                                              '&nbsp;&nbsp;2. Return address (where to jump back when function '
                                              'finishes).<br/>\n'
                                              '&nbsp;&nbsp;3. Local variables.<br/>\n'
                                              '&nbsp;&nbsp;4. Saved frame pointer.<br/><br/>\n'
                                              '\n'
                                              '• <b>Tracing Recursive Functions (Pre-order vs Post-order '
                                              'Actions):</b><br/>\n'
                                              '&nbsp;&nbsp;• Code written <b>BEFORE</b> the recursive call executes on '
                                              'the way DOWN the recursion tree (Pre-order).<br/>\n'
                                              '&nbsp;&nbsp;• Code written <b>AFTER</b> the recursive call executes on '
                                              'the way UP during backtracking (Post-order / unwinding).<br/><br/>\n'
                                              '\n'
                                              '• <b>Static Variables inside Recursive Functions:</b><br/>\n'
                                              '&nbsp;&nbsp;• <code>static int count = 0;</code> is initialized ONLY '
                                              'ONCE when program loads into memory (in the Data Segment).<br/>\n'
                                              '&nbsp;&nbsp;• It does NOT reside on the stack! Every recursive call '
                                              'shares the <b>exact same copy</b> of the static variable!',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In recursive questions with static or '
                                                   'global variables: modifications persist across calls! Never reset '
                                                   'static variables when unwinding the call stack.',
                                   'number': '13.3',
                                   'title': 'Recursion, Call Stacks & Static Storage'}],
                'real_life_examples': [ { 'text': 'A variable is the contents of Hotel Room 104. A pointer is the room '
                                                  "key card displaying 'Room 104'. Dereferencing (*p) is using the key "
                                                  'card to open the door and access what is inside.',
                                          'title': 'Real-Life Analogy: Hotel Room Keys & Pointers'}],
                'title': 'Programming in C & Recursion Tracing',
                'worked_examples': [ { 'answer': 'Output is: 10 20 30 21',
                                       'problem': 'What is the exact output of the following C program?\\n\\nint '
                                                  'main() {\\n    int a[] = {10, 20, 30, 40, 50};\\n    int *p = '
                                                  'a;\\n    int val1 = *p++;\\n    int val2 = (*p)++;\\n    int val3 = '
                                                  '*++p;\\n    printf("%d %d %d %d", val1, val2, val3, a[1]);\\n    '
                                                  'return 0;\\n}',
                                       'steps': [ 'Step 1: Initially array a = {10, 20, 30, 40, 50}. Pointer p points '
                                                  'to a[0] (value 10, address 1000).',
                                                  "Step 2: Line 'int val1 = *p++;': Postfix ++ increments pointer p "
                                                  'AFTER dereference. val1 receives *p = 10. Pointer p moves to point '
                                                  'to a[1] (address 1004).',
                                                  "Step 3: Line 'int val2 = (*p)++;': Parentheses force *p first. val2 "
                                                  'receives current value of a[1] = 20. Then the value in memory at '
                                                  'a[1] is incremented from 20 to 21! Pointer p remains at a[1].',
                                                  "Step 4: Line 'int val3 = *++p;': Prefix ++ increments pointer p "
                                                  'first. p now points to a[2] (address 1008). Then dereferences: val3 '
                                                  '= a[2] = 30.',
                                                  'Step 5: Inspect printed values: val1 = 10, val2 = 20, val3 = 30, '
                                                  'a[1] = 21.'],
                                       'title': 'Worked Example: Comprehensive Pointer Code Trace'}]},
  ('PDS', 1): { 'chapter_number': 14,
                'exam_traps': [ { 'title': 'Stack Element Count from Infix Conversions',
                                  'warning': 'GATE often asks for the MAXIMUM number of operators stored '
                                             'simultaneously on the stack during infix conversion. Be sure to count '
                                             'parentheses if they are pushed onto the operator stack.'}],
                'foundations': [ { 'content': '• <b>Stack (LIFO - Last In, First Out):</b><br/>\n'
                                              '&nbsp;&nbsp;All insertions and deletions happen at one end called the '
                                              '<b>Top</b>. Time complexity for Push and Pop is O(1).<br/><br/>\n'
                                              '\n'
                                              '• <b>Infix to Postfix Conversion Rules (Shunting-Yard '
                                              'Algorithm):</b><br/>\n'
                                              '&nbsp;&nbsp;1. Scan infix expression from left to right.<br/>\n'
                                              '&nbsp;&nbsp;2. If operand (number/variable): Output it directly.<br/>\n'
                                              "&nbsp;&nbsp;3. If '(': Push to stack.<br/>\n"
                                              "&nbsp;&nbsp;4. If ')': Pop and output operators from stack until "
                                              "matching '(' is found. Discard both parentheses.<br/>\n"
                                              '&nbsp;&nbsp;5. If operator op: While stack is non-empty and '
                                              '<code>Precedence(Stack Top) ≥ Precedence(op)</code>, pop and output. '
                                              'Then push op onto stack.<br/>\n'
                                              '&nbsp;&nbsp;&nbsp;&nbsp;<i>Exception:</i> For Right-to-Left associative '
                                              'operators (like exponentiation <code>^</code>), pop only if strictly '
                                              'greater.<br/><br/>\n'
                                              '\n'
                                              '• <b>Evaluating Postfix Expression using Stack:</b><br/>\n'
                                              '&nbsp;&nbsp;- Scan postfix from left to right.<br/>\n'
                                              '&nbsp;&nbsp;- If operand: Push onto stack.<br/>\n'
                                              '&nbsp;&nbsp;- If operator: Pop two operands: <code>op2 = pop()</code>, '
                                              '<code>op1 = pop()</code>. Compute <code>result = op1 (operator) '
                                              'op2</code>. Push result back onto stack!',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: In postfix evaluation: First popped is the '
                                                   'RIGHT operand (op2), second popped is the LEFT operand (op1)! For '
                                                   'non-commutative operations like division (op1 / op2) and '
                                                   'subtraction (op1 - op2), order is critical.',
                                   'number': '14.1',
                                   'title': 'Stack Infix, Postfix & Evaluation Algorithms'},
                                 { 'content': '• <b>Circular Queue Modulo Arithmetic:</b><br/>\n'
                                              "&nbsp;&nbsp;- Solves the 'false overflow' problem of linear array "
                                              'queues.<br/>\n'
                                              '&nbsp;&nbsp;• <b>Enqueue:</b> <code>rear = (rear + 1) % Capacity; '
                                              'queue[rear] = item;</code><br/>\n'
                                              '&nbsp;&nbsp;• <b>Dequeue:</b> <code>item = queue[front]; front = (front '
                                              '+ 1) % Capacity;</code><br/>\n'
                                              '&nbsp;&nbsp;• <b>Queue Full Condition:</b> <code>(rear + 1) % Capacity '
                                              '== front</code> (one slot left empty to distinguish full from '
                                              'empty).<br/>\n'
                                              '&nbsp;&nbsp;• <b>Queue Empty Condition:</b> <code>front == '
                                              'rear</code>.<br/><br/>\n'
                                              '\n'
                                              '• <b>Implementing a Queue using Two Stacks (Stack1 and '
                                              'Stack2):</b><br/>\n'
                                              '&nbsp;&nbsp;• <b>Enqueue(x):</b> Push x onto Stack1. (O(1)).<br/>\n'
                                              '&nbsp;&nbsp;• <b>Dequeue():</b> If Stack2 is empty, pop ALL elements '
                                              'from Stack1 and push them into Stack2 (reverses order!). Then pop from '
                                              'Stack2. (Amortized O(1) time).',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: An array of size N can hold at most N - 1 '
                                                   'elements in a standard circular queue if front == rear indicates '
                                                   'empty.',
                                   'number': '14.2',
                                   'title': 'Circular Queues & Two-Stack Queue Implementation'},
                                 { 'content': '• <b>Singly vs Doubly Linked List Time Complexities:</b><br/>\n'
                                              '&nbsp;&nbsp;• Insertion at head: O(1).<br/>\n'
                                              '&nbsp;&nbsp;• Deletion of given node: O(1) in Doubly Linked List; O(n) '
                                              'in Singly (need predecessor pointer).<br/><br/>\n'
                                              '\n'
                                              "• <b>Floyd's Tortoise and Hare Cycle Detection:</b><br/>\n"
                                              '&nbsp;&nbsp;• Use two pointers: <code>slow</code> (advances 1 step) and '
                                              '<code>fast</code> (advances 2 steps).<br/>\n'
                                              '&nbsp;&nbsp;• <b>Loop Detection:</b> If <code>slow == fast</code> at '
                                              'any point, a cycle exists!<br/>\n'
                                              '&nbsp;&nbsp;• <b>Finding Start Node of Cycle:</b> When slow and fast '
                                              'meet, reset <code>slow = head</code> and keep <code>fast</code> at '
                                              'meeting point. Move both at 1 step per cycle. <b>They will meet exactly '
                                              'at the cycle start node!</b>',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Reversing a singly linked list in-place '
                                                   'takes O(n) time and O(1) auxiliary space using 3 pointers: prev, '
                                                   'curr, next.',
                                   'number': '14.3',
                                   'title': "Linked Lists & Floyd's Cycle Finding Algorithm"}],
                'real_life_examples': [ { 'text': 'Every webpage URL you visit is pushed onto a navigation stack. '
                                                  "Clicking 'Back' pops the current page and reveals the previous URL.",
                                          'title': 'Real-Life Analogy: The Browser Back Button'}],
                'title': 'Linear Data Structures - Stacks, Queues & Linked Lists',
                'worked_examples': [ { 'answer': 'Postfix expression: A B C D ^ E - * +',
                                       'problem': 'Convert the infix expression: A + B * (C ^ D - E) into postfix '
                                                  'notation.',
                                       'steps': [ "Step 1: Scan 'A' ⇒ Output: A. Stack: [].",
                                                  "Step 2: Scan '+' ⇒ Stack: [+].",
                                                  "Step 3: Scan 'B' ⇒ Output: A B. Stack: [+].",
                                                  "Step 4: Scan '*' ⇒ Precedence(*) > Precedence(+), so push. Stack: "
                                                  '[+, *].',
                                                  "Step 5: Scan '(' ⇒ Push to stack. Stack: [+, *, (].",
                                                  "Step 6: Scan 'C' ⇒ Output: A B C. Stack: [+, *, (].",
                                                  "Step 7: Scan '^' ⇒ Push. Stack: [+, *, (, ^].",
                                                  "Step 8: Scan 'D' ⇒ Output: A B C D. Stack: [+, *, (, ^].",
                                                  "Step 9: Scan '-' ⇒ Precedence(-) < Precedence(^), so pop '^'. "
                                                  "Output: A B C D ^. Push '-'. Stack: [+, *, (, -].",
                                                  "Step 10: Scan 'E' ⇒ Output: A B C D ^ E. Stack: [+, *, (, -].",
                                                  "Step 11: Scan ')' ⇒ Pop until '(': pops '-'. Output: A B C D ^ E -. "
                                                  "Discard '('. Stack: [+, *].",
                                                  "Step 12: End of input reached. Pop remaining operators: '*' then "
                                                  "'+'. Output: A B C D ^ E - * +."],
                                       'title': 'Worked Example: Infix to Postfix Conversion'}]},
  ('PDS', 2): { 'chapter_number': 15,
                'exam_traps': [ { 'title': 'Heap Search Complexity Trap',
                                  'warning': 'Searching for an arbitrary key in a binary heap takes O(n) time, NOT '
                                             'O(log n)! A heap is not a BST; there is no relationship between left and '
                                             'right siblings.'}],
                'foundations': [ { 'content': '• <b>Fundamental Binary Tree Properties:</b><br/>\n'
                                              '&nbsp;&nbsp;1. In any binary tree, the number of leaf nodes L is '
                                              'related to the number of nodes of degree 2 (n₂) by:<br/>\n'
                                              '&nbsp;&nbsp;&nbsp;&nbsp;<b><code>L = n₂ + 1</code></b> (Leaf nodes = '
                                              'Internal nodes with 2 children + 1).<br/>\n'
                                              '&nbsp;&nbsp;2. Maximum nodes in a binary tree of height h: <code>N_max '
                                              '= 2^(h + 1) - 1</code> (taking root height = 0).<br/>\n'
                                              '&nbsp;&nbsp;3. Minimum height of a binary tree with N nodes: '
                                              '<code>h_min = ⌈log₂(N + 1)⌉ - 1</code>.<br/><br/>\n'
                                              '\n'
                                              '• <b>Tree Traversals:</b><br/>\n'
                                              '&nbsp;&nbsp;• <b>Preorder:</b> Root → Left → Right.<br/>\n'
                                              '&nbsp;&nbsp;• <b>Inorder:</b> Left → Root → Right.<br/>\n'
                                              '&nbsp;&nbsp;• <b>Postorder:</b> Left → Right → Root.<br/>\n'
                                              '&nbsp;&nbsp;• <b>Level-Order:</b> Breadth-first using a '
                                              'queue.<br/><br/>\n'
                                              '\n'
                                              '• <b>Tree Reconstruction:</b><br/>\n'
                                              '&nbsp;&nbsp;- To construct a <b>unique</b> binary tree, you MUST have '
                                              'the <b>INORDER traversal</b> along with either PREORDER or POSTORDER '
                                              'traversal!<br/>\n'
                                              '&nbsp;&nbsp;- Given only Preorder and Postorder, a unique tree CANNOT '
                                              'be constructed unless every internal node has exactly 2 children '
                                              '(Strict binary tree).',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: The Inorder traversal of a Binary Search '
                                                   'Tree (BST) ALWAYS yields elements in strictly increasing sorted '
                                                   'order! This is the #1 property used in GATE tree questions.',
                                   'number': '15.1',
                                   'title': 'Binary Tree Mathematical Properties & Traversals'},
                                 { 'content': '• <b>BST Property:</b> For every node X: all keys in Left Subtree < '
                                              'X.key < all keys in Right Subtree.<br/><br/>\n'
                                              '\n'
                                              '• <b>Operations & Time Complexity:</b><br/>\n'
                                              '&nbsp;&nbsp;• Search, Insertion, Deletion: Average case = <code>O(log '
                                              'n)</code>; Worst case (skewed tree) = <code>O(n)</code>.<br/>\n'
                                              '&nbsp;&nbsp;• <b>Deletion Cases:</b><br/>\n'
                                              '&nbsp;&nbsp;&nbsp;&nbsp;1. Node is a leaf: Simply remove it.<br/>\n'
                                              '&nbsp;&nbsp;&nbsp;&nbsp;2. Node has 1 child: Replace node with its '
                                              'child.<br/>\n'
                                              '&nbsp;&nbsp;&nbsp;&nbsp;3. Node has 2 children: Replace with its '
                                              '<b>Inorder Predecessor</b> (max in left subtree) OR <b>Inorder '
                                              'Successor</b> (min in right subtree).<br/><br/>\n'
                                              '\n'
                                              '• <b>Counting Structurally Unique BSTs (Catalan Numbers):</b><br/>\n'
                                              '&nbsp;&nbsp;Number of structurally distinct BSTs possible with n '
                                              'unlabeled nodes equals the n-th Catalan number:<br/>\n'
                                              '&nbsp;&nbsp;<code>Cₙ = (1 / (n + 1)) × ²ⁿCₙ</code>.<br/>\n'
                                              '&nbsp;&nbsp;Standard values: C₁ = 1, C₂ = 2, C₃ = 5, C₄ = 14, C₅ = '
                                              '42.<br/>\n'
                                              '&nbsp;&nbsp;If n keys are distinct and labeled, total trees = <code>n! '
                                              '× Cₙ</code>.',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: To find Inorder Successor of node X: If X '
                                                   'has a right child, it is the leftmost node in right subtree. If X '
                                                   'has NO right child, it is the lowest ancestor whose left subtree '
                                                   'contains X.',
                                   'number': '15.2',
                                   'title': 'Binary Search Trees (BST) & Catalan Numbers'},
                                 { 'content': '• <b>What is a Binary Heap?</b><br/>\n'
                                              '&nbsp;&nbsp;A <b>Complete Binary Tree (CBT)</b> stored compactly in an '
                                              'array that satisfies the heap property:<br/>\n'
                                              '&nbsp;&nbsp;• <b>Max-Heap:</b> <code>Parent ≥ Children</code> (Root is '
                                              'maximum).<br/>\n'
                                              '&nbsp;&nbsp;• <b>Min-Heap:</b> <code>Parent ≤ Children</code> (Root is '
                                              'minimum).<br/><br/>\n'
                                              '\n'
                                              '• <b>Array Index Mapping (1-Based Indexing):</b><br/>\n'
                                              '&nbsp;&nbsp;• Parent of node i: <code>⌊i / 2⌋</code>.<br/>\n'
                                              '&nbsp;&nbsp;• Left Child of node i: <code>2i</code>.<br/>\n'
                                              '&nbsp;&nbsp;• Right Child of node i: <code>2i + 1</code>.<br/>\n'
                                              '&nbsp;&nbsp;• Leaves reside from index <code>⌊n / 2⌋ + 1</code> to '
                                              '<code>n</code>.<br/><br/>\n'
                                              '\n'
                                              '• <b>Time Complexities of Heap Operations:</b><br/>\n'
                                              '&nbsp;&nbsp;• Insertion: <code>O(log n)</code> (bubbling up).<br/>\n'
                                              '&nbsp;&nbsp;• Extract-Max / Extract-Min: <code>O(log n)</code> (heapify '
                                              'down).<br/>\n'
                                              '&nbsp;&nbsp;• <b>BUILD-HEAP (from arbitrary array):</b> Takes <b>O(n) '
                                              'time</b> (NOT O(n log n)!).<br/>\n'
                                              '&nbsp;&nbsp;&nbsp;&nbsp;<i>Why?</i> Most nodes are near the leaves '
                                              'where height is small: ∑ (h / 2ʰ) converges to a constant!',
                                   'crucial_rule': '🎯 GOLDEN RULE FOR GATE: Build-Heap takes strictly O(n) linear '
                                                   'time. Heap-Sort takes O(n log n) time because Extract-Max is '
                                                   'called n times.',
                                   'number': '15.3',
                                   'title': 'Binary Heaps & Bottom-Up O(n) Build-Heap'}],
                'real_life_examples': [ { 'text': 'A priority queue (heap) manages emergency patients. The patient '
                                                  'with the highest medical severity is always at the root and treated '
                                                  'first, regardless of arrival order.',
                                          'title': 'Real-Life Analogy: Hospital Emergency Room Triage'}],
                'title': 'Trees, BST & Binary Heaps',
                'worked_examples': [ { 'answer': 'Postorder: D, E, B, F, C, A',
                                       'problem': 'Given Preorder: [A, B, D, E, C, F] and Inorder: [D, B, E, A, F, C], '
                                                  'find the Postorder traversal.',
                                       'steps': [ 'Step 1: First element of Preorder is root ⇒ Root = A.',
                                                  'Step 2: Find A in Inorder: [D, B, E] are in Left Subtree; [F, C] '
                                                  'are in Right Subtree.',
                                                  'Step 3: In Preorder, next elements for Left Subtree are [B, D, E] '
                                                  'with root = B.',
                                                  'Step 4: In Inorder [D, B, E], D is left child of B, E is right '
                                                  'child of B.',
                                                  'Step 5: For Right Subtree [F, C], Preorder has [C, F] with root = '
                                                  'C. In Inorder [F, C], F is left child of C.',
                                                  'Step 6: Compute Postorder (Left, Right, Root): D, E, B, F, C, A.'],
                                       'title': 'Worked Example: Reconstructing Tree from Inorder and Preorder'}]}}
