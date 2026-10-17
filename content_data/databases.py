# Databases Content Module for GATE 2027 CSE
# Weightage: 7-9 Marks

SUBJECT_META = {
    "id": "DB",
    "name": "Databases",
    "folder": "09_Databases",
    "weightage": "7 Marks",
    "topics": [
        "ER-model, relational model: relational algebra, tuple calculus, SQL",
        "Integrity constraints, functional dependencies, normal forms (1NF, 2NF, 3NF, BCNF)",
        "File organization, indexing (B and B+ trees)",
        "Transactions and concurrency control: ACID, serializability, recoverability, locking protocols"
    ]
}

CHAPTERS = [
    {
        "title": "ER-Model, Relational Algebra & SQL",
        "hinglish": "Relational algebra expressions, division operator (queries with 'all' or 'every'), aur SQL me correlated subqueries and GROUP BY HAVING par regular questions aate hain.",
        "theory": (
            "<b>1. ER Model to Relational Schema Conversion:</b><br/>"
            "• Entity with simple attributes -> Table with attributes as columns.<br/>"
            "• Multivalued attribute -> Separate table with primary key of entity + multivalued attribute.<br/>"
            "• 1:N Relationship -> Primary key of '1' side goes as Foreign Key into 'N' side table.<br/>"
            "• 1:1 Relationship -> Foreign key can be placed on either side (prefer total participation side).<br/>"
            "• M:N Relationship -> Requires a separate relation table with primary keys of both entities.<br/><br/>"
            "<b>2. Relational Algebra Operators:</b><br/>"
            "• <b>Select (σ_p):</b> Horizontal filtering of tuples satisfying predicate p.<br/>"
            "• <b>Project (π_L):</b> Vertical selection of attributes in list L (automatically eliminates duplicates).<br/>"
            "• <b>Cartesian Product (R x S):</b> All pairs of tuples. Tuples = |R| * |S|, Attributes = arity(R) + arity(S).<br/>"
            "• <b>Natural Join (R ⋈ S):</b> Equijoin on all common attributes followed by projection to eliminate duplicate attribute columns.<br/>"
            "• <b>Division Operator (R ÷ S):</b> Finds tuples in R that are associated with ALL tuples in S. Expressed as: π_X(R) - π_X((π_X(R) x S) - R).<br/><br/>"
            "<b>3. SQL Three-Valued Logic & Aggregates:</b><br/>"
            "• Three-Valued Logic: True, False, Unknown. Any arithmetic comparison with NULL (e.g. A = NULL) evaluates to UNKNOWN! Must use 'IS NULL' or 'IS NOT NULL'.<br/>"
            "• Aggregate functions (COUNT, SUM, AVG, MIN, MAX): All aggregates IGNORE NULL values EXCEPT COUNT(*)!<br/>"
            "• WHERE filters individual rows BEFORE grouping; HAVING filters groups AFTER GROUP BY."
        ),
        "callouts": [
            ("Division Operator in English", "Whenever an English query asks for 'Find students who have enrolled in ALL courses offered by CSE', it directly translates to Relational Division (R ÷ S)!", "tip"),
            ("NULL in COUNT Trap", "COUNT(attribute) counts non-null values. COUNT(*) counts total rows including rows where attributes are NULL!", "warn")
        ],
        "tables": []
    },
    {
        "title": "Functional Dependencies & Normalization (1NF to BCNF)",
        "hinglish": "Normalization me Candidate Keys nikalna, Canonical Cover find karna, aur 3NF vs BCNF test karna sabse standard GATE numericals hain.",
        "theory": (
            "<b>1. Functional Dependencies & Keys:</b><br/>"
            "• <b>X -> Y:</b> If two tuples agree on attributes X, they MUST agree on attributes Y.<br/>"
            "• <b>Super Key:</b> Attribute set X whose closure X+ contains ALL attributes of relation R.<br/>"
            "• <b>Candidate Key (CK):</b> Minimal Super Key (no proper subset of X is a super key).<br/>"
            "• <b>Prime Attribute:</b> Attribute that belongs to AT LEAST ONE candidate key. Non-prime: not in any CK.<br/><br/>"
            "<b>2. Normal Forms:</b><br/>"
            "• <b>1NF:</b> All attribute values are atomic (no multivalued or composite attributes).<br/>"
            "• <b>2NF:</b> In 1NF and NO Partial Dependency (No Proper Subset of CK -> Non-Prime).<br/>"
            "• <b>3NF:</b> In 2NF and NO Transitive Dependency. For every non-trivial X -> Y:<br/>"
            "  - Either X is a Super Key, OR Y is a Prime Attribute.<br/>"
            "• <b>BCNF (Boyce-Codd NF):</b> For every non-trivial X -> Y, X MUST BE A SUPER KEY!<br/>"
            "  - Strictly stronger than 3NF. Eliminates all redundancy based on FDs.<br/><br/>"
            "<b>3. Decomposition Properties:</b><br/>"
            "• <b>Lossless Join (Mandatory):</b> R1 ⋈ R2 = R iff (R1 ∩ R2) -> R1 OR (R1 ∩ R2) -> R2.<br/>"
            "• <b>Dependency Preservation:</b> (F1 ∪ F2)+ = F+. 3NF decomposition is ALWAYS lossless and dependency-preserving. BCNF decomposition is always lossless, but MAY NOT PRESERVE all dependencies!"
        ),
        "callouts": [
            ("BCNF vs 3NF Tradeoff", "You can ALWAYS decompose any relation into 3NF such that it is both LOSSLESS and DEPENDENCY PRESERVING. For BCNF, lossless is guaranteed, but dependency preservation is NOT always achievable!", "formula"),
            ("Prime Attribute in 3NF", "In 3NF, RHS can be a prime attribute even if LHS is not a super key. In BCNF, LHS MUST be a super key regardless of RHS!", "tip")
        ],
        "tables": []
    },
    {
        "title": "B/B+ Trees, Transactions & Concurrency Control",
        "hinglish": "B+ Tree me leaf nodes data pointers hold karte hain aur doubly linked list banate hain. Transactions me Conflict Serializability (Precedence Graph) se cycles detect kiye jate hain.",
        "theory": (
            "<b>1. Indexing & B/B+ Trees:</b><br/>"
            "• <b>Dense Index:</b> Index record for every search key value in file.<br/>"
            "• <b>Sparse Index:</b> Index record for only some records (usually one per disk block).<br/>"
            "• <b>B+ Tree Node Capacities:</b> For node of order p (block size B, key size K, block pointer P, record pointer R_p):<br/>"
            "  - Internal node: p * P + (p - 1) * K ≤ B.<br/>"
            "  - Leaf node: (p_leaf - 1) * (K + R_p) + P ≤ B.<br/>"
            "  - All leaves are at the exact same level and connected via pointers for sequential range scans.<br/><br/>"
            "<b>2. Transactions & ACID:</b><br/>"
            "• Atomicity (All or nothing - Recovery manager), Consistency (Integrity constraints preserved), Isolation (Concurrency control manager), Durability (Committed changes persist - Log-based recovery).<br/><br/>"
            "<b>3. Conflict Serializability & Precedence Graph:</b><br/>"
            "• Two operations conflict iff they belong to different transactions, access the SAME data item, and at least ONE is a WRITE.<br/>"
            "• Precedence Graph: Node for each transaction Ti. Directed edge Ti -> Tj if Ti executes an operation that conflicts with and precedes an operation of Tj.<br/>"
            "• A schedule is CONFLICT SERIALIZABLE iff its precedence graph contains NO CYCLES (DAG). Topological sort gives the equivalent serial schedule!<br/><br/>"
            "<b>4. Recoverability & Locking:</b><br/>"
            "• <b>Cascadeless Schedule:</b> Transaction Tj reads data item A only AFTER the transaction that wrote A has COMMITTED.<br/>"
            "• <b>Strict Schedule:</b> Transaction Tj neither reads nor writes data item A until the transaction that wrote A has committed.<br/>"
            "• <b>Two-Phase Locking (2PL):</b> Growing phase (acquire locks, release none) -> Shrinking phase (release locks, acquire none). Guarantees Conflict Serializability, but can suffer from DEADLOCK!"
        ),
        "callouts": [
            ("Strict 2PL Advantage", "Strict 2PL (holding all exclusive locks until commit) guarantees both Conflict Serializability AND Cascadeless / Recoverable schedules, preventing cascading aborts!", "tip"),
            ("Conflict vs View Serializability", "Every conflict serializable schedule is view serializable. The reverse is NOT true: view serializability without conflict serializability requires blind writes (writes without reading)!", "formula")
        ],
        "tables": []
    }
]

PRACTICE_QUESTIONS = [
    {
        "id": "DB-Q01",
        "type": "NAT",
        "marks": 2,
        "text": "A relation R(A, B, C, D, E) has the functional dependencies: F = { A -> B, BC -> D, E -> C, D -> A }. What is the total number of CANDIDATE KEYS of relation R?",
        "answer": "3",
        "explanation": "Attribute E never appears on the RHS of any FD, so E MUST be part of every candidate key.<br/>Let's test closures containing E:<br/>• (AE)+: A -> B => {A, B, E}. E -> C => {A, B, C, E}. BC -> D => {A, B, C, D, E}. All attributes! So AE is a candidate key.<br/>• (BCE)+: BC -> D => {B, C, D, E}. D -> A => {A, B, C, D, E}. So BCE is a super key. Since E is necessary, can BE or CE be key? (BE)+ = {B, E, C, D, A} = all attributes! Thus BE is a minimal candidate key (BCE is not minimal).<br/>• (DE)+: D -> A => {A, D, E}. A -> B => {A, B, D, E}. E -> C => {A, B, C, D, E}. All attributes! Thus DE is a candidate key.<br/>• Are there any others? Testing (CE)+: {C, E}. Cannot generate A, B, D.<br/>Therefore, the candidate keys are AE, BE, and DE. Exactly 3 candidate keys.",
        "is_pyq": True,
        "year": 2022,
        "difficulty": "GATE-Level"
    },
    {
        "id": "DB-Q02",
        "type": "NAT",
        "marks": 2,
        "text": "A B+ tree index is constructed on a search key of 12 bytes. Block size is 1024 bytes. Data record pointers are 8 bytes and block pointers are 6 bytes. What is the maximum order (number of block pointers) of an INTERNAL node in this B+ tree?",
        "answer": "57",
        "explanation": "For an internal node of order p, there are p block pointers and p - 1 search keys.<br/>Size constraint: p * (Block Pointer) + (p - 1) * (Key Size) ≤ Block Size.<br/>p * 6 + (p - 1) * 12 ≤ 1024<br/>6p + 12p - 12 ≤ 1024<br/>18p ≤ 1036<br/>p ≤ 1036 / 18 = 57.55.<br/>Since p must be an integer, max order p = 57.",
        "is_pyq": True,
        "year": 2020,
        "difficulty": "Medium"
    },
    {
        "id": "DB-Q03",
        "type": "MSQ",
        "marks": 2,
        "text": "Which of the following schedules is/are GUARANTEED to be CONFLICT SERIALIZABLE?",
        "options": {
            "A": "Any schedule generated by a Basic Two-Phase Locking (2PL) protocol",
            "B": "Any schedule whose precedence graph is acyclic",
            "C": "Any schedule that is free of deadlocks",
            "D": "Any schedule generated by Strict Two-Phase Locking (Strict 2PL)"
        },
        "answer": "A, B, D",
        "explanation": "• A: 2PL is mathematically proven to guarantee conflict serializability.<br/>• B: By definition, a schedule is conflict serializable iff its precedence graph is an acyclic directed graph (DAG).<br/>• C: Deadlock-free does NOT imply conflict serializable (e.g. an interleaved schedule without locks might not deadlock but could violate serializability).<br/>• D: Strict 2PL is a restricted form of 2PL, so it also strictly guarantees conflict serializability.<br/>Hence A, B, D are correct.",
        "is_pyq": False,
        "year": None,
        "difficulty": "GATE-Level"
    },
    {
        "id": "DB-Q04",
        "type": "MCQ",
        "marks": 1,
        "text": "In relational algebra, which of the following expressions is logically equivalent to the Natural Join of relations R(A, B) and S(B, C)?",
        "options": {
            "A": "σ_{R.B = S.B} (R x S)",
            "B": "π_{A, R.B, C} (σ_{R.B = S.B} (R x S))",
            "C": "π_{A, C} (σ_{R.B = S.B} (R x S))",
            "D": "R x S"
        },
        "answer": "B",
        "explanation": "Natural join first computes the Cartesian product (R x S), filters rows where the common attribute matches (σ_{R.B = S.B}), and then projects the attributes such that the common attribute B appears only ONCE (π_{A, R.B, C}). Thus option B is the exact definition.",
        "is_pyq": True,
        "year": 2018,
        "difficulty": "Easy"
    },
    {
        "id": "DB-Q05",
        "type": "MCQ",
        "marks": 1,
        "text": "Which normal form strictly forbids Transitive Dependencies on candidate keys for non-prime attributes?",
        "options": {
            "A": "First Normal Form (1NF)",
            "B": "Second Normal Form (2NF)",
            "C": "Third Normal Form (3NF)",
            "D": "Fourth Normal Form (4NF)"
        },
        "answer": "C",
        "explanation": "2NF forbids Partial Dependencies (Proper Subset of CK -> Non-Prime). 3NF forbids Transitive Dependencies (Non-Prime -> Non-Prime).",
        "is_pyq": True,
        "year": 2019,
        "difficulty": "Easy"
    }
]
