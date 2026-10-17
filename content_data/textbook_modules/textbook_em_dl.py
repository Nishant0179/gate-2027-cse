# textbook_em_dl.py
# In-depth Master Textbook Modules for Engineering Mathematics (EM) and Digital Logic (DL)
# Follows the exact pedagogical and visual architecture of User Images 2 & 3.

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
            "title": "Real-Life Example 1: The Strict Courtroom Contract Clause (Propositional Logic & Implication)",
            "text": "Imagine an employment contract stating: 'If you complete the software milestone by Friday (P), then the company will pay you a ₹50,000 bonus (Q)'. If you finish the code and get the bonus, the contract is honored (T → T = T). If you finish the code and the company refuses to pay, the contract is breached (T → F = F). But what if you DID NOT finish the milestone? The company can either give you a bonus anyway or withhold it; neither violates the original promise! This is why (F → T) and (F → F) are mathematically TRUE (Vacuous Truth)."
        },
        {
            "title": "Real-Life Example 2: The VIP Club Guestlist & Security Check (Set Membership & Relations)",
            "text": "Think of a nightclub with an exclusive guest list A. A relation R on A is a set of approved interactions. If every single guest is allowed to chat with themselves in a mirror, the relation is Reflexive ((x, x) ∈ R). If whenever Alice can high-five Bob, Bob is equally allowed to high-five Alice, the relationship is Symmetric. If Alice trusts Bob, and Bob trusts Charlie, and this guarantees Alice trusts Charlie, it is Transitive. When all three hold, the club naturally fractures into disjoint VIP circles (Equivalence Classes)."
        },
        {
            "title": "Real-Life Example 3: The Airport Baggage Security Scanner (Quantifiers: ∀ vs ∃)",
            "text": "At an international airport, two rules are enforced. Rule 1: 'Every passenger must have a valid boarding pass' (∀x Pass(x)). If even a single passenger lacks one, the system fails. Rule 2: 'At least one customs officer must be stationed at exit gate 4' (∃x Officer(x)). The negation of Rule 1 is NOT 'No passenger has a boarding pass'—it is simply 'There exists at least one passenger without a boarding pass' (∃x ~Pass(x)). This De Morgan's duality governs predicate logic."
        }
    ],
    "foundations": [
        {
            "number": "1.1",
            "title": "Propositional Logic: Truth Values, Logical Connectives & Implication Mechanics",
            "content": (
                "A proposition is a declarative statement that is strictly True (T) or False (F), never both or ambiguous.<br/>"
                "• <b>Conjunction (P ∧ Q):</b> True strictly when both P and Q are True.<br/>"
                "• <b>Disjunction (P ∨ Q):</b> False strictly when both P and Q are False.<br/>"
                "• <b>Conditional Implication (P → Q):</b> Equivalent to (~P ∨ Q). It formalizes 'sufficient condition' (P is sufficient for Q) and 'necessary condition' (Q is necessary for P).<br/>"
                "• <b>Biconditional (P ↔ Q):</b> Equivalent to (P → Q) ∧ (Q → P). True when P and Q share identical truth values."
            ),
            "crucial_rule": "CRUCIAL RULE: The conditional statement P → Q is False ONLY when premise P is True and conclusion Q is False. If premise P is False, the implication P → Q is ALWAYS TRUE regardless of the truth value of Q (Vacuous Truth)."
        },
        {
            "number": "1.2",
            "title": "Contrapositive, Converse, Inverse & Logical Equivalences",
            "content": (
                "Given the conditional proposition P → Q:<br/>"
                "• <b>Contrapositive:</b> ~Q → ~P (100% logically equivalent to original P → Q).<br/>"
                "• <b>Converse:</b> Q → P (NOT logically equivalent to P → Q).<br/>"
                "• <b>Inverse:</b> ~P → ~Q (Logically equivalent to the converse, NOT to the original).<br/>"
                "• <b>Exportation Law:</b> (P ∧ Q) → R ≡ P → (Q → R).<br/>"
                "• <b>Absorption Laws:</b> P ∨ (P ∧ Q) ≡ P and P ∧ (P ∨ Q) ≡ P."
            ),
            "crucial_rule": "CRUCIAL RULE: To prove a theorem of the form P → Q in GATE, proving the contrapositive ~Q → ~P is often 10x simpler when ~Q gives direct structural algebraic constraints."
        },
        {
            "number": "1.3",
            "title": "First-Order Predicate Logic, Scoping & Quantifier Dualities",
            "content": (
                "Predicates add variables and domain assertions. Quantifiers specify scope:<br/>"
                "• <b>Universal Quantifier (∀x):</b> Asserts P(x) holds for every element in the domain.<br/>"
                "• <b>Existential Quantifier (∃x):</b> Asserts P(x) holds for at least one element in domain.<br/>"
                "• <b>De Morgan's Laws for Quantifiers:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;~[∀x P(x)] ≡ ∃x ~P(x)<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;~[∃x P(x)] ≡ ∀x ~P(x)<br/>"
                "• <b>Quantifier Distribution:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;∀x [P(x) ∧ Q(x)] ≡ [∀x P(x)] ∧ [∀x Q(x)] (Universal distributes over AND).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;∃x [P(x) ∨ Q(x)] ≡ [∃x P(x)] ∨ [∃x Q(x)] (Existential distributes over OR)."
            ),
            "crucial_rule": "CRUCIAL RULE: Universal quantifier DOES NOT distribute over OR: ∀x [P(x) ∨ Q(x)] DOES NOT imply [∀x P(x)] ∨ [∀x Q(x)]. Example: Every human is either male or female, but NOT all humans are male, nor all humans are female!"
        },
        {
            "number": "1.4",
            "title": "Set Theory, Counting Relations & Equivalence Classes",
            "content": (
                "For a set A with |A| = n elements, the Cartesian product A × A contains n² ordered pairs.<br/>"
                "• <b>Total possible relations:</b> 2^(n²).<br/>"
                "• <b>Reflexive Relations:</b> Must include all n pairs (a, a). Remaining n² - n pairs can be chosen freely: <b>Total = 2^(n² - n)</b>.<br/>"
                "• <b>Symmetric Relations:</b> Pair (a, b) implies (b, a). There are n diagonal elements and (n² - n)/2 off-diagonal pairs: <b>Total = 2^(n(n+1)/2)</b>.<br/>"
                "• <b>Reflexive and Symmetric Relations:</b> <b>Total = 2^(n(n-1)/2)</b>.<br/>"
                "• <b>Anti-Symmetric Relations:</b> If (a, b) ∈ R and (b, a) ∈ R then a = b: <b>Total = 2^n × 3^(n(n-1)/2)</b>.<br/>"
                "• <b>Equivalence Relations:</b> Partitions the set into disjoint equivalence classes. Number of equivalence relations equals the Bell Number B(n)."
            ),
            "crucial_rule": "CRUCIAL RULE: Bell numbers for small sets: B(1)=1, B(2)=2, B(3)=5, B(4)=15, B(5)=52. In GATE, the number of equivalence relations on a set of size 4 is ALWAYS 15!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Relation Counting & Equivalence Verification",
            "problem": "Let A = {1, 2, 3, 4}. Find: (a) The number of symmetric relations on A, (b) The number of reflexive and symmetric relations, and (c) The number of equivalence relations on A.",
            "steps": [
                "Step 1: Identify n = |A| = 4.",
                "Step 2: Total symmetric relations formula = 2^(n(n+1)/2). Exponent = 4 × 5 / 2 = 10. Value = 2^10 = 1024.",
                "Step 3: Reflexive and symmetric relations formula = 2^(n(n-1)/2). Exponent = 4 × 3 / 2 = 6. Value = 2^6 = 64.",
                "Step 4: Equivalence relations count = Bell Number B(4). Using Bell triangle: Row 1 = [1]; Row 2 = [1, 2]; Row 3 = [2, 3, 5]; Row 4 = [5, 7, 10, 15]. Thus B(4) = 15."
            ],
            "answer": "Outputs: (a) 1024 symmetric relations, (b) 64 reflexive & symmetric relations, (c) 15 equivalence relations."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: The Vacuous Truth Fallacy",
            "warning": "When evaluating propositions like '∀x ∈ S (P(x) → Q(x))', if the set S is empty (∅), the statement is VACUOUSLY TRUE! In GATE 2021, over 40% of aspirants marked this false."
        },
        {
            "title": "Exam Trap 2: Negating Implications Inside Quantifiers",
            "warning": "The negation of 'All students are smart' (∀x (S(x) → Smart(x))) is NOT 'All students are not smart'. Since ~(P → Q) ≡ P ∧ ~Q, the negation is ∃x (S(x) ∧ ~Smart(x)): 'There exists at least one student who is not smart'."
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
            "title": "Real-Life Example 1: The High-Speed Metro Rail Network (Graph Connectivity & Trees)",
            "text": "Imagine designing a metro network connecting 10 major suburbs. If you lay down too few tracks, passengers get stranded (disconnected graph). If you lay down circular tracks everywhere, you waste billions on redundant loops (cycles). The absolute cheapest, zero-redundancy network that connects all 10 stations without any circular deadlocks is a Tree: it uses exactly 9 rail segments (n - 1 edges). Add just one more rail, and you create a cycle; remove one, and the city disconnects."
        },
        {
            "title": "Real-Life Example 2: The Wedding Table Seating Dilemma (Bipartite Graphs & Matching)",
            "text": "At a wedding banquet, you have 50 male guests on the left and 50 female guests on the right. An edge connects a man and a woman if they are mutual friends. Can we seat each man with a compatible woman with no conflicts? This is the Classic Bipartite Matching Problem. If you find any odd-length conflict loop (e.g. A likes B, B likes C, C likes A), a clean two-group separation is mathematically impossible."
        },
        {
            "title": "Real-Life Example 3: The Highway Overpass vs Level Crossing (Planar Graphs & Euler's Formula)",
            "text": "When civil engineers build roads in a single flat plane, intersections require expensive traffic signals. If roads can cross without tunnels or bridges, the map is a Planar Graph. Euler discovered that no matter how squiggly or distorted the roads are, (Vertices - Edges + Enclosed Zones = 2). If you try to connect 5 cities directly to each other without overpasses (Complete Graph K5), geometry breaks down—it is physically impossible to draw without collisions."
        }
    ],
    "foundations": [
        {
            "number": "2.1",
            "title": "Foundational Graph Theorems & Handshaking Lemma",
            "content": (
                "An undirected graph G = (V, E) consists of a non-empty set of vertices V and a set of edges E.<br/>"
                "• <b>Handshaking Lemma:</b> ∑_{v ∈ V} deg(v) = 2|E|.<br/>"
                "• <b>Direct Consequence:</b> The number of vertices having odd degree is ALWAYS EVEN. A graph can never have an odd number of odd-degree vertices.<br/>"
                "• <b>Regular Graph:</b> A graph where every vertex has identical degree k (k-regular). Total edges |E| = n × k / 2."
            ),
            "crucial_rule": "CRUCIAL RULE: In any valid graph, the sum of all vertex degrees MUST BE EVEN. If a question proposes degrees [3, 3, 3, 2], degree sum = 11 (odd), which is topologically IMPOSSIBLE."
        },
        {
            "number": "2.2",
            "title": "Trees, Spanning Trees & Cayley's Formula",
            "content": (
                "A tree is a connected acyclic undirected graph.<br/>"
                "• A tree with n vertices has exactly <b>n - 1 edges</b>.<br/>"
                "• Any two vertices in a tree are connected by a <b>unique simple path</b>.<br/>"
                "• Adding any edge to a tree creates exactly one unique cycle.<br/>"
                "• <b>Cayley's Formula:</b> The number of labeled spanning trees on a complete graph Kn with n vertices is <b>n^(n - 2)</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: For n = 4, labeled spanning trees = 4^(4-2) = 16. For n = 5, labeled spanning trees = 5^(5-2) = 125."
        },
        {
            "number": "2.3",
            "title": "Bipartite Graphs, Coloring & Characterizations",
            "content": (
                "A graph G is Bipartite if its vertex set V can be partitioned into two disjoint subsets V1 and V2 such that every edge connects a vertex in V1 to a vertex in V2.<br/>"
                "• <b>Fundamental Criterion:</b> A graph is bipartite if and only if it contains <b>NO ODD CYCLES</b>.<br/>"
                "• <b>Chromatic Number χ(G):</b> The minimum number of colors needed to color vertices such that no two adjacent vertices share the same color.<br/>"
                "• Trees have χ(T) = 2. Bipartite graphs have χ(G) = 2 (if |E| ≥ 1). Cycles Cn have χ = 2 (if n is even) and χ = 3 (if n is odd)."
            ),
            "crucial_rule": "CRUCIAL RULE: Complete Bipartite Graph Km,n has |V| = m + n, |E| = m × n. Maximum edges in a bipartite graph with n vertices is ⌊n²/4⌋."
        },
        {
            "number": "2.4",
            "title": "Planar Graphs & Euler's Formula",
            "content": (
                "A graph is planar if it can be embedded in the plane with no edges crossing.<br/>"
                "• <b>Euler's Formula:</b> For any connected planar graph with V vertices, E edges, and R regions (including the outer unbounded face): <b>V - E + R = 2</b>.<br/>"
                "• <b>Planarity Edge Bounds:</b> For any simple connected planar graph with V ≥ 3:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;<b>E ≤ 3V - 6</b> (general case)<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;<b>E ≤ 2V - 4</b> (if graph is triangle-free / bipartite / girth ≥ 4).<br/>"
                "• <b>Kuratowski's Theorem:</b> A graph is planar iff it contains no subgraph homeomorphic to K5 or K3,3."
            ),
            "crucial_rule": "CRUCIAL RULE: Complete graph K5 has V=5, E=10. By 3V-6 = 3(5)-6 = 9. Since 10 > 9, K5 is strictly NON-PLANAR!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Planar Regions Calculation",
            "problem": "A connected planar graph has 12 vertices, each of degree 3. How many bounded and unbounded regions does this graph divide the plane into?",
            "steps": [
                "Step 1: Calculate total edges using Handshaking Lemma: 2|E| = ∑ deg(v).",
                "Step 2: Here, 12 vertices each have degree 3, so ∑ deg(v) = 12 × 3 = 36. Therefore, |E| = 36 / 2 = 18 edges.",
                "Step 3: Apply Euler's Planar Formula: V - E + R = 2.",
                "Step 4: Substitute known values: 12 - 18 + R = 2 ⇒ -6 + R = 2 ⇒ R = 8 regions.",
                "Step 5: The total regions = 8 (which includes 7 bounded interior faces and 1 unbounded exterior face)."
            ],
            "answer": "Total regions R = 8 (7 bounded faces + 1 unbounded face)."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Euler's Formula on Disconnected Graphs",
            "warning": "V - E + R = 2 applies ONLY to connected planar graphs! For a disconnected planar graph with k connected components, the formula becomes: V - E + R = 1 + k."
        },
        {
            "title": "Exam Trap 2: Forgetting the Exterior Unbounded Face",
            "warning": "When GATE asks for 'the number of interior/bounded faces', subtract 1 from Euler's total R: Interior Faces = R - 1."
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
            "title": "Real-Life Example 1: The 3D Video Game Graphics Camera (Matrix Transformations & Determinants)",
            "text": "In a 3D video game like GTA or Fortnite, your character's view moves continuously. The game engine multiplies millions of coordinate vectors by a 3×3 transformation matrix to rotate, zoom, and tilt the scene. The Determinant of that matrix tells the GPU how much the world is being stretched: if det(A) = 2, every object doubles in volume; if det(A) = 1, volume is preserved (pure rotation); if det(A) = 0, the 3D world is squashed flat into a pancake (dimension loss), meaning the view is permanently corrupted and non-invertible."
        },
        {
            "title": "Real-Life Example 2: The Google PageRank Search Engine (Eigenvalues & Eigenvectors)",
            "text": "How does Google rank billions of websites? Google models the web as an enormous transition probability matrix where web surfers click random links. An Eigenvector of this matrix represents the stationary distribution: a magical direction where surfers circulate endlessly without changing the proportion of visitors on any page. The corresponding dominant Eigenvalue λ = 1 locks in the definitive PageRank score for every URL."
        },
        {
            "title": "Real-Life Example 3: The Assembly Line Factory Breakdown (LU Decomposition)",
            "text": "When solving 10,000 structural equations for bridge stability with varying wind loads (Ax = b1, Ax = b2, ...), solving Gaussian elimination from scratch every time takes O(n³) operations. LU Decomposition factors matrix A once into a Lower triangular matrix L (materials checklist) and Upper triangular matrix U (assembly steps) in O(n³). Afterwards, solving for any new wind load vector b takes lightning-fast forward and backward substitutions in just O(n²) time!"
        }
    ],
    "foundations": [
        {
            "number": "3.1",
            "title": "Matrix Rank, Systems of Linear Equations (AX = B) & Consistency",
            "content": (
                "For an m × n matrix A and augmented matrix [A|B]:<br/>"
                "• <b>Consistent System:</b> Solution exists iff Rank(A) = Rank([A|B]).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;1. <b>Unique Solution:</b> Rank(A) = Rank([A|B]) = n (number of variables).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;2. <b>Infinitely Many Solutions:</b> Rank(A) = Rank([A|B]) = r < n. Free variables = n - r.<br/>"
                "• <b>Inconsistent System (No Solution):</b> Rank(A) < Rank([A|B]).<br/>"
                "• <b>Homogeneous System (AX = 0):</b> Always consistent (zero trivial solution). Non-trivial (non-zero) solutions exist iff Rank(A) < n (or det(A) = 0 for square matrices)."
            ),
            "crucial_rule": "CRUCIAL RULE: For a square system AX = 0, non-trivial solutions exist IF AND ONLY IF det(A) = 0. If det(A) ≠ 0, ONLY the zero vector (trivial solution) exists."
        },
        {
            "number": "3.2",
            "title": "Eigenvalues, Eigenvectors & Canonical Properties",
            "content": (
                "For square matrix A, non-zero vector X is an eigenvector with eigenvalue λ if <b>AX = λX</b>, or <b>det(A - λI) = 0</b>.<br/>"
                "• <b>Trace Property:</b> Sum of all eigenvalues = Trace(A) = Sum of principal diagonal elements.<br/>"
                "• <b>Determinant Property:</b> Product of all eigenvalues = det(A).<br/>"
                "• If A has eigenvalues λ1, λ2, ..., λn, then:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• A^k has eigenvalues λ1^k, λ2^k, ..., λn^k.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• A^(-1) has eigenvalues 1/λ1, 1/λ2, ..., 1/λn (if det(A) ≠ 0).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• A + cI has eigenvalues λ1 + c, λ2 + c, ..., λn + c.<br/>"
                "• Real Symmetric Matrix: All eigenvalues are strictly <b>REAL</b>, and eigenvectors corresponding to distinct eigenvalues are mutually <b>ORTHOGONAL</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: If any eigenvalue λ = 0, then det(A) = 0, which proves matrix A is SINGULAR and has NO inverse!"
        },
        {
            "number": "3.3",
            "title": "LU Decomposition (Doolittle vs Crout)",
            "content": (
                "A square matrix A can be factored as A = L · U, where L is a lower triangular matrix and U is an upper triangular matrix.<br/>"
                "• <b>Doolittle Algorithm:</b> Diagonal of L has all 1s (unit lower triangular): l_ii = 1.<br/>"
                "• <b>Crout Algorithm:</b> Diagonal of U has all 1s (unit upper triangular): u_ii = 1.<br/>"
                "• LU Decomposition exists without row exchanges iff all leading principal minors of A are non-zero: det(Ak) ≠ 0 for all k = 1, ..., n."
            ),
            "crucial_rule": "CRUCIAL RULE: det(A) = det(L) × det(U). In Doolittle's method, det(L) = 1, so det(A) is simply the product of diagonal elements of U: det(A) = u11 × u22 × ... × unn."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Eigenvalues & Matrix Powers",
            "problem": "Matrix A = [[2, 1], [1, 2]]. Find the eigenvalues of matrix M = A^3 - 3A^2 + 2I.",
            "steps": [
                "Step 1: Find eigenvalues of A using characteristic equation det(A - λI) = 0: (2 - λ)^2 - 1 = 0 ⇒ λ^2 - 4λ + 3 = 0.",
                "Step 2: Factorizing yields (λ - 1)(λ - 3) = 0. So eigenvalues of A are λ1 = 1, λ2 = 3.",
                "Step 3: Check trace and det: Trace = 2 + 2 = 4 (1 + 3 = 4 ✔). Det = 4 - 1 = 3 (1 × 3 = 3 ✔).",
                "Step 4: For polynomial M = f(A) = A^3 - 3A^2 + 2I, eigenvalues are f(λ):",
                "&nbsp;&nbsp;&nbsp;&nbsp;For λ1 = 1: f(1) = 1^3 - 3(1^2) + 2 = 1 - 3 + 2 = 0.",
                "&nbsp;&nbsp;&nbsp;&nbsp;For λ2 = 3: f(3) = 3^3 - 3(3^2) + 2 = 27 - 27 + 2 = 2."
            ],
            "answer": "Eigenvalues of M are 0 and 2."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Assuming Eigenvectors are Unique",
            "warning": "Eigenvectors are NEVER unique! Any scalar non-zero multiple cX (where c ≠ 0) is also an eigenvector for the same eigenvalue λ. GATE options often scale by a constant factor like -1/2 or √2."
        },
        {
            "title": "Exam Trap 2: Linearly Independent vs Orthogonal",
            "warning": "Distinct eigenvalues guarantee linearly independent eigenvectors for ANY matrix. But they guarantee ORTHOGONAL eigenvectors ONLY when the matrix is REAL SYMMETRIC (A = A^T)!"
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
            "title": "Real-Life Example 1: The False Alarm Medical Test Paradox (Bayes' Theorem)",
            "text": "Suppose a rare disease affects 1 in 10,000 people (0.01%). A clinical lab test is 99% accurate (1% false positive rate). You take the test and test positive. Are you 99% doomed? NO! In a population of 10,000, 1 person has the disease and tests positive, but out of 9,999 healthy people, 1% (~100 people) also test positive! Thus, your actual chance of being sick given a positive test is only 1 / (1 + 100) ≈ 1%. Bayes' Theorem balances prior base-rates with observed evidence."
        },
        {
            "title": "Real-Life Example 2: The Call Center Queue Time (Poisson vs Exponential Distribution)",
            "text": "When you call customer support, customer arrivals follow a Poisson Distribution (discrete count of callers arriving per hour, e.g., λ = 30 calls/hr). The time you wait on hold between calls follows a continuous Exponential Distribution with mean 1/λ = 2 minutes. The exponential distribution is 'memoryless': whether you have waited 30 seconds or 10 minutes, your remaining wait time has the exact same distribution!"
        },
        {
            "title": "Real-Life Example 3: The Rollercoaster Crest & Velocity (Maxima, Minima & Derivatives)",
            "text": "As a rollercoaster climbs to its highest peak, its vertical speed slows down until, for one fleeting instant at the very summit, vertical velocity is exactly zero (f'(x) = 0). As it tips over into a stomach-churning dive, the track curves downwards, meaning the rate of change is accelerating downwards (f''(x) < 0). This second-derivative concavity test is how engineers calculate peak safety limits."
        }
    ],
    "foundations": [
        {
            "number": "4.1",
            "title": "Calculus: Limits, L'Hôpital's Rule & Mean Value Theorems",
            "content": (
                "• <b>L'Hôpital's Rule:</b> For indeterminate forms 0/0 or ∞/∞, lim_{x→a} f(x)/g(x) = lim_{x→a} f'(x)/g'(x).<br/>"
                "• <b>Rolle's Theorem:</b> If f(x) is continuous on [a, b], differentiable on (a, b), and f(a) = f(b), then there exists at least one c ∈ (a, b) such that f'(c) = 0.<br/>"
                "• <b>Lagrange Mean Value Theorem (LMVT):</b> If f(x) is continuous on [a, b] and differentiable on (a, b), there exists c ∈ (a, b) such that: <b>f'(c) = [f(b) - f(a)] / (b - a)</b>.<br/>"
                "• <b>Maxima/Minima:</b> Critical points where f'(x) = 0. If f''(x) < 0 ⇒ Local Maximum; if f''(x) > 0 ⇒ Local Minimum; if f''(x) = 0, higher derivatives must be tested."
            ),
            "crucial_rule": "CRUCIAL RULE: L'Hôpital's rule can ONLY be applied when the limit strictly evaluates to 0/0 or ±∞/±∞. Differentiating when the denominator is finite gives a completely wrong answer!"
        },
        {
            "number": "4.2",
            "title": "Axioms of Probability, Conditional Probability & Bayes' Rule",
            "content": (
                "• <b>Conditional Probability:</b> P(A|B) = P(A ∩ B) / P(B), provided P(B) > 0.<br/>"
                "• <b>Independent Events:</b> P(A ∩ B) = P(A) × P(B). Independence implies P(A|B) = P(A).<br/>"
                "• <b>Law of Total Probability:</b> If B1, B2, ..., Bn partition the sample space: P(A) = ∑ P(A|Bi) P(Bi).<br/>"
                "• <b>Bayes' Theorem:</b> <b>P(Bk|A) = [P(A|Bk) P(Bk)] / [∑_{i} P(A|Bi) P(Bi)]</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: Mutually Exclusive events (A ∩ B = ∅) with non-zero probabilities are NEVER independent, because knowing A occurred immediately guarantees B could NOT occur (P(B|A) = 0 ≠ P(B))!"
        },
        {
            "number": "4.3",
            "title": "Probability Distributions: Binomial, Poisson, Uniform & Normal",
            "content": (
                "• <b>Binomial Distribution:</b> P(X = k) = C(n, k) p^k (1-p)^(n-k). Mean = np, Variance = np(1-p).<br/>"
                "• <b>Poisson Distribution:</b> P(X = k) = (e^(-λ) λ^k) / k!. <b>Mean = λ, Variance = λ</b> (Mean equals Variance!).<br/>"
                "• <b>Uniform Distribution U(a, b):</b> f(x) = 1/(b - a). Mean = (a + b)/2, Variance = (b - a)² / 12.<br/>"
                "• <b>Exponential Distribution:</b> f(x) = λ e^(-λx) for x ≥ 0. Mean = 1/λ, Variance = 1/λ². Memoryless: P(X > s + t | X > s) = P(X > t)."
            ),
            "crucial_rule": "CRUCIAL RULE: If a distribution has Mean = 4 and Variance = 4, in GATE it is almost certainly a Poisson distribution with parameter λ = 4!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Bayes' Theorem Application",
            "problem": "Machine 1 produces 60% of all chips with a 2% defect rate. Machine 2 produces 40% of all chips with a 5% defect rate. A randomly inspected chip is found to be DEFECTIVE. What is the probability that it came from Machine 2?",
            "steps": [
                "Step 1: Define events: M1 = Machine 1 (P(M1) = 0.60), M2 = Machine 2 (P(M2) = 0.40).",
                "Step 2: Defect probabilities: P(D|M1) = 0.02, P(D|M2) = 0.05.",
                "Step 3: Total Probability of a defect: P(D) = P(D|M1)P(M1) + P(D|M2)P(M2) = (0.02 × 0.60) + (0.05 × 0.40) = 0.012 + 0.020 = 0.032.",
                "Step 4: Apply Bayes' Theorem: P(M2|D) = [P(D|M2) × P(M2)] / P(D) = 0.020 / 0.032 = 20 / 32 = 5 / 8 = 0.625."
            ],
            "answer": "P(Machine 2 | Defective) = 0.625 (or 62.5%)."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Uniform Distribution Variance Denominator",
            "warning": "The variance of Uniform distribution U(a, b) has denominator 12: Var = (b - a)² / 12. Many students accidentally write (b - a)² / 4 (which is for half-interval squares)."
        },
        {
            "title": "Exam Trap 2: Binomial Variance vs Mean",
            "warning": "In Binomial distribution, Variance = np(1-p) is ALWAYS strictly LESS than Mean = np (since 0 < 1-p < 1). If a GATE question claims Mean = 10, Var = 12 for a Binomial model, it is an impossible question!"
        }
    ]
}

# =============================================================================
# DIGITAL LOGIC (DL)
# =============================================================================

# DL Chapter 0: Boolean Algebra, K-Maps & Minimization
CHAPTERS_EM_DL[("DL", 0)] = {
    "sub_id": "DL",
    "chap_idx": 0,
    "title": "Boolean Algebra, K-Maps & Tabular Method (Quine-McCluskey)",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Multi-Sensor Smart Home Alarm (Boolean Logic Simplification)",
            "text": "Imagine a home security system wired with 4 sensors: Door (A), Window (B), Motion (C), and Smoke (D). The alarm fires when various overlapping combinations occur (e.g. 'Door open AND night', or 'Motion AND Door open AND Smoke'). If an engineer builds the circuit directly from customer descriptions, it uses 25 logic chips costing ₹5,000 and generating tons of heat. By using Karnaugh Map simplification, the Boolean expression collapses to just 2 logic gates: (Door ∧ Motion) ∨ Smoke, slashing cost by 90% and response time to nanoseconds."
        },
        {
            "title": "Real-Life Example 2: The Don't-Care Voting Machine (Don't-Care Optimization)",
            "text": "In a BCD (Binary Coded Decimal) calculator, input digits only range from 0 to 9 (0000 to 1001). The binary codes 1010 through 1111 (10 to 15) CAN NEVER PHYSICALLY OCCUR because the keyboard hardware prevents it. When designing the display decoder circuit, we mark those 6 invalid states as 'Don't-Cares' (X). This allows our K-Map loops to aggressively group with those unused slots, cutting gate count in half for free."
        },
        {
            "title": "Real-Life Example 3: The Highway Bridge Toll Barrier Hazard (Static-1 Logic Hazard)",
            "text": "Imagine a highway boom barrier that stays UP whenever (A ∧ B) ∨ (~A ∧ C) is True. Suppose B=1 and C=1. As signal A flips from 1 to 0, mathematically the barrier should remain OPEN (1 ∨ 1 = 1). But in real silicon chips, ~A requires an inverter gate that takes 2 nanoseconds of propagation delay. For those 2 nanoseconds, both inputs are momentarily 0, causing the output to dip to 0—and the heavy metal boom barrier violently drops onto a passing car! Adding a redundant consensus term (B ∧ C) completely eliminates this lethal Static-1 hazard."
        }
    ],
    "foundations": [
        {
            "number": "5.1",
            "title": "Boolean Algebra Axioms, Duality & Consensus Theorem",
            "content": (
                "Boolean algebra operates on binary variables {0, 1} with operators AND (·), OR (+), and NOT (').<br/>"
                "• <b>Principle of Duality:</b> Any Boolean relation remains valid if AND and OR are swapped, and 0 and 1 are swapped (variables remain unchanged).<br/>"
                "• <b>De Morgan's Laws:</b> (A + B)' = A' · B' and (A · B)' = A' + B'.<br/>"
                "• <b>Consensus Theorem:</b> <b>AB + A'C + BC = AB + A'C</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Conditions: Three variables, each appears twice, one variable complemented, the term without the complemented variable (BC) is redundant and can be dropped!"
            ),
            "crucial_rule": "CRUCIAL RULE: In dual form of Consensus Theorem: (A + B)(A' + C)(B + C) = (A + B)(A' + C). The consensus factor (B + C) can be safely eliminated."
        },
        {
            "number": "5.2",
            "title": "Karnaugh Maps (K-Maps), Implicants & Minimization",
            "content": (
                "K-Maps use Gray code ordering (adjacent cells differ by exactly 1 bit) to identify geometric adjacency.<br/>"
                "• <b>Implicant:</b> Any single minterm or group of minterms where function evaluates to 1.<br/>"
                "• <b>Prime Implicant (PI):</b> A rectangular group of minterms (size 1, 2, 4, 8, 16) that cannot be combined into any larger group.<br/>"
                "• <b>Essential Prime Implicant (EPI):</b> A PI that contains at least one minterm '1' that is NOT covered by ANY OTHER prime implicant.<br/>"
                "• Minimal SOP = All EPIs + minimal selection of remaining non-essential PIs to cover uncovered minterms."
            ),
            "crucial_rule": "CRUCIAL RULE: Don't-cares ('X') can be grouped with 1s to form larger powers-of-two rectangles, but a prime implicant containing ONLY don't-cares is NEVER included in the final minimal expression!"
        },
        {
            "number": "5.3",
            "title": "Dynamic and Static Hazards in Combinational Logic",
            "content": (
                "• <b>Static-1 Hazard:</b> Output momentarily dips to 0 when it should remain 1. Occurs in SOP circuits when adjacent 1s in K-map belong to different prime implicants.<br/>"
                "• <b>Remedy:</b> Add redundant prime implicants (consensus terms) covering the adjacent 1s.<br/>"
                "• <b>Static-0 Hazard:</b> Output momentarily spikes to 1 when it should remain 0. Occurs in POS circuits; eliminated by adding redundant dual consensus terms.<br/>"
                "• <b>Dynamic Hazard:</b> Output transitions multiple times (e.g. 0 → 1 → 0 → 1) during a single input change. Occurs only in multi-level circuits with multiple delay paths."
            ),
            "crucial_rule": "CRUCIAL RULE: Two-level SOP circuits (AND-OR) NEVER contain Static-0 hazards or Dynamic hazards! They can ONLY exhibit Static-1 hazards."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Identifying EPIs and PIs",
            "problem": "Given Boolean function F(A, B, C, D) = ∑m(0, 2, 5, 7, 8, 10, 14, 15). Determine: (1) Total Prime Implicants, (2) Essential Prime Implicants, and (3) Minimal SOP expression.",
            "steps": [
                "Step 1: Plot minterms on 4-variable K-map (A, B rows: 00, 01, 11, 10; C, D columns: 00, 01, 11, 10).",
                "Step 2: Group four corners minterms (0, 2, 8, 10): eliminates A and C ⇒ Term B'D'.",
                "Step 3: Group minterms (5, 7): row 01 (A'B), columns 01, 11 (D) ⇒ Term A'BD.",
                "Step 4: Group minterms (14, 15): row 11 (AB), columns 11, 10 (C) ⇒ Term ABC.",
                "Step 5: Check for essential minterms: minterm 0 is covered only by B'D' (EPI). Minterm 5 is covered only by A'BD (EPI). Minterm 14 is covered only by ABC (EPI).",
                "Step 6: All 3 PIs are Essential Prime Implicants!"
            ],
            "answer": "Total PIs = 3, EPIs = 3. Minimal SOP: F = B'D' + A'BD + ABC."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Minimal SOP Uniqueness Myth",
            "warning": "The minimal SOP form is NOT necessarily unique! Multiple distinct minimal expressions can exist with identical gate counts and literal counts if non-essential PIs provide alternate coverings."
        },
        {
            "title": "Exam Trap 2: Counting Inverters as Literals",
            "warning": "In GATE questions asking for 'minimum number of literals in SOP form', complemented literals like A' count as 1 literal (not 2). Example: A'B + C has 3 literals (A', B, C)."
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
            "title": "Real-Life Example 1: The TV Remote Channel Selector (Multiplexer 2^n to 1)",
            "text": "Imagine a television with 8 different video feeds connected (Cable, PS5, Xbox, AppleTV, Blu-ray, Security Camera, etc.). The TV screen can only display 1 video at a time. The remote control sends a 3-bit binary code (Select lines: S2, S1, S0) to switch the internal electronic funnel directly to the requested input channel. An 8-to-1 Multiplexer routes 8 parallel inputs into a single output using 3 select bits."
        },
        {
            "title": "Real-Life Example 2: The Memory Address Postal Carrier (Binary Decoder n to 2^n)",
            "text": "When a CPU wants to read from RAM address 0110 (binary 6), it sends 4 address lines into a 4-to-16 Decoder. Out of all 16 memory storage banks, exactly ONE word-line (line 6) lights up with +5V, while the other 15 lines remain grounded at 0V. A decoder converts an n-bit compressed address into 2^n unique active selection lines."
        },
        {
            "title": "Real-Life Example 3: The Ripple Carry Delay Traffic Jam (Carry Lookahead Adder)",
            "text": "When adding two 64-bit numbers using simple Full Adders, the 64th adder CANNOT calculate its answer until the carry bit ripples through adders 1 through 63, like a slow wave of dominoes taking 100+ nanoseconds. A Carry Lookahead Adder (CLA) looks across all bits simultaneously using Generate (G = A·B) and Propagate (P = A ⊕ B) logic, computing all carry bits in constant O(1) time regardless of word size."
        }
    ],
    "foundations": [
        {
            "number": "6.1",
            "title": "Multiplexers (MUX) as Universal Logic Modules",
            "content": (
                "A 2^n-to-1 MUX has 2^n data inputs, n select lines, and 1 output.<br/>"
                "• <b>Output Equation for 2-to-1 MUX:</b> Y = S'·I0 + S·I1.<br/>"
                "• <b>Output Equation for 4-to-1 MUX:</b> Y = S1'S0'I0 + S1'S0 I1 + S1 S0' I2 + S1 S0 I3.<br/>"
                "• <b>Universal Property:</b> Any Boolean function of n variables can be implemented using:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;1. A 2^n-to-1 MUX with NO external gates.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;2. A 2^(n-1)-to-1 MUX using one variable (and its complement) connected to data inputs."
            ),
            "crucial_rule": "CRUCIAL RULE: To implement an n-variable function using a 2^(n-1)-to-1 MUX, connect (n-1) variables to select inputs, and express the data inputs as {0, 1, X, X'} where X is the remaining variable."
        },
        {
            "number": "6.2",
            "title": "Decoders, Encoders & Priority Encoders",
            "content": (
                "• <b>Binary Decoder (n-to-2^n):</b> Generates all 2^n fundamental minterms at its outputs. Active-high outputs generate minterms (AND); active-low outputs generate maxterms (NAND).<br/>"
                "• <b>Priority Encoder:</b> When multiple inputs are active simultaneously, it produces the binary code corresponding strictly to the highest-priority input.<br/>"
                "• <b>Cascading MUX/Decoders:</b> To construct a 64-to-1 MUX using 4-to-1 MUXes, total needed = 16 + 4 + 1 = <b>21 MUXes</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: Total 2-to-1 MUXes needed to construct an N-to-1 MUX is always exactly <b>N - 1</b>. Example: To build a 32-to-1 MUX requires 31 2-to-1 MUXes."
        },
        {
            "number": "6.3",
            "title": "Adders: Half Adder, Full Adder & Carry Lookahead Speedup",
            "content": (
                "• <b>Half Adder:</b> Sum = A ⊕ B, Carry = A · B. Requires 1 XOR gate and 1 AND gate.<br/>"
                "• <b>Full Adder:</b> Sum = A ⊕ B ⊕ Cin, Carry = AB + Cin(A ⊕ B). Can be implemented using 2 Half Adders and 1 OR gate.<br/>"
                "• <b>Carry Lookahead Adder (CLA):</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Generate Gi = Ai · Bi (produces carry independently of incoming carry).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Propagate Pi = Ai ⊕ Bi (passes incoming carry forward).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Ci+1 = Gi + Pi · Ci. All carries are computed in parallel in 2 gate delays!"
            ),
            "crucial_rule": "CRUCIAL RULE: Minimum number of NAND gates to implement a Half Adder is 5. Minimum NAND gates to implement a Full Adder is 9."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Function Realization via 4-to-1 MUX",
            "problem": "Implement F(A, B, C) = ∑m(1, 3, 4, 7) using a 4-to-1 MUX with A and B connected to select lines S1 and S0 respectively.",
            "steps": [
                "Step 1: Set S1 = A, S0 = B. The 4 MUX data inputs correspond to AB = 00 (I0), AB = 01 (I1), AB = 10 (I2), AB = 11 (I3).",
                "Step 2: Partition minterms by AB combinations:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• For AB = 00: minterms 0, 1. Here m1 is in F, m0 is not. So when C=1, F=1; when C=0, F=0. Thus <b>I0 = C</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• For AB = 01: minterms 2, 3. Here m3 is in F, m2 is not. Thus <b>I1 = C</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• For AB = 10: minterms 4, 5. Here m4 is in F, m5 is not. So when C=0, F=1; when C=1, F=0. Thus <b>I2 = C'</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• For AB = 11: minterms 6, 7. Here m7 is in F, m6 is not. Thus <b>I3 = C</b>."
            ],
            "answer": "Data inputs: I0 = C, I1 = C, I2 = C', I3 = C."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Active-Low Enable Lines on Decoders",
            "warning": "Decoders in GATE almost always feature an Active-Low Enable (E'). If E' = 1, ALL outputs are 0 regardless of input addresses! Aspirants constantly overlook the inversion bubble on E."
        },
        {
            "title": "Exam Trap 2: CLA Hardware Fan-in Limit",
            "warning": "While CLA has theoretical O(1) delay, in real 64-bit systems gate fan-in becomes unfeasible (requiring 65-input AND gates). Hence real systems use hierarchical Block Carry Lookahead."
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
            "title": "Real-Life Example 1: The Clicky Push-Button Light Switch (T Flip-Flop & Toggling)",
            "text": "In modern luxury hotels, the bedside lamp doesn't use a mechanical rocker switch. It has a single tactile push button. You press it once: lamp turns ON. You press the exact same button a second time: lamp turns OFF. The circuit 'remembers' its previous state and inverts upon each trigger. This is the exact behavior of a T Flip-Flop (Toggle Flip-Flop) triggered by a clock pulse."
        },
        {
            "title": "Real-Life Example 2: The Car Odometer / Mileage Counter (Synchronous vs Asynchronous Counter)",
            "text": "In an old mechanical odometer, the 1s digit spins. When it transitions from 9 to 0, a physical tooth nudges the 10s digit to click forward. That is an Asynchronous (Ripple) Counter: each flip-flop is clocked by the output of the preceding one, accumulating cumulative propagation delays. In contrast, modern digital odometers pulse all digit registers simultaneously from the car's engine ECU: a Synchronous Counter where all stages update on the exact same clock tick."
        },
        {
            "title": "Real-Life Example 3: The Subway Turnstile State Machine (Mealy vs Moore FSM)",
            "text": "A subway turnstile has two states: Locked and Unlocked. In a Moore Machine, the state alone dictates the physical gate: as long as the state is 'Unlocked', green light shines. In a Mealy Machine, the output depends on both state AND current input: if the turnstile is 'Locked' AND a valid metro card is tapped, the gate unlocks immediately on that exact clock edge without waiting for a state transition."
        }
    ],
    "foundations": [
        {
            "number": "7.1",
            "title": "Flip-Flops: SR, JK, D, T & Characteristic Equations",
            "content": (
                "A flip-flop is a bistable multivibrator capable of storing 1 bit of information.<br/>"
                "• <b>SR Flip-Flop:</b> Q(next) = S + R'Q (Invalid state when S = R = 1).<br/>"
                "• <b>JK Flip-Flop:</b> Q(next) = J Q' + K' Q (Toggles when J = K = 1, solves SR invalidity).<br/>"
                "• <b>D Flip-Flop (Data/Delay):</b> Q(next) = D (Stores incoming bit on clock edge).<br/>"
                "• <b>T Flip-Flop (Toggle):</b> Q(next) = T ⊕ Q = T Q' + T' Q (Inverts state when T = 1)."
            ),
            "crucial_rule": "CRUCIAL RULE: Characteristic equations summary:<br/>• SR: Q+ = S + R'Q (SR=0)<br/>• JK: Q+ = JQ' + K'Q<br/>• D: Q+ = D<br/>• T: Q+ = T ⊕ Q."
        },
        {
            "number": "7.2",
            "title": "Timing Parameters: Setup Time, Hold Time & Clock Frequency",
            "content": (
                "• <b>Setup Time (t_setup):</b> The minimum time the input data must remain stable BEFORE the active clock edge arrives.<br/>"
                "• <b>Hold Time (t_hold):</b> The minimum time the input data must remain stable AFTER the active clock edge occurs.<br/>"
                "• <b>Maximum Clock Frequency Calculation:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;T_clk ≥ t_cq(max) + t_comb(max) + t_setup.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;<b>f_max = 1 / T_clk(min)</b>.<br/>"
                "• <b>Hold Time Violation Check:</b> t_cq(min) + t_comb(min) ≥ t_hold. (Independent of clock period T_clk!)."
            ),
            "crucial_rule": "CRUCIAL RULE: Hold time violations CANNOT be fixed by reducing the clock frequency! They depend solely on minimum internal propagation delays."
        },
        {
            "number": "7.3",
            "title": "Synchronous vs Asynchronous (Ripple) Counters & Modulo Numbers",
            "content": (
                "• <b>Modulo-N Counter:</b> A counter that cycles through N distinct states. Requires ⌈log2(N)⌉ flip-flops.<br/>"
                "• <b>Ring Counter:</b> N flip-flops cycling a single '1' through N states (Mod-N).<br/>"
                "• <b>Johnson (Twisted Ring) Counter:</b> Inverted output of last flip-flop feeds back to first. Uses N flip-flops to cycle through <b>2N distinct states</b> (Mod-2N)."
            ),
            "crucial_rule": "CRUCIAL RULE: To design a Mod-10 counter: Ring Counter requires 10 flip-flops, Johnson Counter requires 5 flip-flops, Standard Binary Counter requires 4 flip-flops (2^4 = 16 ≥ 10)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Maximum Clock Frequency Calculation",
            "problem": "A digital circuit connects two flip-flops through a combinational block. Flip-flop propagation delay t_cq = 3 ns, setup time t_setup = 2 ns, hold time t_hold = 1 ns. Combinational delay t_comb ranges between 4 ns and 8 ns. Find the maximum clock frequency f_max.",
            "steps": [
                "Step 1: Identify maximum delay path for clock period: T_clk(min) = t_cq(max) + t_comb(max) + t_setup.",
                "Step 2: Substitute values: T_clk(min) = 3 ns + 8 ns + 2 ns = 13 ns.",
                "Step 3: Calculate maximum operating clock frequency: f_max = 1 / T_clk(min) = 1 / (13 × 10^-9 s) ≈ 76.92 MHz.",
                "Step 4: Verify hold time condition: t_cq(min) + t_comb(min) = 3 ns + 4 ns = 7 ns. Since 7 ns > t_hold (1 ns), no hold violation occurs."
            ],
            "answer": "Maximum clock frequency f_max = 76.92 MHz."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: The JK Race-Around Condition",
            "warning": "Race-around occurs in level-triggered JK flip-flops when J = K = 1 and clock pulse width tp > flip-flop delay t_pd. The output oscillates uncontrollably. It is eliminated by Master-Slave flip-flops or edge-triggering."
        },
        {
            "title": "Exam Trap 2: Unused States in Johnson Counters",
            "warning": "A 4-bit Johnson counter has 2N = 8 valid states out of 2^4 = 16 total states. The remaining 8 states are unused. In GATE, if noise knocks the circuit into an unused state, check if the counter is self-recovering!"
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
            "title": "Real-Life Example 1: The Odometer Rolling Over 99999 to 00000 (Two's Complement Wrap-around)",
            "text": "Imagine a 5-digit car odometer at 99,999 km. If you drive 1 more kilometer, it rolls over to 00,000 km. In computer arithmetic, an 8-bit signed integer at +127 (01111111) that gets incremented by 1 suddenly wraps around to -128 (10000000)! This is Two's Complement modular arithmetic: adding numbers behaves like walking around a clock face, which is why hardware subtracts by simply adding the negative complement."
        },
        {
            "title": "Real-Life Example 2: The $500 Million Ariane 5 Rocket Explosion (Floating-Point Overflow)",
            "text": "In 1996, the European Ariane 5 rocket exploded 39 seconds after launch. The guidance computer converted a 64-bit floating point velocity measurement to a 16-bit signed integer. The horizontal velocity was larger than 32,767 (overflowing the 16-bit integer maximum), triggering an unhandled software exception that sheared off the rocket engines. Precision and representation bounds are mission-critical."
        },
        {
            "title": "Real-Life Example 3: The Microscope Zoom Lens (IEEE 754 Mantissa & Exponent)",
            "text": "How can 32 bits represent both the width of an atom (10^-10 meters) and the distance to the sun (10^11 meters)? If we used fixed decimal points, we would need 100+ bits. Instead, IEEE 754 uses scientific notation: Sign bit (direction), Exponent (the zoom factor / power of 2), and Mantissa (the sharp precision digits). The exponent shifts the binary decimal point like a microscope zoom lens."
        }
    ],
    "foundations": [
        {
            "number": "8.1",
            "title": "Fixed-Point Signed Number Representations: Sign-Magnitude, 1's & 2's Complement",
            "content": (
                "For an n-bit binary representation:<br/>"
                "• <b>Sign-Magnitude:</b> MSB is sign (0=pos, 1=neg), remaining n-1 bits represent magnitude. Range: <b>-(2^(n-1) - 1) to +(2^(n-1) - 1)</b>. Has two representations of zero (+0, -0).<br/>"
                "• <b>1's Complement:</b> Negate all bits. Range: <b>-(2^(n-1) - 1) to +(2^(n-1) - 1)</b>. Also suffers from +0 and -0.<br/>"
                "• <b>2's Complement:</b> 1's complement + 1. Range: <b>-2^(n-1) to +(2^(n-1) - 1)</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Unique representation of zero (0000...0). Extra negative number: -2^(n-1) has no positive counterpart."
            ),
            "crucial_rule": "CRUCIAL RULE: For 8 bits: 2's complement range is -128 to +127. The binary code 10000000 represents strictly -128."
        },
        {
            "number": "8.2",
            "title": "IEEE 754 Floating-Point Standard (Single & Double Precision)",
            "content": (
                "• <b>Single Precision (32-bit):</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;1 Sign bit (s), 8 Exponent bits (e, Bias = 127), 23 Mantissa/Fraction bits (f).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Value = <b>(-1)^s × 1.f × 2^(e - 127)</b> (for normalized numbers 1 ≤ e ≤ 254).<br/>"
                "• <b>Special Representations:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• If e = 0 and f = 0: Represents ±0.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• If e = 0 and f ≠ 0: Denormalized / Subnormal number: (-1)^s × 0.f × 2^(-126).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• If e = 255 and f = 0: Represents ±Infinity (overflow).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• If e = 255 and f ≠ 0: Represents NaN (Not a Number, e.g. 0/0)."
            ),
            "crucial_rule": "CRUCIAL RULE: In normalized numbers, the leading '1.' is implicit (hidden bit) and is NOT stored in the 23-bit mantissa. But in denormalized numbers (e = 0), the hidden bit is explicitly '0.'!"
        },
        {
            "number": "8.3",
            "title": "Arithmetic Overflow Detection in 2's Complement",
            "content": (
                "Overflow occurs when the addition of two numbers of like sign produces a result of the opposite sign.<br/>"
                "• Adding two positive numbers yields a negative result (Positive Overflow).<br/>"
                "• Adding two negative numbers yields a positive result (Negative Overflow).<br/>"
                "• Adding numbers of opposite signs can <b>NEVER</b> produce overflow.<br/>"
                "• <b>Hardware Detection Rule:</b> Overflow = <b>C_in ⊕ C_out</b> of the MSB adder stage."
            ),
            "crucial_rule": "CRUCIAL RULE: If carry into MSB (C_n-1) differs from carry out of MSB (C_n), overflow has definitely occurred!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Decimal to IEEE 754 Single Precision Hexadecimal",
            "problem": "Convert the decimal number -9.75 into 32-bit IEEE 754 floating point format, and represent the final 32 bits in hexadecimal.",
            "steps": [
                "Step 1: Sign bit: Since number is negative, Sign bit s = 1.",
                "Step 2: Convert magnitude 9.75 to binary: Integer 9 = 1001_2; Fractional 0.75 = 0.5 + 0.25 = 0.11_2. Thus 9.75 = 1001.11_2.",
                "Step 3: Normalize binary into scientific notation: 1001.11 = 1.00111 × 2^3.",
                "Step 4: Compute biased exponent: E = e + Bias = 3 + 127 = 130. 130 in 8-bit binary = 10000010_2.",
                "Step 5: Mantissa bits (drop the leading 1): 00111 followed by eighteen 0s (23 bits total): 00111000000000000000000.",
                "Step 6: Assemble 32 bits: [1] [10000010] [00111000000000000000000].",
                "Step 7: Group into 4-bit nibbles: 1100 0001 0001 1100 0000 0000 0000 0000 ⇒ 0xC11C0000."
            ],
            "answer": "IEEE 754 Representation = 0xC11C0000."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Exponent Bias Off-by-One",
            "warning": "For single precision, Bias = 2^(8-1) - 1 = 127. Many aspirants use 128 by mistake. For double precision (11 exponent bits), Bias = 2^(11-1) - 1 = 1023."
        },
        {
            "title": "Exam Trap 2: Smallest Normalized vs Denormalized Number",
            "warning": "The smallest positive NORMALIZED number is 1.0 × 2^(-126) (e=1, f=0). The smallest positive DENORMALIZED number is 2^(-23) × 2^(-126) = 2^(-149) (e=0, f=000...01)."
        }
    ]
}
