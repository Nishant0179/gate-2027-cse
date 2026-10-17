# Engineering Mathematics Content Module for GATE 2027 CSE
# Weightage: 13 Marks (Mandatory Section)

SUBJECT_META = {
    "id": "EM",
    "name": "Engineering Mathematics",
    "folder": "01_Engineering_Mathematics",
    "weightage": "13 Marks",
    "topics": [
        "Discrete Mathematics: Logic, Sets, Relations, Functions, Lattices, Groups, Graphs, Combinatorics",
        "Linear Algebra: Matrices, Determinants, Systems of Linear Equations, Eigenvalues/Eigenvectors, LU Decomposition",
        "Calculus: Limits, Continuity, Differentiability, Maxima/Minima, Mean Value Theorem, Integration",
        "Probability and Statistics: Random Variables, Distributions, Bayes Theorem, Central Tendency"
    ]
}

CHAPTERS = [
    {
        "title": "Discrete Mathematics - Mathematical Logic & Set Theory",
        "hinglish": "Mathematical Logic GATE ka sabse scoring topic hai. Isme statements ki truth values, quantifiers, aur inference rules par directly questions aate hain.",
        "theory": (
            "<b>1. Propositional Logic:</b> A proposition is a declarative statement that is strictly True (T) or False (F).<br/>"
            "• <b>Negation (~p):</b> Opposite truth value.<br/>"
            "• <b>Conjunction (p ^ q):</b> True iff both p and q are True.<br/>"
            "• <b>Disjunction (p v q):</b> False iff both p and q are False.<br/>"
            "• <b>Implication (p -> q):</b> Equivalent to (~p v q). False ONLY when p is True and q is False. If antecedent p is False, implication is vacuously True!<br/>"
            "• <b>Biconditional (p <-> q):</b> True iff p and q have identical truth values.<br/>"
            "• <b>Converse:</b> q -> p &nbsp;|&nbsp; <b>Inverse:</b> ~p -> ~q &nbsp;|&nbsp; <b>Contrapositive:</b> ~q -> ~p (Logically equivalent to p -> q).<br/><br/>"
            "<b>2. First-Order Predicate Logic:</b> Introduces variables, predicates, and quantifiers.<br/>"
            "• Universal Quantifier (∀x): True if P(x) is true for all elements in domain.<br/>"
            "• Existential Quantifier (∃x): True if P(x) is true for at least one element.<br/>"
            "• De Morgan's Laws: ~(∀x P(x)) ≡ ∃x ~P(x) &nbsp;and&nbsp; ~(∃x P(x)) ≡ ∀x ~P(x).<br/>"
            "• Standard Equivalences: (∀x P(x) -> Q) ≡ ∃x (P(x) -> Q) &nbsp;|&nbsp; (∃x P(x) -> Q) ≡ ∀x (P(x) -> Q)."
        ),
        "callouts": [
            ("Vacuous Truth Trap", "In conditional statement p -> q, if p is False, the statement is ALWAYS TRUE regardless of q. Example: 'If 2+2=5, then elephants fly' is mathematically TRUE!", "warn"),
            ("Equivalence Rule", "p -> (q -> r) is logically equivalent to (p ^ q) -> r (Exportation Law).", "formula")
        ],
        "tables": [
            {
                "header": ["Property", "Relation Definition R on set A (|A| = n)", "Total Number of Relations"],
                "rows": [
                    ["Reflexive", "∀a ∈ A, (a, a) ∈ R", "2^(n^2 - n)"],
                    ["Symmetric", "∀a,b, (a, b) ∈ R => (b, a) ∈ R", "2^(n(n+1)/2)"],
                    ["Reflexive & Symmetric", "Both conditions satisfied", "2^(n(n-1)/2)"],
                    ["Anti-symmetric", "∀a,b, ((a,b) ∈ R ^ (b,a) ∈ R) => a = b", "2^n * 3^(n(n-1)/2)"],
                    ["Asymmetric", "∀a,b, (a, b) ∈ R => (b, a) ∉ R", "3^(n(n-1)/2)"],
                    ["Equivalence", "Reflexive, Symmetric, and Transitive", "Bell Number B(n)"]
                ]
            }
        ]
    },
    {
        "title": "Discrete Mathematics - Graph Theory & Combinatorics",
        "hinglish": "Graph theory me Handshaking Lemma, Planar Graphs (Euler formula), Trees, aur Coloring me se har saal 1-2 questions fix aate hain.",
        "theory": (
            "<b>1. Handshaking Lemma:</b> For any undirected graph G = (V, E), sum of degrees of all vertices equals 2|E|: ∑ deg(v) = 2|E|.<br/>"
            "• Consequence: The number of vertices with odd degree is ALWAYS EVEN.<br/><br/>"
            "<b>2. Planar Graphs:</b> A graph that can be drawn in a plane without intersecting edges.<br/>"
            "• <b>Euler's Formula:</b> For a connected planar graph: V - E + R = 2 (where R is the number of regions/faces including outer face).<br/>"
            "• <b>Planarity Edge Bounds:</b> If |V| ≥ 3 and no self-loops/parallel edges: E ≤ 3V - 6.<br/>"
            "• If the graph is bipartite or triangle-free: E ≤ 2V - 4.<br/>"
            "• <b>Kuratowski's Theorem:</b> A graph is planar iff it contains no subgraph homeomorphic to K5 or K3,3.<br/><br/>"
            "<b>3. Graph Coloring:</b> Minimum number of colors needed to color vertices so no adjacent vertices share color (Chromatic number χ(G)).<br/>"
            "• Bipartite graphs (including trees, even cycles): χ(G) = 2.<br/>"
            "• Odd cycle C_(2k+1): χ(G) = 3.<br/>"
            "• Complete graph K_n: χ(G) = n.<br/>"
            "• Planar graph (Four Color Theorem): χ(G) ≤ 4.<br/><br/>"
            "<b>4. Combinatorics & Generating Functions:</b><br/>"
            "• Pigeonhole Principle: If n items put into m containers, at least one container holds ⌈n/m⌉ items.<br/>"
            "• Inclusion-Exclusion Principle: |A ∪ B ∪ C| = |A| + |B| + |C| - (|A ∩ B| + |B ∩ C| + |C ∩ A|) + |A ∩ B ∩ C|.<br/>"
            "• Derangements: D_n = n! [1 - 1/1! + 1/2! - 1/3! + ... + (-1)^n/n!] ≈ n!/e."
        ),
        "callouts": [
            ("Euler Formula Warning", "Remember Euler's formula V - E + R = 2 holds ONLY for CONNECTED planar graphs. If there are k connected components, then V - E + R = 1 + k.", "warn"),
            ("Handshaking Power", "Whenever you see degree sequence questions, always check if sum of degrees is even and odd-degree vertex count is even first!", "tip")
        ],
        "tables": [
            {
                "header": ["Graph Family", "Vertices (V)", "Edges (E)", "Chromatic Number χ(G)", "Planar?"],
                "rows": [
                    ["Complete Graph K_n", "n", "n(n-1)/2", "n", "Planar only for n ≤ 4"],
                    ["Complete Bipartite K_(m,n)", "m+n", "m*n", "2", "Planar only if min(m,n) ≤ 2"],
                    ["Cycle Graph C_n", "n", "n", "2 (n even), 3 (n odd)", "Always Planar"],
                    ["Tree T_n", "n", "n - 1", "2", "Always Planar"]
                ]
            }
        ]
    },
    {
        "title": "Linear Algebra - Systems, Eigenvalues & LU Decomposition",
        "hinglish": "Linear algebra me determinants, system of equations AX=B ki consistency, aur eigenvalues ki properties direct marks deti hain.",
        "theory": (
            "<b>1. System of Linear Equations (AX = B):</b><br/>"
            "• Let [A|B] be the augmented matrix, n = number of variables.<br/>"
            "• <b>Consistent (Solutions exist):</b> rank(A) = rank([A|B]).<br/>"
            "  - Unique Solution: rank(A) = rank([A|B]) = n.<br/>"
            "  - Infinitely Many Solutions: rank(A) = rank([A|B]) = r &lt; n (with n - r free variables).<br/>"
            "• <b>Inconsistent (No solution):</b> rank(A) &lt; rank([A|B]).<br/>"
            "• <b>Homogeneous System (AX = 0):</b> Always consistent (trivial solution X=0 always exists). Non-trivial (infinite) solution iff rank(A) &lt; n (i.e. det(A) = 0 for square matrix).<br/><br/>"
            "<b>2. Eigenvalues and Eigenvectors:</b><br/>"
            "• Characteristic equation: det(A - λI) = 0.<br/>"
            "• <b>Key Properties:</b><br/>"
            "  - Sum of eigenvalues = Trace of matrix A (sum of main diagonal elements).<br/>"
            "  - Product of eigenvalues = Determinant of matrix A.<br/>"
            "  - Eigenvalues of triangular/diagonal matrix are its main diagonal elements.<br/>"
            "  - If λ is eigenvalue of A, then λ^k is eigenvalue of A^k; 1/λ is eigenvalue of A^(-1) (if invertible).<br/>"
            "  - Eigenvalues of symmetric real matrix are always REAL; of skew-symmetric are ZERO or purely IMAGINARY.<br/>"
            "  - Eigenvalues of orthogonal matrix have absolute value 1.<br/><br/>"
            "<b>3. LU Decomposition:</b> Expressing A = L * U where L is lower triangular (with 1s on diagonal for Doolittle algorithm) and U is upper triangular.<br/>"
            "• Requires det(A_k) ≠ 0 for all leading principal submatrices of A."
        ),
        "callouts": [
            ("Trace & Det Shortcut", "In 90% of GATE eigenvalue questions, you don't need to solve the cubic equation! Just verify that sum(λ_i) = Trace(A) and prod(λ_i) = Det(A) against the options.", "tip"),
            ("Zero Eigenvalue Rule", "Matrix A is non-invertible (singular, det(A)=0) if and only if at least one eigenvalue of A is 0.", "formula")
        ],
        "tables": []
    },
    {
        "title": "Calculus & Probability - Distributions and Bayes Theorem",
        "hinglish": "Calculus me Maxima/Minima and Mean Value Theorems aate hain. Probability me Bayes Theorem aur standard distributions (Poisson, Normal, Exponential) par questions aate hain.",
        "theory": (
            "<b>1. Calculus:</b><br/>"
            "• <b>L'Hopital's Rule:</b> For indeterminate forms 0/0 or ∞/∞, lim [f(x)/g(x)] = lim [f'(x)/g'(x)].<br/>"
            "• <b>Rolle's Theorem:</b> If f(x) is continuous on [a, b], differentiable on (a, b), and f(a) = f(b), then ∃ c ∈ (a, b) such that f'(c) = 0.<br/>"
            "• <b>Lagrange's Mean Value Theorem:</b> ∃ c ∈ (a, b) such that f'(c) = [f(b) - f(a)] / (b - a).<br/>"
            "• <b>Maxima and Minima (Single Variable):</b> Critical points where f'(x) = 0.<br/>"
            "  - If f''(x) &lt; 0 -> Local Maximum.<br/>"
            "  - If f''(x) &gt; 0 -> Local Minimum.<br/>"
            "  - If f''(x) = 0 and f'''(x) ≠ 0 -> Inflection Point.<br/><br/>"
            "<b>2. Probability Distributions:</b><br/>"
            "• <b>Binomial Distribution:</b> P(X = k) = C(n, k) * p^k * (1-p)^(n-k). Mean = np, Variance = np(1-p).<br/>"
            "• <b>Poisson Distribution:</b> P(X = k) = (e^(-λ) * λ^k) / k!. Mean = λ, Variance = λ.<br/>"
            "• <b>Exponential Distribution (Continuous):</b> f(x) = λ e^(-λx) for x ≥ 0. Mean = 1/λ, Variance = 1/λ^2. Memoryless: P(X &gt; s+t | X &gt; s) = P(X &gt; t).<br/>"
            "• <b>Normal Distribution:</b> Symmetric bell curve. Mean = μ, Variance = σ^2.<br/><br/>"
            "<b>3. Bayes' Theorem:</b><br/>"
            "• P(A|B) = [P(B|A) * P(A)] / P(B) = [P(B|A) * P(A)] / [∑ P(B|A_i) * P(A_i)]."
        ),
        "callouts": [
            ("Poisson Equality", "In Poisson distribution, Mean == Variance = λ. If exam states mean is equal to variance, it is Poisson!", "formula"),
            ("Conditional Probability Trap", "Remember P(A|B) is NOT equal to P(B|A) in general! Always identify the given conditioned event carefully.", "warn")
        ],
        "tables": []
    }
]

PRACTICE_QUESTIONS = [
    {
        "id": "EM-Q01",
        "type": "MCQ",
        "marks": 1,
        "text": "Let P and Q be two propositions. Which of the following statements is a TAUTOLOGY?",
        "options": {
            "A": "(P -> Q) -> P",
            "B": "P -> (Q -> P)",
            "C": "(P v Q) -> (P ^ Q)",
            "D": "(P -> Q) -> (Q -> P)"
        },
        "answer": "B",
        "explanation": "Expanding option B: P -> (Q -> P) ≡ ~P v (~Q v P) ≡ (~P v P) v ~Q ≡ T v ~Q ≡ T. Since it evaluates to True under all truth assignments, it is a Tautology.",
        "is_pyq": True,
        "year": 2023,
        "difficulty": "Easy"
    },
    {
        "id": "EM-Q02",
        "type": "NAT",
        "marks": 2,
        "text": "A connected planar graph has 10 vertices and divides the plane into 7 regions/faces. What is the number of edges in this graph?",
        "answer": "15",
        "explanation": "By Euler's planar formula for connected graphs: V - E + R = 2. Here V = 10, R = 7. Therefore, 10 - E + 7 = 2 => 17 - E = 2 => E = 15.",
        "is_pyq": True,
        "year": 2022,
        "difficulty": "Medium"
    },
    {
        "id": "EM-Q03",
        "type": "MSQ",
        "marks": 2,
        "text": "Let A be a 3x3 real symmetric matrix with eigenvalues 1, 2, and 3. Which of the following statements is/are CORRECT?",
        "options": {
            "A": "Determinant of A is 6",
            "B": "Trace of A is 6",
            "C": "A is invertible",
            "D": "Eigenvalues of A^2 are 1, 4, and 9"
        },
        "answer": "A, B, C, D",
        "explanation": "Det(A) = 1 * 2 * 3 = 6 (A is true). Trace(A) = 1 + 2 + 3 = 6 (B is true). Det(A) ≠ 0 so A is invertible (C is true). Eigenvalues of A^k are λ^k, so for A^2 they are 1^2=1, 2^2=4, 3^2=9 (D is true). All four choices are correct.",
        "is_pyq": False,
        "year": None,
        "difficulty": "GATE-Level"
    },
    {
        "id": "EM-Q04",
        "type": "NAT",
        "marks": 2,
        "text": "In a communication channel, bit errors occur according to a Poisson process with an average rate of 2 errors per 1000 bits transmitted. If 1000 bits are transmitted, what is the probability (rounded to 3 decimal places) that exactly 0 errors occur? (Take e^(-2) = 0.1353)",
        "answer": "0.135",
        "explanation": "For Poisson distribution, P(X = k) = (e^(-λ) * λ^k) / k!. Here λ = 2 and k = 0. P(X = 0) = (e^(-2) * 2^0) / 0! = e^(-2) = 0.1353 ≈ 0.135.",
        "is_pyq": False,
        "year": None,
        "difficulty": "GATE-Level"
    },
    {
        "id": "EM-Q05",
        "type": "MCQ",
        "marks": 1,
        "text": "What is the chromatic number of the complete bipartite graph K_{3, 5}?",
        "options": {
            "A": "2",
            "B": "3",
            "C": "5",
            "D": "8"
        },
        "answer": "A",
        "explanation": "Any non-empty bipartite graph (complete or otherwise) can be 2-colored by assigning one color to all vertices in partition 1 and a second color to all vertices in partition 2. Hence χ(K_{3, 5}) = 2.",
        "is_pyq": True,
        "year": 2021,
        "difficulty": "Easy"
    }
]
