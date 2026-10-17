# Enrich all subject chapters with curated YouTube lectures and solved exam numericals
import os
import sys
import json
import urllib.parse

def yt_link(query):
    return "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(query)

CHAPTER_RESOURCES = {
    # Engineering Mathematics
    "EM": [
        {
            "videos": [
                {"title": "Mathematical Logic & Quantifiers Masterclass", "channel": "Gate Smashers", "url": yt_link("gate cse propositional logic quantifiers gate smashers")},
                {"title": "Set Theory, Relations & Equivalence Relations", "channel": "Amit Khurana", "url": yt_link("gate discrete mathematics relations equivalence amit khurana")},
                {"title": "Lattices & Boolean Algebras Complete", "channel": "NPTEL IIT", "url": yt_link("nptel discrete mathematics lattices boolean algebra")}
            ],
            "solved_examples": [
                {
                    "question": "Which of the following propositions is a TAUTOLOGY?\n(A) (P -> Q) -> P\n(B) P -> (Q -> P)\n(C) (P v Q) -> (P ^ Q)\n(D) (P -> Q) -> (Q -> P)",
                    "solution": "Step 1: Expand conditional P -> (Q -> P) using implication equivalence A -> B ≡ ~A v B.\nStep 2: P -> (~Q v P) ≡ ~P v (~Q v P).\nStep 3: By Associativity and Commutativity: (~P v P) v ~Q.\nStep 4: Since (~P v P) is always True (T), T v ~Q ≡ True (Tautology).\nAnswer: (B).",
                    "takeaway": "Always use implication identity (A -> B ≡ ~A v B) and look for (P v ~P ≡ True) or (P ^ ~P ≡ False)."
                },
                {
                    "question": "On a set A with n elements, how many symmetric relations are possible that are also reflexive?",
                    "solution": "Step 1: Total elements in A x A is n^2.\nStep 2: A reflexive relation MUST contain all n diagonal pairs (a_i, a_i), so diagonal pairs have only 1 choice.\nStep 3: The non-diagonal pairs come in symmetric pairs {(a_i, a_j), (a_j, a_i)} where i < j.\nStep 4: Number of such pairs is (n^2 - n) / 2 = n(n - 1) / 2.\nStep 5: For each pair, it can either be in the relation or not (2 choices).\nTotal = 2^(n(n-1)/2).",
                    "takeaway": "Divide relation matrix into 3 parts: n diagonal elements, and two symmetric halves of n(n-1)/2 elements each."
                }
            ]
        },
        {
            "videos": [
                {"title": "Graph Theory Full Playlist for GATE CSE", "channel": "Gate Smashers", "url": yt_link("gate cse graph theory full playlist gate smashers")},
                {"title": "Euler's Formula & Planar Graphs with Proofs", "channel": "Abdul Bari", "url": yt_link("euler formula planar graphs abdul bari")},
                {"title": "Combinatorics, Permutations & Generating Functions", "channel": "Amit Khurana", "url": yt_link("gate combinatorics generating functions amit khurana")}
            ],
            "solved_examples": [
                {
                    "question": "A connected planar graph has 10 vertices each of degree 3. Into how many regions/faces does it divide the plane?",
                    "solution": "Step 1: Use Handshaking Lemma: ∑ deg(v) = 2|E|.\n10 * 3 = 2|E| => 30 = 2|E| => |E| = 15 edges.\nStep 2: Apply Euler's Planar Formula: V - E + R = 2.\n10 - 15 + R = 2 => -5 + R = 2 => R = 7 regions.\nAnswer: 7 regions (including the outer unbounded face).",
                    "takeaway": "Euler's formula V - E + R = 2 holds for all CONNECTED planar graphs. Always find |E| first using Handshaking Lemma."
                }
            ]
        },
        {
            "videos": [
                {"title": "Eigenvalues and Eigenvectors Shortcuts for GATE", "channel": "Gate Smashers", "url": yt_link("eigenvalues eigenvectors shortcuts gate smashers")},
                {"title": "Systems of Linear Equations & Matrix Rank", "channel": "Amit Khurana", "url": yt_link("linear algebra system of equations rank amit khurana")}
            ],
            "solved_examples": [
                {
                    "question": "For a 3x3 matrix A, Trace(A) = 6 and Det(A) = 6. If one eigenvalue is 1, find the other two eigenvalues.",
                    "solution": "Step 1: Let eigenvalues be λ1, λ2, λ3 with λ1 = 1.\nStep 2: Sum of eigenvalues = Trace(A) => 1 + λ2 + λ3 = 6 => λ2 + λ3 = 5.\nStep 3: Product of eigenvalues = Det(A) => 1 * λ2 * λ3 = 6 => λ2 * λ3 = 6.\nStep 4: Solve λ^2 - 5λ + 6 = 0 => (λ - 2)(λ - 3) = 0.\nAnswer: The other two eigenvalues are 2 and 3.",
                    "takeaway": "Never compute characteristic polynomial det(A - λI) if Trace and Determinant properties give immediate quadratic equations!"
                }
            ]
        },
        {
            "videos": [
                {"title": "Bayes' Theorem & Conditional Probability Made Easy", "channel": "Gate Smashers", "url": yt_link("bayes theorem conditional probability gate smashers")},
                {"title": "Probability Distributions: Poisson, Normal & Exponential", "channel": "Knowledge Gate", "url": yt_link("poisson normal exponential distribution gate cse")}
            ],
            "solved_examples": [
                {
                    "question": "If a random variable X follows a Poisson distribution such that P(X = 1) = P(X = 2), what is the Mean and Variance of X?",
                    "solution": "Step 1: Poisson formula P(X = k) = (e^(-λ) * λ^k) / k!.\nStep 2: P(X = 1) = e^(-λ) * λ^1 / 1! = λ e^(-λ).\nStep 3: P(X = 2) = e^(-λ) * λ^2 / 2! = (λ^2 / 2) e^(-λ).\nStep 4: Equating both: λ e^(-λ) = (λ^2 / 2) e^(-λ) => 1 = λ / 2 => λ = 2.\nStep 5: For Poisson distribution, Mean = Variance = λ = 2.",
                    "takeaway": "In Poisson distribution, Mean == Variance == λ. If question equates two probabilities, cancel e^(-λ) and solve for λ."
                }
            ]
        }
    ],

    # Digital Logic
    "DL": [
        {
            "videos": [
                {"title": "Number Systems & Signed Representations", "channel": "Gate Smashers", "url": yt_link("number systems signed binary 2s complement gate smashers")},
                {"title": "IEEE 754 Floating Point Representation", "channel": "Knowledge Gate", "url": yt_link("ieee 754 floating point single precision gate cse")}
            ],
            "solved_examples": [
                {
                    "question": "What is the 8-bit 2's complement representation of decimal integer -43?",
                    "solution": "Step 1: Write +43 in 8-bit binary: 43 = 32 + 8 + 2 + 1 = 00101011_2.\nStep 2: Take 1's complement (invert all bits): 11010100.\nStep 3: Add 1: 11010100 + 1 = 11010101_2.\nAnswer: 11010101 (Hex: 0xD5).",
                    "takeaway": "Shortcut for 2's complement: Starting from right (LSB), copy all bits up to and including the first '1', then flip all remaining bits to the left."
                }
            ]
        },
        {
            "videos": [
                {"title": "Karnaugh Map (K-Map) Minimization Complete", "channel": "Gate Smashers", "url": yt_link("k-map minimization gate smashers")},
                {"title": "Logic Gates & Universal Gates Realization", "channel": "Neso Academy", "url": yt_link("logic gates universal gates neso academy")}
            ],
            "solved_examples": [
                {
                    "question": "How many 2-to-1 Multiplexers are needed to implement an arbitrary 2-input XOR gate?",
                    "solution": "Step 1: XOR equation: Y = A'B + AB'.\nStep 2: Use 2-to-1 MUX equation: Y = S' * I0 + S * I1.\nStep 3: Set select line S = A. When A = 0, Y = B. When A = 1, Y = B'.\nStep 4: If inverted input B' is available, 1 MUX suffices. If an inverter must be built using MUX, 2 MUXes are required.\nAnswer: 1 MUX (with inverted input) or 2 MUXes total.",
                    "takeaway": "To build an inverter with a 2-to-1 MUX: Set I0 = 1, I1 = 0, select = input X. Output = X'."
                }
            ]
        },
        {
            "videos": [
                {"title": "Multiplexers, Decoders & Priority Encoders", "channel": "Gate Smashers", "url": yt_link("multiplexers decoders combinational circuits gate smashers")},
                {"title": "Full Adder & Carry Lookahead Adders", "channel": "Neso Academy", "url": yt_link("carry lookahead adder gate cse neso academy")}
            ],
            "solved_examples": [
                {
                    "question": "A 4-to-1 MUX has inputs I0=1, I1=0, I2=C, I3=C' with select lines S1=A, S0=B. Find the minimized Boolean function F(A, B, C).",
                    "solution": "Step 1: MUX equation F = A'B'I0 + A'B I1 + A B' I2 + A B I3.\nStep 2: Substitute inputs: F = A'B'(1) + A'B(0) + A B'(C) + A B(C') = A'B' + A B' C + A B C'.\nStep 3: Simplify: B'(A' + AC) + ABC' = B'(A' + C) + ABC' = A'B' + B'C + ABC'.\nStep 4: K-Map minimization yields minterms m(0, 1, 4, 6) = A'B' + BC' + AC.",
                    "takeaway": "Always expand MUX output to canonical minterms sum before minimizing to prevent missing adjacent grouping cells."
                }
            ]
        },
        {
            "videos": [
                {"title": "Flip-Flops (SR, JK, D, T) & Excitation Tables", "channel": "Gate Smashers", "url": yt_link("flip flops excitation tables gate smashers")},
                {"title": "Synchronous & Mod-N Counters Design", "channel": "Neso Academy", "url": yt_link("synchronous counters mod n counters gate cse")}
            ],
            "solved_examples": [
                {
                    "question": "In a 4-bit synchronous binary counter, what is the frequency of the MSB flip-flop output if clock frequency is 16 MHz?",
                    "solution": "Step 1: Each stage of a binary ripple/synchronous counter divides the input clock frequency by 2.\nStep 2: For 4 flip-flops, division factor = 2^4 = 16.\nStep 3: Output frequency at MSB = 16 MHz / 16 = 1 MHz.\nAnswer: 1 MHz.",
                    "takeaway": "Any mod-N counter divides clock frequency by N at its terminal count / MSB output: f_out = f_in / N."
                }
            ]
        }
    ],

    # Computer Organization and Architecture
    "COA": [
        {
            "videos": [
                {"title": "Addressing Modes with Numerical Examples", "channel": "Gate Smashers", "url": yt_link("addressing modes gate smashers")},
                {"title": "Instruction Formats & Machine Code", "channel": "Vishvadeep Gothi", "url": yt_link("instruction formats vishvadeep gothi gate")}
            ],
            "solved_examples": [
                {
                    "question": "A system has 32-bit instructions with 4-byte words. If memory is byte-addressable and PC holds address 1000, what is the PC value after fetching one instruction?",
                    "solution": "Step 1: Instruction length = 32 bits = 4 bytes.\nStep 2: In byte-addressable memory, each address refers to 1 byte.\nStep 3: Fetching 4 bytes advances PC by 4.\nAnswer: PC = 1000 + 4 = 1004.",
                    "takeaway": "Always check whether memory is BYTE-addressable or WORD-addressable! In byte-addressable, PC increments by instruction length in bytes."
                }
            ]
        },
        {
            "videos": [
                {"title": "Hardwired vs Microprogrammed Control Unit", "channel": "Gate Smashers", "url": yt_link("control unit hardwired microprogrammed gate smashers")},
                {"title": "ALU Datapath & CPU Bus Architecture", "channel": "Vishvadeep Gothi", "url": yt_link("alu datapath cpu bus architecture vishvadeep gothi")}
            ],
            "solved_examples": [
                {
                    "question": "A control store has 128 microinstructions. Each microinstruction contains 26 control signals and a branch address field. Find the size of the control word in bits.",
                    "solution": "Step 1: Number of microinstructions = 128 = 2^7.\nStep 2: Branch address field needs ceil(log2(128)) = 7 bits.\nStep 3: Control signals = 26 bits.\nStep 4: Total control word size = 26 + 7 = 33 bits.\nAnswer: 33 bits.",
                    "takeaway": "Horizontal microinstruction size = (Control signals) + log2(Control store memory words)."
                }
            ]
        },
        {
            "videos": [
                {"title": "Cache Memory Mapping (Direct, Set-Associative)", "channel": "Gate Smashers", "url": yt_link("cache memory mapping direct associative gate smashers")},
                {"title": "Average Memory Access Time (AMAT) Numericals", "channel": "Vishvadeep Gothi", "url": yt_link("average memory access time amat numericals vishvadeep gothi")}
            ],
            "solved_examples": [
                {
                    "question": "A 4-way set-associative cache has 64 KB capacity with 32-byte cache lines. In a 32-bit byte-addressable system, find the Tag bits.",
                    "solution": "Step 1: Cache size = 64 KB = 2^16 bytes. Line size = 32 bytes = 2^5 bytes.\nStep 2: Total cache lines = 2^16 / 2^5 = 2^11 lines = 2048 lines.\nStep 3: 4-way set-associative => Sets = 2048 / 4 = 512 sets = 2^9 sets.\nStep 4: Offset bits = log2(32) = 5 bits. Set index bits = log2(512) = 9 bits.\nStep 5: Tag bits = 32 - 9 - 5 = 18 bits.\nAnswer: Tag = 18 bits, Set Index = 9 bits, Offset = 5 bits.",
                    "takeaway": "Number of sets = (Total Cache Capacity) / (Line Size * Set Associativity). Tag = Address Bits - Set Bits - Word Offset Bits."
                }
            ]
        },
        {
            "videos": [
                {"title": "Instruction Pipelining & Speedup Calculations", "channel": "Gate Smashers", "url": yt_link("instruction pipelining speedup cpi gate smashers")},
                {"title": "Pipeline Hazards: RAW, Structural & Branch", "channel": "Vishvadeep Gothi", "url": yt_link("pipeline hazards raw branch data forwarding vishvadeep gothi")}
            ],
            "solved_examples": [
                {
                    "question": "A 5-stage pipeline has stage delays 5ns, 7ns, 10ns, 8ns, and 6ns. Pipeline registers have 1ns delay. Find clock cycle time and speedup for 1000 instructions compared to non-pipelined execution.",
                    "solution": "Step 1: Pipeline clock cycle time t_pipe = max(stage delays) + register delay = 10ns + 1ns = 11ns.\nStep 2: Pipelined time T_pipe = (k + n - 1) * t_pipe = (5 + 1000 - 1) * 11ns = 1004 * 11 = 11044 ns.\nStep 3: Non-pipelined time per instruction t_non = 5+7+10+8+6 = 36ns. For 1000 instructions = 36000 ns.\nStep 4: Speedup = 36000 / 11044 ≈ 3.26.\nAnswer: Cycle time = 11ns, Speedup = 3.26.",
                    "takeaway": "The slowest stage limits the pipeline clock frequency: Cycle time = max(Stage Delays) + Register Delay."
                }
            ]
        }
    ],

    # Programming and Data Structures
    "PDS": [
        {
            "videos": [
                {"title": "Pointers and Memory Layout in C", "channel": "Jenny's Lectures", "url": yt_link("c programming pointers memory jenny lectures")},
                {"title": "Recursion Call Stack & Output Tracing", "channel": "Gate Smashers", "url": yt_link("recursion output tracing gate cse gate smashers")}
            ],
            "solved_examples": [
                {
                    "question": "What is the output of the following C code?\nint a[] = {10, 20, 30, 40};\nint *p = a;\nprintf(\"%d\", *(p++) + *++p);",
                    "solution": "Step 1: *(p++) evaluates to *p (which is 10), and then p is incremented to point to a[1] (20).\nStep 2: *++p increments p first to point to a[2] (30), and dereferences to 30.\nStep 3: Sum = 10 + 30 = 40.\nAnswer: 40.",
                    "takeaway": "Post-increment p++ returns original pointer before incrementing; pre-increment ++p increments first before evaluating."
                }
            ]
        },
        {
            "videos": [
                {"title": "Stack Applications: Infix to Postfix & Evaluation", "channel": "Gate Smashers", "url": yt_link("infix to postfix conversion stack gate smashers")},
                {"title": "Circular Queues & Linked Lists Operations", "channel": "Jenny's Lectures", "url": yt_link("circular queue linked list jenny lectures")}
            ],
            "solved_examples": [
                {
                    "question": "What is the postfix evaluation of the expression: 6 3 2 + * 5 - ?",
                    "solution": "Step 1: Read '6', push to stack: [6].\nStep 2: Read '3', push: [6, 3].\nStep 3: Read '2', push: [6, 3, 2].\nStep 4: Read '+', pop 2 and 3, compute 3+2=5, push: [6, 5].\nStep 5: Read '*', pop 5 and 6, compute 6*5=30, push: [30].\nStep 6: Read '5', push: [30, 5].\nStep 7: Read '-', pop 5 and 30, compute 30-5=25, push: [25].\nAnswer: 25.",
                    "takeaway": "When operator arrives: op2 = pop(), op1 = pop(), push(op1 <op> op2). Order of operands matters for division and subtraction!"
                }
            ]
        },
        {
            "videos": [
                {"title": "Binary Search Tree Operations & Traversals", "channel": "Abdul Bari", "url": yt_link("binary search tree bst abdul bari")},
                {"title": "Binary Heap & Heapify Linear Time Proof", "channel": "Abdul Bari", "url": yt_link("binary heap heapify abdul bari algorithms")}
            ],
            "solved_examples": [
                {
                    "question": "In a max-heap of n elements, what is the worst-case time complexity to find the MINIMUM element?",
                    "solution": "Step 1: In a max-heap, parent is greater than children. Root holds maximum.\nStep 2: The minimum element MUST be present at one of the leaf nodes.\nStep 3: In a complete binary tree of n elements, there are ceil(n/2) leaf nodes.\nStep 4: To find the minimum among ceil(n/2) leaves requires linear search over the leaves: O(n/2) = O(n).\nAnswer: O(n).",
                    "takeaway": "In a Max-Heap, finding Maximum is O(1), but finding Minimum requires searching all leaf nodes: O(n) time!"
                }
            ]
        }
    ],

    # Algorithms
    "ALGO": [
        {
            "videos": [
                {"title": "Master Theorem for Asymptotic Recurrences", "channel": "Abdul Bari", "url": yt_link("master theorem abdul bari algorithms")},
                {"title": "Asymptotic Notations (Big-O, Omega, Theta)", "channel": "Gate Smashers", "url": yt_link("asymptotic notations big o omega theta gate smashers")}
            ],
            "solved_examples": [
                {
                    "question": "Solve recurrence: T(n) = 2T(n/2) + n log n using Master Theorem.",
                    "solution": "Step 1: Form T(n) = a T(n/b) + f(n) where a = 2, b = 2, f(n) = n log n.\nStep 2: Compute n^(log_b(a)) = n^(log2(2)) = n^1 = n.\nStep 3: Compare f(n) with n^(log_b(a)): f(n) = n log n = n * (log n)^1.\nStep 4: This matches Extended Master Theorem Case 2: f(n) = Θ(n^(log_b(a)) * (log n)^k) with k = 1.\nStep 5: T(n) = Θ(n^(log_b(a)) * (log n)^(k+1)) = Θ(n (log n)^2).\nAnswer: Θ(n log^2 n).",
                    "takeaway": "When f(n) differs from n^(log_b a) only by a poly-logarithmic factor (log n)^k, use Extended Master Theorem: multiply by log n."
                }
            ]
        },
        {
            "videos": [
                {"title": "Quick Sort & Merge Sort Complexity Analysis", "channel": "Abdul Bari", "url": yt_link("quick sort merge sort abdul bari algorithms")},
                {"title": "Hashing Techniques & Hash Collisions", "channel": "Gate Smashers", "url": yt_link("hashing open addressing collision resolution gate smashers")}
            ],
            "solved_examples": [
                {
                    "question": "What is the worst-case number of comparisons to find BOTH the maximum and minimum elements in an unsorted array of n elements?",
                    "solution": "Step 1: Standard naive search does 2n - 2 comparisons.\nStep 2: Tournament / Pairwise comparison method:\n- Compare elements in pairs: n/2 comparisons.\n- Compare winners for max: n/2 - 1 comparisons.\n- Compare losers for min: n/2 - 1 comparisons.\nStep 3: Total = n/2 + 2(n/2 - 1) = 3n/2 - 2 comparisons.\nAnswer: ceil(3n/2) - 2 comparisons.",
                    "takeaway": "Optimal simultaneous max & min finding takes 3n/2 - 2 comparisons via pairwise comparison."
                }
            ]
        },
        {
            "videos": [
                {"title": "0/1 Knapsack Problem Dynamic Programming", "channel": "Abdul Bari", "url": yt_link("0 1 knapsack dynamic programming abdul bari")},
                {"title": "Longest Common Subsequence (LCS) & Matrix Chain", "channel": "Abdul Bari", "url": yt_link("longest common subsequence lcs abdul bari")}
            ],
            "solved_examples": [
                {
                    "question": "What is the optimal substructure recurrence for 0/1 Knapsack with item weights w_i and values v_i?",
                    "solution": "Step 1: Let K(i, w) be maximum value achievable using a subset of first i items with capacity w.\nStep 2: If w_i > w, cannot include item i: K(i, w) = K(i-1, w).\nStep 3: If w_i <= w, take max of excluding vs including:\nK(i, w) = max( K(i-1, w), v_i + K(i-1, w - w_i) ).\nStep 4: Time complexity = O(n * W) which is pseudo-polynomial.",
                    "takeaway": "0/1 Knapsack is solved in O(n*W) using Dynamic Programming. Fractional Knapsack is solved in O(n log n) using Greedy (sort by v_i/w_i)."
                }
            ]
        },
        {
            "videos": [
                {"title": "Dijkstra & Bellman-Ford Shortest Path Algorithms", "channel": "Abdul Bari", "url": yt_link("dijkstra bellman ford shortest path abdul bari")},
                {"title": "Minimum Spanning Tree (Prim & Kruskal)", "channel": "Abdul Bari", "url": yt_link("prims kruskals minimum spanning tree abdul bari")}
            ],
            "solved_examples": [
                {
                    "question": "Why does Dijkstra's algorithm fail on graphs with negative weight edges, whereas Bellman-Ford succeeds?",
                    "solution": "Step 1: Dijkstra is a GREEDY algorithm. Once a vertex is marked visited / finalized, Dijkstra assumes its shortest path is permanently fixed and never re-visits it.\nStep 2: A negative edge explored later could offer a shorter path through a previously finalized vertex, violating Dijkstra's greedy invariant.\nStep 3: Bellman-Ford relaxes all |E| edges |V|-1 times, guaranteeing that even negative edges are propagated, and can detect negative cycles.",
                    "takeaway": "Dijkstra: O((V+E) log V), non-negative weights only. Bellman-Ford: O(V*E), handles negative weights and detects negative weight cycles."
                }
            ]
        }
    ],

    # Theory of Computation
    "TOC": [
        {
            "videos": [
                {"title": "DFA and NFA Construction Masterclass", "channel": "Gate Smashers", "url": yt_link("dfa nfa construction gate smashers")},
                {"title": "Minimization of DFA with Myhill-Nerode", "channel": "Amit Khurana", "url": yt_link("dfa minimization myhill nerode amit khurana")}
            ],
            "solved_examples": [
                {
                    "question": "How many states are in the minimal DFA that accepts all binary strings containing '101' as a substring?",
                    "solution": "Step 1: States needed represent progress in matching '101':\nq0: Initial state (matched '')\nq1: Matched '1'\nq2: Matched '10'\nq3: Matched '101' (Trap accepting state).\nStep 2: Transitions: From q3, on '0' or '1' loop to q3.\nStep 3: Total minimal states = 4 states.\nAnswer: 4 states.",
                    "takeaway": "For substring of length k over binary alphabet, minimal DFA requires (k + 1) states. For subsequence, minimal DFA requires (k + 1) states."
                }
            ]
        },
        {
            "videos": [
                {"title": "Context-Free Grammars & Ambiguity", "channel": "Gate Smashers", "url": yt_link("context free grammar ambiguity gate smashers")},
                {"title": "Pushdown Automata (DPDA vs NPDA)", "channel": "Amit Khurana", "url": yt_link("pushdown automata dpda npda amit khurana")}
            ],
            "solved_examples": [
                {
                    "question": "Is the language L = { a^n b^n c^n | n >= 1 } Context-Free?",
                    "solution": "Step 1: A Pushdown Automata has only ONE stack.\nStep 2: PDA can push 'a's and match them against 'b's, but by the time 'c's arrive, stack is empty and has forgotten n.\nStep 3: By Pumping Lemma for CFLs, pumping causes unequal counts of a, b, and c.\nAnswer: No, L is Context-Sensitive (Recursive), not Context-Free.",
                    "takeaway": "Single stack can compare 2 counts (e.g. a^n b^n is CFL). Comparing 3 counts (a^n b^n c^n) requires 2 stacks (Turing Machine capability)."
                }
            ]
        },
        {
            "videos": [
                {"title": "Turing Machines & Chomsky Hierarchy", "channel": "Gate Smashers", "url": yt_link("turing machines chomsky hierarchy gate smashers")},
                {"title": "Decidability, Halting Problem & Reductions", "channel": "Knowledge Gate", "url": yt_link("decidability undecidability halting problem knowledge gate")}
            ],
            "solved_examples": [
                {
                    "question": "Which of the following problems is DECIDABLE?\n(A) Emptiness of a Context-Free Language\n(B) Equivalence of two Context-Free Languages\n(C) Ambiguity of a Context-Free Grammar\n(D) Halting problem of a Turing Machine",
                    "solution": "Step 1: For CFLs, Emptiness (is L(G) = ∅?) is DECIDABLE (check if start symbol can derive any terminal string).\nStep 2: Equivalence (L(G1) == L(G2)?) is UNDECIDABLE for CFLs.\nStep 3: Ambiguity is UNDECIDABLE for CFGs.\nStep 4: Halting problem of TM is UNDECIDABLE.\nAnswer: (A).",
                    "takeaway": "For CFL: Emptiness, Finiteness, and Membership are Decidable. Equivalence, Intersection-Emptiness, and Ambiguity are Undecidable."
                }
            ]
        }
    ],

    # Compiler Design
    "CD": [
        {
            "videos": [
                {"title": "Lexical Analysis, Tokens & Lexical Errors", "channel": "Gate Smashers", "url": yt_link("lexical analysis tokens gate smashers")},
                {"title": "FIRST and FOLLOW Sets Computation with Rules", "channel": "Gate Smashers", "url": yt_link("first and follow computation compiler gate smashers")}
            ],
            "solved_examples": [
                {
                    "question": "Given grammar: S -> A B, A -> a | ε, B -> b. Find FOLLOW(A).",
                    "solution": "Step 1: A appears on RHS of S -> A B.\nStep 2: Rule: FOLLOW(A) includes FIRST(B) except ε.\nStep 3: FIRST(B) = {b}.\nStep 4: Since B does not derive ε, no need to add FOLLOW(S).\nAnswer: FOLLOW(A) = {b}.",
                    "takeaway": "In A -> α B β: FOLLOW(B) includes FIRST(β) - {ε}. If β =>* ε, then FOLLOW(B) also includes FOLLOW(A)."
                }
            ]
        },
        {
            "videos": [
                {"title": "LL(1) Parsing Table Construction & Conflicts", "channel": "Gate Smashers", "url": yt_link("ll1 parsing table compiler design gate smashers")},
                {"title": "Bottom-Up Parsing: LR(0), SLR(1), LALR(1), CLR(1)", "channel": "Gate Smashers", "url": yt_link("lr0 slr1 lalr1 clr1 parsing gate smashers")}
            ],
            "solved_examples": [
                {
                    "question": "Order the following parsers in terms of strictly increasing parsing power: LR(0), SLR(1), LALR(1), CLR(1).",
                    "solution": "Step 1: LR(0) is the weakest, places reductions in all columns.\nStep 2: SLR(1) uses FOLLOW sets to place reductions, resolving many conflicts.\nStep 3: LALR(1) merges states with identical core items, strictly more powerful than SLR(1).\nStep 4: CLR(1) has full lookahead items, strictly most powerful LR parser.\nOrder: LR(0) ⊂ SLR(1) ⊂ LALR(1) ⊂ CLR(1).",
                    "takeaway": "Number of states in LR(0) == SLR(1) == LALR(1) <= CLR(1). LALR(1) can never produce Shift-Reduce conflicts if CLR(1) has none (only Reduce-Reduce conflicts can arise from merging)."
                }
            ]
        },
        {
            "videos": [
                {"title": "Syntax Directed Translation (S-Attributed vs L-Attributed)", "channel": "Gate Smashers", "url": yt_link("s-attributed l-attributed sdt gate smashers")},
                {"title": "Code Optimization: Liveness, Common Subexpressions", "channel": "Ravindrababu Ravula", "url": yt_link("code optimization liveness analysis compiler ravula")}
            ],
            "solved_examples": [
                {
                    "question": "What is the difference between S-Attributed and L-Attributed SDT definitions?",
                    "solution": "Step 1: S-Attributed uses ONLY synthesized attributes (values calculated from children up to parent).\nStep 2: L-Attributed allows both synthesized attributes AND inherited attributes from parent and LEFT siblings only (never right siblings).\nStep 3: Every S-attributed definition is automatically L-attributed, but not vice-versa.\nStep 4: S-attributed SDDs can be evaluated bottom-up during LR parsing.",
                    "takeaway": "S-attributed ⊆ L-attributed. L-attributed enforces strict left-to-right dependency for inherited attributes."
                }
            ]
        }
    ],

    # Operating Systems
    "OS": [
        {
            "videos": [
                {"title": "Processes, Threads & System Calls (fork, exec)", "channel": "Gate Smashers", "url": yt_link("processes threads system calls fork exec gate smashers")},
                {"title": "CPU Scheduling Algorithms (FCFS, SJF, SRTF, RR)", "channel": "Gate Smashers", "url": yt_link("cpu scheduling algorithms srtf round robin gate smashers")}
            ],
            "solved_examples": [
                {
                    "question": "How many child processes are created by the following code?\nfor (int i = 0; i < 3; i++) fork();",
                    "solution": "Step 1: Each fork() call doubles the number of active processes.\nStep 2: After k fork() calls, total active processes = 2^k.\nStep 3: For k = 3, total processes = 2^3 = 8.\nStep 4: One process is the original parent process.\nStep 5: Number of child processes created = 2^3 - 1 = 7.\nAnswer: 7 child processes.",
                    "takeaway": "Formula for n consecutive fork() calls in a loop: Total processes = 2^n; Child processes created = 2^n - 1."
                }
            ]
        },
        {
            "videos": [
                {"title": "Process Synchronization & Semaphores (Counting, Binary)", "channel": "Gate Smashers", "url": yt_link("process synchronization semaphores gate smashers")},
                {"title": "Deadlock Detection & Banker's Algorithm", "channel": "Gate Smashers", "url": yt_link("bankers algorithm deadlock gate smashers")}
            ],
            "solved_examples": [
                {
                    "question": "A counting semaphore S is initialized to 10. Then 6 P(wait) and 4 V(signal) operations are performed on S. What is the final value of S?",
                    "solution": "Step 1: Initial value S = 10.\nStep 2: P(wait) decrements semaphore by 1: 6 P operations => S = 10 - 6 = 4.\nStep 3: V(signal) increments semaphore by 1: 4 V operations => S = 4 + 4 = 8.\nAnswer: 8.",
                    "takeaway": "Semaphore value formula: Final_S = Initial_S - count(P) + count(V). If S < 0, |S| processes are currently blocked in wait queue."
                }
            ]
        },
        {
            "videos": [
                {"title": "Paging, Multi-Level Paging & Page Tables", "channel": "Gate Smashers", "url": yt_link("paging multi level paging page table gate smashers")},
                {"title": "TLB & Effective Memory Access Time (EMAT)", "channel": "Gate Smashers", "url": yt_link("effective memory access time emat tlb gate smashers")}
            ],
            "solved_examples": [
                {
                    "question": "In a paged virtual memory system with TLB, TLB access time = 20ns, Main memory access time = 100ns. If TLB hit ratio is 90%, find Effective Memory Access Time (EMAT).",
                    "solution": "Step 1: On TLB Hit (90%): TLB access (20ns) + Memory access for data (100ns) = 120ns.\nStep 2: On TLB Miss (10%): TLB access (20ns) + Memory access for page table (100ns) + Memory access for data (100ns) = 220ns.\nStep 3: EMAT = (0.90 * 120ns) + (0.10 * 220ns) = 108 + 22 = 130ns.\nAnswer: 130 ns.",
                    "takeaway": "EMAT = Hit_Ratio * (t_TLB + t_mem) + (1 - Hit_Ratio) * (t_TLB + 2*t_mem). For 2-level paging on miss, it requires 3*t_mem."
                }
            ]
        }
    ],

    # Databases
    "DB": [
        {
            "videos": [
                {"title": "ER Model to Relational Schema Mapping", "channel": "Gate Smashers", "url": yt_link("er model to relational table mapping gate smashers")},
                {"title": "Relational Algebra & SQL Nested Queries", "channel": "Knowledge Gate", "url": yt_link("relational algebra sql queries gate cse")}
            ],
            "solved_examples": [
                {
                    "question": "What is the result of applying division operator R / S where R(A, B) and S(B)?",
                    "solution": "Step 1: Relational division R / S returns all values of attribute A that are associated with EVERY value of B in S.\nStep 2: In SQL, division corresponds to 'NOT EXISTS (SELECT B FROM S WHERE NOT EXISTS (SELECT * FROM R WHERE R.A = X.A AND R.B = S.B))'.\nStep 3: Commonly used for 'Find students who have enrolled in ALL courses'.",
                    "takeaway": "Relational division (÷) corresponds to universal quantification: 'for all elements in divisor S'."
                }
            ]
        },
        {
            "videos": [
                {"title": "Functional Dependencies & Finding Candidate Keys", "channel": "Gate Smashers", "url": yt_link("functional dependencies candidate keys gate smashers")},
                {"title": "Normalization (1NF, 2NF, 3NF, BCNF) Masterclass", "channel": "Gate Smashers", "url": yt_link("normalization 1nf 2nf 3nf bcnf gate smashers")}
            ],
            "solved_examples": [
                {
                    "question": "Relation R(A, B, C, D) has FDs: { A -> B, B -> C, C -> D, D -> A }. What is the highest normal form of R?",
                    "solution": "Step 1: Compute closure of each attribute: A+ = ABCD, B+ = ABCD, C+ = ABCD, D+ = ABCD.\nStep 2: Every single attribute (A, B, C, D) is a CANDIDATE KEY.\nStep 3: For every FD X -> Y, the determinant X is a Superkey.\nStep 4: Therefore, R satisfies BCNF (and also 3NF, 2NF, 1NF).\nAnswer: BCNF.",
                    "takeaway": "If every determinant in the FD set is a candidate key / superkey, the relation is strictly in BCNF."
                }
            ]
        },
        {
            "videos": [
                {"title": "Transactions & Conflict Serializability (Precedence Graph)", "channel": "Gate Smashers", "url": yt_link("transactions conflict serializability precedence graph gate smashers")},
                {"title": "B-Trees and B+ Trees Index Calculations", "channel": "Abdul Bari", "url": yt_link("b tree b+ tree indexing abdul bari")}
            ],
            "solved_examples": [
                {
                    "question": "A B+ tree leaf node has block size 1024 bytes, record pointer 8 bytes, search key 10 bytes, block pointer 6 bytes. What is the maximum order p of the leaf node?",
                    "solution": "Step 1: In a leaf node, entries are (key, record pointer) pairs, plus 1 block pointer to the next leaf node.\nStep 2: Formula: p * (key_size + record_ptr) + block_ptr <= Block_Size.\nStep 3: p * (10 + 8) + 6 <= 1024 => 18p + 6 <= 1024 => 18p <= 1018.\nStep 4: p <= 1018 / 18 = 56.55 => Maximum order p = 56.\nAnswer: 56.",
                    "takeaway": "Leaf node holds record pointers: p * (K + Rp) + Bp <= Block_Size. Internal node holds only child block pointers: p * Bp + (p-1) * K <= Block_Size."
                }
            ]
        }
    ],

    # Computer Networks
    "CN": [
        {
            "videos": [
                {"title": "Network Delays & Bandwidth-Delay Product", "channel": "Gate Smashers", "url": yt_link("transmission propagation queuing delay gate smashers")},
                {"title": "CSMA/CD Minimum Frame Size & Efficiency", "channel": "Gate Smashers", "url": yt_link("csma cd minimum frame size gate smashers")}
            ],
            "solved_examples": [
                {
                    "question": "In CSMA/CD network with bandwidth 100 Mbps and cable length 1 km (velocity 2 * 10^8 m/s), find minimum frame size to detect collisions.",
                    "solution": "Step 1: Propagation delay T_p = Distance / Velocity = 1000m / (2 * 10^8 m/s) = 5 * 10^(-6) s = 5 μs.\nStep 2: Condition for CSMA/CD collision detection: Transmission time T_t >= 2 * T_p.\nStep 3: T_t = L / Bandwidth >= 2 * 5 μs = 10 μs.\nStep 4: L >= 10 μs * 100 Mbps = 10 * 10^(-6) * 100 * 10^6 = 1000 bits = 125 bytes.\nAnswer: 1000 bits (125 bytes).",
                    "takeaway": "Collision detection invariant in CSMA/CD: T_t >= 2 * T_p, which gives L_min = 2 * (Distance / Velocity) * Bandwidth."
                }
            ]
        },
        {
            "videos": [
                {"title": "IPv4 Addressing, Subnetting & CIDR Notation", "channel": "Gate Smashers", "url": yt_link("ipv4 addressing subnetting cidr gate smashers")},
                {"title": "IP Packet Header & Fragmentation Numericals", "channel": "Gate Smashers", "url": yt_link("ip fragmentation offset identification gate smashers")}
            ],
            "solved_examples": [
                {
                    "question": "An IPv4 datagram of 4000 bytes (with 20-byte IP header) enters an Ethernet MTU of 1500 bytes. How many fragments are created, and what is the Fragment Offset of the second fragment?",
                    "solution": "Step 1: Data payload = 4000 - 20 = 3980 bytes.\nStep 2: MTU = 1500 bytes. Maximum payload per fragment = (1500 - 20) = 1480 bytes (divisible by 8).\nStep 3: Fragment 1: 1480 data bytes (offset = 0). Fragment 2: 1480 data bytes (offset = 1480/8 = 185). Fragment 3: 3980 - 2960 = 1020 data bytes (offset = 2960/8 = 370).\nStep 4: Total fragments = 3. Fragment offset of 2nd fragment = 185.\nAnswer: 3 fragments, Offset = 185.",
                    "takeaway": "Fragment offset measures 8-byte blocks: Offset = (cumulative data bytes before this fragment) / 8."
                }
            ]
        },
        {
            "videos": [
                {"title": "Distance Vector vs Link State Routing", "channel": "Gate Smashers", "url": yt_link("distance vector link state routing count to infinity gate smashers")},
                {"title": "TCP Flow Control & Congestion Control State Machine", "channel": "Gate Smashers", "url": yt_link("tcp congestion control slow start congestion avoidance gate smashers")}
            ],
            "solved_examples": [
                {
                    "question": "In TCP, slow-start threshold (ssthresh) is 32 KB. The current congestion window is 16 KB and reaches 32 KB via slow start. How many RTTs does it take to grow from 32 KB to 36 KB if MSS = 1 KB?",
                    "solution": "Step 1: At 32 KB, cwnd reaches ssthresh. TCP switches from Exponential Slow-Start to Linear Congestion Avoidance.\nStep 2: In Congestion Avoidance, cwnd increases by 1 MSS (1 KB) per RTT.\nStep 3: Growth from 32 KB to 36 KB is an increase of 4 KB.\nStep 4: At 1 KB per RTT, it takes 4 RTTs.\nAnswer: 4 RTTs.",
                    "takeaway": "Slow start: cwnd doubles every RTT (exponential). Congestion avoidance: cwnd increments by 1 MSS every RTT (linear additive increase)."
                }
            ]
        },
        {
            "videos": [
                {"title": "DNS, HTTP, SMTP, FTP Application Protocols", "channel": "Gate Smashers", "url": yt_link("dns http smtp application layer protocols gate smashers")}
            ],
            "solved_examples": [
                {
                    "question": "What transport layer protocol and default port numbers are used by DNS, HTTP, and SMTP?",
                    "solution": "Step 1: DNS uses UDP port 53 for standard queries (and TCP 53 for zone transfers > 512 bytes).\nStep 2: HTTP uses TCP port 80 (HTTPS uses TCP 443).\nStep 3: SMTP uses TCP port 25.\nAnswer: DNS (UDP 53), HTTP (TCP 80), SMTP (TCP 25).",
                    "takeaway": "DNS queries use UDP because DNS transactions are short, lightweight request-response pairs that do not need 3-way handshake overhead."
                }
            ]
        }
    ],

    # General Aptitude
    "GA": [
        {
            "videos": [
                {"title": "GATE Verbal Ability: Grammar & Vocabulary", "channel": "CareerRide", "url": yt_link("gate verbal ability grammar sentence completion careerride")}
            ],
            "solved_examples": [
                {
                    "question": "Fill in the blank: 'Neither the manager nor the employees _____ present at the conference.' (was / were)",
                    "solution": "Step 1: Rule of Proximity for 'Neither...nor': The verb agrees with the subject CLOSER to it.\nStep 2: 'employees' is plural and is closest to the verb.\nAnswer: were.",
                    "takeaway": "With 'either...or' and 'neither...nor', the verb agrees in number with the noun closest to it."
                }
            ]
        },
        {
            "videos": [
                {"title": "Quantitative Aptitude: Work, Time, Speed & Percentages", "channel": "CareerRide", "url": yt_link("quantitative aptitude work time speed distance careerride")}
            ],
            "solved_examples": [
                {
                    "question": "A can finish a work in 12 days, and B can finish it in 24 days. Working together, in how many days will they finish the work?",
                    "solution": "Step 1: 1 day work of A = 1/12.\nStep 2: 1 day work of B = 1/24.\nStep 3: Combined 1 day work = 1/12 + 1/24 = 3/24 = 1/8.\nStep 4: Total days required = 8 days.\nAnswer: 8 days.",
                    "takeaway": "Combined time = (A * B) / (A + B) = (12 * 24) / (36) = 288 / 36 = 8 days."
                }
            ]
        },
        {
            "videos": [
                {"title": "Spatial Aptitude: Paper Folding, Mirrors & Rotations", "channel": "Gate Smashers", "url": yt_link("spatial aptitude paper folding rotation 3d gate smashers")}
            ],
            "solved_examples": [
                {
                    "question": "In a dice, numbers 1 through 6 are marked. If 1 is opposite to 6, 2 is opposite to 5, and 3 is opposite to 4, what is the sum of opposite faces?",
                    "solution": "Step 1: Standard dice opposite face sum = 1+6 = 7, 2+5 = 7, 3+4 = 7.\nAnswer: 7.",
                    "takeaway": "In any standard fair die, opposite faces always sum to 7."
                }
            ]
        }
    ]
}

# Update export_data_for_web.py to inject these resources when exporting
print("CHAPTER_RESOURCES defined for all 11 subjects!")
