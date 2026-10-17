# textbook_db_cn_ga.py
# In-depth Master Textbook Modules for Databases (DB), Computer Networks (CN), and General Aptitude (GA)
# Follows the exact pedagogical and visual architecture of User Images 2 & 3.

CHAPTERS_DB_CN_GA = {}

# =============================================================================
# DATABASES (DB)
# =============================================================================

# DB Chapter 0: ER-Model, Relational Algebra & SQL
CHAPTERS_DB_CN_GA[("DB", 0)] = {
    "sub_id": "DB",
    "chap_idx": 0,
    "title": "ER-Model, Relational Algebra & SQL",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Architect's Blueprints vs The Concrete Skyscraper (ER Model to Relational Schema)",
            "text": "Before building a 50-story hospital, architects sketch blueprints showing doctors, patients, and rooms (ER Diagram: Entities and Relationships). You don't live in the sketch! The construction crew pours concrete walls, numbered room slots, and patient ID wristbands into organized physical structures (Relational Tables with primary and foreign keys). If the ER blueprint has a 'Many-to-Many' relationship (Doctors treat many Patients, Patients see many Doctors), you MUST construct an intermediate hallway junction table (Cross-reference table) to prevent structural collapse."
        },
        {
            "title": "Real-Life Example 2: The Sieve vs The Cookie Cutter (Selection σ vs Projection π in Relational Algebra)",
            "text": "Imagine a basket of 100 apples of various colors and sizes. Selection (σ_color='red'(Apples)) acts like a sieve: it filters ROWS horizontally, keeping only the red apples and discarding green ones (all attributes preserved). Projection (π_weight(Apples)) acts like a cookie cutter: it slices COLUMNS vertically, extracting only the weight tag and discarding color, origin, and farmer names. Relational Algebra is the pure mathematical engine that SQL compiles down to."
        },
        {
            "title": "Real-Life Example 3: The Three-Valued Logic of an Unmarked Exam Paper (NULL Values in SQL)",
            "text": "In SQL, `NULL` does NOT mean 0, and it does NOT mean an empty string `\"\"`. `NULL` means 'Unknown / Missing'. If a student's marks are NULL, what does `marks > 50` evaluate to? It is neither True nor False: it evaluates to UNKNOWN! In SQL three-valued logic: `NOT(UNKNOWN)` is still `UNKNOWN`, and `NULL = NULL` is NOT True—it is UNKNOWN! This is why queries using `WHERE marks = NULL` return zero rows; you must write `WHERE marks IS NULL`."
        }
    ],
    "foundations": [
        {
            "number": "29.1",
            "title": "ER Model Constructs & Mapping to Relational Schema Rules",
            "content": (
                "• <b>Weak Entity:</b> Does not have a primary key; existence depends on identifying strong entity. Connected via double rectangle, identified by <b>Discriminator (Partial Key)</b> dashed underline.<br/>"
                "• <b>Cardinality Ratios & Table Reduction:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• <b>1:1 Relationship:</b> Can be merged into 2 tables, or 1 single table if total participation on both sides.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• <b>1:N Relationship:</b> Relationship table can be merged into the 'N' side table by placing primary key of '1' side as foreign key.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• <b>M:N Relationship:</b> CANNOT be merged! Requires a <b>separate relationship table</b> containing primary keys of both participating entities."
            ),
            "crucial_rule": "CRUCIAL RULE: In 1:N relationship mapping, the foreign key ALWAYS goes into the relation on the 'MANY' (N) side, NEVER into the '1' side!"
        },
        {
            "number": "29.2",
            "title": "Relational Algebra: Fundamental & Derived Operators",
            "content": (
                "• <b>Fundamental Operators (Turing Complete set):</b> Selection (σ), Projection (π), Union (∪), Set Difference (-), Cartesian Product (×), Rename (ρ).<br/>"
                "• <b>Derived Operators:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• Set Intersection (∩): R ∩ S = R - (R - S).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• Natural Join (⋈): Combines Cartesian product, selection on matching common attributes, and projection to remove duplicate columns.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• Division (÷): R ÷ S answers 'Find entities that relate to <b>ALL</b> elements in S'.<br/>"
                "• <b>Tuple Relational Calculus (TRC) & Domain Relational Calculus (DRC):</b> Declarative non-procedural query formalisms (Codd's Theorem: TRC, DRC, and Relational Algebra have equivalent expressive power)."
            ),
            "crucial_rule": "CRUCIAL RULE: Relational algebra automatically eliminates duplicate rows (Set Semantics). In contrast, SQL preserves duplicates by default (Bag/Multiset Semantics) unless `DISTINCT` is explicitly requested!"
        },
        {
            "number": "29.3",
            "title": "SQL Subqueries, Correlated Subqueries & Aggregations",
            "content": (
                "• <b>Correlated Subquery:</b> Inner query references columns of the outer query. Evaluated <b>ONCE FOR EVERY ROW</b> processed by the outer query (O(n²) performance).<br/>"
                "• <b>HAVING vs WHERE:</b> `WHERE` filters individual rows BEFORE grouping. `HAVING` filters aggregated groups AFTER `GROUP BY`.<br/>"
                "• <b>Set Operations in SQL:</b> `UNION`, `INTERSECT`, `EXCEPT` automatically eliminate duplicates. Use `UNION ALL` to retain duplicates.<br/>"
                "• <b>Self-Join:</b> Joining a table with itself; crucial for hierarchy traversal (e.g. Employee-Manager)."
            ),
            "crucial_rule": "CRUCIAL RULE: Aggregate functions (COUNT, SUM, AVG, MIN, MAX) IGNORE NULL values completely, EXCEPT for `COUNT(*)`, which counts all rows including those with NULLs!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Minimum Relational Tables for ER Schema",
            "problem": "An ER diagram has 3 strong entity sets E1, E2, E3, and 1 weak entity set W (identifying relationship R_w with E1). There is a 1:N relationship R1 between E1 and E2, and an M:N relationship R2 between E2 and E3. What is the minimum number of relational tables required?",
            "steps": [
                "Step 1: Entity E1 requires 1 table: Table(E1).",
                "Step 2: Weak entity W: Table(W) includes W's partial key + Primary Key of E1 as Foreign Key. Identifying relationship R_w is subsumed into Table(W). Total so far = 2 tables.",
                "Step 3: Relationship R1 (1:N between E1 and E2): Can be merged into the N-side (E2) table by placing E1's primary key into Table(E2). Total so far = 3 tables: Table(E1), Table(W), Table(E2).",
                "Step 4: Relationship R2 (M:N between E2 and E3): An M:N relationship MUST have its own independent table! Table(R2) stores PK(E2) and PK(E3).",
                "Step 5: Entity E3 requires 1 table: Table(E3).",
                "Step 6: Total tables = Table(E1) + Table(W) + Table(E2) + Table(E3) + Table(R2) = 5 tables."
            ],
            "answer": "Minimum number of tables = 5."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: NOT IN with NULL Subquery Return",
            "warning": "If the subquery inside `WHERE id NOT IN (SELECT id FROM ...)` returns even a SINGLE `NULL` value, the entire outer query returns ZERO ROWS! This happens because `id != NULL` evaluates to UNKNOWN, causing the entire AND condition to fail."
        }
    ]
}

# DB Chapter 1: Functional Dependencies & Normalization
CHAPTERS_DB_CN_GA[("DB", 1)] = {
    "sub_id": "DB",
    "chap_idx": 1,
    "title": "Functional Dependencies & Normalization (1NF to BCNF)",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Redundant Student College Roster (Update & Deletion Anomalies)",
            "text": "Imagine a university spreadsheet with 50,000 rows where every row repeats: Student Name, Course, Department Name, Department HOD, and HOD Mobile Number. If the Physics HOD changes their phone number, an administrative assistant must manually update 2,000 separate student rows (Update Anomaly). If they miss 3 rows, the database becomes corrupt. Even worse: if the last student drops out of Astronomy, deleting that row completely erases the Astronomy department's existence from the university! Normalization splits this monster into clean, decoupled tables."
        },
        {
            "title": "Real-Life Example 2: The Driving License Identity Key (Candidate Keys & Attribute Closure)",
            "text": "Your driving license number determines your Full Name, Blood Group, and Home Address. Does your Blood Group determine your Name? No! To find the Candidate Key of a relation, Attribute Closure (X+) starts with a seed attribute and cascades down all functional dependency dominoes. If X+ unlocks every single column in the entire table, X is a Superkey. If no subset of X can do that, X is crowned a minimal Candidate Key."
        },
        {
            "title": "Real-Life Example 3: The Broken LEGO Castle (Lossless Join vs Dependency Preserving)",
            "text": "When you disassemble a relational table into two smaller sub-tables, you must be able to snap them back together using Natural Join without creating 'ghost rows' (Lossless Decomposition). If joining Table 1 and Table 2 generates 100 fake students who never existed, the decomposition is Lossy and fatal. Furthermore, you want all database integrity constraints testable locally within each sub-table without expensive multi-table joins (Dependency Preservation)."
        }
    ],
    "foundations": [
        {
            "number": "30.1",
            "title": "Functional Dependencies, Armstrong's Axioms & Attribute Closure",
            "content": (
                "A functional dependency X → Y states that if two tuples agree on attributes X, they MUST agree on attributes Y.<br/>"
                "• <b>Armstrong's Axioms (Sound and Complete):</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;1. <b>Reflexivity:</b> If Y ⊆ X, then X → Y.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;2. <b>Augmentation:</b> If X → Y, then XZ → YZ.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;3. <b>Transitivity:</b> If X → Y and Y → Z, then X → Z.<br/>"
                "• <b>Canonical Cover (Minimal Cover):</b> Equivalent FD set where every RHS has exactly 1 attribute, no extraneous attributes on LHS, and no redundant FDs."
            ),
            "crucial_rule": "CRUCIAL RULE: Candidate Key Definition: K is a candidate key of R iff K+ = R (uniqueness) AND no proper subset K' ⊂ K satisfies K'+ = R (minimality)."
        },
        {
            "number": "30.2",
            "title": "Normal Forms Hierarchy: 1NF, 2NF, 3NF & BCNF",
            "content": (
                "• <b>1NF:</b> All attribute values are atomic (no repeating groups or arrays).<br/>"
                "• <b>2NF:</b> In 1NF and <b>NO PARTIAL DEPENDENCY</b> (no non-prime attribute depends on a proper subset of any candidate key).<br/>"
                "• <b>3NF:</b> In 2NF and <b>NO TRANSITIVE DEPENDENCY</b>. For every non-trivial FD X → A:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Either <b>X is a Superkey</b> OR <b>A is a Prime Attribute</b> (part of some candidate key).<br/>"
                "• <b>BCNF (Boyce-Codd):</b> Strictly for every non-trivial FD X → A:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;<b>X MUST BE A SUPERKEY</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: <b>BCNF ⊂ 3NF ⊂ 2NF ⊂ 1NF</b>. Any relation with strictly 2 attributes is ALWAYS in BCNF! A 3NF decomposition can ALWAYS achieve BOTH Lossless Join AND Dependency Preservation; a BCNF decomposition guarantees Lossless Join, but may NOT preserve dependencies!"
        },
        {
            "number": "30.3",
            "title": "Lossless Join Decomposition Testing Criterion",
            "content": (
                "Decomposing relation R into R1 and R2 is Lossless iff:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;<b>(R1 ∩ R2) → R1</b> &nbsp;OR&nbsp; <b>(R1 ∩ R2) → R2</b>.<br/>"
                "That is, the common attribute(s) MUST form a Superkey of at least one of the decomposed relations!"
            ),
            "crucial_rule": "CRUCIAL RULE: If (R1 ∩ R2)+ contains all attributes of R1, the decomposition is GUARANTEED LOSSLESS. If common attributes form a key of neither, it is LOSSY!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Highest Normal Form Identification",
            "problem": "Relation R(A, B, C, D) with FDs: { AB → C, C → D, D → A }. Determine: (1) Candidate Keys, and (2) Highest Normal Form of R.",
            "steps": [
                "Step 1: Compute candidate keys using attribute closure:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;B never appears on RHS, so B MUST be in every candidate key.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• (AB)+ = {A, B, C, D} ⇒ <b>AB is a Candidate Key</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• Since D → A, substitute D for A: (BD)+ = {B, D, A, C} ⇒ <b>BD is a Candidate Key</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• Since C → D, substitute C for D: (BC)+ = {B, C, D, A} ⇒ <b>BC is a Candidate Key</b>.<br/>"
                "Step 2: Candidate Keys = {AB, BC, BD}. Prime Attributes = {A, B, C, D}. All attributes are prime!",
                "Step 3: Check BCNF: In C → D, is C a superkey? (C)+ = {C, D, A} ≠ R. C is not a superkey. Fails BCNF!",
                "Step 4: Check 3NF: In C → D, D is a Prime Attribute (part of key BD). In D → A, A is a Prime Attribute (part of key AB). Since RHS of every non-superkey FD is a prime attribute, 3NF holds!"
            ],
            "answer": "Candidate Keys = {AB, BC, BD}. Highest Normal Form = 3NF."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Forgetting that Prime Attribute Can Save 3NF",
            "warning": "In 3NF, the condition is 'X is superkey OR A is prime'. Even if X is not a superkey, as long as A is part of ANY candidate key, the dependency DOES NOT violate 3NF!"
        }
    ]
}

# DB Chapter 2: B/B+ Trees & Transactions
CHAPTERS_DB_CN_GA[("DB", 2)] = {
    "sub_id": "DB",
    "chap_idx": 2,
    "title": "B/B+ Trees, Transactions & Concurrency Control",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Multi-Volume Encyclopedia Index (B+ Tree File Organization)",
            "text": "Imagine a 50-volume encyclopedia. The master index at the entrance tells you: 'Volume 1 holds A-C, Volume 2 holds D-G...' (Internal Router Nodes). These internal index cards do not contain encyclopedia articles: they only hold pointers directing you to the correct shelf. The actual rich articles reside exclusively on the shelf pages (Leaf Nodes). Furthermore, all shelf volumes are linked side-by-side with a physical rope (Leaf Level Doubly Linked List), allowing you to scan pages sequentially without climbing back up to the entrance catalog."
        },
        {
            "title": "Real-Life Example 2: The ATM Cash Withdrawal Transfer (ACID Properties)",
            "text": "You transfer ₹5,000 from Savings to Checking. If the server debits Savings, but the power plug is yanked out before crediting Checking, where is your ₹5,000? Atomicity (All-or-Nothing) guarantees the transaction rolls back as if nothing happened. Consistency preserves the total money invariant. Isolation guarantees that your spouse checking the balance from mobile banking doesn't see a phantom balance. Durability ensures that once 'Transfer Complete' flashes, no power outage can erase the record from the database log."
        },
        {
            "title": "Real-Life Example 3: The Two-Phase Traffic Light Corridor (Strict 2-Phase Locking - 2PL)",
            "text": "Strict 2PL divides life into two phases: Growing Phase (acquire locks, NEVER release any lock) and Shrinking Phase (release locks at commit/abort). It acts like a VIP presidential motorcade: security locks down every intersection ahead before the car moves. Once the motorcade clears the city and commits, all intersections are unlocked simultaneously. This guarantees Conflict Serializability and prevents Cascading Aborts."
        }
    ],
    "foundations": [
        {
            "number": "31.1",
            "title": "B-Tree vs B+ Tree Structural Properties & Node Capacities",
            "content": (
                "For a B+ Tree of order p (maximum child block pointers = p):<br/>"
                "• <b>Internal Node Structure:</b> Contains at most p child pointers and p - 1 search keys.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Size equation: <b>p × P_block + (p - 1) × Key_size ≤ Block_Size</b>.<br/>"
                "• <b>Leaf Node Structure:</b> Contains search keys, data/record pointers, and 1 sibling block pointer P_next.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Size equation: <b>m × (Key_size + P_record) + P_block ≤ Block_Size</b>.<br/>"
                "• <b>Differences:</b> In B-Trees, data pointers are stored in both internal and leaf nodes. In B+ Trees, data pointers reside <b>EXCLUSIVELY in Leaf Nodes</b>, allowing internal nodes to hold far more keys, maximizing fan-out and minimizing tree height."
            ),
            "crucial_rule": "CRUCIAL RULE: In B+ Trees of order p: Root has at least 2 children. Internal nodes have at least ⌈p/2⌉ children. Leaf nodes have at least ⌈(m)/2⌉ keys."
        },
        {
            "number": "31.2",
            "title": "Conflict Serializability & Precedence (Serialization) Graph",
            "content": (
                "Two operations in a schedule are in conflict if they belong to different transactions, access the SAME data item, and at least ONE operation is a <b>WRITE</b> (R-W, W-R, W-W).<br/>"
                "• <b>Precedence Graph Construction:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Create a node for each transaction Ti.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Draw directed edge Ti → Tj if Ti executes a conflicting operation BEFORE Tj executes its conflicting operation.<br/>"
                "• <b>Fundamental Theorem:</b> A schedule S is Conflict Serializable <b>IF AND ONLY IF its precedence graph contains NO CYCLES</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: If the precedence graph is a Directed Acyclic Graph (DAG), topological sorting of the graph yields the equivalent serial schedule ordering!"
        },
        {
            "number": "31.3",
            "title": "Recoverability & Cascading Rollback Classification",
            "content": (
                "• <b>Recoverable Schedule:</b> If Tj reads a value written by Ti (Dirty Read), Ti MUST COMMIT BEFORE Tj COMMITS.<br/>"
                "• <b>Cascadeless Schedule (Avoids Cascading Abort - ACA):</b> A transaction reads only COMMITTED data (no dirty reads allowed: Tj cannot read data until Ti commits).<br/>"
                "• <b>Strict Schedule:</b> No transaction can read OR write a data item until the previous transaction that wrote it commits or aborts.<br/>"
                "• <b>Venn Hierarchy:</b> <b>Strict ⊂ Cascadeless ⊂ Recoverable</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: If a schedule is Cascadeless, it is AUTOMATICALLY Recoverable! But a Recoverable schedule is NOT necessarily Cascadeless."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Calculating Maximum B+ Tree Internal Node Order",
            "problem": "A disk block size is 1024 bytes. Data record pointer size = 8 bytes, block pointer size = 6 bytes, and search key size = 14 bytes. Calculate the maximum order p of an internal node in this B+ tree.",
            "steps": [
                "Step 1: In an internal node of order p, there are p block pointers and (p - 1) search key values (no data record pointers stored in internal nodes!).",
                "Step 2: Formulate inequality: p × (Block Pointer Size) + (p - 1) × (Key Size) ≤ Block Size.",
                "Step 3: Substitute values: p × 6 + (p - 1) × 14 ≤ 1024.",
                "Step 4: Expand: 6p + 14p - 14 ≤ 1024 ⇒ 20p - 14 ≤ 1024 ⇒ 20p ≤ 1038.",
                "Step 5: Solve for p: p ≤ 1038 / 20 = 51.9.",
                "Step 6: Since p must be an integer, maximum order p = ⌊51.9⌋ = 51."
            ],
            "answer": "Maximum order of internal node p = 51."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: View Serializability vs Conflict Serializability",
            "warning": "Every Conflict Serializable schedule is View Serializable, but NOT vice versa! A View Serializable schedule that is NOT Conflict Serializable MUST contain Blind Writes (W(X) without preceding R(X))."
        }
    ]
}

# =============================================================================
# COMPUTER NETWORKS (CN)
# =============================================================================

# CN Chapter 0: Layering & Performance Metrics
CHAPTERS_DB_CN_GA[("CN", 0)] = {
    "sub_id": "CN",
    "chap_idx": 0,
    "title": "Layering, Switching & Network Performance Metrics",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Sending an International Courier Parcel (OSI / TCP/IP Layering)",
            "text": "When you mail a birthday gift overseas, you don't pilot the airplane yourself! The Application layer is writing your heartfelt birthday letter. The Presentation/Session layer translates it into English and seals it in an envelope. The Transport layer slaps on a tracking number (Port numbers & reliability). The Network layer prints the destination postal code and country (IP Address routing). The Data Link layer stamps the truck license plate (MAC address) for the first airport depot. The Physical layer is the highway asphalt and jet fuel."
        },
        {
            "title": "Real-Life Example 2: The High-Speed Train vs Slow Megaship (Bandwidth vs Latency)",
            "text": "Suppose you need to transport 10,000 tons of iron ore across the ocean. A bullet train carries 100 tons at 300 km/h (Low Latency, Low Bandwidth). A cargo ship carries 50,000 tons but moves at 25 km/h (High Latency, High Bandwidth). Bandwidth is the width of the pipe (bits per second); Propagation Delay is how fast light travels through glass (distance / velocity). A high-bandwidth satellite link can download a 4K movie in seconds, but playing competitive counter-strike online is unplayable due to 600 ms latency."
        },
        {
            "title": "Real-Life Example 3: The Highway Packet Pipeline (Bandwidth-Delay Product - BDP)",
            "text": "Imagine a 1,000-kilometer highway between Delhi and Mumbai with 4 lanes. If cars enter at 100 cars/minute, at any given moment there are 10,000 cars driving in transit on the road between the two cities! Bandwidth-Delay Product (BDP = Bandwidth × Propagation Delay) measures the 'volume of the pipe': the maximum number of unacknowledged bits that can be flying through the fiber optic cable simultaneously before the first bit hits the receiver's receiver."
        }
    ],
    "foundations": [
        {
            "number": "32.1",
            "title": "Network Latency Components: Transmission, Propagation, Queueing & Processing",
            "content": (
                "Total End-to-End Latency = <b>T_trans + T_prop + T_queue + T_proc</b>.<br/>"
                "• <b>Transmission Delay (T_trans):</b> Time to push packet bits onto the physical wire: <b>T_trans = L / B</b> (Packet Length L bits / Bandwidth B bps).<br/>"
                "• <b>Propagation Delay (T_prop):</b> Time for 1 bit to travel across physical distance: <b>T_prop = d / v</b> (Distance d / Propagation speed v ≈ 2 × 10^8 m/s in fiber).<br/>"
                "• <b>Queueing Delay:</b> Time packet waits in router memory buffer before transmission.<br/>"
                "• <b>Processing Delay:</b> Time router takes to inspect IP header, verify checksum, and consult routing table."
            ),
            "crucial_rule": "CRUCIAL RULE: Transmission delay depends strictly on Packet Size and Bandwidth (L / B). Propagation delay depends strictly on Distance and Cable Speed of Light (d / v). Bandwidth NEVER affects propagation speed!"
        },
        {
            "number": "32.2",
            "title": "Circuit Switching vs Packet Switching",
            "content": (
                "• <b>Circuit Switching (e.g. Traditional Landline Telecom):</b> Dedicated physical circuit reserved prior to call (Call Setup phase). Guaranteed bandwidth, zero congestion, zero queueing delay, but highly inefficient if link is idle.<br/>"
                "• <b>Packet Switching (e.g. The Internet):</b> Data split into packets. Dynamic statistical multiplexing.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Datagram Approach:</b> Packets routed independently; can arrive out-of-order.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Virtual Circuit Approach:</b> Logical connection established; all packets follow same route in order."
            ),
            "crucial_rule": "CRUCIAL RULE: In store-and-forward packet switching over N identical hops: Total time for M packets of size L over bandwidth B with propagation delay T_prop per hop = <b>(N + M - 1) × (L / B) + N × T_prop</b>."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Store-and-Forward Packet Switching Delay",
            "problem": "A 1 MB file is sent over a network of 3 router hops (4 links) with bandwidth 10 Mbps and link distance 1000 km per link (speed of light v = 2 × 10^8 m/s). The file is broken into 1000 packets of 1 KB each. Neglect header sizes and queueing delays. Find total transmission completion time.",
            "steps": [
                "Step 1: Convert units: Bandwidth B = 10 Mbps = 10 × 10^6 bps. Packet size L = 1 KB = 8000 bits (or 8192 bits). Using 1 KB = 8000 bits: T_trans = 8000 / 10^7 = 0.8 ms.",
                "Step 2: Propagation delay per link: T_prop = d / v = (1000 × 10^3 m) / (2 × 10^8 m/s) = 0.005 s = 5 ms.",
                "Step 3: Number of links N = 4, Number of packets M = 1000.",
                "Step 4: Pipelined packet transfer formula: Total Time = (N + M - 1) × T_trans + N × T_prop.",
                "Step 5: Compute: Total Time = (4 + 1000 - 1) × 0.8 ms + 4 × 5 ms = 1003 × 0.8 ms + 20 ms = 802.4 ms + 20 ms = 822.4 ms."
            ],
            "answer": "Total Completion Time = 822.4 milliseconds."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Confusing Bits vs Bytes in Bandwidth Calculations",
            "warning": "Network bandwidth is ALWAYS measured in bits per second (bps, Mbps, Gbps). File sizes are usually given in Bytes (MB, KB). You MUST multiply bytes by 8 before dividing by bandwidth!"
        }
    ]
}

# CN Chapter 1: Data Link Layer & MAC
CHAPTERS_DB_CN_GA[("CN", 1)] = {
    "sub_id": "CN",
    "chap_idx": 1,
    "title": "Data Link Layer, CRC & Medium Access Control (CSMA/CD)",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Cocktail Party Conversation Protocol (CSMA/CD & Backoff)",
            "text": "At a loud dinner party, guests want to talk over a shared medium (the room air). If you want to speak, you listen first: if someone else is talking, you stay quiet (Carrier Sense). If the room is quiet, you begin your story. But if you and another guest start talking at the exact same millisecond, your words collide into gibberish (Collision Detection). Both of you immediately shout 'Oops!' (Jamming signal), stop talking, roll a mental dice, and wait a random number of seconds (Binary Exponential Backoff) before trying again."
        },
        {
            "title": "Real-Life Example 2: The Two-Way Walkie-Talkie Over-and-Out (Stop-and-Wait vs Sliding Window)",
            "text": "In Stop-and-Wait, an army soldier says: 'Squad, move to the river, OVER' and stands frozen for 30 seconds waiting for the sergeant to reply: 'Copy that, ROGER'. Efficiency is terrible because the radio wire sits idle while waiting. In a Sliding Window protocol (Go-Back-N or Selective Repeat), the commander fires off 7 commands consecutively without waiting. As acknowledgments arrive back, the window slides forward continuously, keeping the radio channel 100% utilized."
        },
        {
            "title": "Real-Life Example 3: The Checksum Security Seal on a Shipping Container (Cyclic Redundancy Check - CRC)",
            "text": "A cargo ship seals a shipping container with a tamper-evident barcode. CRC treats the entire data file as one massive binary polynomial. It divides that polynomial by an agreed-upon generator polynomial using XOR binary arithmetic (modulo 2). The remainder is glued to the end of the packet. If even a single cosmic ray flips one bit during transit, the receiver's polynomial division fails to yield zero, and the packet is immediately rejected."
        }
    ],
    "foundations": [
        {
            "number": "33.1",
            "title": "Sliding Window Protocols: Stop-and-Wait, Go-Back-N (GBN) & Selective Repeat (SR)",
            "content": (
                "Define parameter <b>a = T_prop / T_trans</b>.<br/>"
                "• <b>Stop-and-Wait Efficiency:</b> <b>η = 1 / (1 + 2a)</b>.<br/>"
                "• <b>Sliding Window Efficiency:</b> <b>η = min(1, W / (1 + 2a))</b> (Optimal window W = 1 + 2a).<br/>"
                "• <b>Go-Back-N (GBN):</b> Sender window = 2^k - 1, Receiver window = 1. Uses cumulative ACKs. On packet loss, retransmits entire window of N packets.<br/>"
                "• <b>Selective Repeat (SR):</b> Sender window = 2^(k-1), Receiver window = 2^(k-1). Independent buffers. Retransmits ONLY the damaged packet."
            ),
            "crucial_rule": "CRUCIAL RULE: In Go-Back-N with k sequence bits, maximum sender window size = 2^k - 1 (Receiver window = 1). In Selective Repeat, maximum window size = 2^(k-1) to avoid sequence number overlap ambiguity!"
        },
        {
            "number": "33.2",
            "title": "CSMA/CD & Minimum Frame Size Condition",
            "content": (
                "For Ethernet CSMA/CD to detect collisions before finishing transmission:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;<b>T_trans ≥ 2 × T_prop</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;<b>(L_min / B) ≥ 2 × (d / v)</b> ⇒ <b>L_min ≥ 2 × (d / v) × B</b>.<br/>"
                "• <b>Binary Exponential Backoff:</b> After k collisions, pick random backoff slot r ∈ [0, 2^k - 1] (capped at k=10). After 16 collisions, packet is aborted."
            ),
            "crucial_rule": "CRUCIAL RULE: If a frame is smaller than L_min, a collision occurring at the far end of the cable will arrive back at the sender AFTER transmission has ended, leading to silent undetected packet corruption!"
        },
        {
            "number": "33.3",
            "title": "Cyclic Redundancy Check (CRC) Polynomial Division",
            "content": (
                "• Generator polynomial G(x) of degree r requires appending <b>r zeros</b> to the data bit string.<br/>"
                "• Division uses <b>Modulo-2 Binary Arithmetic (XOR subtraction)</b>.<br/>"
                "• The r-bit remainder replaces the r trailing zeros to form the transmitted codeword.<br/>"
                "• Receiver divides received codeword by G(x): remainder must be strictly 0."
            ),
            "crucial_rule": "CRUCIAL RULE: A CRC with generator polynomial of degree r appends exactly r CRC check bits, NOT r+1 bits!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: CSMA/CD Minimum Frame Size Calculation",
            "problem": "A 100 Mbps CSMA/CD Ethernet network has a maximum cable length of 1 km with signal propagation speed v = 2 × 10^8 m/s. What is the minimum frame size in bytes required for collision detection?",
            "steps": [
                "Step 1: Compute Propagation Delay: T_prop = d / v = 1000 m / (2 × 10^8 m/s) = 5 × 10^-6 seconds = 5 µs.",
                "Step 2: Two-way Round Trip Time (RTT): 2 × T_prop = 2 × 5 µs = 10 µs.",
                "Step 3: CSMA/CD condition: T_trans ≥ 2 × T_prop ⇒ L_min / B ≥ 10 µs.",
                "Step 4: Bandwidth B = 100 Mbps = 100 × 10^6 bps.",
                "Step 5: Minimum frame size L_min = 10 × 10^-6 s × 100 × 10^6 bps = 1000 bits.",
                "Step 6: Convert to bytes: 1000 / 8 = 125 Bytes."
            ],
            "answer": "Minimum frame size = 125 Bytes (1000 bits)."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Forgetting Round Trip Factor of 2 in CSMA/CD",
            "warning": "In CSMA/CD, the formula is T_trans ≥ 2 × T_prop (round-trip), NOT 1 × T_prop! The worst-case collision happens at the last millisecond right at the destination, and the collision signal must travel all the way back."
        }
    ]
}

# CN Chapter 2: Routing Protocols & IPv4
CHAPTERS_DB_CN_GA[("CN", 2)] = {
    "sub_id": "CN",
    "chap_idx": 2,
    "title": "Routing Protocols & IPv4 Addressing (CIDR, Fragmentation, NAT)",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Multi-Unit Apartment Mailbox (CIDR Subnetting)",
            "text": "Imagine an apartment building with postal address '192.168.1.0/24' (256 units). If the landlord rents floor 1 to medical clinics needing 64 offices (/26), floor 2 to law firms needing 32 offices (/27), and the top floor to small startups needing 16 offices (/28), Classless Inter-Domain Routing (CIDR) carves up the IP block into custom variable-length subnet masks (VLSM). The postal carrier reads only the prefix bits to drop the mailbag into the correct floor chute."
        },
        {
            "title": "Real-Life Example 2: The Giant Sofa Chopped for the Narrow Staircase (IPv4 Fragmentation)",
            "text": "You buy an 8-foot long sectional sofa, but your apartment staircase door (Maximum Transmission Unit - MTU) can only fit 3-foot boxes. You cannot push the 8-foot sofa through the door! The delivery team disassembles the sofa into three smaller numbered boxes with offset tags: Box 1 (Offset 0, More Fragments MF=1), Box 2 (Offset 375, MF=1), Box 3 (Offset 750, MF=0). In IPv4, routers chop packets exceeding link MTU into fragments, where Fragment Offset measures 8-byte blocks."
        },
        {
            "title": "Real-Life Example 3: The Rumor Mill Whispering Game (Distance Vector Routing & Count-to-Infinity)",
            "text": "In Distance Vector routing (RIP: Bellman-Ford), routers whisper to their direct neighbors every 30 seconds: 'I can reach London in 3 hops'. If the cable to London snaps, Router A tells B 'London is dead'. But B had previously heard from A that London was 3 hops, so B tells A: 'I can reach London in 4 hops!'. A believes B, updates to 5 hops, and tells B... both bounce the number back and forth to 6, 7, 8... up to infinity! Split Horizon and Poisoned Reverse prevent this toxic rumor cycle."
        }
    ],
    "foundations": [
        {
            "number": "34.1",
            "title": "IPv4 Header Fields, Fragmentation & Offset Rules",
            "content": (
                "IPv4 header size ranges from 20 bytes to 60 bytes (governed by 4-bit HLEN field in 4-byte units).<br/>"
                "• <b>Total Length:</b> 16-bit field (max IP packet = 65,535 bytes).<br/>"
                "• <b>Flags:</b> 3 bits [Reserved (0) | Don't Fragment (DF) | More Fragments (MF)].<br/>"
                "• <b>Fragment Offset:</b> 13 bits. Measures data offset in <b>units of 8 bytes (64 bits)</b>.<br/>"
                "• <b>Fragmentation Rule:</b> Fragment payload size MUST be a multiple of 8 (except for the last fragment)."
            ),
            "crucial_rule": "CRUCIAL RULE: Fragment Offset = (Payload Bytes prior to this fragment) / 8. If an exam problem gives offset = 100, the data payload starts at byte 100 × 8 = 800!"
        },
        {
            "number": "34.2",
            "title": "CIDR Subnetting, Supernetting & Longest Prefix Match",
            "content": (
                "• Subnet Mask /n: First n bits represent Network ID, remaining 32 - n bits represent Host ID.<br/>"
                "• Total usable host addresses in /n subnet = <b>2^(32 - n) - 2</b> (Network ID and Direct Broadcast Address subtracted).<br/>"
                "• <b>Longest Prefix Match:</b> When a router consults its forwarding table, if an IP matches multiple subnet entries, the packet is ALWAYS routed to the interface with the <b>LONGEST SUBNET MASK (most specific match)</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: In Longest Prefix Matching, if destination matches both `128.16.0.0/16` and `128.16.64.0/20`, the router ALWAYS forwards according to `/20` because it has the longer prefix length!"
        },
        {
            "number": "34.3",
            "title": "Routing Algorithms: Distance Vector (RIP) vs Link State (OSPF)",
            "content": (
                "• <b>Distance Vector (RIP):</b> Distributed Bellman-Ford. Exits routers share complete routing tables with immediate neighbors periodically. Suffers from <b>Count-to-Infinity</b>; solved by Split Horizon and Poison Reverse (Infinity = 16 hops).<br/>"
                "• <b>Link State (OSPF):</b> Uses Dijkstra's algorithm. Every router floods link state packets (LSP) across the entire network to build an identical global map of the topology. Faster convergence, zero loops."
            ),
            "crucial_rule": "CRUCIAL RULE: RIP runs on top of UDP (port 520). OSPF runs directly on top of IP (Protocol number 89). BGP runs on top of TCP (port 179)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: IPv4 Packet Fragmentation Trace",
            "problem": "An IPv4 datagram of 4000 bytes (including 20-byte IP header) arrives at a router whose outgoing MTU is 1500 bytes. Show the fragmentation details (Total Length, MF, Offset) for each fragment.",
            "steps": [
                "Step 1: Total Data Payload = 4000 - 20 = 3980 bytes.",
                "Step 2: MTU = 1500 bytes. Header per fragment = 20 bytes. Maximum payload per fragment = 1500 - 20 = 1480 bytes.",
                "Step 3: Check multiple of 8: 1480 / 8 = 185 (exact integer ✔).",
                "Step 4: Fragment 1: Payload = 1480 bytes. Total Length = 1480 + 20 = 1500. MF = 1. Offset = 0 / 8 = 0.",
                "Step 5: Fragment 2: Payload = 1480 bytes. Total Length = 1500. MF = 1. Offset = 1480 / 8 = 185.",
                "Step 6: Remaining data = 3980 - (1480 + 1480) = 3980 - 2960 = 1020 bytes.",
                "Step 7: Fragment 3: Payload = 1020 bytes. Total Length = 1020 + 20 = 1040. MF = 0 (last fragment). Offset = 2960 / 8 = 370."
            ],
            "answer": "Frag 1: Length=1500, MF=1, Offset=0 | Frag 2: Length=1500, MF=1, Offset=185 | Frag 3: Length=1040, MF=0, Offset=370."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Forgetting IP Header in MTU Calculation",
            "warning": "When dividing data by MTU, DO NOT divide the total datagram by MTU! You must subtract the 20-byte IP header from MTU first, then round down the payload to the nearest multiple of 8!"
        }
    ]
}

# CN Chapter 3: Transport Layer & Applications
CHAPTERS_DB_CN_GA[("CN", 3)] = {
    "sub_id": "CN",
    "chap_idx": 3,
    "title": "Transport Layer (TCP), Sockets & Application Protocols (DNS, HTTP)",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Three-Way Marriage Handshake (TCP 3-Way Handshake)",
            "text": "Before two diplomats exchange classified documents, they perform a rigorous handshake. Diplomat A says: 'I would like to speak, my sequence number is 5000' (SYN). Diplomat B replies: 'I hear you loud and clear on 5000; I acknowledge 5001, and my own sequence number is 8000' (SYN + ACK). Diplomat A concludes: 'I acknowledge your 8000 with 8001; connection established' (ACK). Data can now flow securely. Without this 3-way handshake, delayed ghost packets from old sessions would crash connections."
        },
        {
            "title": "Real-Life Example 2: The Squeezing Water Pipe (TCP Congestion Control - AIMD)",
            "text": "When TCP sends data across the internet, it doesn't know the capacity of intermediate routers. It starts with a tiny drip (Slow Start: Congestion Window doubles every RTT: 1, 2, 4, 8...). Once it hits a threshold (ssthresh), it switches to additive increase (Congestion Avoidance: +1 MSS per RTT). If a packet drops (congestion detected via 3 duplicate ACKs), it cuts its speed in HALF (Multiplicative Decrease: AIMD). This stabilizes the entire global internet."
        },
        {
            "title": "Real-Life Example 3: The Phonebook of the Entire Planet (DNS Hierarchy)",
            "text": "When you type `google.com` into your browser, computers only understand IP addresses like `142.250.190.46`. Your PC queries the Local DNS Server -> Root Server (`.`) -> Top-Level Domain TLD Server (`.com`) -> Authoritative DNS Server for `google.com`. The hierarchical tree resolves human names to binary IP coordinates in milliseconds using fast, lightweight UDP (port 53)."
        }
    ],
    "foundations": [
        {
            "number": "35.1",
            "title": "TCP Connection Management, 3-Way Handshake & Teardown",
            "content": (
                "• <b>3-Way Handshake:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;1. Client → Server: `SYN = 1, seq = x`.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;2. Server → Client: `SYN = 1, ACK = 1, seq = y, ack_seq = x + 1`.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;3. Client → Server: `ACK = 1, seq = x + 1, ack_seq = y + 1`.<br/>"
                "• <b>Connection Teardown (4-Way):</b> FIN, ACK, FIN, ACK.<br/>"
                "• <b>TIME_WAIT State:</b> Client waits for <b>2MSL (Maximum Segment Lifetime)</b> before closing to ensure final ACK was delivered and old duplicate segments die out in network."
            ),
            "crucial_rule": "CRUCIAL RULE: SYN and FIN packets CONSUME 1 SEQUENCE NUMBER in the sequence space, even though they carry zero bytes of user data! Plain ACKs consume 0 sequence numbers."
        },
        {
            "number": "35.2",
            "title": "TCP Congestion Control: Slow Start, Congestion Avoidance, Fast Retransmit & Fast Recovery",
            "content": (
                "• <b>Slow Start:</b> cwnd initialized to 1 MSS. On each ACK received, cwnd increases exponentially (doubles every RTT). Transitions to Congestion Avoidance when cwnd ≥ ssthresh.<br/>"
                "• <b>Congestion Avoidance:</b> cwnd increases linearly by <b>+1 MSS per RTT</b> (Additive Increase).<br/>"
                "• <b>Timeout (Severe Congestion):</b> ssthresh = cwnd / 2; <b>cwnd resets to 1 MSS</b>; enters Slow Start.<br/>"
                "• <b>3 Duplicate ACKs (Mild Congestion - Fast Retransmit & Fast Recovery):</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;ssthresh = cwnd / 2; <b>cwnd = ssthresh + 3</b> (TCP Reno skips resetting to 1!)."
            ),
            "crucial_rule": "CRUCIAL RULE: In TCP Tahoe, ANY packet loss resets cwnd to 1 MSS. In TCP Reno, 3 duplicate ACKs triggers Fast Recovery where cwnd drops to ssthresh (half), NOT 1 MSS!"
        },
        {
            "number": "35.3",
            "title": "Application Protocols: DNS, HTTP, SMTP & Port Numbers",
            "content": (
                "• <b>DNS (Port 53):</b> Uses UDP for queries (fast, low overhead); uses TCP for Zone Transfers between servers.<br/>"
                "• <b>HTTP (Port 80):</b> HTTP/1.0 uses non-persistent connections (new TCP handshake per image). HTTP/1.1 uses <b>Persistent Connections with Pipelining</b>.<br/>"
                "• <b>SMTP (Port 25):</b> Push protocol for sending email (TCP).<br/>"
                "• <b>POP3 (Port 110) & IMAP (Port 143):</b> Pull protocols for retrieving email from mailbox server."
            ),
            "crucial_rule": "CRUCIAL RULE: HTTP is a STATELESS protocol. To remember user shopping carts and logins, web applications use Cookies and Session Tokens."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: TCP Congestion Window Growth Trace",
            "problem": "TCP Reno starts Slow Start with cwnd = 1 MSS and ssthresh = 16 MSS. No packet loss occurs for 6 RTTs. Find the cwnd value after 6 RTTs.",
            "steps": [
                "Step 1: Start (RTT 0): cwnd = 1 MSS.",
                "Step 2: RTT 1: cwnd doubles ⇒ 2 MSS (Slow Start).",
                "Step 3: RTT 2: cwnd doubles ⇒ 4 MSS (Slow Start).",
                "Step 4: RTT 3: cwnd doubles ⇒ 8 MSS (Slow Start).",
                "Step 5: RTT 4: cwnd doubles ⇒ 16 MSS (Hits ssthresh = 16!). Enters Congestion Avoidance.",
                "Step 6: RTT 5: Linear increase (+1) ⇒ 16 + 1 = 17 MSS.",
                "Step 7: RTT 6: Linear increase (+1) ⇒ 17 + 1 = 18 MSS."
            ],
            "answer": "After 6 RTTs, cwnd = 18 MSS."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: TCP Window Wrapping & PAWS",
            "warning": "The TCP Sequence Number field is 32 bits. On a 10 Gbps fiber network, sequence numbers wrap around in just 3.4 seconds! Protection Against Wrapped Sequences (PAWS) uses timestamps to distinguish old wrapped packets."
        }
    ]
}

# =============================================================================
# GENERAL APTITUDE (GA)
# =============================================================================

# GA Chapter 0: Verbal Aptitude
CHAPTERS_DB_CN_GA[("GA", 0)] = {
    "sub_id": "GA",
    "chap_idx": 0,
    "title": "Verbal Aptitude - Grammar, Vocabulary & Comprehension",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Misunderstood Legal Will (Subject-Verb Agreement)",
            "text": "Consider the sentence: 'The director, along with all 100 department engineers, (was/were) present at the product launch'. Many people see '100 engineers' and pick 'were'. But in English grammar, parenthetical phrases introduced by 'along with', 'as well as', or 'accompanied by' do NOT modify the grammatical number of the subject. The true grammatical subject is 'The director' (singular), so the verb MUST be 'was'. In GATE, subject-verb agreement traps cost thousands of aspirants easy marks."
        },
        {
            "title": "Real-Life Example 2: The Ambiguous Billboard Headline (Dangling Modifiers)",
            "text": "A road sign reads: 'Walking into the bank, the heavy glass door struck Alice on the forehead'. Grammatically, this means the glass door was taking a pleasant stroll into the bank before it attacked Alice! Modifiers must attach directly to the noun performing the action: 'While Alice was walking into the bank, she was struck by the door'. Identifying dangling modifiers is a staple GATE verbal question."
        },
        {
            "title": "Real-Life Example 3: The Cryptic Word Roots (Etymology & Vocabulary Decoding)",
            "text": "When you encounter an unfamiliar word like 'Benevolent' on GATE, you don't panic if you know root words: 'Bene' means Good (Benefit, Benefactor), and 'Vol' means Wish/Will (Volunteer). So Benevolent = Wishing good upon others. Conversely, 'Malevolent' ('Mal' = Bad) = Wishing harm. Deciphering prefixes, roots, and suffixes unlocks thousands of vocabulary meanings effortlessly."
        }
    ],
    "foundations": [
        {
            "number": "36.1",
            "title": "Core English Grammar Rules & Subject-Verb Agreement",
            "content": (
                "• <b>Subject-Verb Rule:</b> Singular subjects take singular verbs; plural subjects take plural verbs.<br/>"
                "• <b>Neither/Either Rules:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• In 'Neither A nor B' and 'Either A or B', verb agrees with the <b>SUBJECT CLOSEST TO THE VERB</b>.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Example: 'Neither the teacher nor the students <b>were</b> ready.' vs 'Neither the students nor the teacher <b>was</b> ready.'<br/>"
                "• <b>Collective Nouns:</b> Words like 'Committee', 'Team', 'Jury' take singular verbs when acting as a unified body, but plural verbs when members act individually."
            ),
            "crucial_rule": "CRUCIAL RULE: Words like 'Each', 'Everyone', 'Neither of', 'Either of' are STRICTLY SINGULAR! 'Each of the candidates <b>has</b> submitted their application' (NOT 'have')."
        },
        {
            "number": "36.2",
            "title": "Tenses, Conditionals & Parallelism",
            "content": (
                "• <b>Conditional Sentences:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• Zero Conditional (Universal Truth): If + Present, Present.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• First Conditional (Real Future): If + Present, Will + Verb.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• Second Conditional (Hypothetical): If + Past, Would + Verb.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• Third Conditional (Past Regret): <b>If + Had + V3, Would Have + V3</b>.<br/>"
                "• <b>Parallelism Rule:</b> Items in a series must share identical grammatical form. Example: 'She likes hiking, swimming, and <b>to ride bikes</b>' is INCORRECT. Correct: '...and biking'."
            ),
            "crucial_rule": "CRUCIAL RULE: In Third Conditional: 'If he had studied hard, he would have cleared GATE.' Never write 'If he would have studied'!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Sentence Correction Trace",
            "problem": "Select the grammatically correct sentence:\n(A) One of the students who has participated in the contest are winning.\n(B) One of the students who have participated in the contest is winning.\n(C) One of the students who has participated in the contest is winning.\n(D) One of the students who have participated in the contest are winning.",
            "steps": [
                "Step 1: Analyze relative clause: 'students who have/has participated'. The relative pronoun 'who' refers to its antecedent 'students' (plural). Therefore, the relative clause verb must be plural: 'who have participated'.",
                "Step 2: Eliminate options (A) and (C) which use 'who has'.",
                "Step 3: Analyze main sentence subject: 'One of the students... is/are winning'. The subject is 'One' (singular). Therefore, main verb must be singular: 'is winning'.",
                "Step 4: Option (B) correctly combines 'who have participated' with main verb 'is winning'."
            ],
            "answer": "Correct Sentence is (B)."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Confusing Complement vs Compliment",
            "warning": "'Compliment' is praise ('She gave me a nice compliment'). 'Complement' is something that completes ('Wine complements cheese'). GATE verbal loves testing homophones."
        }
    ]
}

# GA Chapter 1: Quantitative Aptitude
CHAPTERS_DB_CN_GA[("GA", 1)] = {
    "sub_id": "GA",
    "chap_idx": 1,
    "title": "Quantitative Aptitude - Arithmetic, Algebra & Mensuration",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Escalator Walk Up (Relative Speed & Time-Distance)",
            "text": "You are late for a train at the metro station. The moving escalator carries people up at 1 meter/second. If you stand still, it takes 60 seconds to reach the top. If you run up the escalator at 2 m/s, your relative speed adds to the escalator: (2 + 1) = 3 m/s, rocketing you to the top in just 20 seconds! But if you foolishly try running DOWN an UP escalator, your net velocity is (2 - 1) = 1 m/s upwards. Relative velocity explains trains, boats, streams, and escalators."
        },
        {
            "title": "Real-Life Example 2: The Two Workers Painting a House (Time and Work Efficiencies)",
            "text": "Alice can paint a house in 10 days (Efficiency: 1/10 house per day = 10% daily). Bob can paint the same house in 15 days (Efficiency: 1/15 house per day = 6.67% daily). When they work together as a team, their efficiencies add directly: (1/10 + 1/15) = (3 + 2)/30 = 5/30 = 1/6 house per day! Working together, the entire house is painted in exactly 6 days."
        },
        {
            "title": "Real-Life Example 3: The Retail End-of-Season Sale Trap (Successive Percentages)",
            "text": "A clothing store advertises: 'Mega Diwali Clearance: 50% Flat Off PLUS Extra 50% Off!'. Does that mean the clothes are 100% Free? Absolutely not! The first 50% off cuts a ₹2,000 shirt down to ₹1,000. The second 50% discount applies ONLY to the remaining ₹1,000, bringing the price to ₹500. The true combined discount is 75%, NOT 100%. Successive percentages follow the golden formula: Net = A + B + (AB / 100)."
        }
    ],
    "foundations": [
        {
            "number": "37.1",
            "title": "Percentages, Profit & Loss, Simple & Compound Interest",
            "content": (
                "• <b>Successive Percentage Change:</b> Net change = <b>[ a + b + (ab / 100) ]%</b>.<br/>"
                "• <b>Profit & Loss:</b> Profit% = (Profit / CP) × 100 | Loss% = (Loss / CP) × 100 (ALWAYS calculated on Cost Price CP!).<br/>"
                "• <b>Simple Interest:</b> SI = (P × R × T) / 100.<br/>"
                "• <b>Compound Interest:</b> Amount A = P (1 + R/100)^T. Difference between CI and SI for 2 years: <b>Diff = P (R / 100)²</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: If price of an item increases by R%, consumption must decrease by <b>[ R / (100 + R) ] × 100%</b> to keep total expenditure constant!"
        },
        {
            "number": "37.2",
            "title": "Time, Speed, Distance & Boats and Streams",
            "content": (
                "• <b>Average Speed:</b> Total Distance / Total Time. (For equal distances covered at speeds v1 and v2: <b>v_avg = 2 v1 v2 / (v1 + v2)</b>).<br/>"
                "• <b>Relative Speed:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Opposite directions: Speeds ADD (v1 + v2).<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Same direction: Speeds SUBTRACT (|v1 - v2|).<br/>"
                "• <b>Boats and Streams:</b> Downstream speed = u + v; Upstream speed = u - v (where u = boat speed in still water, v = stream speed)."
            ),
            "crucial_rule": "CRUCIAL RULE: Speed of boat in still water u = (Downstream + Upstream) / 2. Speed of stream v = (Downstream - Upstream) / 2."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Time and Work Alternate Days",
            "problem": "A can finish a task in 12 days, and B can finish it in 18 days. They work on alternate days starting with A on day 1. In how many days will the entire work be completed?",
            "steps": [
                "Step 1: Find total work using LCM of (12, 18): LCM = 36 units.",
                "Step 2: Calculate daily efficiencies:<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Efficiency of A = 36 / 12 = 3 units/day.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;Efficiency of B = 36 / 18 = 2 units/day.",
                "Step 3: In 1 cycle of 2 days (Day 1: A, Day 2: B), work completed = 3 + 2 = 5 units.",
                "Step 4: Number of complete 2-day cycles to reach near 36 units: 36 / 5 = 7 cycles (remainder 1 unit).",
                "Step 5: Work in 7 cycles (14 days) = 7 × 5 = 35 units. Remaining work = 36 - 35 = 1 unit.",
                "Step 6: Day 15 is A's turn. A finishes 3 units per day, so A completes the remaining 1 unit in 1/3 of a day.",
                "Step 7: Total time = 14 + 1/3 = 14.33 days (or 14 days and 8 hours)."
            ],
            "answer": "Total time = 14 1/3 days (14.33 days)."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Average Speed Harmonic Mean Misconception",
            "warning": "Average speed is (v1 + v2) / 2 ONLY if time intervals are equal! If DISTANCES are equal, average speed is strictly the harmonic mean: 2v1v2 / (v1 + v2)."
        }
    ]
}

# GA Chapter 2: Analytical & Spatial Aptitude
CHAPTERS_DB_CN_GA[("GA", 2)] = {
    "sub_id": "GA",
    "chap_idx": 2,
    "title": "Analytical & Spatial Aptitude - Logic, Reasoning & 2D/3D Shapes",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Origami Crane Fold (Paper Folding & Punching)",
            "text": "Origami transforms a flat sheet of paper into a 3D crane through folding. In GATE Spatial Aptitude, a square paper is folded in half, folded into a quarter, and a circular hole is punched through the folded corner. When unfolded, the crease lines act as mirror reflection axes: 1 punched hole in a 4-fold paper mirrors symmetrically across horizontal and vertical axes to produce 4 holes in the final unfolded sheet."
        },
        {
            "title": "Real-Life Example 2: The Flat-Pack IKEA Cardboard Box (Cube Nets & 3D Assembly)",
            "text": "When you buy an IKEA dresser, the cardboard packaging arrives flat with 6 connected square flaps (Cube Net). When you fold the flaps along the creases to assemble the 3D box, which sides end up opposite to each other? The Golden Cube Net Rule states: In any straight strip of squares, alternate faces (separated by exactly 1 intervening square) are ALWAYS OPPOSITE in the folded 3D cube!"
        },
        {
            "title": "Real-Life Example 3: The Blood Relation Family Tree Detective",
            "text": "A detective reads a statement: 'Pointing to a photograph, John said: His mother is the only daughter of my mother'. Who is in the photo? Work backwards from 'My mother': 'Only daughter of my mother' is John's sister. 'His mother is John's sister'. Therefore, the boy in the photo is John's nephew! Drawing structured hierarchical family trees with standard symbols (circles for females, squares for males) makes complex blood relations trivial."
        }
    ],
    "foundations": [
        {
            "number": "38.1",
            "title": "Syllogisms, Venn Diagrams & Logical Deductions",
            "content": (
                "• <b>Syllogism Quantifiers:</b><br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• 'All A are B' (A ⊆ B): Universal Positive.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• 'No A is B' (A ∩ B = ∅): Universal Negative.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• 'Some A are B' (A ∩ B ≠ ∅): Particular Positive.<br/>"
                "&nbsp;&nbsp;&nbsp;&nbsp;• 'Some A are not B' (A - B ≠ ∅): Particular Negative.<br/>"
                "• <b>Validity Rule:</b> A conclusion is valid IF AND ONLY IF it holds true across <b>ALL POSSIBLE VENN DIAGRAM INTERPRETATIONS</b>. If even one valid Venn diagram violates the conclusion, it is FALSE."
            ),
            "crucial_rule": "CRUCIAL RULE: Complementary Pairs (Either-Or): 'Some A are B' and 'No A is B' form a complementary pair: if neither conclusion follows definitively, the answer is 'Either 1 or 2 follows'!"
        },
        {
            "number": "38.2",
            "title": "Spatial Aptitude: 2D Transformations, Reflections, Paper Folding & Cube Nets",
            "content": (
                "• <b>Mirror Image:</b> Left and right are reversed; top and bottom remain unchanged.<br/>"
                "• <b>Water Image:</b> Top and bottom are inverted; left and right remain unchanged.<br/>"
                "• <b>2D Rotation:</b> Clockwise vs Counter-Clockwise rotation by 90°, 180°, 270°.<br/>"
                "• <b>Opposite Faces in a Cube Net:</b> In any linear run of 3 or more squares, <b>faces separated by one square are mutually opposite</b>."
            ),
            "crucial_rule": "CRUCIAL RULE: In a folded cube, two OPPOSITE faces can NEVER appear adjacent to each other! If an option shows two opposite faces sharing an edge, eliminate that option immediately."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Worked Exam Problem: Cube Net Opposite Face Identification",
            "problem": "A standard dice net has a vertical strip of 4 squares: [1, 2, 3, 4] from top to bottom, with square 5 attached to the left of 2, and square 6 attached to the right of 3. Which faces are opposite to each other?",
            "steps": [
                "Step 1: In the vertical strip [1, 2, 3, 4], alternate faces are opposite:",
                "&nbsp;&nbsp;&nbsp;&nbsp;• Face 1 is opposite to Face 3 (separated by face 2).",
                "&nbsp;&nbsp;&nbsp;&nbsp;• Face 2 is opposite to Face 4 (separated by face 3).",
                "Step 2: The two remaining flaps sticking out on opposite sides must fold to be opposite:",
                "&nbsp;&nbsp;&nbsp;&nbsp;• Face 5 (left flap) is opposite to Face 6 (right flap)."
            ],
            "answer": "Opposite face pairs: (1, 3), (2, 4), and (5, 6)."
        }
    ],
    "exam_traps": [
        {
            "title": "Exam Trap 1: Assuming 'Some' Means 'Some but not all'",
            "warning": "In formal logic, 'Some' means 'AT LEAST ONE, and possibly all'! If 'All dogs are animals' is true, then 'Some dogs are animals' is mathematically 100% TRUE!"
        }
    ]
}
