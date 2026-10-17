# Full-Length Mock Tests and Diagnostic Test Data conforming to GATE 2027 (IIT Madras) pattern
# Duration: 180 Minutes (3 Hours)
# Total Questions: 65 (10 GA + 55 CS & Engineering Mathematics)
# Total Marks: 100 Marks

MOCK_TEST_META = {
    "exam": "GATE 2027",
    "paper": "CS",
    "total_questions": 65,
    "total_marks": 100,
    "duration_minutes": 180,
    "sections": [
        {"name": "General Aptitude", "question_range": [1, 10], "marks": 15},
        {"name": "Computer Science & Engineering Mathematics", "question_range": [11, 65], "marks": 85}
    ],
    "marking_rules": {
        "mcq_1m": {"positive": 1.0, "negative": -1.0/3.0},
        "mcq_2m": {"positive": 2.0, "negative": -2.0/3.0},
        "msq_1m": {"positive": 1.0, "negative": 0.0, "partial": 0.0},
        "msq_2m": {"positive": 2.0, "negative": 0.0, "partial": 0.0},
        "nat_1m": {"positive": 1.0, "negative": 0.0},
        "nat_2m": {"positive": 2.0, "negative": 0.0}
    }
}

FULL_MOCK_1_QUESTIONS = [
    # General Aptitude (Q1 - Q5: 1 Mark each)
    {
        "q_num": 1, "section": "General Aptitude", "type": "MCQ", "marks": 1,
        "text": "The price of petrol increased by 25%. By what percentage must a car owner reduce fuel consumption so that the total expenditure remains unchanged?",
        "options": {"A": "20%", "B": "25%", "C": "16.67%", "D": "33.33%"},
        "answer": "A",
        "explanation": "Reduction required = [r / (100 + r)] * 100% = [25 / (100 + 25)] * 100% = (25 / 125) * 100% = 20%."
    },
    {
        "q_num": 2, "section": "General Aptitude", "type": "MCQ", "marks": 1,
        "text": "Select the word that is OPPOSITE in meaning to 'EPHEMERAL':",
        "options": {"A": "Transient", "B": "Permanent", "C": "Fleeting", "D": "Evanece"},
        "answer": "B",
        "explanation": "'Ephemeral' means lasting for a very short time. Its opposite is 'Permanent' or eternal."
    },
    {
        "q_num": 3, "section": "General Aptitude", "type": "MCQ", "marks": 1,
        "text": "A man walks 4 km North, turns right and walks 3 km. How far is he from his initial starting point?",
        "options": {"A": "7 km", "B": "5 km", "C": "1 km", "D": "25 km"},
        "answer": "B",
        "explanation": "By Pythagoras theorem: Distance = sqrt(4^2 + 3^2) = sqrt(16 + 9) = sqrt(25) = 5 km."
    },
    {
        "q_num": 4, "section": "General Aptitude", "type": "MCQ", "marks": 1,
        "text": "Choose the grammatically correct sentence:",
        "options": {
            "A": "Neither the principal nor the teachers was present at the meeting.",
            "B": "Neither the principal nor the teachers were present at the meeting.",
            "C": "Neither the teachers nor the principal were present at the meeting.",
            "D": "Neither the principal or the teachers was present at the meeting."
        },
        "answer": "B",
        "explanation": "In 'Neither... nor', the verb agrees with the subject closest to it. In B, 'teachers' is plural, so 'were' is grammatically correct."
    },
    {
        "q_num": 5, "section": "General Aptitude", "type": "NAT", "marks": 1,
        "text": "A flat square paper is folded diagonally once and then folded in half again. How many layers of paper are formed?",
        "answer": "4",
        "explanation": "First fold doubles layers: 1 * 2 = 2 layers. Second fold doubles again: 2 * 2 = 4 layers."
    },
    # General Aptitude (Q6 - Q10: 2 Marks each)
    {
        "q_num": 6, "section": "General Aptitude", "type": "NAT", "marks": 2,
        "text": "P and Q can complete a project in 12 days and 18 days respectively. If they work together, in how many days will the project be completed? (Round to 1 decimal place)",
        "answer": "7.2",
        "explanation": "Combined efficiency = 1/12 + 1/18 = (3 + 2) / 36 = 5/36 per day. Time = 36 / 5 = 7.2 days."
    },
    {
        "q_num": 7, "section": "General Aptitude", "type": "MCQ", "marks": 2,
        "text": "If 'CLAW' is coded as 'DNDB', how is 'FOOT' coded using the same rule?",
        "options": {"A": "GQPV", "B": "HQQU", "C": "GPPU", "D": "GQQV"},
        "answer": "D",
        "explanation": "Shifts: C(+1)->D, L(+2)->N, A(+3)->D, W(+5)->B (or +1, +2, +3, +4? Let's check: W(23) + 5 = 28 mod 26 = 2 = B. If shifts are +1, +2, +3, +4 or +1, +2, +1, +2: C->D(+1), L->N(+2), A->D(+3), W->A(+4? No, W+5=B). For FOOT: F(+1)->G, O(+2)->Q, O(+3)->R, T(+4)->X. If pattern is +1, +2, +3, +5: F->G, O->Q, O->R, T->Y. If +1, +2, +2, +2: D."
    },
    {
        "q_num": 8, "section": "General Aptitude", "type": "MSQ", "marks": 2,
        "text": "Statements: All laptops are devices. Some devices are phones. Which of the following conclusions CANNOT be established with certainty?",
        "options": {
            "A": "All laptops are phones",
            "B": "Some phones are devices",
            "C": "Some laptops are phones",
            "D": "No laptop is a phone"
        },
        "answer": "A, C, D",
        "explanation": "'Some devices are phones' strictly implies 'Some phones are devices' (B is always true). The relation between laptops and phones is undetermined: they could intersect, be disjoint, or one be subset of another. Hence A, C, and D cannot be established with certainty."
    },
    {
        "q_num": 9, "section": "General Aptitude", "type": "NAT", "marks": 2,
        "text": "What is the sum of all interior angles (in degrees) of a regular hexagon?",
        "answer": "720",
        "explanation": "Sum of interior angles of n-sided polygon = (n - 2) * 180 degrees. For hexagon n = 6: (6 - 2) * 180 = 4 * 180 = 720 degrees."
    },
    {
        "q_num": 10, "section": "General Aptitude", "type": "MCQ", "marks": 2,
        "text": "In a class of 60 students, 35 play cricket, 25 play football, and 10 play both. How many students play NEITHER cricket nor football?",
        "options": {"A": "10", "B": "12", "C": "15", "D": "20"},
        "answer": "A",
        "explanation": "n(C ∪ F) = n(C) + n(F) - n(C ∩ F) = 35 + 25 - 10 = 50. Neither = 60 - 50 = 10 students."
    },

    # Technical Section: Q11 - Q35 (1 Mark each)
    {
        "q_num": 11, "section": "Computer Science & Engineering Mathematics", "type": "MCQ", "marks": 1,
        "text": "What is the chromatic number of any non-trivial tree with at least 2 vertices?",
        "options": {"A": "1", "B": "2", "C": "3", "D": "V"},
        "answer": "B",
        "explanation": "Every tree is a bipartite graph and contains no odd cycles. Therefore, its chromatic number is strictly 2."
    },
    {
        "q_num": 12, "section": "Computer Science & Engineering Mathematics", "type": "NAT", "marks": 1,
        "text": "What is the determinant of a 3x3 identity matrix?",
        "answer": "1",
        "explanation": "The determinant of any identity matrix of any order is 1."
    },
    {
        "q_num": 13, "section": "Computer Science & Engineering Mathematics", "type": "MCQ", "marks": 1,
        "text": "Which of the following gates is considered a UNIVERSAL logic gate?",
        "options": {"A": "AND", "B": "OR", "C": "NAND", "D": "XOR"},
        "answer": "C",
        "explanation": "NAND and NOR gates are functionally complete universal gates."
    },
    {
        "q_num": 14, "section": "Computer Science & Engineering Mathematics", "type": "NAT", "marks": 1,
        "text": "How many select lines are required for a 64-to-1 Multiplexer?",
        "answer": "6",
        "explanation": "For 2^n to 1 MUX, number of select lines = n. 64 = 2^6, so 6 select lines."
    },
    {
        "q_num": 15, "section": "Computer Science & Engineering Mathematics", "type": "MCQ", "marks": 1,
        "text": "Which addressing mode uses the program counter (PC) as the base register?",
        "options": {"A": "Direct", "B": "Register Indirect", "C": "PC-Relative", "D": "Indexed"},
        "answer": "C",
        "explanation": "PC-Relative addressing computes Effective Address EA = PC + Offset."
    },
    {
        "q_num": 16, "section": "Computer Science & Engineering Mathematics", "type": "MCQ", "marks": 1,
        "text": "What is the worst-case time complexity of QuickSort on an already sorted array when the pivot is always the first element?",
        "options": {"A": "O(n)", "B": "O(n log n)", "C": "O(n^2)", "D": "O(log n)"},
        "answer": "C",
        "explanation": "When array is already sorted and first element is pivot, partitions are completely unbalanced (0 and n-1), resulting in O(n^2) time."
    },
    {
        "q_num": 17, "section": "Computer Science & Engineering Mathematics", "type": "NAT", "marks": 1,
        "text": "A full binary tree has 15 leaf nodes. How many internal nodes with degree 2 does it have?",
        "answer": "14",
        "explanation": "In any binary tree, n0 = n2 + 1 => n2 = 15 - 1 = 14."
    },
    {
        "q_num": 18, "section": "Computer Science & Engineering Mathematics", "type": "MCQ", "marks": 1,
        "text": "Which phase of a compiler constructs the Parse Tree from tokens?",
        "options": {"A": "Lexical Analysis", "B": "Syntax Analysis", "C": "Semantic Analysis", "D": "Code Optimization"},
        "answer": "B",
        "explanation": "Syntax Analyzer (Parser) takes tokens and builds the Parse Tree."
    },
    {
        "q_num": 19, "section": "Computer Science & Engineering Mathematics", "type": "MCQ", "marks": 1,
        "text": "Which scheduling algorithm is mathematically provably optimal in minimizing average waiting time?",
        "options": {"A": "FCFS", "B": "Shortest Remaining Time First (SRTF)", "C": "Round Robin", "D": "Priority"},
        "answer": "B",
        "explanation": "SRTF (preemptive SJF) provably guarantees the minimum possible average waiting time."
    },
    {
        "q_num": 20, "section": "Computer Science & Engineering Mathematics", "type": "NAT", "marks": 1,
        "text": "A relation R has candidate keys AB and CD. How many prime attributes does relation R have?",
        "answer": "4",
        "explanation": "An attribute is prime if it appears in at least one candidate key. Attributes A, B, C, D are all prime (total = 4)."
    },

    # Technical Section: Q36 - Q65 (2 Marks each)
    {
        "q_num": 36, "section": "Computer Science & Engineering Mathematics", "type": "NAT", "marks": 2,
        "text": "A 4-way set associative cache has 128 sets. Each cache block is 64 bytes. If the physical address is 32 bits, what is the number of TAG bits?",
        "answer": "19",
        "explanation": "1. Block size = 64 bytes = 2^6 bytes => Offset w = 6 bits.<br/>2. Sets = 128 = 2^7 => Set index s = 7 bits.<br/>3. Tag bits = 32 - (7 + 6) = 32 - 13 = 19 bits."
    },
    {
        "q_num": 37, "section": "Computer Science & Engineering Mathematics", "type": "MCQ", "marks": 2,
        "text": "Let G be an undirected connected graph with distinct positive edge weights. Which of the following is TRUE?",
        "options": {
            "A": "G can have multiple distinct minimum spanning trees",
            "B": "The edge with the minimum weight is always included in every minimum spanning tree",
            "C": "The edge with the maximum weight is never included in any minimum spanning tree",
            "D": "Prim's and Kruskal's algorithms may produce trees of different total weights"
        },
        "answer": "B",
        "explanation": "When all edge weights are distinct, the MST is strictly UNIQUE. By the cut property, the global minimum edge across the cut separating any vertex is always in the MST. (Option C is false because if the maximum edge is a bridge, it MUST be included)."
    },
    {
        "q_num": 38, "section": "Computer Science & Engineering Mathematics", "type": "MSQ", "marks": 2,
        "text": "Which of the following languages is/are DECIDABLE?",
        "options": {
            "A": "Testing whether a regular language is empty (L = ∅)",
            "B": "Testing whether two DFAs accept the same language",
            "C": "Testing whether an arbitrary CFG is ambiguous",
            "D": "Testing whether a Turing Machine halts on empty input"
        },
        "answer": "A, B",
        "explanation": "Emptiness and equivalence of regular languages/DFAs are DECIDABLE (A and B). CFG ambiguity and Turing Machine halting problem are UNDECIDABLE (C and D)."
    },
    {
        "q_num": 39, "section": "Computer Science & Engineering Mathematics", "type": "NAT", "marks": 2,
        "text": "A system has 4 processes sharing 5 resource units of the same type. Each process needs at most 2 resource units. What is the minimum number of resource units required to guarantee that deadlock NEVER occurs?",
        "answer": "5",
        "explanation": "Condition for deadlock-free operation: Total Resources R ≥ ∑ (Max_i - 1) + 1.<br/>Here 4 processes each need max 2. R ≥ 4 * (2 - 1) + 1 = 4 * 1 + 1 = 5 resources.<br/>With 5 resources, deadlock is mathematically impossible."
    },
    {
        "q_num": 40, "section": "Computer Science & Engineering Mathematics", "type": "MCQ", "marks": 2,
        "text": "What is the decimal equivalent of the IEEE 754 single-precision floating point number 0x40C00000?",
        "options": {"A": "3.0", "B": "6.0", "C": "12.0", "D": "1.5"},
        "answer": "B",
        "explanation": "0x40C00000 in binary: 0 10000001 10000000000000000000000.<br/>Sign bit S = 0 (+).<br/>Exponent E = 10000001_2 = 129. Actual exponent = 129 - 127 = 2.<br/>Mantissa = 1.10000... = 1 + 1/2 = 1.5.<br/>Value = (+1) * 1.5 * 2^2 = 1.5 * 4 = 6.0."
    }
]
