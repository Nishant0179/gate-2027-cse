# GATE 2027 Study Timetable and Personalized Study Planner Module
# From October 2026 to Examination Day (February 6, 2027)

STUDY_PLANS = {
    "target_exam_date": "2027-02-06",
    "total_weeks": 16,
    "schedules": {
        "2_hours": {
            "title": "2 Hours/Day (Working Professional & Final Year College Plan)",
            "daily_breakdown": {
                "concept_study_mins": 60,
                "practice_pyq_mins": 45,
                "revision_mins": 15
            },
            "strategy": "High-yield topic prioritization. Study 1 subject at a time, solve 15 quality questions daily, dedicate Sunday to weekly revision and tests."
        },
        "4_hours": {
            "title": "4 Hours/Day (Standard Comprehensive Plan - Recommended)",
            "daily_breakdown": {
                "concept_study_mins": 120,
                "practice_pyq_mins": 90,
                "revision_mins": 30
            },
            "strategy": "Parallel subject pairing (1 Core Technical + 1 Math/Aptitude). Solve 30-40 questions daily, full-length tests on alternate weekends."
        },
        "6_hours": {
            "title": "6 Hours/Day (Intensive Rank-Booster / Full-Time Plan)",
            "daily_breakdown": {
                "concept_study_mins": 180,
                "practice_pyq_mins": 120,
                "revision_mins": 60
            },
            "strategy": "Deep dive into edge cases and multi-concept MSQs. Solve 60+ questions daily, complete 2 full subject revisions, 15+ full-length mocks."
        }
    },
    "weekly_roadmap": [
        {
            "week": 1,
            "phase": "Foundation & Core Mathematics",
            "subjects": ["Engineering Mathematics (Discrete Mathematics)"],
            "topics": ["Propositional & First Order Logic", "Sets, Relations, Functions, Equivalence Relations", "Lattices & Boolean Algebras"],
            "targets": "Study notes, solve 50 practice questions, 15 verified PYQs",
            "buffer_day": "Sunday Evening: Backlog recovery and 30-min weekly quiz"
        },
        {
            "week": 2,
            "phase": "Foundation & Core Mathematics",
            "subjects": ["Engineering Mathematics (Discrete Math & Linear Algebra)"],
            "topics": ["Graph Theory (Euler formula, coloring, trees)", "Combinatorics & Generating Functions", "Matrices, Determinants, Systems of Equations"],
            "targets": "Master Handshaking lemma, Planar graphs, Matrix rank, solve 60 questions",
            "buffer_day": "Sunday Evening: Linear algebra quiz"
        },
        {
            "week": 3,
            "phase": "Digital Hardware & Fundamentals",
            "subjects": ["Digital Logic", "Engineering Mathematics (Calculus)"],
            "topics": ["Boolean Algebra, K-Maps, Tabular Method", "Combinational Circuits (MUX, Decoders, Adders)", "Limits, Continuity, Maxima/Minima"],
            "targets": "Build MUX implementations, practice K-map grouping, 40 PYQs",
            "buffer_day": "Sunday: Full subject test on Digital Logic"
        },
        {
            "week": 4,
            "phase": "Digital Hardware & Architecture",
            "subjects": ["Digital Logic", "Computer Organization & Architecture"],
            "topics": ["Sequential Circuits (Flip-Flops, Counters, FSM)", "Number Representation (2's complement, IEEE 754)", "Instruction Sets & Addressing Modes"],
            "targets": "Design mod-N counters, practice IEEE 754 single precision conversions",
            "buffer_day": "Sunday: Combined Hardware Assessment"
        },
        {
            "week": 5,
            "phase": "Computer Systems & Hardware",
            "subjects": ["Computer Organization & Architecture"],
            "topics": ["Cache Memory Mapping & Performance (AMAT)", "ALU & Control Unit (Hardwired vs Microprogrammed)", "I/O Interface (DMA, Interrupts)"],
            "targets": "Solve 30 numericals on cache tags, set associativity, and AMAT",
            "buffer_day": "Sunday: Cache memory deep-dive quiz"
        },
        {
            "week": 6,
            "phase": "Computer Systems & Hardware",
            "subjects": ["Computer Organization & Architecture", "General Aptitude"],
            "topics": ["Instruction Pipelining & Hazards (RAW, Structural, Branch)", "Verbal Aptitude: Grammar & Sentence Completion", "Quantitative: Ratios, Percentages, Work & Time"],
            "targets": "Master pipeline speedup and stall cycle calculations",
            "buffer_day": "Sunday: COA Subject Test (50 Marks)"
        },
        {
            "week": 7,
            "phase": "Programming & Data Structures",
            "subjects": ["Programming in C", "Linear Data Structures"],
            "topics": ["Pointers, Pointer Arithmetic, Operator Precedence", "Recursion & Call Stack Tracing", "Arrays, Stacks (Infix/Postfix), Queues (Circular)"],
            "targets": "Trace 25 tricky C code snippets, implement stack evaluation",
            "buffer_day": "Sunday: C Output Tracing Challenge"
        },
        {
            "week": 8,
            "phase": "Data Structures & Algorithms",
            "subjects": ["Programming and Data Structures", "Algorithms"],
            "topics": ["Linked Lists & Cycle Finding", "Trees, BST, Binary Heaps", "Asymptotic Analysis & Master Theorem"],
            "targets": "Master BST deletion, heapify linear time proof, 40 PYQs",
            "buffer_day": "Sunday: Mid-Term Diagnostic Mock Test (65 Questions, 100 Marks)"
        },
        {
            "week": 9,
            "phase": "Algorithms & Complexity",
            "subjects": ["Algorithms"],
            "topics": ["Divide-and-Conquer (Merge Sort, Quick Sort)", "Greedy (Knapsack, Huffman)", "Dynamic Programming (0/1 Knapsack, LCS, Matrix Chain)"],
            "targets": "Write recurrence relations for DP problems, solve 50 questions",
            "buffer_day": "Sunday: Algorithms Subject Test"
        },
        {
            "week": 10,
            "phase": "Graph Algorithms & Computation Theory",
            "subjects": ["Algorithms", "Theory of Computation"],
            "topics": ["Graph Traversals (BFS, DFS, Topological Sort)", "MST (Prim, Kruskal) & Shortest Paths (Dijkstra, Bellman-Ford)", "DFA, NFA, Minimization & Regular Expressions"],
            "targets": "Construct minimal DFAs, practice Dijkstra and Bellman-Ford",
            "buffer_day": "Sunday: TOC Foundations Quiz"
        },
        {
            "week": 11,
            "phase": "Theory of Computation & Compilers",
            "subjects": ["Theory of Computation", "Compiler Design"],
            "topics": ["Pumping Lemma (Regular & CFL)", "Pushdown Automata (DPDA vs NPDA)", "Lexical Analysis & LL(1) Parsing (FIRST and FOLLOW)"],
            "targets": "Compute FIRST/FOLLOW tables, prove non-regularity with Pumping Lemma",
            "buffer_day": "Sunday: TOC & Compiler Design Test"
        },
        {
            "week": 12,
            "phase": "Compilers & Operating Systems",
            "subjects": ["Compiler Design", "Operating Systems"],
            "topics": ["Bottom-Up Parsing (LR(0), SLR(1), LALR(1))", "Local Optimization & Data Flow Analysis (Constant propagation, Liveness)", "System Calls, Processes, Threads, CPU Scheduling (SRTF, Round Robin)"],
            "targets": "Solve parsing table conflict problems, draw CPU Gantt charts",
            "buffer_day": "Sunday: Operating Systems Scheduling Quiz"
        },
        {
            "week": 13,
            "phase": "Operating Systems & Concurrency",
            "subjects": ["Operating Systems"],
            "topics": ["Process Synchronization (Peterson, Semaphores, Classic Problems)", "Deadlocks (Banker's Algorithm, Coffman conditions)", "Memory Management (Paging, Multi-level Paging, TLB, EMAT)"],
            "targets": "Trace semaphore code snippets, solve Banker's safety numericals",
            "buffer_day": "Sunday: OS Subject Test (50 Marks)"
        },
        {
            "week": 14,
            "phase": "Databases & Storage",
            "subjects": ["Databases"],
            "topics": ["Relational Algebra & SQL (Subqueries, Aggregates)", "Functional Dependencies & Normal Forms (1NF to BCNF)", "B/B+ Trees, Transactions, Concurrency Control (2PL, Serializability)"],
            "targets": "Find candidate keys, verify lossless join and dependency preservation",
            "buffer_day": "Sunday: Databases Full Subject Test"
        },
        {
            "week": 15,
            "phase": "Computer Networks & Applied Systems",
            "subjects": ["Computer Networks", "General Aptitude"],
            "topics": ["Layering, Performance Delays, CSMA/CD Minimum Frame Size", "IPv4 Addressing (CIDR, Fragmentation, Subnetting)", "TCP Congestion Control & Sockets, Analytical & Spatial Aptitude"],
            "targets": "Solve IP fragmentation numericals, TCP window calculations",
            "buffer_day": "Sunday: Computer Networks Subject Test"
        },
        {
            "week": 16,
            "phase": "Final Sprint & All-India Mock Tests",
            "subjects": ["Full Syllabus Comprehensive Revision"],
            "topics": ["Full-Length Mock Test 1", "Full-Length Mock Test 2", "Weak Topic Remediation & Formula Book Drills"],
            "targets": "Simulate exact CBT 3-hour examination conditions twice, review mistakes",
            "buffer_day": "Final Days: Rapid-fire formula sheets and relaxation"
        }
    ]
}
