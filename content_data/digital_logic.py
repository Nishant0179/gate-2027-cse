# Digital Logic Content Module for GATE 2027 CSE
# Weightage: 5-7 Marks

SUBJECT_META = {
    "id": "DL",
    "name": "Digital Logic",
    "folder": "02_Digital_Logic",
    "weightage": "6 Marks",
    "topics": [
        "Boolean algebra and minimization – algebraic technique, Karnaugh map, tabular method",
        "Design of combinational circuits: Multiplexers, Decoders, Encoders, Adders, Subtractors",
        "Design of sequential circuits: Latches, Flip-Flops, Registers, Counters, State Diagrams",
        "Number representation and arithmetic: Fixed point, Signed representations, Floating point (IEEE 754)"
    ]
}

CHAPTERS = [
    {
        "title": "Boolean Algebra, K-Maps & Tabular Method (Quine-McCluskey)",
        "hinglish": "Boolean algebra me SOP (Sum of Products) aur POS (Product of Sums) ka minimization sabse fundamental step hai. GATE 2027 syllabus me Tabular method explicitly mention kiya gaya hai.",
        "theory": (
            "<b>1. Boolean Axioms & Theorems:</b><br/>"
            "• Identity: A + 0 = A, A . 1 = A.<br/>"
            "• Null / Dominance: A + 1 = 1, A . 0 = 0.<br/>"
            "• Idempotent: A + A = A, A . A = A.<br/>"
            "• Complement: A + A' = 1, A . A' = 0.<br/>"
            "• Involution: (A')' = A.<br/>"
            "• <b>De Morgan's Laws:</b> (A + B)' = A' . B' &nbsp;and&nbsp; (A . B)' = A' + B'.<br/>"
            "• <b>Consensus Theorem:</b> AB + A'C + BC = AB + A'C &nbsp;(Dual: (A+B)(A'+C)(B+C) = (A+B)(A'+C)).<br/>"
            "• <b>Transposition Theorem:</b> AB + A'C = (A + C)(A' + B).<br/><br/>"
            "<b>2. Karnaugh Maps (K-Maps):</b><br/>"
            "• Gray code ordering (adjacent cells differ by exactly 1 bit: 00, 01, 11, 10).<br/>"
            "• Grouping sizes must be powers of 2 (1, 2, 4, 8, 16). Larger groups eliminate more variables.<br/>"
            "• <b>Prime Implicant (PI):</b> A group of 1s (or 0s) that cannot be combined with any larger group.<br/>"
            "• <b>Essential Prime Implicant (EPI):</b> A PI that covers at least one '1' that is not covered by any other PI. All EPIs MUST be in the minimal SOP expression!<br/><br/>"
            "<b>3. Tabular Method (Quine-McCluskey):</b> Systematic method suited for higher variable counts (&gt;4).<br/>"
            "• Step 1: Group minterms by the count of 1s in their binary representation.<br/>"
            "• Step 2: Combine terms differing by exactly 1 bit (replace differing bit with hyphen '-').<br/>"
            "• Step 3: Repeat until no further combinations can be made. Remaining terms are Prime Implicants.<br/>"
            "• Step 4: Construct PI chart and select Essential Prime Implicants."
        ),
        "callouts": [
            ("Consensus Elimination", "In AB + A'C + BC, check if B and C appear with complement pair A and A'. The term BC is redundant and can be dropped immediately!", "tip"),
            ("Don't Care Condition", "Don't care minterms (d) can be included as '1' in K-map to make larger groups, but NEVER form a group consisting solely of don't cares!", "warn")
        ],
        "tables": [
            {
                "header": ["Gate Type", "Boolean Output", "Universal Gate?", "Parity Check Property"],
                "rows": [
                    ["NAND", "(AB)'", "Yes (Functionally Complete)", "Active LOW enable logic"],
                    ["NOR", "(A+B)'", "Yes (Functionally Complete)", "Dual of NAND"],
                    ["XOR (⊕)", "A'B + AB'", "No", "Odd Parity detector (1 when odd number of 1s)"],
                    ["XNOR (⊙)", "AB + A'B'", "No", "Even Parity detector / 1-bit Equivalence comparator"]
                ]
            }
        ]
    },
    {
        "title": "Combinational Circuits - MUX, Decoders & Arithmetic Circuits",
        "hinglish": "Multiplexer (MUX) ko universal combinational circuit kaha jata hai kyunki ek 2^n to 1 MUX se n+1 variable ka koi bhi function bina external gate ke implement ho sakta hai.",
        "theory": (
            "<b>1. Multiplexers (Data Selectors):</b><br/>"
            "• 2^n to 1 MUX has 2^n input lines, n select lines, and 1 output line.<br/>"
            "• Function Implementation: An n-variable function requires a 2^(n-1) to 1 MUX without external inverters if complements are available, or with at most 1 NOT gate.<br/><br/>"
            "<b>2. Decoders & Demultiplexers:</b><br/>"
            "• n to 2^n decoder activates exactly 1 of 2^n output minterms for each input code.<br/>"
            "• Active LOW outputs (using NAND) generate maxterms directly.<br/><br/>"
            "<b>3. Adders and Arithmetic:</b><br/>"
            "• <b>Half Adder:</b> Sum = A ⊕ B, Carry = A . B.<br/>"
            "• <b>Full Adder:</b> Sum = A ⊕ B ⊕ C_in, Carry = AB + BC_in + AC_in.<br/>"
            "• <b>Carry Look-Ahead Adder (CLA):</b> Eliminates ripple propagation delay.<br/>"
            "  - Generate: G_i = A_i . B_i &nbsp;|&nbsp; Propagate: P_i = A_i ⊕ B_i.<br/>"
            "  - Carry C_(i+1) = G_i + P_i . C_i. Constant delay O(1) regardless of number of bits!"
        ),
        "callouts": [
            ("CLA Delay Advantage", "Ripple carry adder delay is O(n), whereas CLA delay is O(1) in ideal gates or O(log n) with fan-in limits.", "formula"),
            ("MUX Implementation Trick", "For f(A, B, C), connect A and B to select lines S1, S0. The 4 data inputs (I0, I1, I2, I3) will be chosen from {0, 1, C, C'}.", "tip")
        ],
        "tables": []
    },
    {
        "title": "Sequential Circuits - Flip-Flops, Counters & State Machines",
        "hinglish": "Sequential circuits me memory element (Flip-Flop) hota hai jiska next state current input aur present state par depend karta hai.",
        "theory": (
            "<b>1. Flip-Flops and Characteristic Equations:</b><br/>"
            "• <b>SR Flip-Flop:</b> Q_(next) = S + R'Q (Constraint: S . R = 0). Invalid when S = R = 1.<br/>"
            "• <b>JK Flip-Flop:</b> Q_(next) = J Q' + K' Q. Eliminates race condition; toggles when J = K = 1.<br/>"
            "• <b>D Flip-Flop (Delay):</b> Q_(next) = D. Transmits input directly on clock edge.<br/>"
            "• <b>T Flip-Flop (Toggle):</b> Q_(next) = T ⊕ Q = T Q' + T' Q. Toggles when T = 1, holds when T = 0.<br/><br/>"
            "<b>2. Excitation Tables (Present Q -> Next Q'):</b><br/>"
            "• SR: 0->0: S=0,R=d | 0->1: S=1,R=0 | 1->0: S=0,R=1 | 1->1: S=d,R=0.<br/>"
            "• JK: 0->0: J=0,K=d | 0->1: J=1,K=d | 1->0: J=d,K=1 | 1->1: J=d,K=0.<br/>"
            "• D: 0->0: D=0 | 0->1: D=1 | 1->0: D=0 | 1->1: D=1.<br/>"
            "• T: 0->0: T=0 | 0->1: T=1 | 1->0: T=1 | 1->1: T=0.<br/><br/>"
            "<b>3. Counters:</b><br/>"
            "• Mod-N counter counts N distinct states (requires k flip-flops where 2^(k-1) &lt; N ≤ 2^k).<br/>"
            "• Johnson Counter (Twisted Ring): Uses k flip-flops, provides 2k states.<br/>"
            "• Ring Counter: Uses k flip-flops, provides k states."
        ),
        "callouts": [
            ("Master-Slave FF Purpose", "Master-Slave configuration is used in level-triggered JK flip-flops specifically to eliminate Race-Around Condition when J=K=1 and pulse width tp &gt; propagation delay.", "tip"),
            ("Unused States & Lock-up", "In counter design with unused states, always verify that the circuit recovers to the valid cycle if accidentally started in an unused state (Self-starting counter).", "warn")
        ],
        "tables": []
    },
    {
        "title": "Number Representation & Floating Point (IEEE 754)",
        "hinglish": "2's complement representation aur IEEE 754 standard GATE exam me repeated numericals ke favourite topics hain.",
        "theory": (
            "<b>1. Signed Number Representations (n-bit):</b><br/>"
            "• <b>Sign-Magnitude:</b> Range - (2^(n-1) - 1) to + (2^(n-1) - 1). Has two zeros (+0 and -0).<br/>"
            "• <b>1's Complement:</b> Range - (2^(n-1) - 1) to + (2^(n-1) - 1). Also has two zeros.<br/>"
            "• <b>2's Complement:</b> Range - 2^(n-1) to + (2^(n-1) - 1). UNIQUE ZERO! Range is asymmetric with one extra negative number (-2^(n-1)).<br/>"
            "• <b>2's complement shortcut:</b> Copy bits from right to left up to and including the first '1', then invert all remaining bits to the left.<br/><br/>"
            "<b>2. IEEE 754 Single Precision (32-bit):</b><br/>"
            "• <b>Sign bit (S):</b> 1 bit (0 for positive, 1 for negative).<br/>"
            "• <b>Exponent (E):</b> 8 bits, biased with +127 (Biased Exponent = Actual Exponent + 127).<br/>"
            "• <b>Mantissa / Fraction (M):</b> 23 bits, represents normalized fraction with implicit leading 1: (1.M)_2.<br/>"
            "• <b>Value formula:</b> (-1)^S * (1.M) * 2^(E - 127).<br/>"
            "• Special Values: E=0, M=0 -> Zero; E=255, M=0 -> ±Infinity; E=255, M≠0 -> NaN (Not a Number)."
        ),
        "callouts": [
            ("2's Complement Overflow", "Overflow occurs during addition of two numbers of the SAME SIGN when the result has the OPPOSITE SIGN. In terms of carry: Overflow = C_(in to MSB) ⊕ C_(out of MSB).", "formula"),
            ("Implicit 1 in IEEE 754", "Remember that the leading 1 before the binary point is IMPLICIT and NOT stored in the 23 mantissa bits! Do not write the leading 1 into the mantissa field.", "warn")
        ],
        "tables": []
    }
]

PRACTICE_QUESTIONS = [
    {
        "id": "DL-Q01",
        "type": "MCQ",
        "marks": 1,
        "text": "The minimum number of 2-to-1 multiplexers required to realize a 2-input XOR gate is:",
        "options": {
            "A": "1",
            "B": "2",
            "C": "3",
            "D": "4"
        },
        "answer": "B",
        "explanation": "XOR function is f(A, B) = A B' + A' B. Using a 2-to-1 MUX with A as select line: when A=0, output is B; when A=1, output must be B'. To generate B', a first 2-to-1 MUX is needed configured as an inverter (Select B, inputs 1 and 0). Then the second MUX implements XOR. Thus, exactly 2 MUXes are required.",
        "is_pyq": True,
        "year": 2022,
        "difficulty": "Easy"
    },
    {
        "id": "DL-Q02",
        "type": "NAT",
        "marks": 2,
        "text": "A 4-bit synchronous modulo-12 up-counter is constructed using T flip-flops. What is the count value (in decimal) immediately following the count 11 (1011_2)?",
        "answer": "0",
        "explanation": "A modulo-12 counter counts 12 distinct states from 0 up to 11 (0, 1, 2, ..., 11) and then wraps around directly to 0 on the next clock pulse.",
        "is_pyq": False,
        "year": None,
        "difficulty": "GATE-Level"
    },
    {
        "id": "DL-Q03",
        "type": "MCQ",
        "marks": 2,
        "text": "The decimal number -19.625 represented in IEEE 754 single-precision (32-bit) floating point format has which hexadecimal representation?",
        "options": {
            "A": "0xC19D0000",
            "B": "0x419D0000",
            "C": "0xC1A50000",
            "D": "0xC21D0000"
        },
        "answer": "A",
        "explanation": "1. Negative number -> Sign bit S = 1.<br/>2. 19.625 in binary: 19 = 10011_2, 0.625 = 0.101_2. Total = 10011.101_2.<br/>3. Normalized form: 1.0011101 * 2^4. Hence actual exponent = 4.<br/>4. Biased Exponent E = 4 + 127 = 131 = 10000011_2.<br/>5. Mantissa (23 bits after binary point): 0011101 0000000000000000.<br/>6. Combine: S (1) | E (10000011) | M (00111010000000000000000).<br/>7. Grouping in 4s: 1100 0001 1001 1101 0000 0000 0000 0000 = 0xC19D0000.",
        "is_pyq": True,
        "year": 2020,
        "difficulty": "Medium"
    },
    {
        "id": "DL-Q04",
        "type": "MSQ",
        "marks": 2,
        "text": "Which of the following Boolean functions is/are SELF-DUAL?",
        "options": {
            "A": "f(A, B, C) = AB + BC + CA",
            "B": "f(A, B) = A ⊕ B",
            "C": "f(A, B, C) = A ⊕ B ⊕ C",
            "D": "f(A) = A"
        },
        "answer": "A, C, D",
        "explanation": "A function is self-dual if f_dual = f. The dual is obtained by replacing AND with OR, OR with AND (leaving variables uncomplemented).<br/>A: Dual of AB + BC + CA is (A+B)(B+C)(C+A) = AB + BC + CA (Self-dual!).<br/>B: A ⊕ B = A'B + AB'. Dual is (A'+B)(A+B') = A'B' + AB = A ⊙ B ≠ A ⊕ B (Not self-dual).<br/>C: A ⊕ B ⊕ C with odd number of variables is always self-dual!<br/>D: f(A) = A, dual is A (Self-dual). Hence A, C, D are self-dual.",
        "is_pyq": False,
        "year": None,
        "difficulty": "GATE-Level"
    },
    {
        "id": "DL-Q05",
        "type": "NAT",
        "marks": 1,
        "text": "What is the maximum number of prime implicants that a 3-variable Boolean function can have?",
        "answer": "6",
        "explanation": "For an n-variable function, the maximum number of prime implicants is given by 2^(n-1) * 3^(n - n) pattern or specific configurations. For n = 3, an alternating checkerboard pattern like f = m(1, 2, 4, 7) or m(0, 3, 5, 6) has 4 PIs, but functions like m(1, 2, 4) with don't cares or 6 minterms can yield up to 6 prime implicants.",
        "is_pyq": False,
        "year": None,
        "difficulty": "Medium"
    }
]
