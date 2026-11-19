# textbook_em_dl.py
# Simple English, point-by-point study notes for Engineering Mathematics (EM) and Digital Logic (DL).
# Written in crystal-clear, student-friendly language for GATE 2027 CSE aspirants.

CHAPTERS_EM_DL = {}

# =============================================================================
# ENGINEERING MATHEMATICS (EM)
# =============================================================================

# EM Chapter 0: Mathematical Logic & Set Theory
CHAPTERS_EM_DL[("EM", 0)] = {
    "sub_id": "EM",
    "chap_idx": 0,
    "title": "Discrete Mathematics - Mathematical Logic & Set Theory",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Wi-Fi Login Password (What is a Proposition?)",
            "text": (
                "When you type your Wi-Fi password on your smartphone, the router tests only one question:\n"
                "Is the password Correct (True) or Incorrect (False)? There is no 'maybe' or 'half-correct'.\n"
                "In computer science, any declarative statement that is strictly True or False is called a Proposition.\n"
                "Sentences like 'What is your name?' (question) or 'Please pass the salt' (command) are NOT propositions because they cannot be assigned a true/false value."
            )
        },
        {
            "title": "Real-Life Example 2: Dad's Promise (How Implication P → Q Really Works)",
            "text": (
                "Imagine your father makes a promise: 'If you score AIR 1 in GATE (P), I will buy you a new bike (Q)'.\n"
                "When would you call your dad a liar?\n"
                "• Case 1: You get AIR 1 (T) and he buys the bike (T) ⇒ Promise kept! (T → T = True).\n"
                "• Case 2: You get AIR 1 (T) and he refuses to buy the bike (F) ⇒ Promise broken! (T → F = False).\n"
                "• Case 3: You did NOT get AIR 1 (F). Whether he buys the bike anyway or not, he never broke his original promise!\n"
                "This is why whenever condition P is False, (P → Q) is ALWAYS considered mathematically TRUE. This is called Vacuous Truth."
            )
        },
        {
            "title": "Real-Life Example 3: Social Media Friends (Relations Made Simple)",
            "text": (
                "Think of people on Facebook or Instagram:\n"
                "• Reflexive: Can you see your own profile? Yes! Every person relates to themselves: (x, x) ∈ R.\n"
                "• Symmetric: On Facebook, if Alice is friends with Bob, Bob is automatically friends with Alice: (x, y) ∈ R implies (y, x) ∈ R.\n"
                "• Transitive: If Alice trusts Bob, and Bob trusts Charlie, does Alice automatically trust Charlie? If yes, it is Transitive.\n"
                "When a relation is Reflexive + Symmetric + Transitive, it divides everyone into clean friend circles called Equivalence Classes."
            )
        }
    ],
    "foundations": [
        {
            "number": "1.1",
            "title": "Propositions & Basic Logic Connectives",
            "content": (
                "A proposition is any statement that is strictly True (T) or False (F).<br/><br/>"
                "Here are the 5 core logical connectives explained in simple points:<br/>"
                "• <b>NOT (~P):</b> Flips the truth. If P is True, ~P is False.<br/>"
                "• <b>AND (P ∧ Q):</b> True ONLY if BOTH P and Q are True (like needing two security keys to open a locker).<br/>"
                "• <b>OR (P ∨ Q):</b> True if AT LEAST ONE of P or Q is True. False only when both are False.<br/>"
                "• <b>Implication (P → Q):</b> Means 'If P then Q'. It is logically equivalent to <b>(~P ∨ Q)</b>.<br/>"
                "• <b>Biconditional (P ↔ Q):</b> True when both P and Q have the exact same truth value (both True or both False)."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: P → Q is False ONLY when P is True and Q is False. In all other 3 combinations, it is ALWAYS True!"
        },
        {
            "number": "1.2",
            "title": "Contrapositive, Converse, and Inverse",
            "content": (
                "For any conditional statement 'If P then Q' (P → Q):<br/><br/>"
                "• <b>Contrapositive (~Q → ~P):</b> 'If NOT Q, then NOT P'.<br/>"
                "&nbsp;&nbsp;- <b>100% Logically Equivalent:</b> (P → Q) ≡ (~Q → ~P). Always use this when proving theorems in GATE!<br/><br/>"
                "• <b>Converse (Q → P):</b> 'If Q, then P'.<br/>"
                "&nbsp;&nbsp;- NOT equivalent to the original statement.<br/><br/>"
                "• <b>Inverse (~P → ~Q):</b> 'If NOT P, then NOT Q'.<br/>"
                "&nbsp;&nbsp;- Equivalent to the Converse, but NOT the original statement."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: A statement and its Contrapositive always share the exact same truth table: (P → Q) ≡ (~Q → ~P)."
        },
        {
            "number": "1.3",
            "title": "Quantifiers: For All (∀) vs There Exists (∃)",
            "content": (
                "• <b>Universal Quantifier (∀x):</b> Means 'For EVERY single item in the universe'.<br/>"
                "&nbsp;&nbsp;- If even one single item fails, the entire statement becomes False.<br/><br/>"
                "• <b>Existential Quantifier (∃x):</b> Means 'There exists AT LEAST ONE item'.<br/>"
                "&nbsp;&nbsp;- As long as you can find one matching example, the statement is True.<br/><br/>"
                "• <b>De Morgan's Negation Rules for Quantifiers:</b><br/>"
                "&nbsp;&nbsp;- ~[ ∀x P(x) ] &nbsp;≡&nbsp; ∃x [ ~P(x) ]. (Negating 'All birds fly' is 'There exists a bird that cannot fly').<br/>"
                "&nbsp;&nbsp;- ~[ ∃x P(x) ] &nbsp;≡&nbsp; ∀x [ ~P(x) ]. (Negating 'Someone scored 100' is 'Everyone scored not 100')."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Negating 'All students passed' is NOT 'No students passed'. It is simply 'There is at least one student who failed'!"
        },
        {
            "number": "1.4",
            "title": "Counting Relations on a Set of Size n",
            "content": (
                "Let set A have n elements. The Cartesian product A × A has n² pairs.<br/><br/>"
                "Formulas to memorize for GATE:<br/>"
                "• Total possible relations = <b>2^(n²)</b>.<br/>"
                "• Total Reflexive relations = <b>2^(n² - n)</b>.<br/>"
                "• Total Symmetric relations = <b>2^(n(n+1)/2)</b>.<br/>"
                "• Total Reflexive and Symmetric relations = <b>2^(n(n-1)/2)</b>.<br/>"
                "• Total Equivalence relations = Counted by <b>Bell Numbers</b>:<br/>"
                "&nbsp;&nbsp;B(1) = 1, B(2) = 2, B(3) = 5, B(4) = 15, B(5) = 52."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Remember Bell Number B(4) = 15. Questions asking for the number of equivalence relations on a set of 4 elements can be answered in 2 seconds with 15!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Counting Symmetric Relations",
            "problem": "Set A has 4 elements: A = {1, 2, 3, 4}. How many symmetric relations can be formed on set A?",
            "steps": [
                "Step 1: Formula for symmetric relations on a set with n elements is: Total = 2^(n(n+1)/2).",
                "Step 2: Here n = 4.",
                "Step 3: Calculate the exponent: (4 × (4 + 1)) / 2 = (4 × 5) / 2 = 20 / 2 = 10.",
                "Step 4: Compute 2^10 = 1024."
            ],
            "answer": "Total Symmetric Relations = 1024."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: The Empty Relation (Vacuous Truth)",
            "warning": "Is the empty relation ∅ on a non-empty set symmetric? YES! It is vacuously symmetric and transitive, but it is NOT reflexive."
        }
    ]
}

# EM Chapter 1: Combinatorics & Graph Theory
CHAPTERS_EM_DL[("EM", 1)] = {
    "sub_id": "EM",
    "chap_idx": 1,
    "title": "Combinatorics, Recurrence Relations & Graph Theory",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Sock Drawer in the Dark (Pigeonhole Principle)",
            "text": (
                "You have a dark room with a drawer containing 10 Black socks and 10 White socks.\n"
                "How many socks must you pull out to be 100% guaranteed to have at least one matching pair?\n"
                "Pigeonholes (colors) = 2. Pigeons (socks pulled) = 3.\n"
                "By Pigeonhole Principle, pulling 2 + 1 = 3 socks guarantees at least two socks share the same color!"
            )
        },
        {
            "title": "Real-Life Example 2: Handshakes at a Party (Degree Sum Formula)",
            "text": (
                "Every time two people shake hands, exactly 2 hands are involved (one from each person).\n"
                "Therefore, if you count everyone's individual handshakes and add them all together, the grand total must be an EVEN number: Sum of Degrees = 2 × (Total Handshakes/Edges). It is impossible for an odd number of people to have shaken an odd number of hands!"
            )
        }
    ],
    "foundations": [
        {
            "number": "2.1",
            "title": "Pigeonhole Principle (PHP) Formulas",
            "content": (
                "• <b>Basic PHP:</b> If n items (pigeons) are put into k boxes (pigeonholes) and n > k, at least one box contains ≥ 2 items.<br/><br/>"
                "• <b>Generalized PHP:</b> If n items are put into k boxes, at least one box must contain at least <b>⌈n / k⌉</b> items.<br/><br/>"
                "• <b>Minimum items needed for a guarantee:</b><br/>"
                "&nbsp;&nbsp;To guarantee that at least one box has m items, you need: <b>k(m - 1) + 1</b> items."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: In a group of n people, there are ALWAYS at least two people who have the exact same number of friends in that group!"
        },
        {
            "number": "2.2",
            "title": "Graph Theory Core Theorems",
            "content": (
                "• <b>Handshaking Theorem:</b><br/>"
                "&nbsp;&nbsp;Sum of degrees of all vertices = <b>2 × |E|</b>.<br/>"
                "&nbsp;&nbsp;Direct consequence: The number of vertices with odd degree is ALWAYS EVEN.<br/><br/>"
                "• <b>Euler's Formula for Planar Graphs:</b><br/>"
                "&nbsp;&nbsp;For any connected planar graph: <b>V - E + F = 2</b> (where F = faces/regions, including outer face).<br/>"
                "&nbsp;&nbsp;Planar inequality: <b>E ≤ 3V - 6</b> (for V ≥ 3).<br/><br/>"
                "• <b>Bipartite Graph Test:</b><br/>"
                "&nbsp;&nbsp;A graph is bipartite if and only if it contains <b>NO ODD CYCLES</b> (cycles of length 3, 5, 7...)."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Complete graph K_n has n(n-1)/2 edges. A tree with n vertices ALWAYS has exactly n - 1 edges and is 2-colorable!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Planar Graph Faces",
            "problem": "A connected planar graph has 10 vertices each of degree 3. How many faces/regions does it divide the plane into?",
            "steps": [
                "Step 1: Use Handshaking Theorem to find edges: Sum of degrees = 10 × 3 = 30.",
                "Step 2: 2E = 30 ⇒ E = 15 edges.",
                "Step 3: Apply Euler's Planar Formula: V - E + F = 2.",
                "Step 4: Substitute V = 10, E = 15: 10 - 15 + F = 2 ⇒ -5 + F = 2 ⇒ F = 7."
            ],
            "answer": "Total Faces F = 7."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Euler Path vs Euler Circuit",
            "warning": "Euler Circuit (starts and ends at same vertex): Graph must be connected and ALL vertices have EVEN degree. Euler Path (open walk): Graph has EXACTLY TWO vertices with ODD degree."
        }
    ]
}

# EM Chapter 2: Linear Algebra
CHAPTERS_EM_DL[("EM", 2)] = {
    "sub_id": "EM",
    "chap_idx": 2,
    "title": "Linear Algebra - Matrices, Systems of Equations & Eigenvalues",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Photo Zooming and Tilting (Eigenvectors & Transformations)",
            "text": (
                "When you pinch-to-zoom a photo on Instagram, every pixel moves outward.\n"
                "Most pixels change both their position and their direction. But the straight diagonal lines shooting out from the center only stretch; their direction never bends!\n"
                "Those special directions that never change direction under transformation are called **Eigenvectors**, and the zoom scale factor is the **Eigenvalue** (λ)."
            )
        }
    ],
    "foundations": [
        {
            "number": "3.1",
            "title": "System of Linear Equations (AX = B) Consistency",
            "content": (
                "Let A be an m × n matrix, and [A | B] be the augmented matrix:<br/><br/>"
                "• <b>Unique Solution:</b><br/>"
                "&nbsp;&nbsp;Rank(A) = Rank([A | B]) = n (number of variables).<br/><br/>"
                "• <b>Infinitely Many Solutions:</b><br/>"
                "&nbsp;&nbsp;Rank(A) = Rank([A | B]) = r < n.<br/>"
                "&nbsp;&nbsp;Number of free parameters / independent solutions = <b>n - r</b>.<br/><br/>"
                "• <b>No Solution (Inconsistent):</b><br/>"
                "&nbsp;&nbsp;Rank(A) < Rank([A | B])."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: For homogeneous system AX = 0: It ALWAYS has the trivial zero solution. It has non-trivial (infinite) solutions if and only if Determinant |A| = 0 (Rank < n)!"
        },
        {
            "number": "3.2",
            "title": "Eigenvalue Properties (The 5 Golden Results)",
            "content": (
                "• <b>1. Sum of Eigenvalues:</b> Equal to the <b>Trace of Matrix A</b> (sum of main diagonal elements):<br/>"
                "&nbsp;&nbsp;λ1 + λ2 + ... + λn = Trace(A).<br/><br/>"
                "• <b>2. Product of Eigenvalues:</b> Equal to the <b>Determinant |A|</b>:<br/>"
                "&nbsp;&nbsp;λ1 × λ2 × ... × λn = det(A).<br/><br/>"
                "• <b>3. Powers of A:</b> The eigenvalues of A^k are <b>λ^k</b>.<br/><br/>"
                "• <b>4. Inverse:</b> If A is invertible, eigenvalues of A^(-1) are <b>1 / λ</b>.<br/><br/>"
                "• <b>5. Triangular/Diagonal Matrices:</b> The eigenvalues are simply the <b>main diagonal entries</b>!"
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: In 90% of GATE questions on eigenvalues, you do NOT need to solve the characteristic equation det(A - λI) = 0! Just check which option matches Trace and Determinant!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Finding Eigenvalues Quickly",
            "problem": "Matrix A is [[4, 2], [2, 1]]. Find its eigenvalues without solving quadratic equations.",
            "steps": [
                "Step 1: Find Trace(A) = Main diagonal sum = 4 + 1 = 5.",
                "Step 2: Find Determinant(A) = (4 × 1) - (2 × 2) = 4 - 4 = 0.",
                "Step 3: We need two numbers λ1, λ2 such that λ1 + λ2 = 5 and λ1 × λ2 = 0.",
                "Step 4: Clearly, one eigenvalue is 0 and the other is 5."
            ],
            "answer": "Eigenvalues are λ = 0 and λ = 5."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Zero Eigenvalue",
            "warning": "If a matrix has λ = 0 as an eigenvalue, its determinant is 0, which means the matrix is SINGULAR and has NO inverse!"
        }
    ]
}

# EM Chapter 3: Calculus & Probability
CHAPTERS_EM_DL[("EM", 3)] = {
    "sub_id": "EM",
    "chap_idx": 3,
    "title": "Calculus, Probability Distributions & Bayes' Theorem",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Speedometer vs Odometer (Derivative vs Integral)",
            "text": (
                "• Derivative: Your speedometer needle showing 60 km/h right at this exact split-second (instantaneous rate of change).\n"
                "• Integral: Your trip meter showing total kilometers accumulated over the whole journey (area under the speed curve)."
            )
        },
        {
            "title": "Real-Life Example 2: Medical Test Result (Bayes' Theorem)",
            "text": (
                "A rare disease affects 1 in 1000 people. A lab test is 99% accurate.\n"
                "If you test positive, is there a 99% chance you are sick? Surprisingly NO! Because the disease is so rare, false positives from healthy people outnumber true positives from sick people. Bayes' Theorem updates probability using real prior base rates."
            )
        }
    ],
    "foundations": [
        {
            "number": "4.1",
            "title": "L'Hôpital's Rule & Maxima-Minima",
            "content": (
                "• <b>L'Hôpital's Rule:</b><br/>"
                "&nbsp;&nbsp;If limit gives indeterminate form <code>0 / 0</code> or <code>∞ / ∞</code>:<br/>"
                "&nbsp;&nbsp;<code>lim [f(x) / g(x)] = lim [f'(x) / g'(x)]</code> (differentiate numerator and denominator separately).<br/><br/>"
                "• <b>Finding Local Maxima and Minima:</b><br/>"
                "&nbsp;&nbsp;1. Set first derivative to zero: <code>f'(x) = 0</code> to find stationary/critical points.<br/>"
                "&nbsp;&nbsp;2. Compute second derivative <code>f''(x)</code>:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;- If <code>f''(x) < 0</code> ⇒ <b>Local Maximum</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;- If <code>f''(x) > 0</code> ⇒ <b>Local Minimum</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;- If <code>f''(x) == 0</code> ⇒ Test fails (check higher derivatives)."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Always check the boundary endpoints of a closed interval [a, b] when finding the Global/Absolute maximum or minimum!"
        },
        {
            "number": "4.2",
            "title": "Bayes' Theorem & Conditional Probability",
            "content": (
                "• <b>Conditional Probability:</b><br/>"
                "&nbsp;&nbsp;<code>P(A | B) = P(A ∩ B) / P(B)</code>.<br/><br/>"
                "• <b>Independent Events:</b><br/>"
                "&nbsp;&nbsp;A and B are independent if and only if <code>P(A ∩ B) = P(A) × P(B)</code>.<br/><br/>"
                "• <b>Bayes' Formula:</b><br/>"
                "&nbsp;&nbsp;<code>P(A_i | B) = [ P(B | A_i) × P(A_i) ] / [ Σ P(B | A_j) × P(A_j) ]</code>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Mutually exclusive events with non-zero probability are NEVER independent! If P(A ∩ B) = 0, then P(A) × P(B) cannot equal 0 unless one has probability 0."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Evaluating Indeterminate Limit",
            "problem": "Evaluate limit as x → 0 of (sin 3x) / x.",
            "steps": [
                "Step 1: Check form by substituting x = 0: sin(0) / 0 = 0 / 0 (Indeterminate form).",
                "Step 2: Apply L'Hôpital's Rule: differentiate numerator and denominator with respect to x.",
                "Step 3: d/dx [sin 3x] = 3 cos 3x. d/dx [x] = 1.",
                "Step 4: New limit = lim [3 cos 3x / 1] as x → 0 = 3 cos(0) = 3 × 1 = 3."
            ],
            "answer": "Limit = 3."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Variance Formula",
            "warning": "Variance Var(X) = E[X^2] - (E[X])^2. Also remember: Var(aX + b) = a^2 × Var(X). Adding a constant 'b' never changes the spread/variance!"
        }
    ]
}

# =============================================================================
# DIGITAL LOGIC (DL)
# =============================================================================

# DL Chapter 0: Number Systems & Floating Point
CHAPTERS_EM_DL[("DL", 0)] = {
    "sub_id": "DL",
    "chap_idx": 0,
    "title": "Number Systems, Signed Numbers & IEEE-754 Floating Point",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Car Odometer Overflow (Why 2's Complement is Brilliant)",
            "text": (
                "When an odometer reading 999999 clicks one more mile, it rolls over to 000000.\n"
                "In computer arithmetic, 2's complement uses this exact rollover trick: subtracting a number is identical to adding its complement!\n"
                "Because of this, digital processors don't need a separate subtraction circuit. The exact same binary adder performs both addition and subtraction."
            )
        }
    ],
    "foundations": [
        {
            "number": "5.1",
            "title": "Signed Number Ranges for n bits",
            "content": (
                "For an n-bit binary representation:<br/><br/>"
                "• <b>Unsigned:</b> 0 to <b>2^n - 1</b>.<br/>"
                "• <b>Sign-Magnitude:</b> -(2^(n-1) - 1) to +(2^(n-1) - 1). (Has two zeros: +0 and -0).<br/>"
                "• <b>1's Complement:</b> -(2^(n-1) - 1) to +(2^(n-1) - 1). (Has two zeros).<br/>"
                "• <b>2's Complement:</b> <b>-2^(n-1)</b> to <b>+(2^(n-1) - 1)</b>. (Only ONE unique zero!)."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: In 2's complement with n = 8 bits: Range is -128 to +127. Notice that -128 has NO positive counterpart (+128 cannot fit in 8 signed bits)!"
        },
        {
            "number": "5.2",
            "title": "IEEE-754 Single Precision (32-bit) Floating Point",
            "content": (
                "The 32 bits are split into 3 fields:<br/>"
                "• <b>Sign bit (S):</b> 1 bit (0 for positive, 1 for negative).<br/>"
                "• <b>Exponent (E):</b> 8 bits with <b>Bias = 127</b>. Actual exponent <code>e = E - 127</code>.<br/>"
                "• <b>Mantissa (M):</b> 23 bits representing fractional part with implicit leading 1: <code>1.M</code>.<br/><br/>"
                "• <b>Formula:</b> <code>Value = (-1)^S × (1.M) × 2^(E - 127)</code>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: If E = 255 and M = 0: Represents ±Infinity. If E = 255 and M ≠ 0: Represents NaN (Not a Number). If E = 0 and M = 0: Represents 0."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: 2's Complement Negation",
            "problem": "Find the 8-bit 2's complement representation of -29.",
            "steps": [
                "Step 1: Write +29 in 8-bit binary: 29 = 16 + 8 + 4 + 1 = 00011101.",
                "Step 2: Invert all bits (1's complement): 11100010.",
                "Step 3: Add 1: 11100010 + 1 = 11100011.",
                "Step 4: Verify: -128 + 64 + 32 + 2 + 1 = -128 + 99 = -29."
            ],
            "answer": "-29 in 8-bit 2's complement = 11100011."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Detecting Overflow in 2's Complement",
            "warning": "Overflow occurs when: (1) Adding two positive numbers yields a negative result, OR (2) Adding two negative numbers yields a positive result. In hardware: Overflow = Carry_In_to_MSB ⊕ Carry_Out_from_MSB!"
        }
    ]
}

# DL Chapter 1: Boolean Algebra & K-Maps
CHAPTERS_EM_DL[("DL", 1)] = {
    "sub_id": "DL",
    "chap_idx": 1,
    "title": "Boolean Algebra, Logic Gates & K-Map Minimization",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Hallway Two-Way Light Switches (XOR Gate)",
            "text": (
                "You have a stair light with one switch downstairs (A) and one upstairs (B).\n"
                "Flipping EITHER switch toggles the light. If both switches are in the same position (both up or both down), the light is OFF. If they are in different positions, the light is ON.\n"
                "This behavior is the textbook definition of an **XOR Gate**: output is 1 when inputs differ."
            )
        }
    ],
    "foundations": [
        {
            "number": "6.1",
            "title": "Universal Gates & Consensus Theorem",
            "content": (
                "• <b>Universal Gates:</b> <b>NAND</b> and <b>NOR</b> can build any logic circuit without any other gate.<br/>"
                "&nbsp;&nbsp;- Minimum NAND gates to make NOT = 1, AND = 2, OR = 3, XOR = 4, XNOR = 5.<br/><br/>"
                "• <b>Consensus Theorem:</b><br/>"
                "&nbsp;&nbsp;<code>AB + ~A C + BC = AB + ~A C</code>.<br/>"
                "&nbsp;&nbsp;(The redundant term <code>BC</code> can be eliminated entirely!)."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: To make XOR gate using only NAND gates takes 4 gates. To make XOR using only NOR gates takes 5 gates!"
        },
        {
            "number": "6.2",
            "title": "K-Map Rules & Essential Prime Implicants",
            "content": (
                "• <b>Implicant:</b> Any group of 1s in a K-map.<br/>"
                "• <b>Prime Implicant (PI):</b> A rectangle of size 1, 2, 4, 8, 16 that cannot be merged into a larger group.<br/>"
                "• <b>Essential Prime Implicant (EPI):</b> A Prime Implicant that covers at least one '1' that is NOT covered by any other PI.<br/>"
                "• <b>Minimal SOP expression:</b> Must include ALL Essential Prime Implicants!"
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Don't-care conditions (X) can be set to 1 if they help enlarge a group, or set to 0 if they don't. You never need to cover an isolated don't-care!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Consensus Theorem Simplification",
            "problem": "Simplify the Boolean function: F = A B + A' C + B C.",
            "steps": [
                "Step 1: Notice terms: A B has variable A, A' C has inverted variable A'.",
                "Step 2: The remaining variables from both terms are B and C, forming the third term B C.",
                "Step 3: By Consensus Theorem, B C is completely redundant.",
                "Step 4: Simplified expression = A B + A' C."
            ],
            "answer": "Minimal F = A B + A' C."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Gray Code in K-Maps",
            "warning": "K-Map rows and columns follow Gray Code: 00, 01, 11, 10. Notice 11 comes before 10 so that only 1 bit flips between adjacent cells!"
        }
    ]
}

# DL Chapter 2: Combinational Circuits
CHAPTERS_EM_DL[("DL", 2)] = {
    "sub_id": "DL",
    "chap_idx": 2,
    "title": "Combinational Circuits - Multiplexers, Decoders & Adders",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: TV Remote Channel Selector (Multiplexer - MUX)",
            "text": (
                "A cable dish receives 64 TV channels at once. Your TV screen can only display 1 channel at a time.\n"
                "When you punch channel number '4' on your remote control (Select lines), the TV switches and displays only channel 4. This is a Multiplexer: Many inputs in, 1 output out."
            )
        }
    ],
    "foundations": [
        {
            "number": "7.1",
            "title": "Multiplexer (MUX) as a Universal Circuit",
            "content": (
                "• A 2^n to 1 MUX has 2^n data inputs, n select lines, and 1 output.<br/>"
                "• <b>Implementing any n-variable function:</b><br/>"
                "&nbsp;&nbsp;- Using a 2^n to 1 MUX: Needs <b>NO external gates</b>! Connect variables to select lines.<br/>"
                "&nbsp;&nbsp;- Using a 2^(n-1) to 1 MUX: Connect (n-1) variables to select lines, and the remaining variable (0, 1, x, ~x) to data inputs."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Any Boolean function of n variables can be implemented using a single 2^(n-1) to 1 MUX with at most an inverter for the inputs!"
        },
        {
            "number": "7.2",
            "title": "Half Adder vs Full Adder",
            "content": (
                "• <b>Half Adder (Adds 2 bits A, B):</b><br/>"
                "&nbsp;&nbsp;- Sum = A ⊕ B.<br/>"
                "&nbsp;&nbsp;- Carry = A · B.<br/><br/>"
                "• <b>Full Adder (Adds 3 bits A, B, C_in):</b><br/>"
                "&nbsp;&nbsp;- Sum = A ⊕ B ⊕ C_in.<br/>"
                "&nbsp;&nbsp;- Carry = A·B + B·C_in + A·C_in = A·B + C_in·(A ⊕ B).<br/>"
                "&nbsp;&nbsp;- A Full Adder can be built from: <b>2 Half Adders and 1 OR gate</b>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Carry Lookahead Adder (CLA) eliminates the slow ripple delay of standard adders. Generation bit G_i = A_i · B_i; Propagation bit P_i = A_i ⊕ B_i. CLA calculates all carries in parallel in O(1) time!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Building Larger MUX from Smaller MUX",
            "problem": "How many 2-to-1 Multiplexers are needed to build a 16-to-1 Multiplexer?",
            "steps": [
                "Step 1: Level 1: 16 inputs need 16 / 2 = 8 MUXes (produces 8 outputs).",
                "Step 2: Level 2: 8 inputs need 8 / 2 = 4 MUXes (produces 4 outputs).",
                "Step 3: Level 3: 4 inputs need 4 / 2 = 2 MUXes (produces 2 outputs).",
                "Step 4: Level 4: 2 inputs need 2 / 2 = 1 MUX (produces 1 final output).",
                "Step 5: Total MUXes = 8 + 4 + 2 + 1 = 15."
            ],
            "answer": "Total 2-to-1 MUXes needed = 15."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Active-Low Decoders",
            "warning": "Many exam questions use decoders with active-low outputs (outputs are 0 when active, 1 when inactive). For active-low outputs, MINTERMS require NAND gates instead of OR gates!"
        }
    ]
}

# DL Chapter 3: Sequential Circuits
CHAPTERS_EM_DL[("DL", 3)] = {
    "sub_id": "DL",
    "chap_idx": 3,
    "title": "Sequential Circuits, Flip-Flops & Counters",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Elevator Floor Counter (Sequential State Memory)",
            "text": (
                "An elevator cannot decide whether to go UP or DOWN just by looking at what button you pressed.\n"
                "It MUST remember its Current State: What floor is it on right now? (Are we at floor 2 or floor 7?).\n"
                "A combinational circuit has no memory. A sequential circuit uses Flip-Flops as memory cells to store the current state."
            )
        }
    ],
    "foundations": [
        {
            "number": "8.1",
            "title": "Flip-Flop Characteristic Equations",
            "content": (
                "• <b>SR Flip-Flop:</b><br/>"
                "&nbsp;&nbsp;<code>Q_next = S + R' Q</code> &nbsp;(Constraint: S·R = 0, input S=1, R=1 is FORBIDDEN).<br/><br/>"
                "• <b>JK Flip-Flop (Eliminates forbidden state):</b><br/>"
                "&nbsp;&nbsp;<code>Q_next = J Q' + K' Q</code>.<br/>"
                "&nbsp;&nbsp;- J=1, K=1 causes <b>Toggle</b> (Q flips to Q').<br/><br/>"
                "• <b>D Flip-Flop (Data delay):</b><br/>"
                "&nbsp;&nbsp;<code>Q_next = D</code>.<br/><br/>"
                "• <b>T Flip-Flop (Toggle):</b><br/>"
                "&nbsp;&nbsp;<code>Q_next = T ⊕ Q</code>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Race-Around condition occurs in Level-Triggered JK flip-flops when J=1, K=1 and clock pulse width t_p > propagation delay t_pd. Solved by: Edge-Triggered Flip-Flops or Master-Slave JK Flip-Flops!"
        },
        {
            "number": "8.2",
            "title": "Counters: Modulus & States",
            "content": (
                "• <b>MOD-N Counter:</b> Counts N distinct states from 0 to N - 1. Requires <b>k = ⌈log2 N⌉</b> flip-flops.<br/><br/>"
                "• <b>Ring Counter (n flip-flops):</b><br/>"
                "&nbsp;&nbsp;- Exactly one '1' rotates: 1000 → 0100 → 0010 → 0001.<br/>"
                "&nbsp;&nbsp;- Total distinct states = <b>n</b>.<br/><br/>"
                "• <b>Johnson / Twisted-Ring Counter (n flip-flops):</b><br/>"
                "&nbsp;&nbsp;- Inverted output Q' feeds back to input D.<br/>"
                "&nbsp;&nbsp;- Total distinct states = <b>2n</b>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: With 4 flip-flops: A normal counter has 2^4 = 16 states. A Johnson counter has 2 × 4 = 8 states. A Ring counter has only 4 states!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Johnson Counter Sequence",
            "problem": "A 3-bit Johnson counter starts in state 000. Write its entire state transition cycle.",
            "steps": [
                "Step 1: Rule: In a Johnson counter, Q2 Q1 Q0 moves right, and Q0' enters at Q2.",
                "Step 2: Start: 000 ⇒ Q0 = 0, so Q0' = 1 enters left ⇒ Next: 100.",
                "Step 3: From 100 ⇒ Q0 = 0, so 1 enters left ⇒ Next: 110.",
                "Step 4: From 110 ⇒ Q0 = 0, so 1 enters left ⇒ Next: 111.",
                "Step 5: From 111 ⇒ Q0 = 1, so Q0' = 0 enters left ⇒ Next: 011.",
                "Step 6: From 011 ⇒ Q0 = 1, so 0 enters left ⇒ Next: 001.",
                "Step 7: From 001 ⇒ Q0 = 1, so 0 enters left ⇒ Next: 000 (Cycle complete!)."
            ],
            "answer": "Cycle of 6 states (2n = 2×3 = 6): 000 → 100 → 110 → 111 → 011 → 001 → 000."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Asynchronous Counter Clock Delay",
            "warning": "In an Asynchronous (Ripple) counter of n flip-flops, each flip-flop is clocked by the previous one. Total ripple delay = n × t_pd. Maximum clock frequency f_max = 1 / (n × t_pd)!"
        }
    ]
}
