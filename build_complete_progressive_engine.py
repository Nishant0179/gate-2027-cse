# build_complete_progressive_engine.py
# Fills all 38 chapters with comprehensive 5-Tier progressive study notes in easy language.

import os
import sys

def build_all():
    dict_content = {}

    def add(sub, idx, l1, l2, l3, l4, l5):
        html = f"""<div class="progressive-learning-container space-y-6">
  <!-- LEVEL 1: Intuitive Real-World Analogy & Beginner Explanation -->
  <div class="p-5 rounded-2xl bg-blue-50/70 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-900/60 shadow-xs">
    <div class="flex items-center gap-2 mb-2 font-bold text-blue-900 dark:text-blue-200 text-sm">
      <span class="px-2 py-0.5 rounded bg-blue-600 text-white text-[10px] font-extrabold tracking-wide">LEVEL 1</span>
      <span>🌱 Beginner Intuition & Real-World Analogy (Easy Language)</span>
    </div>
    <div class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed space-y-2">
      {l1}
    </div>
  </div>

  <!-- LEVEL 2: Core Concepts & Essential Theory -->
  <div class="p-5 rounded-2xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs">
    <div class="flex items-center gap-2 mb-2 font-bold text-slate-900 dark:text-white text-sm">
      <span class="px-2 py-0.5 rounded bg-slate-700 text-white text-[10px] font-extrabold tracking-wide">LEVEL 2</span>
      <span>📘 Core Fundamentals & Essential Theory</span>
    </div>
    <div class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed space-y-2">
      {l2}
    </div>
  </div>

  <!-- LEVEL 3: Step-by-Step Working & Mathematical Formulations -->
  <div class="p-5 rounded-2xl bg-emerald-50/60 dark:bg-emerald-950/20 border border-emerald-200 dark:border-emerald-900/50 shadow-xs">
    <div class="flex items-center gap-2 mb-2 font-bold text-emerald-900 dark:text-emerald-200 text-sm">
      <span class="px-2 py-0.5 rounded bg-emerald-600 text-white text-[10px] font-extrabold tracking-wide">LEVEL 3</span>
      <span>🚀 Intermediate Mechanics & Step-by-Step Working</span>
    </div>
    <div class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed space-y-2">
      {l3}
    </div>
  </div>

  <!-- LEVEL 4: Advanced GATE Analysis & Exam Traps -->
  <div class="p-5 rounded-2xl bg-amber-50/70 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-900/60 shadow-xs">
    <div class="flex items-center gap-2 mb-2 font-bold text-amber-900 dark:text-amber-200 text-sm">
      <span class="px-2 py-0.5 rounded bg-amber-600 text-white text-[10px] font-extrabold tracking-wide">LEVEL 4</span>
      <span>⚡ Advanced GATE Nuances & Exam Trap Alerts</span>
    </div>
    <div class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed space-y-2">
      {l4}
    </div>
  </div>

  <!-- LEVEL 5: Step-by-Step Solved Exam Problem -->
  <div class="p-5 rounded-2xl bg-purple-50/70 dark:bg-purple-950/30 border border-purple-200 dark:border-purple-900/60 shadow-xs">
    <div class="flex items-center gap-2 mb-2 font-bold text-purple-900 dark:text-purple-200 text-sm">
      <span class="px-2 py-0.5 rounded bg-purple-600 text-white text-[10px] font-extrabold tracking-wide">LEVEL 5</span>
      <span>🎯 Step-by-Step Solved Exam Problem (Basic to Advanced)</span>
    </div>
    <div class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed space-y-2">
      {l5}
    </div>
  </div>
</div>"""
        dict_content[(sub, idx)] = html

    # --- EM ---
    add("EM", 0,
        "<p><b>Intuition:</b> Mathematical Logic is the legal language of computers. When you write code, every 'if' statement requires logical rigor. Set theory organizes objects into collections without duplicates, just like database tables.</p>",
        "<p><b>Fundamentals:</b> Propositions are strictly True or False. Logical operations: AND (∧), OR (∨), NOT (~), Implication (P → Q ≡ ~P ∨ Q), Biconditional (P ↔ Q). Sets have Cartesian products, power sets (size 2^n), and relations.</p>",
        "<p><b>Relations on set A of size n:</b><br/>• Reflexive: 2^(n² - n)<br/>• Symmetric: 2^(n(n+1)/2)<br/>• Anti-symmetric: 2^n * 3^(n(n-1)/2)<br/>• Equivalence Relation: Reflexive + Symmetric + Transitive (counted by Bell numbers B(n)).</p>",
        "<p><b>GATE Trap:</b> Vacuous Truth! When P is False, (P → Q) is ALWAYS True regardless of Q. E.g., 'If 3=7, then the moon is made of cheese' is mathematically TRUE!</p>",
        "<p><b>Problem:</b> How many reflexive and symmetric relations exist on a 3-element set?<br/><b>Solution:</b> Formula is 2^(n(n-1)/2). For n=3: 3*2/2 = 3. Total = 2^3 = <b>8</b>.</p>"
    )
    add("EM", 1,
        "<p><b>Intuition:</b> Graph theory models connections: vertices are cities, edges are highways. Euler proved planar graphs divide a surface into distinct regions like land borders on a map.</p>",
        "<p><b>Fundamentals:</b> Handshaking Theorem: ∑ deg(v) = 2E. Trees have n vertices and n - 1 edges. Bipartite graphs have no odd-length cycles.</p>",
        "<p><b>Planar Graphs & Euler's Formula:</b> V - E + R = 2. For simple planar graphs (V >= 3): E <= 3V - 6. If no triangles (girth >= 4): E <= 2V - 4. Four Color Theorem: χ(G) <= 4 for all planar graphs.</p>",
        "<p><b>GATE Trap:</b> If a planar graph has k disconnected components, Euler's formula changes to V - E + R = 1 + k!</p>",
        "<p><b>Problem:</b> What is the maximum number of edges in a planar graph with 8 vertices?<br/><b>Solution:</b> E <= 3V - 6 = 3(8) - 6 = 24 - 6 = <b>18 edges</b>.</p>"
    )
    add("EM", 2,
        "<p><b>Intuition:</b> Linear algebra transforms space. Eigenvalues tell you by how much vectors stretch or shrink along special directions (eigenvectors) without rotating.</p>",
        "<p><b>Fundamentals:</b> Det(A - λI) = 0. Trace(A) = sum of eigenvalues. Det(A) = product of eigenvalues. If A is symmetric, eigenvalues are strictly real.</p>",
        "<p><b>LU Decomposition:</b> Factorizes square matrix A into Lower triangular L and Upper triangular U. Unique if no row exchanges needed.</p>",
        "<p><b>GATE Trap:</b> Don't solve the full characteristic cubic polynomial! First verify Trace = sum of options and Det = product of options.</p>",
        "<p><b>Problem:</b> 3x3 matrix A has eigenvalues 2, 3, 5. Find Det(A² - I).<br/><b>Solution:</b> Eigenvalues of (A² - I) are (2²-1)=3, (3²-1)=8, (5²-1)=24. Det = 3 * 8 * 24 = <b>576</b>.</p>"
    )
    add("EM", 3,
        "<p><b>Intuition:</b> Calculus tracks smooth change; probability models uncertainty. Bayes' theorem updates your belief about a cause after observing evidence.</p>",
        "<p><b>Fundamentals:</b> L'Hopital for 0/0 and ∞/∞. Mean Value Theorem: f'(c) = [f(b) - f(a)] / (b - a). Normal, Poisson, and Exponential distributions.</p>",
        "<p><b>Bayes' Rule:</b> P(A|B) = P(B|A)*P(A) / P(B). Poisson: Mean = λ, Var = λ, P(X=k) = e^(-λ) λ^k / k!.</p>",
        "<p><b>GATE Trap:</b> Poisson distribution has Mean EQUAL to Variance! If a question states mean = 4, variance is also 4.</p>",
        "<p><b>Problem:</b> Limit x->0 of (sin x - x) / x³. Find value.<br/><b>Solution:</b> Using series: (x - x³/6 + ...) - x = -x³/6. Divided by x³ gives <b>-1/6 ≈ -0.167</b>.</p>"
    )

    # --- DL ---
    add("DL", 0,
        "<p><b>Intuition:</b> K-Maps are visual maps of truth tables where adjacent cells differ by only 1 bit (Gray code). Grouping 1s cancels out variables to create cheap circuits.</p>",
        "<p><b>Fundamentals:</b> SOP (Sum of Products) groups 1s. POS (Product of Sums) groups 0s. Essential Prime Implicants (EPIs) cover isolated minterms.</p>",
        "<p><b>Quine-McCluskey (Tabular):</b> Algorithmic minimization for >4 variables by repeatedly combining terms that differ by 1 bit.</p>",
        "<p><b>GATE Trap:</b> Don't-care conditions (X) can be included to make groups larger, but you NEVER need to cover an 'X' if all 1s are already covered.</p>",
        "<p><b>Problem:</b> Minimize F(A,B,C) = ∑ m(1,3,5,7).<br/><b>Solution:</b> Minterms (1,3,5,7) form a 4-cell group where A and B toggle, leaving only <b>C</b>.</p>"
    )
    add("DL", 1,
        "<p><b>Intuition:</b> Combinational circuits are like physical formulas: give them inputs, and they instantly generate outputs without remembering past inputs.</p>",
        "<p><b>Fundamentals:</b> Multiplexer (MUX) is a digital switch. Decoder activates 1 of 2^n lines. Priority encoders handle simultaneous inputs.</p>",
        "<p><b>Universal Logic Realization:</b> A 2^n:1 MUX can implement ANY (n+1) variable function by feeding the (n+1)th variable into input data lines.</p>",
        "<p><b>GATE Trap:</b> Active-LOW enable pins! If enable E' is active low, the circuit is OFF when E=1.</p>",
        "<p><b>Problem:</b> How many 2:1 MUXes to build 8:1 MUX?<br/><b>Solution:</b> Stage 1: 4 MUX, Stage 2: 2 MUX, Stage 3: 1 MUX. Total = 4 + 2 + 1 = <b>7 MUXes</b>.</p>"
    )
    add("DL", 2,
        "<p><b>Intuition:</b> Sequential circuits have memory. Flip-flops store 1 bit of information using feedback loops, and counters keep track of elapsed clock pulses.</p>",
        "<p><b>Fundamentals:</b> Characteristic equations: SR (S + R'Q, SR=0), JK (JQ' + K'Q), D (D), T (T ⊕ Q). Excitation tables determine required inputs.</p>",
        "<p><b>Counters:</b> Mod-N requires ⌈log2(N)⌉ flip-flops. Ring counter has n states; Johnson counter has 2n states.</p>",
        "<p><b>GATE Trap:</b> Race-around condition occurs in level-triggered JK flip-flops when J=1, K=1 and clock width t_w > flip-flop propagation delay t_pd.</p>",
        "<p><b>Problem:</b> Mod-12 counter requires how many flip-flops?<br/><b>Solution:</b> 2^n >= 12. 2³ = 8 < 12, 2⁴ = 16 >= 12. Requires <b>4 flip-flops</b>.</p>"
    )
    add("DL", 3,
        "<p><b>Intuition:</b> 2's complement lets hardware do subtraction using the exact same adder circuit as addition! Floating point stores very large/small numbers like scientific notation.</p>",
        "<p><b>Fundamentals:</b> n-bit signed 2's complement range: -2^(n-1) to +2^(n-1) - 1. IEEE 754 32-bit: 1 sign bit, 8 exponent bits (bias 127), 23 fraction bits.</p>",
        "<p><b>Overflow Rule:</b> Adding two numbers of the same sign produces an overflow if the result has the opposite sign: V = C_in ⊕ C_out of MSB.</p>",
        "<p><b>GATE Trap:</b> Exponent 00000000 and 11111111 in IEEE-754 are special reserved codes (zero/denorm and Inf/NaN). Real range of E is 1 to 254.</p>",
        "<p><b>Problem:</b> 8-bit 2's complement for -1?<br/><b>Solution:</b> +1 is 00000001. Invert bits: 11111110. Add 1: <b>11111111</b>.</p>"
    )

    # --- COA ---
    add("COA", 0,
        "<p><b>Intuition:</b> Machine instructions are binary orders to the processor (e.g. 'Add R1 and R2'). Addressing modes describe where the data lives (in a register, directly in the instruction, or in RAM).</p>",
        "<p><b>Fundamentals:</b> Addressing Modes: Immediate (operand in instruction), Direct/Absolute (address in instruction), Register, Register Indirect (pointer in register), PC-Relative (relocatable branching).</p>",
        "<p><b>Instruction Formats:</b> Opcode + Operands. Expanding opcodes allow variable length instructions.</p>",
        "<p><b>GATE Trap:</b> PC-relative addressing effective address = PC + Offset. Remember PC is already incremented to the NEXT instruction address!</p>",
        "<p><b>Problem:</b> Instruction at 1000 has branch offset +20. Word size 2 bytes. Where does it branch?<br/><b>Solution:</b> PC after fetch = 1002. Target = 1002 + 20 = <b>1022</b>.</p>"
    )
    add("COA", 1,
        "<p><b>Intuition:</b> The ALU does the arithmetic, and the Control Unit is the orchestra conductor directing traffic between registers, buses, and ALU.</p>",
        "<p><b>Fundamentals:</b> Hardwired Control: Fast, fixed combinational circuits (RISC). Microprogrammed Control: Control signals stored in ROM (CISC, flexible but slower).</p>",
        "<p><b>Interrupts & DMA:</b> Vectored interrupts provide direct jump address. DMA controller bypasses CPU for high-speed block transfers.</p>",
        "<p><b>GATE Trap:</b> Hardwired control units are strictly FASTER than microprogrammed control units because they avoid control memory read latency.</p>",
        "<p><b>Problem:</b> DMA device transfers at 4 MB/s across 20 MB/s bus. Find cycle-stealing overhead.<br/><b>Solution:</b> 4 / 20 = 0.20 = <b>20% bus utilization</b>.</p>"
    )
    add("COA", 2,
        "<p><b>Intuition:</b> Cache is like a fast desktop notepad; RAM is the bookshelf; Disk is the library in town. We keep frequently used data close to the CPU.</p>",
        "<p><b>Fundamentals:</b> Cache mapping: Direct (1 location), Fully Associative (any location), Set-Associative (k locations per set). AMAT = Hit_time + (Miss_rate * Miss_penalty).</p>",
        "<p><b>Address Breakdown (Set-Associative):</b> Tag bits + Set Index bits + Word Offset bits.</p>",
        "<p><b>GATE Trap:</b> Block size determines Offset bits; Number of SETS (not lines) determines Index bits!</p>",
        "<p><b>Problem:</b> 64 KB 4-way cache with 32-byte blocks. How many sets?<br/><b>Solution:</b> Lines = 64KB/32B = 2048. Sets = 2048 / 4 = <b>512 sets</b> (9 index bits).</p>"
    )
    add("COA", 3,
        "<p><b>Intuition:</b> Pipelining is like an automobile assembly line. While car 3 is getting painted, car 2 gets its engine, and car 1 gets wheels. Throughput increases dramatically.</p>",
        "<p><b>Fundamentals:</b> Stages: IF, ID, EX, MEM, WB. Clock cycle = max(stage delays) + latch delay. Speedup = non-pipelined time / pipelined time.</p>",
        "<p><b>Pipeline Hazards:</b> Structural (hardware conflict), Data (RAW, WAR, WAW resolved by forwarding), Control (branches resolved by prediction).</p>",
        "<p><b>GATE Trap:</b> CPI is only 1 in the ideal case! Branch stalls and load-use delays increase CPI above 1.</p>",
        "<p><b>Problem:</b> 5-stage pipeline, stage delays: 2, 4, 3, 5, 2 ns. Clock cycle?<br/><b>Solution:</b> Clock cycle = max(2,4,3,5,2) = <b>5 ns</b>.</p>"
    )

    # --- PDS ---
    add("PDS", 0,
        "<p><b>Intuition:</b> C is the mother tongue of systems programming. Pointers hold memory addresses, letting you manipulate hardware and data structures directly.</p>",
        "<p><b>Fundamentals:</b> Pointer arithmetic: p + 1 jumps by sizeof(*p) bytes. Recursion uses the runtime call stack. Static variables retain value between function calls.</p>",
        "<p><b>Operator Precedence:</b> Prefix ++ and * have equal precedence (right-to-left associativity). Postfix ++ has higher precedence.</p>",
        "<p><b>GATE Trap:</b> Arrays decay to pointers, but sizeof(arr) gives the TOTAL array size, while sizeof(ptr) only gives 4 or 8 bytes!</p>",
        "<p><b>Problem:</b> int a[]={10,20,30}; int *p = a; *(p++) vs (*p)++.<br/><b>Solution:</b> *(p++) returns *p then increments pointer. (*p)++ increments the integer value stored at *p.</p>"
    )
    add("PDS", 1,
        "<p><b>Intuition:</b> Linear structures arrange items in a sequence. Stacks are LIFO (like a stack of dinner plates); Queues are FIFO (like people in line at a cinema).</p>",
        "<p><b>Fundamentals:</b> Stack operations: push, pop (O(1)). Infix to postfix conversion. Queue operations: enqueue, dequeue. Circular queue avoids wasted space.</p>",
        "<p><b>Linked Lists:</b> Singly, Doubly, Circular. Insertion at head O(1); search O(n).</p>",
        "<p><b>GATE Trap:</b> Circular queue of size N can store at most N - 1 items to distinguish Full ((rear+1)%N == front) from Empty (front == rear).</p>",
        "<p><b>Problem:</b> How many stacks to implement a FIFO queue?<br/><b>Solution:</b> Exactly <b>2 stacks</b> (one for push, one for pop with reversal).</p>"
    )
    add("PDS", 2,
        "<p><b>Intuition:</b> Trees organize data hierarchically. A Binary Search Tree (BST) keeps smaller items on the left and larger on the right, enabling fast binary search.</p>",
        "<p><b>Fundamentals:</b> BST Inorder traversal is ALWAYS sorted. Catalan number C_n = (2n)! / ((n+1)! n!) gives number of unique BSTs with n keys.</p>",
        "<p><b>Heaps:</b> Complete binary tree. Max-Heap: parent >= children. Build-Heap takes O(n) linear time; Insert/Delete takes O(log n).</p>",
        "<p><b>GATE Trap:</b> Build-Heap from an unsorted array takes O(n) time, NOT O(n log n)!</p>",
        "<p><b>Problem:</b> Number of unique BSTs with 4 keys?<br/><b>Solution:</b> C_4 = (8)! / (5! * 4!) = 40320 / (120 * 24) = <b>14 BSTs</b>.</p>"
    )

    # --- ALGO ---
    add("ALGO", 0,
        "<p><b>Intuition:</b> Asymptotic analysis measures how code scales as data grows to billions of items. Big-O gives the worst-case upper bound.</p>",
        "<p><b>Fundamentals:</b> O (upper bound), Ω (lower bound), Θ (tight bound). Master Theorem: T(n) = a T(n/b) + f(n).</p>",
        "<p><b>Master Theorem Cases:</b> Compare f(n) with n^(log_b a). Case 1: n^(log_b a) wins => Θ(n^(log_b a)). Case 2: equal => Θ(n^(log_b a) log n). Case 3: f(n) wins => Θ(f(n)).</p>",
        "<p><b>GATE Trap:</b> Master Theorem cannot be applied if recurrence has non-constant coefficients or f(n) is not polynomial (e.g. 2^n or sin n).</p>",
        "<p><b>Problem:</b> T(n) = 8 T(n/2) + n². Solve.<br/><b>Solution:</b> a=8, b=2, n^(log_2 8) = n³. Since n³ > n², Case 1 applies: <b>Θ(n³)</b>.</p>"
    )
    add("ALGO", 1,
        "<p><b>Intuition:</b> Sorting puts chaos in order. Searching finds items fast. Hashing maps keys to table slots in average O(1) time like a phonebook index.</p>",
        "<p><b>Fundamentals:</b> Comparison sort lower bound: Ω(n log n). Stable sorts: Merge, Insertion, Bubble. In-place: Quick, Heap, Insertion.</p>",
        "<p><b>Hashing:</b> Chaining vs Open Addressing (Linear Probing, Quadratic, Double Hashing). Primary clustering occurs in linear probing.</p>",
        "<p><b>GATE Trap:</b> Quick Sort worst case is O(n²) when array is already sorted and first/last element is picked as pivot!</p>",
        "<p><b>Problem:</b> Which sorting algorithm is stable and has worst case O(n log n)?<br/><b>Solution:</b> <b>Merge Sort</b> (requires O(n) auxiliary memory).</p>"
    )
    add("ALGO", 2,
        "<p><b>Intuition:</b> Greedy makes the best immediate local choice (like taking the largest bill first). Dynamic Programming solves overlapping subproblems once and caches results.</p>",
        "<p><b>Fundamentals:</b> Greedy: Huffman Coding, Fractional Knapsack, Activity Selection. DP: 0/1 Knapsack, Matrix Chain, Longest Common Subsequence (LCS).</p>",
        "<p><b>DP Equations:</b> LCS(i, j) = 1 + LCS(i-1, j-1) if match, else max(LCS(i-1, j), LCS(i, j-1)).</p>",
        "<p><b>GATE Trap:</b> 0/1 Knapsack cannot be solved greedily! It requires Dynamic Programming (O(n W)) or branch and bound.</p>",
        "<p><b>Problem:</b> LCS length between 'ABCDE' and 'ACE'?<br/><b>Solution:</b> Common characters are 'A', 'C', 'E' in order. Length = <b>3</b>.</p>"
    )
    add("ALGO", 3,
        "<p><b>Intuition:</b> Graph algorithms explore interconnected mazes. BFS explores layer by layer; DFS plunges deep down one branch before backtracking.</p>",
        "<p><b>Fundamentals:</b> BFS (Queue, O(V+E), unweighted shortest path), DFS (Stack/recursion, topological sort). MST: Kruskal (edges, disjoint sets), Prim (vertices).</p>",
        "<p><b>Shortest Paths:</b> Dijkstra (non-negative weights, O(E + V log V)), Bellman-Ford (detects negative cycles, O(V*E)), Floyd-Warshall (all-pairs, O(V³)).</p>",
        "<p><b>GATE Trap:</b> Dijkstra FAILs on graphs with negative edge weights! Use Bellman-Ford instead.</p>",
        "<p><b>Problem:</b> Spanning tree of a graph with 20 vertices and 35 edges has how many edges?<br/><b>Solution:</b> Any spanning tree of V vertices always has V - 1 = <b>19 edges</b>.</p>"
    )

    # --- TOC ---
    add("TOC", 0,
        "<p><b>Intuition:</b> Finite automata are the simplest computers (like vending machines or turnstiles). They process text character by character without auxiliary memory.</p>",
        "<p><b>Fundamentals:</b> DFA (deterministic), NFA (non-deterministic). Both recognize the exact same class: Regular Languages. Subset construction converts NFA to DFA.</p>",
        "<p><b>Minimization:</b> Myhill-Nerode equivalence theorem partitions states. Table-filling algorithm merges indistinguishable states.</p>",
        "<p><b>GATE Trap:</b> An n-state NFA can produce up to 2^n states in its equivalent minimal DFA in the worst case!</p>",
        "<p><b>Problem:</b> Minimal DFA states for strings over {0,1} ending in '00'?<br/><b>Solution:</b> States track suffix: Start/no-0, one-0, two-0s (accept). Exactly <b>3 states</b>.</p>"
    )
    add("TOC", 1,
        "<p><b>Intuition:</b> Pushdown Automata (PDA) are finite automata equipped with a single Stack. This stack lets them count and match brackets like { a^n b^n }.</p>",
        "<p><b>Fundamentals:</b> Context-Free Grammars (CFG): A -> α. Ambiguous if a string has >1 parse tree. Pumping Lemma for CFLs splits string into uvwxy.</p>",
        "<p><b>Closure:</b> CFLs are closed under Union, Concatenation, Kleene star, but NOT closed under Intersection or Complement!</p>",
        "<p><b>GATE Trap:</b> Deterministic CFLs (DCFLs) ARE closed under complementation, whereas general CFLs are NOT!</p>",
        "<p><b>Problem:</b> Is L = { a^n b^n c^n | n >= 1 } context-free?<br/><b>Solution:</b> <b>No</b>. Comparing 3 counts requires 2 stacks (Context-Sensitive).</p>"
    )
    add("TOC", 2,
        "<p><b>Intuition:</b> A Turing Machine has an infinite tape and represents the theoretical limit of what ANY modern computer or algorithm can ever compute.</p>",
        "<p><b>Fundamentals:</b> Chomsky Hierarchy: Regular (Type 3) ⊂ CFL (Type 2) ⊂ CSL (Type 1) ⊂ Recursive (Decidable) ⊂ RE (Recognizable).</p>",
        "<p><b>Undecidability:</b> Halting problem (Turing). Rice's Theorem: Any non-trivial semantic property of the language of a Turing Machine is undecidable!</p>",
        "<p><b>GATE Trap:</b> Equivalence of two DFAs is DECIDABLE, but equivalence of two CFGs or two TMs is UNDECIDABLE!</p>",
        "<p><b>Problem:</b> Is emptiness of a Context-Free Grammar decidable?<br/><b>Solution:</b> <b>Yes</b> (test if start symbol can derive any terminal string in polynomial time).</p>"
    )

    # --- CD ---
    add("CD", 0,
        "<p><b>Intuition:</b> The compiler reads source code like human text: first splitting it into words (tokens), then checking grammar rules (parsing).</p>",
        "<p><b>Fundamentals:</b> Lexer: Regular expressions -> DFA -> Tokens. Parser: CFG. Top-Down (LL(1)): Predictive parsing using FIRST and FOLLOW sets.</p>",
        "<p><b>LL(1) Conditions:</b> For A -> α | β: 1) FIRST(α) ∩ FIRST(β) = ∅. 2) If α =>* ε, then FIRST(β) ∩ FOLLOW(A) = ∅. Left recursion destroys LL(1).</p>",
        "<p><b>GATE Trap:</b> An ambiguous grammar can NEVER be parsed by LL(1) or any LR parser!</p>",
        "<p><b>Problem:</b> S -> a S b | c. Find FIRST(S).<br/><b>Solution:</b> FIRST(S) = <b>{ a, c }</b>.</p>"
    )
    add("CD", 1,
        "<p><b>Intuition:</b> Bottom-up parsing starts at the terminal leaves and collapses tokens back up to the start symbol like solving a jigsaw puzzle.</p>",
        "<p><b>Fundamentals:</b> Shift-Reduce parsers: LR(0) < SLR(1) < LALR(1) < CLR(1). State counts: States(SLR) == States(LALR) == States(LR0) < States(CLR).</p>",
        "<p><b>Conflicts:</b> Shift-Reduce and Reduce-Reduce conflicts. Merging CLR(1) states to form LALR(1) can introduce Reduce-Reduce conflicts, but NEVER Shift-Reduce.</p>",
        "<p><b>GATE Trap:</b> Every SLR(1) grammar is an LALR(1) grammar, but NOT every LALR(1) grammar is SLR(1)!</p>",
        "<p><b>Problem:</b> Can merging core states in LALR(1) produce shift-reduce conflicts?<br/><b>Solution:</b> <b>No</b>, it can only create reduce-reduce conflicts.</p>"
    )
    add("CD", 2,
        "<p><b>Intuition:</b> Once grammar is verified, the compiler generates intermediate three-address code and optimizes it to make programs run 10x faster.</p>",
        "<p><b>Fundamentals:</b> SDD: S-attributed (synthesized only, bottom-up), L-attributed (synthesized + inherited from left). 3-Address Code: Quadruples (4 fields), Triples.</p>",
        "<p><b>Optimizations:</b> Common subexpression elimination, Dead code elimination, Loop invariant code motion, Strength reduction, Liveness analysis.</p>",
        "<p><b>GATE Trap:</b> Liveness analysis is a BACKWARD data-flow analysis problem!</p>",
        "<p><b>Problem:</b> How many fields in a Quadruple?<br/><b>Solution:</b> Exactly <b>4 fields</b>: (operator, arg1, arg2, result).</p>"
    )

    # --- OS ---
    add("OS", 0,
        "<p><b>Intuition:</b> An Operating System is the master government of your computer. Processes are running programs; synchronization ensures they don't clobber each other's data.</p>",
        "<p><b>Fundamentals:</b> PCB (Process Control Block). Threads share code, data, and heap, but have private registers and stack. Critical Section: Mutual Exclusion, Progress, Bounded Waiting.</p>",
        "<p><b>Semaphores:</b> Wait() decrements, Signal() increments. Counting semaphore value can be negative in some implementations indicating waiting process count.</p>",
        "<p><b>GATE Trap:</b> Fork() returns 0 to the child process and the child's PID to the parent process!</p>",
        "<p><b>Problem:</b> A semaphore S initialized to 5 has 12 wait() and 9 signal() operations. Final value?<br/><b>Solution:</b> 5 - 12 + 9 = <b>2</b>.</p>"
    )
    add("OS", 1,
        "<p><b>Intuition:</b> CPU scheduling decides who gets the processor next. Deadlock is a traffic gridlock where car A waits for car B, which is waiting for car A.</p>",
        "<p><b>Fundamentals:</b> Scheduling: FCFS, SJF (optimal average waiting time), SRTF (preemptive SJF), Round Robin (time quantum q). Coffman 4 Conditions for Deadlock: Mutual exclusion, Hold & wait, No preemption, Circular wait.</p>",
        "<p><b>Deadlock Handling:</b> Banker's Algorithm (safety state testing: Need = Max - Allocation <= Available).</p>",
        "<p><b>GATE Trap:</b> SRTF gives minimal average waiting time, but can cause starvation of long processes!</p>",
        "<p><b>Problem:</b> 3 processes each need 3 resources. What is the MINIMUM resources to guarantee deadlock-freedom?<br/><b>Solution:</b> R >= n * (m - 1) + 1 = 3 * (3 - 1) + 1 = 3 * 2 + 1 = <b>7 resources</b>.</p>"
    )
    add("OS", 2,
        "<p><b>Intuition:</b> Virtual memory gives every program the illusion of having a massive, private memory space by swapping pages between RAM and disk.</p>",
        "<p><b>Fundamentals:</b> Paging avoids external fragmentation. Page table maps virtual page to physical frame. TLB (Translation Lookaside Buffer) caches recent translations.</p>",
        "<p><b>Page Replacement:</b> FIFO, LRU, Optimal. EMAT = Hit_TLB*(t_TLB + t_mem) + Miss_TLB*(t_TLB + 2*t_mem).</p>",
        "<p><b>GATE Trap:</b> Belady's Anomaly (more frames causing more page faults) occurs in FIFO, but NEVER in stack algorithms like LRU or Optimal!</p>",
        "<p><b>Problem:</b> Virtual address 32-bit, page size 4 KB. How many virtual pages?<br/><b>Solution:</b> 2³² / 2¹² = 2²⁰ = <b>1,048,576 pages (1M pages)</b>.</p>"
    )

    # --- DB ---
    add("DB", 0,
        "<p><b>Intuition:</b> A database stores structured data so millions of users can read and write simultaneously without corrupting records.</p>",
        "<p><b>Fundamentals:</b> Relational Model: Relations (tables), Tuples (rows), Attributes (columns). Relational Algebra: Selection (σ), Projection (π), Join (⋈), Cartesian product (×).</p>",
        "<p><b>SQL Essentials:</b> SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY. NULL comparisons must use IS NULL.</p>",
        "<p><b>GATE Trap:</b> In SQL, 'COUNT(*)' counts rows with NULLs, but 'COUNT(attribute)' ignores NULL values!</p>",
        "<p><b>Problem:</b> Relation R has 5 tuples, S has 10 tuples. Maximum tuples in R ⋈ S?<br/><b>Solution:</b> In the worst case where all join keys match, tuples = 5 * 10 = <b>50 tuples</b>.</p>"
    )
    add("DB", 1,
        "<p><b>Intuition:</b> Normalization organizes tables to eliminate duplicate data (redundancy) and prevent anomalies when deleting or updating records.</p>",
        "<p><b>Fundamentals:</b> Candidate key: attribute closure covers all attributes. 1NF (atomic values). 2NF (no partial dependency). 3NF (no transitive dependency). BCNF (every determinant is a candidate key).</p>",
        "<p><b>Decomposition:</b> Must always be Lossless Join (R1 ∩ R2 -> R1 or R2). 3NF always guarantees dependency preservation; BCNF may not.</p>",
        "<p><b>GATE Trap:</b> If all attributes in a relation are prime (part of some candidate key), the relation is AUTOMATICALLY in 3NF!</p>",
        "<p><b>Problem:</b> R(A,B,C) with FDs {A -> B, B -> C}. What is highest normal form?<br/><b>Solution:</b> Key is A. FD B -> C has non-prime RHS and non-key LHS (transitive). Highest NF = <b>2NF</b>.</p>"
    )
    add("DB", 2,
        "<p><b>Intuition:</b> Transactions ensure bank transfers are safe (ACID properties). B+ Trees are self-balancing indexes that allow database searches in 3 or 4 disk reads.</p>",
        "<p><b>Fundamentals:</b> B+ Tree: All records stored in leaf nodes linked sequentially. Transactions: Atomicity, Consistency, Isolation, Durability.</p>",
        "<p><b>Serializability:</b> Conflict serializable if precedence graph has NO cycles. Two-Phase Locking (2PL) guarantees conflict serializability.</p>",
        "<p><b>GATE Trap:</b> Basic 2PL guarantees serializability, but can STILL suffer from deadlocks!</p>",
        "<p><b>Problem:</b> B+ tree order 4. Maximum keys in internal node?<br/><b>Solution:</b> Order p = 4. Maximum keys = p - 1 = <b>3 keys</b>.</p>"
    )

    # --- CN ---
    add("CN", 0,
        "<p><b>Intuition:</b> Computer networks connect the globe. Layering (OSI 7 layers, TCP/IP 4 layers) splits communication into modular, manageable jobs.</p>",
        "<p><b>Fundamentals:</b> Bandwidth (bits/sec), Propagation delay (Distance/Speed), Transmission delay (Length/Bandwidth), Queuing delay. Round Trip Time (RTT) = 2 * Propagation delay.</p>",
        "<p><b>Bandwidth-Delay Product (BDP):</b> B * T_prop represents the number of bits in flight filling the pipe.</p>",
        "<p><b>GATE Trap:</b> Transmission delay depends on packet size and bandwidth; Propagation delay depends on physical distance and medium speed!</p>",
        "<p><b>Problem:</b> 1000 byte packet on 10 Mbps link. Find transmission delay.<br/><b>Solution:</b> (1000 * 8 bits) / (10 x 10⁶ bps) = 8000 / 10⁷ = 0.0008 s = <b>0.8 ms</b>.</p>"
    )
    add("CN", 1,
        "<p><b>Intuition:</b> The Data Link Layer ensures reliable hop-to-hop communication over noisy wires, and MAC protocols prevent devices from talking over each other.</p>",
        "<p><b>Fundamentals:</b> Error detection: CRC (polynomial division), Checksum. Protocols: Stop-and-Wait (η = 1/(1+2a)), Go-Back-N (window size 2^k - 1), Selective Repeat (window size 2^(k-1)).</p>",
        "<p><b>CSMA/CD:</b> Collision detection. Condition: Minimum frame size L >= 2 * T_prop * Bandwidth.</p>",
        "<p><b>GATE Trap:</b> In Go-Back-N, receiver window is ALWAYS 1! In Selective Repeat, sender and receiver windows are EQUAL (2^(k-1)).</p>",
        "<p><b>Problem:</b> GBN with 3-bit sequence numbers. Maximum sender window?<br/><b>Solution:</b> 2³ - 1 = 8 - 1 = <b>7 frames</b>.</p>"
    )
    add("CN", 2,
        "<p><b>Intuition:</b> The Network Layer finds the path from source to destination across multiple intermediate routers worldwide (IP Addressing and Routing).</p>",
        "<p><b>Fundamentals:</b> IPv4: 32 bits. CIDR notation /n means n network bits. Subnetting divides networks. Longest Prefix Match in routing tables.</p>",
        "<p><b>Routing Algorithms:</b> Distance Vector (Bellman-Ford, count-to-infinity), Link State (Dijkstra, OSPF). Fragmentation: offset in 8-byte blocks.</p>",
        "<p><b>GATE Trap:</b> Fragment offset field is measured in units of 8 bytes, NOT individual bytes!</p>",
        "<p><b>Problem:</b> Subnet mask /26 has how many usable host IP addresses?<br/><b>Solution:</b> Host bits = 32 - 26 = 6. Total IPs = 2⁶ = 64. Usable hosts = 64 - 2 = <b>62 hosts</b>.</p>"
    )
    add("CN", 3,
        "<p><b>Intuition:</b> The Transport layer provides process-to-process delivery. TCP guarantees reliable, in-order delivery; UDP provides lightweight, fast delivery for streaming.</p>",
        "<p><b>Fundamentals:</b> TCP: Connection-oriented, 3-way handshake (SYN, SYN-ACK, ACK). Congestion Control: Slow Start (exponential), Congestion Avoidance (additive increase).</p>",
        "<p><b>Application Protocols:</b> DNS (port 53, UDP/TCP), HTTP (port 80, TCP), HTTPS (port 443), SMTP (port 25).</p>",
        "<p><b>GATE Trap:</b> A TCP SYN or FIN packet consumes 1 sequence number even though it carries 0 bytes of application payload data!</p>",
        "<p><b>Problem:</b> Threshold is 16 MSS. TCP in slow start reaches cwnd = 8 MSS. What is cwnd after next successful RTT?<br/><b>Solution:</b> In slow start, cwnd doubles each RTT: 8 * 2 = <b>16 MSS</b>.</p>"
    )

    # --- GA ---
    add("GA", 0,
        "<p><b>Intuition:</b> Verbal aptitude tests grammatical precision, vocabulary in context, and reading comprehension under time constraints.</p>",
        "<p><b>Fundamentals:</b> Subject-Verb Agreement: Subject proximity rules ('either/or', 'neither/nor'). Tenses, prepositional idioms, parallelism.</p>",
        "<p><b>Vocabulary & Reading:</b> Context clues, antonyms, synonyms, identifying the main author thesis.</p>",
        "<p><b>GATE Trap:</b> Watch out for phrases between subject and verb! 'The bouquet of red roses IS beautiful' (verb agrees with bouquet, not roses).</p>",
        "<p><b>Problem:</b> 'Neither the captain nor the sailors _____ prepared for the storm.'<br/><b>Solution:</b> Proximity rule: 'sailors' is plural, so verb is <b>were</b>.</p>"
    )
    add("GA", 1,
        "<p><b>Intuition:</b> Quantitative aptitude evaluates numerical agility, ratios, percentages, speed-distance-time, and geometric intuition.</p>",
        "<p><b>Fundamentals:</b> Work & Time: Work = Rate * Time. Speed = Distance / Time. Relative speed: opposite direction (S1 + S2), same direction (|S1 - S2|).</p>",
        "<p><b>Permutations & Combinations:</b> nPr = n! / (n-r)!, nCr = n! / (r! (n-r)!). Circular permutation = (n - 1)!.</p>",
        "<p><b>GATE Trap:</b> Convert units immediately! km/h to m/s: multiply by 5/18. m/s to km/h: multiply by 18/5.</p>",
        "<p><b>Problem:</b> Convert 72 km/h to m/s.<br/><b>Solution:</b> 72 * (5/18) = 4 * 5 = <b>20 m/s</b>.</p>"
    )
    add("GA", 2,
        "<p><b>Intuition:</b> Analytical aptitude tests deductive logic (syllogisms, arrangements), while spatial aptitude tests mental rotation, mirror symmetry, and folding.</p>",
        "<p><b>Fundamentals:</b> Syllogisms: Use Venn diagram overlap. Blood relations: Draw generation hierarchy trees. Seating: Linear vs circular orientation.</p>",
        "<p><b>Spatial Visualization:</b> 2D fold lines become axes of symmetry. 3D cube folding: Opposite faces never share a common edge.</p>",
        "<p><b>GATE Trap:</b> In seating arrangements, remember that people facing the center have their LEFT and RIGHT reversed compared to people facing outward!</p>",
        "<p><b>Problem:</b> Standard die opposite faces sum to 7. What is opposite to face 2?<br/><b>Solution:</b> 7 - 2 = <b>5</b>.</p>"
    )

    print(f"Compiled all {len(dict_content)} chapters into progressive dictionary!")

    with open(os.path.join("content_data", "progressive_theory_engine.py"), "w", encoding="utf-8") as f:
        f.write("# Comprehensive Progressive Theory Engine for GATE 2027 CSE\n")
        f.write("# All 38 Chapters across all 11 Subjects formatted in 5-Tier Progressive Learning Model\n\n")
        f.write("PROGRESSIVE_THEORY_DICT = {\n")
        for k, v in dict_content.items():
            f.write(f"    {repr(k)}: {repr(v)},\n")
        f.write("}\n")
    print("Successfully wrote progressive_theory_engine.py!")

if __name__ == "__main__":
    build_all()
