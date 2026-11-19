# textbook_em_dl.py
# Simplified, crystal-clear study notes for Engineering Mathematics (EM) and Digital Logic (DL).
# Written in simple, friendly, easy-to-understand language for GATE 2027 CSE aspirants.

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
            "text": "When you enter a Wi-Fi password on your phone, the router checks only one thing: Is the password Correct (True) or Incorrect (False)? There is no 'maybe' or 'half-correct'. In computer science, any statement that is strictly True or False is called a Proposition. Sentences like 'What is your name?' (a question) or 'Please give me water' (a request) are NOT propositions because they cannot be true or false."
        },
        {
            "title": "Real-Life Example 2: Dad's Promise (How Implication P → Q Really Works)",
            "text": "Imagine your father makes a promise: 'If you score AIR 1 in GATE (P), I will buy you a new bike (Q)'. When would you call your dad a liar? ONLY if you score AIR 1 and he refuses to buy the bike (True → False = False). What if you did NOT score AIR 1? He never broke his promise, whether he buys the bike anyway or not! That is why whenever the condition P is False, the statement (P → Q) is ALWAYS considered TRUE in logic. This is known as Vacuous Truth."
        },
        {
            "title": "Real-Life Example 3: Social Media Friends (Types of Relations Made Simple)",
            "text": "Think of people on Facebook or Instagram:\n• Reflexive: Can you follow or see your own profile? Yes! (Every person relates to themselves).\n• Symmetric: On Facebook, if Alice is friends with Bob, Bob is automatically friends with Alice (Friendship works both ways).\n• Transitive: If Alice trusts Bob, and Bob trusts Charlie, does Alice automatically trust Charlie? If yes, it is Transitive.\nWhen a relation is Reflexive + Symmetric + Transitive, it divides everyone into tight-knit friend groups called Equivalence Classes."
        }
    ],
    "foundations": [
        {
            "number": "1.1",
            "title": "Propositions & Basic Logic Connectives",
            "content": (
                "A proposition is any clear statement that is either True (T) or False (F).<br/>"
                "• <b>NOT (~P):</b> Flips the truth. If P is True, ~P is False.<br/>"
                "• <b>AND (P ∧ Q):</b> True ONLY if BOTH P and Q are True (like both keys needed to open a safe).<br/>"
                "• <b>OR (P ∨ Q):</b> True if AT LEAST ONE of P or Q is True (False only if both are False).<br/>"
                "• <b>Implication (P → Q):</b> Means 'If P then Q'. It is equivalent to <b>(~P ∨ Q)</b>.<br/>"
                "• <b>Double Arrow (P ↔ Q):</b> True when both have the exact same value (both True or both False)."
            ),
            "crucial_rule": "GOLDEN RULE: P → Q is False ONLY when P is True and Q is False. In all other 3 cases, it is ALWAYS True!"
        },
        {
            "number": "1.2",
            "title": "Contrapositive, Converse, and Inverse",
            "content": (
                "For any statement 'If P then Q' (P → Q):<br/>"
                "• <b>Contrapositive (~Q → ~P):</b> 'If NOT Q, then NOT P'. This is <b>100% equivalent</b> to the original statement! (Always use this in GATE when solving proofs).<br/>"
                "• <b>Converse (Q → P):</b> 'If Q, then P'. NOT always equal to original.<br/>"
                "• <b>Inverse (~P → ~Q):</b> 'If NOT P, then NOT Q'. Equal to Converse, but NOT the original."
            ),
            "crucial_rule": "GOLDEN RULE: A statement and its Contrapositive always have the exact same truth value: (P → Q) ≡ (~Q → ~P)."
        },
        {
            "number": "1.3",
            "title": "Quantifiers: For All (∀) vs There Exists (∃)",
            "content": (
                "• <b>Universal Quantifier (∀x):</b> Means 'For EVERY single item in the group'. Even if one item fails, the whole statement becomes False.<br/>"
                "• <b>Existential Quantifier (∃x):</b> Means 'There is AT LEAST ONE item'. As long as one item works, it is True.<br/>"
                "• <b>Negation Rule (De Morgan):</b><br/>"
                "&nbsp;&nbsp;~[ For all x, P(x) ] = There exists at least one x where NOT P(x).<br/>"
                "&nbsp;&nbsp;~[ There exists x, P(x) ] = For all x, NOT P(x)."
            ),
            "crucial_rule": "GOLDEN RULE: Negating 'All birds can fly' is NOT 'No birds can fly'. It is simply 'There exists at least one bird that cannot fly' (like a penguin)!"
        },
        {
            "number": "1.4",
            "title": "Counting Relations on a Set of Size n",
            "content": (
                "If a set A has n elements, total pairs in A × A is n².<br/>"
                "• <b>Total possible relations:</b> 2^(n²)<br/>"
                "• <b>Reflexive relations:</b> 2^(n² - n)<br/>"
                "• <b>Symmetric relations:</b> 2^(n(n+1)/2)<br/>"
                "• <b>Reflexive + Symmetric:</b> 2^(n(n-1)/2)<br/>"
                "• <b>Equivalence relations:</b> Counted by Bell Numbers: B(1)=1, B(2)=2, B(3)=5, B(4)=15."
            ),
            "crucial_rule": "GOLDEN RULE: Remember the Bell number for size 4: B(4) = 15. GATE asks this number directly!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Counting Symmetric Relations",
            "problem": "Set A has 4 elements: A = {1, 2, 3, 4}. How many symmetric relations can be formed on set A?",
            "steps": [
                "Step 1: Note the formula for symmetric relations: Total = 2^(n(n+1)/2).",
                "Step 2: Here n = 4.",
                "Step 3: Calculate the power: (4 × (4 + 1)) / 2 = (4 × 5) / 2 = 20 / 2 = 10.",
                "Step 4: Compute 2^10 = 1024."
            ],
            "answer": "Total Symmetric Relations = 1024."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: The Empty Set (Vacuous Truth)",
            "warning": "If a question says 'For all elements in set S, property P holds', and set S is completely EMPTY, the statement is ALWAYS TRUE! Don't mark it False."
        }
    ]
}

# EM Chapter 1: Graph Theory & Combinatorics
CHAPTERS_EM_DL[("EM", 1)] = {
    "sub_id": "EM",
    "chap_idx": 1,
    "title": "Discrete Mathematics - Graph Theory & Combinatorics",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Google Maps Road Network (Vertices and Edges)",
            "text": "Think of Google Maps: every city or junction is a dot (Vertex), and every road connecting two junctions is a line (Edge). The degree of a junction is simply the number of roads meeting at that point. If you add up the number of road-ends across all junctions, every road has 2 ends, so the sum of all degrees is always twice the number of roads. This simple fact is called the Handshaking Lemma."
        },
        {
            "title": "Real-Life Example 2: The Cheapest Metro Track (What is a Tree?)",
            "text": "Suppose you need to connect 6 metro stations so passengers can travel between any two stations without wasting money building redundant loops. The minimum number of track segments needed is always (Stations - 1) = 6 - 1 = 5 tracks. A connected network with no circular loops is called a Tree. If you add even 1 extra track, you create a loop; if you remove 1, someone gets disconnected."
        },
        {
            "title": "Real-Life Example 3: Printed Circuit Boards (Planar Graphs)",
            "text": "When engineers print electrical copper wires on a flat board, wires cannot cross each other or they will cause a short circuit. A graph that can be drawn on a flat sheet without any edges crossing is called a Planar Graph. Euler proved that for any such flat network: (Vertices - Edges + Enclosed Regions = 2)."
        }
    ],
    "foundations": [
        {
            "number": "2.1",
            "title": "Handshaking Lemma & Degree Sum Rule",
            "content": (
                "In any undirected graph:<br/>"
                "• <b>Sum of degrees of all vertices = 2 × (Number of Edges)</b>.<br/>"
                "• <b>Direct result:</b> The count of vertices having an ODD degree is ALWAYS EVEN (0, 2, 4, 6...)."
            ),
            "crucial_rule": "GOLDEN RULE: If an exam question gives vertex degrees like [3, 3, 3, 2], degree sum = 11 (odd number), which is IMPOSSIBLE! No such graph can ever exist."
        },
        {
            "number": "2.2",
            "title": "Trees & Spanning Trees",
            "content": (
                "A tree is a connected graph with no cycles.<br/>"
                "• A tree with n vertices always has exactly <b>n - 1 edges</b>.<br/>"
                "• There is exactly one simple path between any two vertices.<br/>"
                "• <b>Cayley's Formula:</b> Number of labeled spanning trees for complete graph Kn is <b>n^(n - 2)</b>."
            ),
            "crucial_rule": "GOLDEN RULE: For n = 4 vertices: Spanning trees = 4^(4-2) = 4^2 = 16. For n = 5: 5^(5-2) = 5^3 = 125."
        },
        {
            "number": "2.3",
            "title": "Bipartite Graphs & Graph Coloring",
            "content": (
                "• <b>Bipartite Graph:</b> You can divide vertices into two sets (Boys and Girls) such that edges only go between sets, never within the same set.<br/>"
                "• <b>Check rule:</b> A graph is Bipartite if and only if it has <b>NO ODD-LENGTH CYCLES</b> (no triangles, no 5-cycles).<br/>"
                "• <b>Chromatic Number χ(G):</b> Minimum colors needed so no two connected dots share the same color. Trees need 2 colors. Bipartite graphs need 2 colors."
            ),
            "crucial_rule": "GOLDEN RULE: If a graph has even one cycle of odd length (like 3 or 5), it CANNOT be bipartite!"
        },
        {
            "number": "2.4",
            "title": "Planar Graphs & Euler's Formula",
            "content": (
                "• For any connected flat (planar) graph: <b>V - E + R = 2</b> (where R includes the outer space).<br/>"
                "• <b>Edge limit:</b> For simple planar graphs with 3 or more vertices: <b>E ≤ 3V - 6</b>.<br/>"
                "• If graph has no triangles (like bipartite): <b>E ≤ 2V - 4</b>."
            ),
            "crucial_rule": "GOLDEN RULE: K5 (5 vertices, 10 edges) is NOT planar because 10 > 3(5) - 6 = 9. K3,3 is also NOT planar."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Finding Regions in a Planar Graph",
            "problem": "A connected planar graph has 10 vertices and 15 edges. How many regions does it divide the plane into?",
            "steps": [
                "Step 1: Write Euler's formula: V - E + R = 2.",
                "Step 2: Plug in V = 10 and E = 15: 10 - 15 + R = 2.",
                "Step 3: Simplify: -5 + R = 2.",
                "Step 4: Solve for R: R = 2 + 5 = 7 regions."
            ],
            "answer": "Total Regions R = 7 (6 inside faces + 1 outside face)."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Interior vs Total Regions",
            "warning": "Euler's R = 7 includes the 1 outer infinite region! If the question asks for 'enclosed' or 'bounded' regions, subtract 1: Bounded = 7 - 1 = 6."
        }
    ]
}

# EM Chapter 2: Linear Algebra
CHAPTERS_EM_DL[("EM", 2)] = {
    "sub_id": "EM",
    "chap_idx": 2,
    "title": "Linear Algebra - Systems, Eigenvalues & LU Decomposition",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Resizing a Photo on Your Phone (Determinant)",
            "text": "When you pinch and zoom a photo on your smartphone, the graphics chip multiplies coordinates by a 2x2 matrix. The Determinant tells you how much the picture's area changes. If det = 2, the image area doubles. If det = 1, it only rotates without stretching. If det = 0, the photo is completely squished flat into a single line (area becomes 0), meaning you can never restore the original picture (it has no inverse!)."
        },
        {
            "title": "Real-Life Example 2: The Google PageRank Magic (Eigenvalues & Eigenvectors)",
            "text": "When you search on Google, how does it know which page is most important? Google models billions of web pages as an enormous matrix of links. An Eigenvector is a special list of numbers that doesn't change direction when multiplied by the link matrix—it represents the steady popularity score of every website. The matching Eigenvalue is 1."
        },
        {
            "title": "Real-Life Example 3: Solving 10,000 Equations in Seconds (LU Decomposition)",
            "text": "If you have a set of equations Ax = b, solving them from scratch every time takes a lot of computing power (O(n³)). LU Decomposition splits matrix A once into a Lower triangle L and an Upper triangle U. After this one-time split, solving for any new target 'b' takes just a split second (O(n²))!"
        }
    ],
    "foundations": [
        {
            "number": "3.1",
            "title": "Rank of a Matrix & Solving AX = B",
            "content": (
                "Rank is simply the number of non-zero rows after converting the matrix to row echelon form.<br/>"
                "For system AX = B with n unknowns:<br/>"
                "• <b>Unique Solution:</b> Rank(A) = Rank([A|B]) = n.<br/>"
                "• <b>Infinitely Many Solutions:</b> Rank(A) = Rank([A|B]) < n.<br/>"
                "• <b>No Solution (Inconsistent):</b> Rank(A) < Rank([A|B])."
            ),
            "crucial_rule": "GOLDEN RULE: For homogeneous equations AX = 0, a non-zero solution exists IF AND ONLY IF det(A) = 0!"
        },
        {
            "number": "3.2",
            "title": "Eigenvalues & Their Super Useful Shortcuts",
            "content": (
                "Eigenvalues (λ) are found using det(A - λI) = 0.<br/>"
                "• <b>Trace Shortcut:</b> Sum of all eigenvalues = Sum of diagonal elements (Trace of A).<br/>"
                "• <b>Determinant Shortcut:</b> Product of all eigenvalues = det(A).<br/>"
                "• If A has eigenvalues λ1, λ2, then:<br/>"
                "&nbsp;&nbsp;• A² has eigenvalues λ1², λ2².<br/>"
                "&nbsp;&nbsp;• A⁻¹ has eigenvalues 1/λ1, 1/λ2 (if det ≠ 0).<br/>"
                "&nbsp;&nbsp;• A + 3I has eigenvalues λ1 + 3, λ2 + 3."
            ),
            "crucial_rule": "GOLDEN RULE: In GATE, use the Trace and Determinant shortcuts first! You can eliminate 3 out of 4 options in 15 seconds without solving the characteristic equation."
        },
        {
            "number": "3.3",
            "title": "LU Decomposition Basics",
            "content": (
                "Matrix A is factored into A = L × U (L = Lower triangular, U = Upper triangular).<br/>"
                "• In Doolittle's method, diagonal of L has all 1s.<br/>"
                "• Because det(L) = 1, <b>det(A) is simply the product of the diagonal elements of U</b>!"
            ),
            "crucial_rule": "GOLDEN RULE: det(A) = det(L) × det(U). In Doolittle, det(A) = u11 × u22 × ... × unn."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Finding Eigenvalues Quickly",
            "problem": "Matrix A = [[3, 2], [1, 4]]. Find its eigenvalues without writing full determinant expansion.",
            "steps": [
                "Step 1: Calculate Trace (sum of diagonal): 3 + 4 = 7.",
                "Step 2: Calculate Determinant: (3 × 4) - (2 × 1) = 12 - 2 = 10.",
                "Step 3: We need two numbers whose SUM = 7 and PRODUCT = 10.",
                "Step 4: The numbers are clearly 2 and 5 (since 2 + 5 = 7 and 2 × 5 = 10)."
            ],
            "answer": "Eigenvalues are λ = 2 and λ = 5."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Zero as an Eigenvalue",
            "warning": "If even one eigenvalue is 0, then the product of eigenvalues is 0, which means det(A) = 0! Such a matrix has NO inverse."
        }
    ]
}

# EM Chapter 3: Calculus & Probability
CHAPTERS_EM_DL[("EM", 3)] = {
    "sub_id": "EM",
    "chap_idx": 3,
    "title": "Calculus & Probability - Distributions and Bayes Theorem",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The False Alarm Medical Test (Bayes' Theorem)",
            "text": "Suppose a disease is very rare (only 1 in 1,000 people have it). A medical test is 99% accurate. If you test positive, are you 99% likely to be sick? NO! In a town of 1,000 people: 1 sick person tests positive, but 10 healthy people will also test positive by mistake (1% false alarm). So out of 11 positive results, only 1 is actually sick (about 9% chance)! Bayes' Theorem calculates your true probability by combining the test result with how common the disease actually is."
        },
        {
            "title": "Real-Life Example 2: Waiting for the Elevator (Poisson vs Exponential)",
            "text": "How many people enter an elevator per hour? That is a count of discrete events: Poisson Distribution. How many minutes do you wait between two elevator arrivals? That is continuous time: Exponential Distribution. The exponential distribution is 'memoryless'—even if you already waited 5 minutes, your chance of waiting 2 more minutes is the exact same as when you first arrived!"
        },
        {
            "title": "Real-Life Example 3: The Crest of a Rollercoaster (Maxima and Minima)",
            "text": "At the very top peak of a rollercoaster track, the car stops rising for a split second: vertical speed is zero (First derivative f'(x) = 0). As it tips downward, the curve bends down like an upside-down bowl (Second derivative f''(x) < 0). That is the mathematical test for a local maximum!"
        }
    ],
    "foundations": [
        {
            "number": "4.1",
            "title": "Limits, L'Hôpital's Rule & Maxima/Minima",
            "content": (
                "• <b>L'Hôpital's Rule:</b> When a limit gives 0/0 or ∞/∞, take derivative of top and derivative of bottom: lim f(x)/g(x) = lim f'(x)/g'(x).<br/>"
                "• <b>Finding Maxima/Minima:</b><br/>"
                "&nbsp;&nbsp;1. Set f'(x) = 0 to find critical points.<br/>"
                "&nbsp;&nbsp;2. Check f''(x): if negative (< 0) -> Maximum; if positive (> 0) -> Minimum."
            ),
            "crucial_rule": "GOLDEN RULE: Apply L'Hôpital ONLY when the fraction evaluates to 0/0 or ∞/∞. Don't apply it if the denominator is a normal non-zero number!"
        },
        {
            "number": "4.2",
            "title": "Conditional Probability & Bayes' Formula",
            "content": (
                "• <b>P(A|B):</b> Probability of A happening given that B already happened = P(A ∩ B) / P(B).<br/>"
                "• <b>Independent Events:</b> P(A ∩ B) = P(A) × P(B).<br/>"
                "• <b>Bayes' Theorem:</b> P(Cause A | Effect B) = [ P(B|A) × P(A) ] / P(B)."
            ),
            "crucial_rule": "GOLDEN RULE: Two events with positive probabilities CANNOT be both mutually exclusive (cannot happen together) and independent at the same time!"
        },
        {
            "number": "4.3",
            "title": "Standard Probability Distributions to Memorize",
            "content": (
                "• <b>Poisson Distribution:</b> Mean = λ, <b>Variance = λ</b> (Mean equals Variance!).<br/>"
                "• <b>Uniform Distribution U(a, b):</b> Mean = (a + b)/2, <b>Variance = (b - a)² / 12</b>.<br/>"
                "• <b>Exponential Distribution:</b> Mean = 1/λ, Variance = 1/λ²."
            ),
            "crucial_rule": "GOLDEN RULE: If an exam question mentions a distribution where Mean = 3 and Variance = 3, it is definitely a POISSON distribution with λ = 3."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Bayes' Theorem in Action",
            "problem": "Box 1 has 2 Gold coins. Box 2 has 1 Gold and 1 Silver coin. You pick a box at random and draw a Gold coin. What is the probability it came from Box 1?",
            "steps": [
                "Step 1: Probability of picking either box = 1/2.",
                "Step 2: P(Gold | Box 1) = 2/2 = 1. P(Gold | Box 2) = 1/2.",
                "Step 3: Total probability of Gold: (1/2 × 1) + (1/2 × 1/2) = 1/2 + 1/4 = 3/4.",
                "Step 4: By Bayes' Theorem: P(Box 1 | Gold) = (1/2 × 1) / (3/4) = (1/2) / (3/4) = 2/3."
            ],
            "answer": "Probability = 2/3 (or 66.7%)."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Uniform Distribution Variance Formula",
            "warning": "The denominator in Uniform variance is 12: Var = (b - a)² / 12. Many students wrongly write 4 or 6. Don't lose 1 mark here!"
        }
    ]
}

# =============================================================================
# DIGITAL LOGIC (DL)
# =============================================================================

# DL Chapter 0: Boolean Algebra & K-Maps
CHAPTERS_EM_DL[("DL", 0)] = {
    "sub_id": "DL",
    "chap_idx": 0,
    "title": "Boolean Algebra, K-Maps & Tabular Method (Quine-McCluskey)",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Smart Home Light Switch (Boolean Logic)",
            "text": "Imagine a hallway light with two switches (one downstairs, one upstairs). The light turns on when either switch is flipped, but turns off if both are in the same position. That is an XOR gate! Boolean algebra is the math of simple on/off switches that makes computers possible."
        },
        {
            "title": "Real-Life Example 2: Cleaning Up Redundant Wire Clutter (Karnaugh Maps)",
            "text": "Imagine you built a circuit with 15 logic gates that takes 5 seconds to respond. A Karnaugh Map (K-Map) is a visual puzzle grid that groups adjacent 1s into groups of 2, 4, or 8. By circling these blocks, you can reduce those 15 messy gates into just 2 simple gates, making the chip 10x faster and cheaper to manufacture."
        },
        {
            "title": "Real-Life Example 3: The Car Gear Shift (Don't Care Conditions)",
            "text": "In a car with 5 gears (1 to 5), an electronic 3-bit sensor represents gears: 001 is 1st gear, 010 is 2nd, etc. But binary codes 110 (6) and 111 (7) can never physically happen because the gearbox doesn't have 6th or 7th gears. We mark these unused codes as 'Don't Care' (X). On a K-Map, we can treat X as 1 if it helps make a bigger group, or treat it as 0 if it doesn't!"
        }
    ],
    "foundations": [
        {
            "number": "5.1",
            "title": "Boolean Laws & De Morgan's Rules",
            "content": (
                "• <b>De Morgan's Laws:</b> (A + B)' = A' · B' &nbsp;|&nbsp; (A · B)' = A' + B' (Break the line, change the sign!).<br/>"
                "• <b>Consensus Theorem:</b> AB + A'C + BC = AB + A'C (The term BC is redundant and can be dropped).<br/>"
                "• <b>Duality Principle:</b> Swap AND with OR, and swap 0 with 1. (Keep variables as they are)."
            ),
            "crucial_rule": "GOLDEN RULE: NAND and NOR are called UNIVERSAL GATES because you can build ANY digital circuit using only NAND or only NOR gates!"
        },
        {
            "number": "5.2",
            "title": "K-Map Rules & Essential Prime Implicants",
            "content": (
                "• K-Map cells are arranged in <b>Gray Code order</b> (00, 01, 11, 10) so only 1 bit changes between adjacent cells.<br/>"
                "• <b>Prime Implicant (PI):</b> The largest possible rectangle of 1s (size 1, 2, 4, 8, 16).<br/>"
                "• <b>Essential Prime Implicant (EPI):</b> A prime implicant that covers at least one '1' that NO OTHER group covers.<br/>"
                "• Minimal SOP = All EPIs + minimal other PIs to cover any remaining 1s."
            ),
            "crucial_rule": "GOLDEN RULE: Always group in powers of two (1, 2, 4, 8, 16). Larger groups mean fewer variables in the final answer!"
        },
        {
            "number": "5.3",
            "title": "Static-1 Hazards & How to Fix Them",
            "content": (
                "A Static-1 hazard happens when an output is supposed to stay 1, but momentarily glitches to 0 because an inverter gate takes a few nanoseconds of delay.<br/>"
                "• <b>Fix:</b> Look at the K-Map. If two adjacent 1s belong to two different groups, add a redundant overlapping circle (consensus term) to bridge them."
            ),
            "crucial_rule": "GOLDEN RULE: Two-level AND-OR (SOP) circuits can only have Static-1 hazards. They NEVER have Static-0 hazards!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Simplifying with Consensus Theorem",
            "problem": "Simplify the Boolean expression: F = A B + A' C + B C.",
            "steps": [
                "Step 1: Check the 3 terms: AB, A'C, BC.",
                "Step 2: Notice that variable A appears normal in first term (A) and complemented in second term (A').",
                "Step 3: The third term (BC) contains the remaining variables from the first two terms.",
                "Step 4: By Consensus Theorem, term BC is completely redundant and can be dropped!"
            ],
            "answer": "Simplified Expression = A B + A' C."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Gray Code Ordering in K-Maps",
            "warning": "Never write columns as 00, 01, 10, 11! The correct Gray code is 00, 01, 11, 10. Swapping 11 and 10 will ruin your entire K-Map grouping."
        }
    ]
}

# DL Chapter 1: Combinational Circuits
CHAPTERS_EM_DL[("DL", 1)] = {
    "sub_id": "DL",
    "chap_idx": 1,
    "title": "Combinational Circuits - MUX, Decoders & Arithmetic Circuits",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The TV Remote Input Selector (Multiplexer 2^n to 1)",
            "text": "Your TV has multiple inputs: Cable TV, PlayStation, Xbox, and Chromecast. But the TV screen can only show 1 video at a time. The remote control uses select buttons to choose which input feeds to the screen. A Multiplexer (MUX) does the exact same thing: it selects 1 of many data inputs and forwards it to a single output line based on select lines."
        },
        {
            "title": "Real-Life Example 2: The Memory Address Postal Worker (Decoder n to 2^n)",
            "text": "When the CPU wants to read from RAM memory slot #5, it sends binary 101 (3 bits). A 3-to-8 Decoder reads 101 and lights up exactly wire #5, leaving all other 7 memory wires off. A decoder turns a compressed binary code into a single active line."
        },
        {
            "title": "Real-Life Example 3: Fast Addition (Carry Lookahead Adder)",
            "text": "In regular addition, the 4th digit cannot be added until the carry bit ripples from digit 1 to 2 to 3 (Ripple Carry Adder: slow like dominoes). A Carry Lookahead Adder (CLA) uses clever logic to calculate all carry bits simultaneously in just 2 gate delays, making 64-bit addition blazing fast."
        }
    ],
    "foundations": [
        {
            "number": "6.1",
            "title": "Multiplexers (MUX) as Universal Function Generators",
            "content": (
                "A 2^n-to-1 MUX has 2^n input lines, n select lines, and 1 output.<br/>"
                "• <b>2-to-1 MUX equation:</b> Y = S' I0 + S I1.<br/>"
                "• <b>4-to-1 MUX equation:</b> Y = S1' S0' I0 + S1' S0 I1 + S1 S0' I2 + S1 S0 I3.<br/>"
                "• <b>Universal property:</b> ANY n-variable Boolean function can be implemented using a 2^(n-1)-to-1 MUX without needing extra gates!"
            ),
            "crucial_rule": "GOLDEN RULE: Total 2-to-1 MUXes needed to build an N-to-1 MUX is always exactly N - 1. Example: To build a 16-to-1 MUX requires 15 2-to-1 MUXes."
        },
        {
            "number": "6.2",
            "title": "Decoders & Priority Encoders",
            "content": (
                "• <b>Decoder (n to 2^n):</b> Generates all 2^n minterms. If active-high, output is AND; if active-low, output is NAND.<br/>"
                "• <b>Priority Encoder:</b> If multiple inputs are active at the same time, it outputs the code of only the highest priority input."
            ),
            "crucial_rule": "GOLDEN RULE: Always check if the Enable pin (E) is Active-Low (E'). If E' = 1, the decoder is OFF and all outputs remain 0!"
        },
        {
            "number": "6.3",
            "title": "Half Adder vs Full Adder",
            "content": (
                "• <b>Half Adder (adds 2 bits):</b> Sum = A ⊕ B, Carry = A · B. (Needs 1 XOR, 1 AND).<br/>"
                "• <b>Full Adder (adds 3 bits):</b> Sum = A ⊕ B ⊕ Cin, Carry = AB + Cin(A ⊕ B).<br/>"
                "• Can build 1 Full Adder using <b>2 Half Adders and 1 OR gate</b>."
            ),
            "crucial_rule": "GOLDEN RULE: Minimum NAND gates needed: 5 NAND gates for a Half Adder, and 9 NAND gates for a Full Adder."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Building 64-to-1 MUX Using 4-to-1 MUXes",
            "problem": "How many 4-to-1 MUXes are needed to build a single 64-to-1 MUX?",
            "steps": [
                "Step 1: First level: 64 inputs / 4 = 16 MUXes (produces 16 outputs).",
                "Step 2: Second level: 16 inputs / 4 = 4 MUXes (produces 4 outputs).",
                "Step 3: Third level: 4 inputs / 4 = 1 MUX (produces final 1 output).",
                "Step 4: Sum all levels: 16 + 4 + 1 = 21 MUXes."
            ],
            "answer": "Total 4-to-1 MUXes required = 21."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Missing Enable Lines",
            "warning": "When cascading decoders (e.g. building a 4-to-16 decoder using 2-to-4 decoders), use the highest address bit to drive the Enable pin of the decoders!"
        }
    ]
}

# DL Chapter 2: Sequential Circuits
CHAPTERS_EM_DL[("DL", 2)] = {
    "sub_id": "DL",
    "chap_idx": 2,
    "title": "Sequential Circuits - Flip-Flops, Counters & State Machines",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Push-Button Lamp (Toggle Flip-Flop)",
            "text": "A bedside lamp with a single push button: Press it once -> light turns ON. Press it again -> light turns OFF. The button remembers its previous state! This 1-bit memory is a Toggle (T) Flip-Flop. Unlike combinational circuits whose output depends only on current inputs, sequential circuits have MEMORY."
        },
        {
            "title": "Real-Life Example 2: The Car Odometer (Asynchronous vs Synchronous Counter)",
            "text": "In an old car odometer, when the 1s wheel rolls from 9 to 0, it pushes the 10s wheel. That is an Asynchronous (Ripple) counter: each digit waits for the previous one to finish moving. In modern digital cars, all digits update at the exact same clock pulse: a Synchronous Counter."
        },
        {
            "title": "Real-Life Example 3: The Subway Turnstile (Finite State Machine)",
            "text": "A subway turnstile has two states: Locked and Unlocked. Tapping your metro card moves it to Unlocked. Pushing through the turnstile moves it back to Locked. This is a Finite State Machine: it remembers which state it is in and changes state only when valid triggers happen."
        }
    ],
    "foundations": [
        {
            "number": "7.1",
            "title": "The 4 Basic Flip-Flops & Their Equations",
            "content": (
                "• <b>SR Flip-Flop:</b> Q(next) = S + R' Q (Condition: S·R = 0, S=1 and R=1 is invalid).<br/>"
                "• <b>JK Flip-Flop:</b> Q(next) = J Q' + K' Q (Toggles when J=1, K=1; fixes the SR bug!).<br/>"
                "• <b>D Flip-Flop:</b> Q(next) = D (Delays/Stores whatever data is at input D).<br/>"
                "• <b>T Flip-Flop:</b> Q(next) = T ⊕ Q (Inverts state when T=1; keeps state when T=0)."
            ),
            "crucial_rule": "GOLDEN RULE: Quick Characteristic Equations to memorize:<br/>• JK: Q+ = JQ' + K'Q<br/>• D: Q+ = D<br/>• T: Q+ = T ⊕ Q."
        },
        {
            "number": "7.2",
            "title": "Setup Time, Hold Time & Maximum Clock Frequency",
            "content": (
                "• <b>Setup Time (t_setup):</b> Data must be stable BEFORE the clock tick.<br/>"
                "• <b>Hold Time (t_hold):</b> Data must remain stable AFTER the clock tick.<br/>"
                "• <b>Max Clock Frequency:</b> Clock Period T ≥ t_clk_to_q + t_combinational + t_setup. Frequency f_max = 1 / T."
            ),
            "crucial_rule": "GOLDEN RULE: Hold time violations CANNOT be fixed by slowing down the clock! They depend only on internal gate delays."
        },
        {
            "number": "7.3",
            "title": "Counters: Mod-N, Ring & Johnson Counters",
            "content": (
                "• <b>Mod-N Counter:</b> Counts N states (needs ⌈log2(N)⌉ flip-flops).<br/>"
                "• <b>Ring Counter:</b> N flip-flops give exactly <b>N states</b> (1 hot bit circulating).<br/>"
                "• <b>Johnson (Twisted Ring) Counter:</b> N flip-flops give <b>2N states</b> (Inverted output fed back)."
            ),
            "crucial_rule": "GOLDEN RULE: With 4 flip-flops: Standard counter gives 2^4 = 16 states, Johnson counter gives 2(4) = 8 states, Ring counter gives 4 states."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Maximum Clock Frequency",
            "problem": "A circuit has flip-flop delay t_cq = 2 ns, combinational logic delay = 5 ns, and setup time = 3 ns. What is the maximum operating clock frequency?",
            "steps": [
                "Step 1: Compute minimum clock period: T_min = t_cq + t_comb + t_setup.",
                "Step 2: Add values: T_min = 2 ns + 5 ns + 3 ns = 10 ns = 10 × 10^-9 s.",
                "Step 3: Frequency f_max = 1 / T_min = 1 / (10 × 10^-9) = 10^8 Hz = 100 MHz."
            ],
            "answer": "Maximum Clock Frequency = 100 MHz."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Race-Around Condition",
            "warning": "Race-around happens in level-triggered JK flip-flops when J=1, K=1 and clock pulse width is longer than flip-flop delay. Solution: Use Edge-Triggered or Master-Slave flip-flops."
        }
    ]
}

# DL Chapter 3: Number Representation & Floating Point
CHAPTERS_EM_DL[("DL", 3)] = {
    "sub_id": "DL",
    "chap_idx": 3,
    "title": "Number Representation & Floating Point (IEEE 754)",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Car Odometer Rolling from 99999 to 00000 (Two's Complement)",
            "text": "When an odometer hits 99,999 and you drive 1 more km, it rolls over to 00,000. In computer math, if an 8-bit signed integer is at +127 (01111111) and you add 1, it wraps around to -128 (10000000)! This is Two's Complement arithmetic. Computers love it because subtraction is done by simply adding the negative number."
        },
        {
            "title": "Real-Life Example 2: The Rocket Disaster (Floating Point Overflow)",
            "text": "In 1996, the Ariane 5 space rocket exploded 37 seconds after launch because the software converted a 64-bit floating point number into a 16-bit integer. The number was too big to fit into 16 bits, causing an overflow error that crashed the navigation engines. Understanding number limits is critical!"
        },
        {
            "title": "Real-Life Example 3: Scientific Notation on a Calculator (IEEE 754)",
            "text": "On a pocket calculator, very big numbers are shown as 6.02 × 10^23. In computers, IEEE 754 does the exact same thing in binary: 1 Sign bit (+ or -), 8 Exponent bits (power of 2), and 23 Mantissa bits (the actual precision digits). This lets 32 bits represent both the width of an atom and the distance to Mars."
        }
    ],
    "foundations": [
        {
            "number": "8.1",
            "title": "Signed Number Ranges (n bits)",
            "content": (
                "• <b>Unsigned:</b> 0 to 2^n - 1.<br/>"
                "• <b>Sign-Magnitude:</b> -(2^(n-1) - 1) to +(2^(n-1) - 1). (Has two zeros: +0 and -0).<br/>"
                "• <b>1's Complement:</b> -(2^(n-1) - 1) to +(2^(n-1) - 1). (Also has two zeros).<br/>"
                "• <b>2's Complement:</b> <b>-2^(n-1) to +(2^(n-1) - 1)</b>. (Has only ONE unique zero! Has one extra negative number)."
            ),
            "crucial_rule": "GOLDEN RULE: For 8 bits in 2's complement: Range is -128 to +127. The binary code 10000000 represents -128."
        },
        {
            "number": "8.2",
            "title": "IEEE 754 Single Precision (32-bit)",
            "content": (
                "• <b>Bit Split:</b> 1 Sign bit (s) | 8 Exponent bits (e, Bias = 127) | 23 Mantissa bits (f).<br/>"
                "• <b>Formula:</b> Value = (-1)^s × (1.f) × 2^(e - 127).<br/>"
                "• Note: The leading '1.' is hidden (not stored in the 23 bits)."
            ),
            "crucial_rule": "GOLDEN RULE: If e = 0 and f = 0, it represents ±0. If e = 255 and f = 0, it represents ±Infinity. If e = 255 and f ≠ 0, it is NaN (Not a Number)."
        },
        {
            "number": "8.3",
            "title": "Overflow Detection Rule",
            "content": (
                "In 2's complement addition:<br/>"
                "• Overflow happens when two positive numbers add to give a negative result, OR two negative numbers add to give a positive result.<br/>"
                "• <b>Hardware test:</b> Overflow = <b>Carry_in ⊕ Carry_out</b> of the sign bit (MSB)."
            ),
            "crucial_rule": "GOLDEN RULE: Adding a positive and a negative number can NEVER produce an overflow!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Converting -9.75 to IEEE 754 Hex",
            "problem": "Represent decimal number -9.75 in 32-bit IEEE 754 format.",
            "steps": [
                "Step 1: Sign is negative ⇒ Sign bit s = 1.",
                "Step 2: Convert 9.75 to binary: 9 = 1001, 0.75 = 0.5 + 0.25 = 0.11 ⇒ 1001.11.",
                "Step 3: Normalize: 1001.11 = 1.00111 × 2^3.",
                "Step 4: Biased exponent: E = 3 + 127 = 130 ⇒ in binary 10000010.",
                "Step 5: Mantissa (drop leading 1): 00111000... (23 bits).",
                "Step 6: Combine: [1] [10000010] [00111000000000000000000] = 0xC11C0000."
            ],
            "answer": "Hex representation = 0xC11C0000."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Single vs Double Precision Bias",
            "warning": "For Single Precision (32-bit), Bias = 127. For Double Precision (64-bit with 11 exponent bits), Bias = 1023 (NOT 1024!)."
        }
    ]
}
