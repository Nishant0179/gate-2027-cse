# Final Revision and Rapid Review Module for GATE 2027 CSE
# Includes: Master Formula Compilation, High-Yield Traps, Last-Month, Final-Week, and Last-Day Packs

FINAL_REVISION_DATA = {
    "master_formulas": [
        {
            "subject": "Engineering Mathematics",
            "formulas": [
                ("Handshaking Lemma", "∑ deg(v) = 2 |E| (Odd-degree vertices count is always even)"),
                ("Euler's Planar Formula", "V - E + R = 2 (for connected planar graphs)"),
                ("Planar Edge Bound", "E ≤ 3V - 6 (for V ≥ 3); E ≤ 2V - 4 (if triangle-free)"),
                ("Eigenvalue Trace Property", "∑ λ_i = Trace(A) = ∑ a_ii"),
                ("Eigenvalue Determinant Property", "∏ λ_i = det(A)"),
                ("Poisson Distribution", "P(X = k) = (e^(-λ) * λ^k) / k! (Mean = Variance = λ)"),
                ("Bayes' Theorem", "P(A|B) = [P(B|A) * P(A)] / P(B)"),
                ("Derangements Formula", "D_n = n! ∑_{k=0}^n (-1)^k / k! ≈ n! / e")
            ]
        },
        {
            "subject": "Digital Logic",
            "formulas": [
                ("De Morgan's Laws", "(A + B)' = A' B' and (AB)' = A' + B'"),
                ("Consensus Theorem", "AB + A'C + BC = AB + A'C"),
                ("2's Complement Range", "-2^(n-1) to +(2^(n-1) - 1)"),
                ("IEEE 754 Single Precision", "Value = (-1)^S * (1.M) * 2^(E - 127) (E in [1, 254])"),
                ("Carry Look-Ahead Adder", "G_i = A_i B_i, P_i = A_i ⊕ B_i, C_{i+1} = G_i + P_i C_i (O(1) delay)")
            ]
        },
        {
            "subject": "Computer Organization & Architecture",
            "formulas": [
                ("Direct Mapped Cache Bits", "Tag = Physical Address Bits - (Line Index Bits + Block Offset Bits)"),
                ("Set Associative Cache Bits", "Tag = Physical Address Bits - (Set Index Bits + Block Offset Bits)"),
                ("AMAT (Single Level)", "AMAT = Hit_Time + (Miss_Rate * Miss_Penalty)"),
                ("Pipeline Execution Time", "Time = [k + (n - 1)] * τ (for k stages, n instructions)"),
                ("Ideal Pipeline Speedup", "S_ideal = k (as n -> ∞)")
            ]
        },
        {
            "subject": "Programming and Data Structures",
            "formulas": [
                ("Array Pointer Equivalence", "a[i] ≡ *(a + i) ≡ *(i + a) ≡ i[a]"),
                ("Binary Tree Leaves vs Degree 2", "n0 = n2 + 1"),
                ("Catalan Numbers C_n", "C_n = (2n)! / ((n+1)! * n!) (BSTs with n keys, stack permutations)"),
                ("Max Nodes in Binary Tree", "N_max = 2^(h+1) - 1 (height h, root at 0)")
            ]
        },
        {
            "subject": "Algorithms",
            "formulas": [
                ("Master Theorem Case 1", "If log_b(a) > k => T(n) = Θ(n^(log_b a))"),
                ("Master Theorem Case 2", "If log_b(a) == k => T(n) = Θ(n^k * log^(p+1) n) for p > -1"),
                ("Comparison Sorting Bound", "Worst case comparisons ≥ Ω(n log n)"),
                ("Hash Table Load Factor", "α = n / m (Chaining: any α; Open Addressing: α ≤ 1)")
            ]
        },
        {
            "subject": "Theory of Computation",
            "formulas": [
                ("Regular Pumping Lemma", "s = xyz, |y| > 0, |xy| ≤ p, ∀i: x y^i z ∈ L"),
                ("CFL Pumping Lemma", "s = uvwxy, |vx| > 0, |vwx| ≤ p, ∀i: u v^i w x^i y ∈ L"),
                ("Myhill-Nerode Theorem", "L is regular iff the number of equivalence classes of R_L is FINITE")
            ]
        },
        {
            "subject": "Operating Systems",
            "formulas": [
                ("Turnaround & Waiting Times", "TAT = CT - AT; WT = TAT - BT"),
                ("Effective Memory Access (TLB)", "EMAT = c * (t + m) + (1 - c) * (t + 2m)"),
                ("Deadlock Avoidance Condition", "R ≥ ∑ (Max_i - 1) + 1 guarantees no deadlock")
            ]
        },
        {
            "subject": "Databases",
            "formulas": [
                ("Lossless Join Decomposition", "R1 ⋈ R2 is lossless iff (R1 ∩ R2) -> R1 OR (R1 ∩ R2) -> R2"),
                ("BCNF Condition", "For every non-trivial X -> Y, X must be a SUPER KEY"),
                ("B+ Tree Internal Node Order", "p * P + (p - 1) * K ≤ Block_Size")
            ]
        },
        {
            "subject": "Computer Networks",
            "formulas": [
                ("CSMA/CD Minimum Frame Size", "L_min ≥ 2 * Bandwidth * Propagation_Delay (T_t ≥ 2 T_p)"),
                ("Sliding Window Efficiency", "η = W / (1 + 2a) where a = T_p / T_t (100% when W ≥ 1 + 2a)"),
                ("IPv4 Fragment Offset", "Offset = (Payload Bytes Preceding) / 8")
            ]
        }
    ],
    "last_month_strategy": [
        "Day 30 to 21: Complete rapid revision of high-yield subjects (Math, DS, Algo, TOC, OS).",
        "Day 20 to 11: Daily subject test + 1 full-length mock test every alternate day. Analyze every single wrong question.",
        "Day 10 to 4: Solve all remaining verified PYQs (2020-2026) under timed test conditions.",
        "Day 3 to 1: Formula sheet drills, memory aids, and mental rest."
    ],
    "final_week_pack": [
        "Day 7: Engineering Mathematics & General Aptitude formula marathon.",
        "Day 6: Digital Logic & COA numerical formulas (Cache tags, IEEE 754, Pipeline speedup).",
        "Day 5: Programming & Data Structures (C code tracing, Tree properties, Catalan numbers).",
        "Day 4: Algorithms & TOC (Sorting complexities, Graph algorithms, Language closure tables).",
        "Day 3: Operating Systems & Databases (EMAT, Belady's anomaly, Normal forms, Serializability).",
        "Day 2: Computer Networks (Delays, CSMA/CD, IPv4 fragmentation, TCP congestion control).",
        "Day 1 (Last Day): Light review of master formula sheet. No heavy problem solving. Check admit card, photo ID, and test center."
    ]
}
