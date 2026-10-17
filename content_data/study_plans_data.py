# GATE 2027 Study Timetable and Personalized Study Planner Module
# 3-Month-Early Completion Architecture: 100% Syllabus Completed 3 Months Prior to Examination (Nov 1, 2026)
# Followed by a Dedicated 90-Day Advanced Revision & Full-Length CBT Mock Series (Nov 2026 - Feb 2027)

STUDY_PLANS = {
    "target_exam_date": "2027-02-06",
    "syllabus_completion_date": "2026-11-01",
    "buffer_months_count": 3,
    "strategy_name": "3-Month-Early Syllabus Completion & 90-Day All-India CBT Test Series Masterplan",
    "schedules": {
        "2_hours": {
            "title": "2 Hours/Day (Working Professional & Final Year College Plan)",
            "daily_breakdown": {
                "concept_study_mins": 60,
                "practice_pyq_mins": 45,
                "revision_mins": 15
            },
            "strategy": "3-Month-Early Completion Mode: High-yield core topic prioritization. Pair 1 technical subject with daily 15-min math/aptitude bursts. Complete 100% of all 11 subjects by November 1, leaving November, December, and January entirely free for 10+ mock tests and targeted error-log revision."
        },
        "4_hours": {
            "title": "4 Hours/Day (Standard Balanced Plan - Recommended)",
            "daily_breakdown": {
                "concept_study_mins": 120,
                "practice_pyq_mins": 90,
                "revision_mins": 30
            },
            "strategy": "3-Month-Early Completion Mode: Dual-track parallel study (Morning: Core Technical Subject; Evening: Engineering Math / General Aptitude). Solve 30-40 questions daily. Finish all syllabus topics by November 1, dedicating the final 90 days to 3 systematic revision cycles, 15+ full-length CBT mocks, and speed optimization."
        },
        "6_hours": {
            "title": "6 Hours/Day (Intensive Rank-Booster / Full-Time Plan)",
            "daily_breakdown": {
                "concept_study_mins": 180,
                "practice_pyq_mins": 120,
                "revision_mins": 60
            },
            "strategy": "3-Month-Early Completion Mode: Aggressive multi-subject deep dive. Tackle advanced edge cases and multi-concept MSQs. Finish the complete syllabus by November 1, followed by 3 exhaustive revision rounds, 50+ subject tests, and 20+ full-length simulated CBT exams to target AIR < 100."
        }
    },
    "weekly_roadmap": [
        # --- PHASE 1: 100% ACCELERATED SYLLABUS COMPLETION (FINISHES 3 MONTHS BEFORE EXAM) ---
        {
            "week": 1,
            "phase": "Syllabus Phase: Discrete Mathematics",
            "phase_category": "syllabus",
            "subjects": ["Engineering Mathematics (Discrete Mathematics)"],
            "topics": ["Propositional & First Order Logic", "Sets, Relations, Functions, Equivalence Relations", "Lattices & Boolean Algebras"],
            "targets": "Study notes, solve 50 practice questions, 15 verified PYQs",
            "buffer_day": "Sunday Evening: Backlog recovery and 30-min weekly quiz"
        },
        {
            "week": 2,
            "phase": "Syllabus Phase: Discrete Math & Linear Algebra",
            "phase_category": "syllabus",
            "subjects": ["Engineering Mathematics (Discrete Math & Linear Algebra)"],
            "topics": ["Graph Theory (Euler formula, coloring, trees)", "Combinatorics & Generating Functions", "Matrices, Determinants, Systems of Equations, Eigenvalues"],
            "targets": "Master Handshaking lemma, Planar graphs, Matrix rank & diagonalization, solve 60 questions",
            "buffer_day": "Sunday Evening: Linear algebra & discrete math quiz"
        },
        {
            "week": 3,
            "phase": "Syllabus Phase: Calculus & Digital Hardware",
            "phase_category": "syllabus",
            "subjects": ["Digital Logic", "Engineering Mathematics (Calculus & Probability)"],
            "topics": ["Boolean Algebra, K-Maps, Logic Gates", "Combinational Circuits (Multiplexers, Decoders, Adders)", "Calculus (Limits, Maxima/Minima) & Conditional Probability"],
            "targets": "Build MUX implementations, practice K-map grouping, solve 45 PYQs",
            "buffer_day": "Sunday: Full subject test on Digital Logic"
        },
        {
            "week": 4,
            "phase": "Syllabus Phase: Sequential Circuits & Architecture",
            "phase_category": "syllabus",
            "subjects": ["Digital Logic", "Computer Organization & Architecture"],
            "topics": ["Sequential Circuits (Flip-Flops, Counters, FSM)", "Number Representation (2's complement, IEEE 754)", "Instruction Sets & Addressing Modes"],
            "targets": "Design mod-N synchronous counters, practice IEEE 754 single precision conversions",
            "buffer_day": "Sunday: Combined Hardware & Digital Assessment"
        },
        {
            "week": 5,
            "phase": "Syllabus Phase: Memory Hierarchy & ALU",
            "phase_category": "syllabus",
            "subjects": ["Computer Organization & Architecture"],
            "topics": ["Cache Memory Mapping (Direct, Set-Associative, Fully-Associative)", "AMAT & Cache Miss Latency", "ALU & Control Unit (Hardwired vs Microprogrammed)", "I/O Interface & DMA"],
            "targets": "Solve 35 numericals on cache tags, set associativity, and AMAT",
            "buffer_day": "Sunday: Cache memory deep-dive test"
        },
        {
            "week": 6,
            "phase": "Syllabus Phase: Pipelining & Verbal Aptitude",
            "phase_category": "syllabus",
            "subjects": ["Computer Organization & Architecture", "General Aptitude"],
            "topics": ["Instruction Pipelining & Hazards (RAW, WAR, Structural, Branch)", "Pipeline Speedup & CPI Calculations", "Verbal Aptitude: Grammar, Vocabulary, Sentence Completion"],
            "targets": "Master pipeline speedup and stall cycle calculations, solve 40 aptitude items",
            "buffer_day": "Sunday: COA Subject Test (50 Marks)"
        },
        {
            "week": 7,
            "phase": "Syllabus Phase: Programming in C",
            "phase_category": "syllabus",
            "subjects": ["Programming in C", "Linear Data Structures"],
            "topics": ["Pointers, Pointer Arithmetic, Operator Precedence", "Recursion & Call Stack Tracing", "Arrays, Stacks (Infix to Postfix), Queues (Circular)"],
            "targets": "Trace 30 tricky C code snippets, implement stack evaluation & recursion dry-runs",
            "buffer_day": "Sunday: C Output Tracing Challenge"
        },
        {
            "week": 8,
            "phase": "Syllabus Phase: Data Structures & Asymptotic Analysis",
            "phase_category": "syllabus",
            "subjects": ["Programming and Data Structures", "Algorithms"],
            "topics": ["Linked Lists & Cycle Finding (Floyd's Algorithm)", "Binary Trees, BST, Binary Heaps", "Asymptotic Analysis (Big-O, Omega, Theta) & Master Theorem"],
            "targets": "Master BST deletion, heapify linear time proof, solve 45 PYQs",
            "buffer_day": "Sunday: Data Structures Full Subject Test"
        },
        {
            "week": 9,
            "phase": "Syllabus Phase: Algorithm Design Techniques",
            "phase_category": "syllabus",
            "subjects": ["Algorithms"],
            "topics": ["Divide-and-Conquer (Merge Sort, Quick Sort)", "Greedy Strategies (Activity Selection, Huffman Coding)", "Dynamic Programming (0/1 Knapsack, LCS, Matrix Chain Multiplication)"],
            "targets": "Formulate recurrence relations for DP problems, solve 50 practice questions",
            "buffer_day": "Sunday: Algorithms Subject Test"
        },
        {
            "week": 10,
            "phase": "Syllabus Phase: Graph Algorithms & Automata",
            "phase_category": "syllabus",
            "subjects": ["Algorithms", "Theory of Computation"],
            "topics": ["Graph Traversals (BFS, DFS, Topological Sort)", "MST (Prim, Kruskal) & Shortest Paths (Dijkstra, Bellman-Ford)", "DFA, NFA, Minimization & Regular Expressions"],
            "targets": "Construct minimal DFAs, practice Dijkstra and Bellman-Ford algorithms",
            "buffer_day": "Sunday: TOC Foundations Quiz"
        },
        {
            "week": 11,
            "phase": "Syllabus Phase: Formal Languages & Compilers",
            "phase_category": "syllabus",
            "subjects": ["Theory of Computation", "Compiler Design"],
            "topics": ["Pumping Lemma (Regular & CFL)", "Pushdown Automata (DPDA vs NPDA)", "Turing Machines & Decidability", "Lexical Analysis & LL(1) Parsing (FIRST and FOLLOW)"],
            "targets": "Compute FIRST/FOLLOW sets, prove non-regularity with Pumping Lemma",
            "buffer_day": "Sunday: TOC & Compiler Design Test"
        },
        {
            "week": 12,
            "phase": "Syllabus Phase: Bottom-Up Parsing & Optimization",
            "phase_category": "syllabus",
            "subjects": ["Compiler Design"],
            "topics": ["Bottom-Up Parsing (LR(0), SLR(1), LALR(1), CLR(1))", "Syntax Directed Translation (SDT - S-attributed vs L-attributed)", "Intermediate Code Generation & Basic Blocks", "Local Optimization & Data Flow Analysis (Constant Propagation, Liveness)"],
            "targets": "Solve parsing table conflict problems, trace data flow liveness",
            "buffer_day": "Sunday: Compiler Design Subject Test"
        },
        {
            "week": 13,
            "phase": "Syllabus Phase: Operating Systems (CPU & Concurrency)",
            "phase_category": "syllabus",
            "subjects": ["Operating Systems"],
            "topics": ["System Calls, Processes & Threads", "CPU Scheduling (FCFS, SJF, SRTF, Round Robin)", "Process Synchronization (Peterson's Algorithm, Semaphores, Producer-Consumer)", "Deadlocks (Banker's Algorithm, Resource Allocation Graphs)"],
            "targets": "Solve Gantt chart scheduling numericals, trace semaphore synchronization primitives",
            "buffer_day": "Sunday: OS Scheduling & Concurrency Assessment"
        },
        {
            "week": 14,
            "phase": "Syllabus Phase: OS Memory Management & Relational DBMS",
            "phase_category": "syllabus",
            "subjects": ["Operating Systems", "Databases"],
            "topics": ["Virtual Memory, Paging, Multi-level Paging, TLB & Effective Access Time", "Page Replacement Algorithms (FIFO, LRU, Optimal)", "ER Modeling, Relational Algebra & SQL (Joins, Nested Queries, Aggregates)"],
            "targets": "Calculate EMAT with TLB, solve 30 complex relational algebra and SQL queries",
            "buffer_day": "Sunday: OS & SQL Mixed Subject Test"
        },
        {
            "week": 15,
            "phase": "Syllabus Phase: Normalization & Storage",
            "phase_category": "syllabus",
            "subjects": ["Databases"],
            "topics": ["Functional Dependencies & Normal Forms (1NF, 2NF, 3NF, BCNF)", "Lossless Decomposition & Dependency Preservation", "B-Trees & B+ Trees (Node capacity, Index depth)", "Transactions, ACID Properties, Serializability & 2PL"],
            "targets": "Find candidate keys, test serializability using precedence graphs",
            "buffer_day": "Sunday: Databases Full Subject Test (50 Marks)"
        },
        {
            "week": 16,
            "phase": "Syllabus Phase: Computer Networks & Quantitative Aptitude",
            "phase_category": "syllabus",
            "subjects": ["Computer Networks", "General Aptitude"],
            "topics": ["Layering & Delay Calculations, CSMA/CD Minimum Frame Size", "IPv4 Addressing, Subnetting, CIDR & Fragmentation", "Routing (Distance Vector vs Link State)", "TCP Flow & Congestion Control (Slow Start, Congestion Avoidance)", "Quantitative & Spatial Aptitude"],
            "targets": "Solve IP fragmentation numericals, TCP congestion window problems, finish remaining syllabus",
            "buffer_day": "🎯 OFFICIAL MILESTONE: 100% SYLLABUS COMPLETED (3 MONTHS BEFORE EXAM)!"
        },

        # --- PHASE 2: MONTH -3 (NOVEMBER 2026) - ROUND 1 REVISION & SUBJECT TESTS ---
        {
            "week": 17,
            "phase": "Month -3 Revision: Engineering Math, Digital & COA",
            "phase_category": "revision",
            "subjects": ["Engineering Mathematics", "Digital Logic", "Computer Organization"],
            "topics": ["Formula consolidation across Linear Algebra, Calculus & Discrete Math", "K-Map minimization & mod-N counter error correction", "Cache mapping & pipelining hazard rapid problem solving", "Subject Test 1 (Math), Subject Test 2 (Digital), Subject Test 3 (COA)"],
            "targets": "Re-solve all starred PYQs, complete 3 subject-level timed tests, log errors in mistake notebook",
            "buffer_day": "Sunday: Complete Revision Assessment (Math + Hardware)"
        },
        {
            "week": 18,
            "phase": "Month -3 Revision: Programming, Data Structures & Algorithms",
            "phase_category": "revision",
            "subjects": ["Programming in C", "Data Structures", "Algorithms"],
            "topics": ["Pointers & recursion dry-run drills", "BST, Heapify & Graph traversal edge cases", "Dynamic Programming recurrence practice & Greedy correctness", "Subject Test 4 (C & DS), Subject Test 5 (Algorithms)"],
            "targets": "Solve 75 high-difficulty questions, re-test tricky C pointers, 2 full subject tests",
            "buffer_day": "Sunday: Coding & Algorithms Marathon Review"
        },
        {
            "week": 19,
            "phase": "Month -3 Revision: TOC, Compilers & OS",
            "phase_category": "revision",
            "subjects": ["Theory of Computation", "Compiler Design", "Operating Systems"],
            "topics": ["DFA construction shortcuts, undecidability closure tables", "FIRST/FOLLOW computation & LR parsing conflicts", "Deadlocks, Bankers algorithm & Paging EMAT speed calculations", "Subject Test 6 (TOC & CD), Subject Test 7 (OS)"],
            "targets": "Master closure property tables, solve 10 tricky parsing conflict questions",
            "buffer_day": "Sunday: Systems & Automata Full Test"
        },
        {
            "week": 20,
            "phase": "Month -3 Revision: Databases, Networks & Aptitude Grand Review",
            "phase_category": "revision",
            "subjects": ["Databases", "Computer Networks", "General Aptitude"],
            "topics": ["Normalization algorithm review, serializability test graphs", "IP subnetting speed drills, TCP congestion control state machine", "Spatial & Analytical reasoning drills", "Subject Test 8 (DBMS), Subject Test 9 (Networks), Subject Test 10 (Aptitude)"],
            "targets": "Complete Month -3 revision cycle with all 10 subject tests submitted and reviewed",
            "buffer_day": "Sunday: Month -3 Comprehensive Review & Error Log Audit"
        },

        # --- PHASE 3: MONTH -2 (DECEMBER 2026) - ALL-INDIA FULL-LENGTH CBT MOCK SERIES ---
        {
            "week": 21,
            "phase": "Month -2 Mocks: Full-Length CBT Simulation 1 & 2",
            "phase_category": "mocks",
            "subjects": ["Full GATE CSE Syllabus (65 Questions, 180 Minutes, IIT Pattern)"],
            "topics": ["Full-Length Mock Test 1 (Under strict 3-hour timer, exact negative marking)", "Deep 4-Hour Post-Exam Diagnostic (Segregate conceptual vs silly vs calculation errors)", "Full-Length Mock Test 2", "Remediation of identified weak areas"],
            "targets": "Score > 60/100, analyze negative marks, eliminate unforced errors",
            "buffer_day": "Sunday: Virtual Calculator calculation drill (30 minutes)"
        },
        {
            "week": 22,
            "phase": "Month -2 Mocks: Full-Length CBT Simulation 3 & 4",
            "phase_category": "mocks",
            "subjects": ["Full GATE CSE Syllabus"],
            "topics": ["Full-Length Mock Test 3", "Time Allocation Strategy Calibration (60m Aptitude & Math, 90m CS Core, 30m Review)", "Full-Length Mock Test 4", "Multi-Select Questions (MSQ) high-precision practice"],
            "targets": "Simulate exact exam hall conditions, optimize question-skipping strategy",
            "buffer_day": "Sunday: Multi-concept MSQ mastery session"
        },
        {
            "week": 23,
            "phase": "Month -2 Mocks: Full-Length CBT Simulation 5 & 6",
            "phase_category": "mocks",
            "subjects": ["Full GATE CSE Syllabus"],
            "topics": ["Full-Length Mock Test 5", "Speed Tuning for Numerical Answer Type (NAT) Questions", "Full-Length Mock Test 6", "Cross-subject mixed revision (Engg Math + Algorithms + OS)"],
            "targets": "Zero negative marks in 1-mark questions, NAT numerical precision check",
            "buffer_day": "Sunday: High-yield formula sheet review"
        },
        {
            "week": 24,
            "phase": "Month -2 Mocks: Full-Length CBT Simulation 7 & 8",
            "phase_category": "mocks",
            "subjects": ["Full GATE CSE Syllabus"],
            "topics": ["Full-Length Mock Test 7", "Full-Length Mock Test 8", "Comprehensive performance trajectory audit (Targeting consistent 70+ marks)", "Mistake notebook consolidation"],
            "targets": "Consolidate 8 completed full-length tests into one master weak-point sheet",
            "buffer_day": "Sunday: Rest, mental recharge, and strategy review"
        },

        # --- PHASE 4: MONTH -1 (JANUARY 2027) - WEAK-AREA ERADICATION & FINAL LAP ---
        {
            "week": 25,
            "phase": "Month -1 Final Sprint: CBT Mock 9 & 10 + High-Yield Concepts",
            "phase_category": "final_sprint",
            "subjects": ["Full GATE CSE Syllabus"],
            "topics": ["Full-Length Mock Test 9 (Official exam environment)", "Full-Length Mock Test 10 (Last full-length mock)", "Deep dive into top 25 high-probability GATE concepts (Cache AMAT, Pipeline Hazards, Paging, Normalization, LL/LR parsing, Graph algorithms)"],
            "targets": "Lock in final mock test scoring baseline, review every single error across all 10 mocks",
            "buffer_day": "Sunday: Final full-length exam retrospective"
        },
        {
            "week": 26,
            "phase": "Month -1 Final Sprint: Master Formula Sheet Drills",
            "phase_category": "final_sprint",
            "subjects": ["All 11 GATE CSE Subjects"],
            "topics": ["Master Formula Sheet & Cheat Sheet rapid drills", "Handshaking lemma, Planar graphs, Eigenvalues, Paging formulas, AMAT equations, Minimum frame size", "Zero-calculation conceptual sanity checks"],
            "targets": "Memorize and reproduce all essential formulas on blank paper within 90 minutes",
            "buffer_day": "Sunday: 60-Minute rapid-fire formula quiz"
        },
        {
            "week": 27,
            "phase": "Month -1 Final Sprint: Recent 5-Year PYQs (2022-2026)",
            "phase_category": "final_sprint",
            "subjects": ["Verified Recent GATE Papers (2022, 2023, 2024, 2025, 2026)"],
            "topics": ["Solve official GATE 2026 CS paper in one sitting", "Solve official GATE 2025 & 2024 CS papers", "Identify latest examination style nuances, tricky MSQs, and trap NATs"],
            "targets": "Achieve 75+ in recent actual exam papers to build peak exam-day confidence",
            "buffer_day": "Sunday: Error log final clearance"
        },
        {
            "week": 28,
            "phase": "Month -1 Final Sprint: 30-Day Battle Plan & Weakness Elimination",
            "phase_category": "final_sprint",
            "subjects": ["Full Preparation Architecture"],
            "topics": ["30-Day sprint protocol execution", "Read Quick Revision Notes across all 11 subjects", "Zero new learning: Only revision of proven strengths and high-yield anchors"],
            "targets": "Achieve complete peace of mind with 100% preparation, 10 mocks, and 14 years of PYQs completed",
            "buffer_day": "Sunday: Light review and transition to Exam Week"
        },

        # --- PHASE 5: EXAM WEEK (FEBRUARY 1-6, 2027) - CALIBRATION & D-DAY ---
        {
            "week": 29,
            "phase": "Exam Week: Final-Week and Last-Day Revision Pack",
            "phase_category": "exam_week",
            "subjects": ["Final Week Protocol"],
            "topics": ["Final-week and last-day revision pack review", "Admit card, photo ID, station verification", "Circadian rhythm synchronization: Match wake-up and peak mental alertness to GATE exam shift time", "Positive mindset calibration and stress reduction"],
            "targets": "Review 1-page cheat sheets, sleep 8+ hours nightly, arrive at test center with absolute clarity",
            "buffer_day": "February 6, 2027: GATE 2027 Examination Day — Peak Performance!"
        }
    ]
}
