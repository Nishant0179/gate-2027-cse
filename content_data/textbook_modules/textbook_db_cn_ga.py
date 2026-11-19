# textbook_db_cn_ga.py
# Simple English, point-by-point study notes for Databases, Computer Networks, and General Aptitude.
# Written in crystal-clear, student-friendly language for GATE 2027 CSE aspirants.

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
            "title": "Real-Life Example 1: Hospital Blueprints vs Real Rooms (ER to Relational Tables)",
            "text": (
                "Before constructing a hospital, you sketch an architect's blueprint of Doctors, Patients, and Wards (ER Diagram).\n"
                "When building it, you pour real concrete rooms with ID numbers (Relational Tables).\n"
                "Because one Doctor treats many Patients (1:N relationship), you don't build a separate building: you simply write the Doctor's ID on each Patient's medical chart (Foreign Key placed on the N-side!)."
            )
        },
        {
            "title": "Real-Life Example 2: Slicing Vegetables (Selection σ vs Projection π)",
            "text": (
                "• Selection (σ): Filtering rows. Like picking only the red tomatoes from a vegetable basket and ignoring the potatoes (filters horizontally).\n"
                "• Projection (π): Slicing columns. Like taking a photo of a person's face only and cropping out their clothes and shoes (slices vertically)."
            )
        },
        {
            "title": "Real-Life Example 3: The Missing Exam Mark (SQL NULL Behaviour)",
            "text": (
                "In SQL, `NULL` does NOT mean zero, and it does NOT mean empty text. It means 'UNKNOWN / MISSING'.\n"
                "If a student's mark is NULL, is their mark greater than 50? The answer is UNKNOWN!\n"
                "In SQL three-valued logic, `NULL = NULL` is NOT True—it is UNKNOWN! That is why writing `WHERE mark = NULL` returns 0 rows; you must write `WHERE mark IS NULL`."
            )
        }
    ],
    "foundations": [
        {
            "number": "29.1",
            "title": "ER to Relational Table Conversion Rules",
            "content": (
                "How to convert ER relationships into minimal relational tables:<br/><br/>"
                "• <b>1:1 Relationship:</b><br/>"
                "&nbsp;&nbsp;- Combine into 2 tables by placing the primary key of either entity as a foreign key in the other.<br/>"
                "&nbsp;&nbsp;- If both entities have Total Participation, they can be merged into a <b>single table</b>.<br/><br/>"
                "• <b>1:N Relationship:</b><br/>"
                "&nbsp;&nbsp;- Combine into 2 tables.<br/>"
                "&nbsp;&nbsp;- The Foreign Key <b>ALWAYS goes to the 'N' (Many) side table</b>!<br/><br/>"
                "• <b>M:N Relationship:</b><br/>"
                "&nbsp;&nbsp;- CANNOT be merged into either entity table.<br/>"
                "&nbsp;&nbsp;- Strictly requires a <b>separate relationship table</b> containing the primary keys of both participating entities.<br/><br/>"
                "• <b>Weak Entity:</b><br/>"
                "&nbsp;&nbsp;- Always merged with its identifying relationship into 1 table."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: In a 1:N relationship, NEVER put the foreign key on the '1' side! It must go to the 'N' side to prevent duplicate rows or multi-valued attributes."
        },
        {
            "number": "29.2",
            "title": "Relational Algebra vs SQL Rules",
            "content": (
                "• <b>Duplicate Elimination:</b><br/>"
                "&nbsp;&nbsp;- Relational Algebra automatically eliminates duplicates (Set Semantics).<br/>"
                "&nbsp;&nbsp;- SQL keeps duplicates (Bag/Multiset Semantics) unless you write <code>DISTINCT</code>.<br/><br/>"
                "• <b>Aggregate Functions (SUM, AVG, MIN, MAX):</b><br/>"
                "&nbsp;&nbsp;- All aggregate functions <b>completely IGNORE NULL values</b>!<br/>"
                "&nbsp;&nbsp;- Exception: <code>COUNT(*)</code> counts all rows, including rows containing NULLs.<br/><br/>"
                "• <b>WHERE vs HAVING:</b><br/>"
                "&nbsp;&nbsp;- <code>WHERE</code> filters individual rows BEFORE grouping.<br/>"
                "&nbsp;&nbsp;- <code>HAVING</code> filters aggregated groups AFTER <code>GROUP BY</code>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Writing WHERE AVG(salary) > 50000 causes an SQL SYNTAX ERROR! Aggregate conditions MUST be placed inside the HAVING clause, never WHERE."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Finding Minimal Tables",
            "problem": "An ER diagram has 3 entities E1, E2, E3. E1 has a 1:N relationship with E2, and E2 has an M:N relationship with E3. No weak entities. What is the minimum number of relational tables needed?",
            "steps": [
                "Step 1: Entity E1 gets Table E1.",
                "Step 2: 1:N relationship between E1 and E2 is merged into Table E2 (with E1's primary key as foreign key).",
                "Step 3: Entity E3 gets Table E3.",
                "Step 4: M:N relationship between E2 and E3 CANNOT be merged; it requires a separate Table R.",
                "Step 5: Total tables = Table E1 + Table E2 + Table E3 + Table R = 4 tables."
            ],
            "answer": "Minimum relational tables = 4."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: NOT IN with NULL values",
            "warning": "If a subquery returns even one NULL value, `WHERE x NOT IN (subquery)` returns EMPTY SET (zero rows)! Because `x != NULL` evaluates to UNKNOWN, making the whole condition fail. Always use `NOT EXISTS` instead!"
        }
    ]
}

# DB Chapter 1: Normalization & Indexing
CHAPTERS_DB_CN_GA[("DB", 1)] = {
    "sub_id": "DB",
    "chap_idx": 1,
    "title": "Functional Dependencies, Normalization & B+ Trees",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Updating Your Home Address (Why Normalization Matters)",
            "text": (
                "Imagine a messy college spreadsheet where your home address is typed next to every single course you take.\n"
                "If you enroll in 6 courses, your address is repeated 6 times (Redundancy!). If you move house, the registrar must update 6 rows (Update Anomaly). If they miss one, your records contradict each other.\n"
                "Normalization separates Student Address into its own clean table so it is stored in exactly ONE place."
            )
        }
    ],
    "foundations": [
        {
            "number": "30.1",
            "title": "The Step-by-Step Normal Forms Checklist",
            "content": (
                "For every Functional Dependency <b>X → Y</b> in relation R:<br/><br/>"
                "• <b>1NF:</b> All attribute values must be atomic (no multi-valued sets or arrays).<br/><br/>"
                "• <b>2NF:</b> Relation is in 1NF AND contains <b>NO PARTIAL DEPENDENCIES</b>.<br/>"
                "&nbsp;&nbsp;- (No proper subset of Candidate Key can determine a non-prime attribute).<br/><br/>"
                "• <b>3NF:</b> Relation is in 2NF AND for every X → Y:<br/>"
                "&nbsp;&nbsp;- Either <b>X is a Superkey</b>, OR <b>Y is a Prime Attribute</b> (part of some Candidate Key).<br/><br/>"
                "• <b>BCNF (Boyce-Codd):</b> Strictly requires that for every X → Y:<br/>"
                "&nbsp;&nbsp;- <b>X MUST BE A SUPERKEY</b>!"
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Every relation with only 2 attributes is AUTOMATICALLY in BCNF! A decomposition into 3NF is always guaranteed to be both Lossless Join AND Dependency Preserving. A decomposition into BCNF is always Lossless Join, but might NOT preserve dependencies."
        },
        {
            "number": "30.2",
            "title": "B-Tree vs B+ Tree Core Properties",
            "content": (
                "In a B+ Tree of order p (maximum pointer capacity):<br/>"
                "• <b>Internal Nodes:</b> Store only search keys and child pointers (no data records!). Can hold up to <code>p</code> pointers and <code>p - 1</code> keys.<br/>"
                "• <b>Leaf Nodes:</b> Store ALL actual data pointers and keys, linked together as a <b>doubly linked list</b> for fast range queries.<br/><br/>"
                "• <b>Node Capacity Conditions:</b><br/>"
                "&nbsp;&nbsp;- Root node: At least 2 child pointers (if not leaf).<br/>"
                "&nbsp;&nbsp;- Internal / Leaf nodes: At least <b>⌈p / 2⌉</b> child pointers / keys."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: To calculate the order p of a B-tree node fitting in a disk block of B bytes with Key size K and Pointer size P: Equation is: p × P + (p - 1) × K ≤ B!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: B+ Tree Node Order",
            "problem": "Block size = 512 bytes, Key size = 8 bytes, Block Pointer size = 4 bytes. Find the maximum order p of an internal node.",
            "steps": [
                "Step 1: In an internal node of order p, there are p block pointers and (p - 1) keys.",
                "Step 2: Total size equation: p × (Block Pointer) + (p - 1) × (Key) ≤ Block Size.",
                "Step 3: Substitute values: p × 4 + (p - 1) × 8 ≤ 512.",
                "Step 4: 4p + 8p - 8 ≤ 512 ⇒ 12p ≤ 520 ⇒ p ≤ 520 / 12 = 43.33.",
                "Step 5: Since order p must be an integer: p = 43."
            ],
            "answer": "Maximum order p = 43."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Lossless Join Condition",
            "warning": "Decomposition of R into R1 and R2 is Lossless Join if and only if the common attributes (R1 ∩ R2) form a Superkey of AT LEAST ONE of the relations: (R1 ∩ R2) → R1 OR (R1 ∩ R2) → R2!"
        }
    ]
}

# DB Chapter 2: Transactions & Concurrency
CHAPTERS_DB_CN_GA[("DB", 2)] = {
    "sub_id": "DB",
    "chap_idx": 2,
    "title": "Transactions, Serializability & Two-Phase Locking (2PL)",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: ATM Cash Withdrawal (ACID Properties)",
            "text": (
                "• Atomicity (All or Nothing): If the ATM dispenses cash but the power cuts before debiting your bank balance, the whole transaction rolls back.\n"
                "• Consistency: Total money before and after transfer remains constant.\n"
                "• Isolation: If your spouse transfers money at the exact same second, transactions run isolated without interfering.\n"
                "• Durability: Once the transaction commits, a power blackout cannot erase the record."
            )
        }
    ],
    "foundations": [
        {
            "number": "31.1",
            "title": "Conflict Serializability & Precedence Graphs",
            "content": (
                "Two operations conflict if they: (1) belong to different transactions, (2) access the SAME data item, and (3) <b>AT LEAST ONE IS A WRITE</b>.<br/><br/>"
                "• <b>Testing Conflict Serializability:</b><br/>"
                "&nbsp;&nbsp;1. Draw a directed Precedence Graph with a node for each transaction Ti.<br/>"
                "&nbsp;&nbsp;2. Draw an edge <code>Ti → Tj</code> if an operation in Ti conflicts with and happens BEFORE an operation in Tj.<br/>"
                "&nbsp;&nbsp;3. <b>The schedule is Conflict Serializable IF AND ONLY IF the Precedence Graph has NO CYCLES!</b>"
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Every Conflict Serializable schedule is automatically View Serializable! But a View Serializable schedule with no blind writes is guaranteed to be Conflict Serializable."
        },
        {
            "number": "31.2",
            "title": "Two-Phase Locking (2PL)",
            "content": (
                "• <b>Basic 2PL:</b><br/>"
                "&nbsp;&nbsp;- Growing Phase: Can acquire locks, CANNOT release locks.<br/>"
                "&nbsp;&nbsp;- Shrinking Phase: Can release locks, CANNOT acquire new locks.<br/>"
                "&nbsp;&nbsp;- <b>Guarantees Conflict Serializability, but can STILL SUFFER FROM DEADLOCKS!</b><br/><br/>"
                "• <b>Strict 2PL:</b> All exclusive (write) locks held until COMMIT/ABORT. Prevents cascading rollbacks.<br/>"
                "• <b>Rigorous 2PL:</b> ALL locks (read and write) held until COMMIT/ABORT."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Basic 2PL is NOT deadlock-free! Two transactions can easily wait on each other's locks in basic 2PL."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Precedence Graph Cycle Check",
            "problem": "Check if Schedule S: r1(X); r2(Y); w1(Y); w2(X) is Conflict Serializable.",
            "steps": [
                "Step 1: Check pair r2(Y) and w1(Y): Both access Y, one is write. r2 is before w1 ⇒ Edge T2 → T1.",
                "Step 2: Check pair r1(X) and w2(X): Both access X, one is write. r1 is before w2 ⇒ Edge T1 → T2.",
                "Step 3: Graph has edges T2 → T1 and T1 → T2, forming a DIRECTED CYCLE: T1 ⇆ T2.",
                "Step 4: Because there is a cycle, schedule S is NOT conflict serializable."
            ],
            "answer": "Schedule is NOT Conflict Serializable."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Recoverability vs Cascadelessness",
            "warning": "Recoverable schedule: If Tj reads from Ti, Ti MUST commit BEFORE Tj commits! Cascadeless schedule: If Tj reads from Ti, Ti must commit BEFORE Tj even READS the data!"
        }
    ]
}

# =============================================================================
# COMPUTER NETWORKS (CN)
# =============================================================================

# CN Chapter 0: OSI Layers, Framing & Error Detection
CHAPTERS_DB_CN_GA[("CN", 0)] = {
    "sub_id": "CN",
    "chap_idx": 0,
    "title": "OSI/TCP-IP Layers, Framing & CRC",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Sending an International Gift (Layered Architecture)",
            "text": (
                "When sending a gift overseas:\n"
                "• Application: You choose the watch gift.\n"
                "• Presentation: Gift wrapping.\n"
                "• Transport: Tracking number & guarantee of delivery.\n"
                "• Network: Postal address with Country and Zip code (Routing).\n"
                "• Data Link: Local delivery van driving from warehouse to sorting hub (Hop-by-hop delivery).\n"
                "• Physical: The actual road asphalt and tires."
            )
        }
    ],
    "foundations": [
        {
            "number": "32.1",
            "title": "CRC (Cyclic Redundancy Check) Polynomial Division",
            "content": (
                "CRC uses binary modulo-2 arithmetic (XOR without carry):<br/><br/>"
                "• 1. If generator polynomial G(x) has degree <b>k</b>, append <b>k zeros</b> to the original data bitstring.<br/>"
                "• 2. Perform modulo-2 division of the padded data by G(x).<br/>"
                "• 3. The <b>k-bit remainder</b> is the CRC checksum.<br/>"
                "• 4. Transmitted frame = <code>Original Data + Remainder</code>.<br/>"
                "• 5. Receiver divides received frame by G(x): If remainder is 0, frame is error-free!"
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: If a generator polynomial G(x) has degree k, it ALWAYS appends exactly k parity bits! A polynomial detects all odd-bit errors if it has (x + 1) as a factor."
        },
        {
            "number": "32.2",
            "title": "Hamming Code Distance & Error Detection/Correction",
            "content": (
                "• <b>Hamming Distance (d):</b> Number of bit positions in which two codewords differ.<br/>"
                "• To detect <b>t</b> errors: Minimum distance <code>d_min ≥ t + 1</code>.<br/>"
                "• To correct <b>t</b> errors: Minimum distance <code>d_min ≥ 2t + 1</code>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: To correct single-bit errors (t = 1), d_min must be at least 2(1) + 1 = 3! Parity bit positions in Hamming code are powers of 2: 1, 2, 4, 8, 16..."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Hamming Distance Detection",
            "problem": "A code has minimum Hamming distance d_min = 5. How many bit errors can it detect, and how many can it correct?",
            "steps": [
                "Step 1: Formula for error detection: d_min ≥ t_detect + 1 ⇒ t_detect = d_min - 1.",
                "Step 2: Maximum detectable errors = 5 - 1 = 4 errors.",
                "Step 3: Formula for error correction: d_min ≥ 2 t_correct + 1 ⇒ 2 t_correct ≤ 5 - 1 = 4.",
                "Step 4: Maximum correctable errors = 4 / 2 = 2 errors."
            ],
            "answer": "Can detect up to 4 errors, can correct up to 2 errors."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Byte Stuffing / Flag Byte",
            "warning": "In byte stuffing, if the escape byte (ESC) or flag byte (FLAG) appears inside payload data, the sender inserts an extra ESC byte immediately before it."
        }
    ]
}

# CN Chapter 1: Flow & Congestion Control
CHAPTERS_DB_CN_GA[("CN", 1)] = {
    "sub_id": "CN",
    "chap_idx": 1,
    "title": "Flow Control Protocols & CSMA/CD",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Walkie-Talkie vs Phone Call (Stop-and-Wait vs Sliding Window)",
            "text": (
                "• Stop-and-Wait: Walkie-talkie. You say one sentence, say 'Over', and wait in dead silence until the other person replies 'Received, Over'. Most of the time is wasted waiting for replies!\n"
                "• Sliding Window: Phone call. You speak continuously without stopping, while the listener nods in the background. High efficiency!"
            )
        }
    ],
    "foundations": [
        {
            "number": "33.1",
            "title": "Sliding Window Protocol Efficiency Formulas",
            "content": (
                "Let <code>T_t = Packet Size / Bandwidth</code> (Transmission time), and <code>T_p = Distance / Speed</code> (Propagation time).<br/>"
                "Define <code>a = T_p / T_t</code>.<br/><br/>"
                "• <b>Stop-and-Wait Efficiency (η):</b><br/>"
                "&nbsp;&nbsp;<code>η = 1 / (1 + 2a)</code>.<br/><br/>"
                "• <b>Sliding Window with window size W:</b><br/>"
                "&nbsp;&nbsp;<code>η = min(1, W / (1 + 2a))</code>.<br/>"
                "&nbsp;&nbsp;Optimal window size for 100% efficiency: <b>W_opt = 1 + 2a</b>.<br/><br/>"
                "• <b>Window Sizes for n-bit sequence numbers:</b><br/>"
                "&nbsp;&nbsp;- Go-Back-N (GBN): Sender Window = <b>2^n - 1</b>, Receiver Window = <b>1</b>.<br/>"
                "&nbsp;&nbsp;- Selective Repeat (SR): Sender Window = <b>2^(n-1)</b>, Receiver Window = <b>2^(n-1)</b>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: In Selective Repeat, Sender Window + Receiver Window ≤ 2^n. If sender and receiver share equal window sizes, maximum window size is exactly 2^(n-1)!"
        },
        {
            "number": "33.2",
            "title": "CSMA/CD Minimum Frame Size",
            "content": (
                "In Ethernet CSMA/CD, a sender must keep transmitting long enough to detect a collision from the farthest end of the cable:<br/>"
                "• <b>Transmission Time ≥ 2 × Propagation Time</b>: <code>T_t ≥ 2 × T_p</code>.<br/>"
                "• <b>Minimum Frame Length:</b><br/>"
                "&nbsp;&nbsp;<code>Length_min = 2 × (Distance / Signal Speed) × Bandwidth</code>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: If bandwidth doubles, the minimum frame size MUST DOUBLE to keep collision detection working over the same cable length!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Minimum Frame Size in CSMA/CD",
            "problem": "A 10 Mbps Ethernet has a 1 km cable with signal speed 2 × 10^8 m/s. Find minimum frame size.",
            "steps": [
                "Step 1: Calculate T_p = Distance / Speed = 1000 m / (2 × 10^8 m/s) = 5 × 10^-6 s = 5 μs.",
                "Step 2: Condition for CSMA/CD: T_t ≥ 2 × T_p = 2 × 5 μs = 10 μs.",
                "Step 3: Minimum Frame Size = Bandwidth × T_t = 10 × 10^6 bps × 10 × 10^-6 s = 100 bits."
            ],
            "answer": "Minimum frame size = 100 bits."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Go-Back-N Retransmissions",
            "warning": "In GBN, if packet k is lost, ALL subsequent packets in the window (k+1, k+2...) are DISCARDED by the receiver and must be retransmitted by the sender!"
        }
    ]
}

# CN Chapter 2: Network Layer & Routing
CHAPTERS_DB_CN_GA[("CN", 2)] = {
    "sub_id": "CN",
    "chap_idx": 2,
    "title": "IPv4, Subnetting, Routing & Fragmentation",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Cutting a Huge Birthday Cake (IP Fragmentation)",
            "text": (
                "A bakery delivers a 1500 cm long cake, but your small doorway allows boxes of at most 500 cm (MTU: Maximum Transmission Unit).\n"
                "You slice the cake into three 500 cm boxes and attach labels: 'Box 1, Offset 0', 'Box 2, Offset 500', 'Box 3, Offset 1000'.\n"
                "In IPv4, Fragment Offset counts 8-byte chunks so the receiver can reconstruct the packet in the exact right order."
            )
        }
    ],
    "foundations": [
        {
            "number": "34.1",
            "title": "IPv4 Subnetting & Usable Hosts",
            "content": (
                "In CIDR notation <code>a.b.c.d / n</code>:<br/>"
                "• Network bits = <code>n</code>. Host bits = <code>32 - n</code>.<br/>"
                "• Total IP addresses in subnet = <code>2^(32 - n)</code>.<br/>"
                "• <b>Usable Host addresses = 2^(32 - n) - 2</b>.<br/>"
                "&nbsp;&nbsp;(Subtract 2: First address is Network ID; Last address is Direct Broadcast ID)."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: In a /30 subnet: 2^(32-30) = 4 IPs. Minus 2 = exactly 2 usable host addresses (ideal for point-to-point router links)!"
        },
        {
            "number": "34.2",
            "title": "Fragmentation Offset Calculation Rules",
            "content": (
                "• <b>Fragment Offset:</b> Offset field in IPv4 header is measured in units of <b>8 bytes</b>.<br/>"
                "&nbsp;&nbsp;<code>Offset = (Byte offset of data) / 8</code>.<br/>"
                "• <b>Data payload in each fragment (except last) MUST be a multiple of 8 bytes!</b><br/>"
                "• <b>MF (More Fragments) Flag:</b> 1 for all fragments EXCEPT the last fragment (which has MF = 0)."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: IP header size (typically 20 bytes) is subtracted from MTU first! If MTU = 1500 bytes: Max data per fragment = 1500 - 20 = 1480 bytes (which is a multiple of 8: 1480 / 8 = 185)."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Subnet Mask Calculation",
            "problem": "An organization needs 4 subnets, each supporting up to 50 hosts. Find the smallest CIDR subnet mask.",
            "steps": [
                "Step 1: For 50 hosts, find host bits h: 2^h - 2 ≥ 50 ⇒ 2^h ≥ 52 ⇒ h = 6 bits (2^6 - 2 = 62 hosts).",
                "Step 2: Subnet prefix length n = 32 - h = 32 - 6 = 26 bits.",
                "Step 3: Subnet mask in slash notation = /26 (in dotted decimal: 255.255.255.192)."
            ],
            "answer": "Subnet Mask = /26 (255.255.255.192)."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Count to Infinity Problem",
            "warning": "Distance Vector routing (RIP) uses Bellman-Ford and suffers from the Count-to-Infinity problem when a link breaks. Solved by Split Horizon and Poison Reverse."
        }
    ]
}

# CN Chapter 3: Transport & Application Layers
CHAPTERS_DB_CN_GA[("CN", 3)] = {
    "sub_id": "CN",
    "chap_idx": 3,
    "title": "TCP Congestion Control & Application Protocols",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Testing Ice on a Frozen Pond (TCP Congestion Control)",
            "text": (
                "• Slow Start: You step on the ice, take 1 step, then 2 steps, then 4 steps (doubling exponentially) to see if it holds.\n"
                "• Congestion Avoidance: Once you pass threshold (ssthresh), you slow down and advance carefully by 1 step per round (linear additive increase).\n"
                "• Multiplicative Decrease: If the ice cracks (packet loss), you panic and immediately cut your speed by half or reset to 1!"
            )
        }
    ],
    "foundations": [
        {
            "number": "35.1",
            "title": "TCP Congestion Window Phases",
            "content": (
                "• <b>1. Slow Start Phase (cwnd < ssthresh):</b><br/>"
                "&nbsp;&nbsp;- Window grows <b>EXPONENTIALLY</b>: Doubles every RTT (<code>cwnd = cwnd * 2</code>).<br/><br/>"
                "• <b>2. Congestion Avoidance Phase (cwnd ≥ ssthresh):</b><br/>"
                "&nbsp;&nbsp;- Window grows <b>LINEARLY</b>: Increases by 1 MSS every RTT (Additive Increase).<br/><br/>"
                "• <b>3. On Congestion Event:</b><br/>"
                "&nbsp;&nbsp;- <b>Timeout (severe congestion):</b> <code>ssthresh = cwnd / 2</code>, and <code>cwnd is RESET to 1 MSS</code>.<br/>"
                "&nbsp;&nbsp;- <b>3 Duplicate ACKs (mild congestion / Fast Recovery):</b> <code>ssthresh = cwnd / 2</code>, and <code>cwnd = ssthresh</code> (continues linear growth)."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: If cwnd is 32 KB and a TIMEOUT occurs: ssthresh becomes 32/2 = 16 KB, and cwnd resets to 1 KB! If 3 duplicate ACKs occur: cwnd drops to 16 KB directly without resetting to 1."
        },
        {
            "number": "35.2",
            "title": "Application Layer Protocols Summary",
            "content": (
                "• <b>DNS:</b> Port 53, uses <b>UDP</b> for fast queries; uses TCP for zone transfers.<br/>"
                "• <b>HTTP:</b> Port 80, TCP-based. Persistent HTTP/1.1 uses 1 RTT per connection.<br/>"
                "• <b>SMTP:</b> Port 25, TCP-based push protocol for sending emails.<br/>"
                "• <b>POP3 / IMAP:</b> Ports 110 / 143, TCP-based pull protocols for retrieving emails.<br/>"
                "• <b>FTP:</b> Uses 2 separate TCP connections: <b>Port 21 for Control</b>, <b>Port 20 for Data</b>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: FTP is an Out-of-Band protocol because it transmits commands on Port 21 and payload data on a completely separate connection on Port 20!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Tracing TCP Window Growth",
            "problem": "TCP starts with cwnd = 1 MSS, ssthresh = 8 MSS. How many RTTs are required for cwnd to reach 12 MSS if no packets are lost?",
            "steps": [
                "Step 1: Start RTT 0: cwnd = 1 MSS (Slow Start).",
                "Step 2: RTT 1: cwnd = 2 MSS.",
                "Step 3: RTT 2: cwnd = 4 MSS.",
                "Step 4: RTT 3: cwnd = 8 MSS (Hits ssthresh = 8! Switches to Congestion Avoidance / linear growth).",
                "Step 5: RTT 4: cwnd = 8 + 1 = 9 MSS.",
                "Step 6: RTT 5: cwnd = 10 MSS.",
                "Step 7: RTT 6: cwnd = 11 MSS.",
                "Step 8: RTT 7: cwnd = 12 MSS."
            ],
            "answer": "7 RTTs are required."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: TCP Header Size",
            "warning": "The minimum TCP header size is 20 bytes (when Options field is empty). The 4-bit Data Offset (header length) field is multiplied by 4 bytes, so maximum header size is 15 × 4 = 60 bytes!"
        }
    ]
}

# =============================================================================
# GENERAL APTITUDE (GA)
# =============================================================================

# GA Chapter 0: Quantitative Aptitude
CHAPTERS_DB_CN_GA[("GA", 0)] = {
    "sub_id": "GA",
    "chap_idx": 0,
    "title": "Quantitative Aptitude - Work, Speed, Ratios & Percentages",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The '50% + 50% Off' Diwali Sale Trick",
            "text": (
                "A store advertises 'Flat 50% + 50% Discount'. Is the item completely free (100% off)? Of course not!\n"
                "If a shirt costs ₹1000, first 50% off cuts it to ₹500. The second 50% off takes half of ₹500 = ₹250.\n"
                "Total discount is 75%, NOT 100%! Formula: Net Discount = x + y - (xy / 100)."
            )
        }
    ],
    "foundations": [
        {
            "number": "36.1",
            "title": "Time, Speed, Distance & Relative Speed",
            "content": (
                "• <b>Unit Conversion:</b> Multiply km/h by <b>5 / 18</b> to convert to m/s.<br/><br/>"
                "• <b>Relative Speed:</b><br/>"
                "&nbsp;&nbsp;- Opposite directions (moving towards each other): Relative Speed = <b>S1 + S2</b>.<br/>"
                "&nbsp;&nbsp;- Same direction (chasing): Relative Speed = <b>|S1 - S2|</b>.<br/><br/>"
                "• <b>Average Speed for equal distance covered at speeds S1 and S2:</b><br/>"
                "&nbsp;&nbsp;Average Speed = <b>(2 × S1 × S2) / (S1 + S2)</b> (Harmonic Mean, NOT arithmetic average!)."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: If a person travels to college at 60 km/h and returns at 40 km/h, the average speed is NOT 50 km/h! It is 2(60)(40)/(60+40) = 4800/100 = 48 km/h!"
        },
        {
            "number": "36.2",
            "title": "Time & Work (The 1-Day Work Method)",
            "content": (
                "• If Person A completes a work in D days, A's 1-day work = <b>1 / D</b>.<br/>"
                "• If A and B work together: Combined 1-day work = <code>(1 / D_A) + (1 / D_B)</code>.<br/>"
                "• <b>Total days needed together:</b> <code>(D_A × D_B) / (D_A + D_B)</code>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: You can also solve Time & Work by taking the LCM of individual days as total work units, turning fractions into simple integer additions!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Work Together Calculation",
            "problem": "A can finish a task in 12 days, and B can finish it in 24 days. How many days will they take working together?",
            "steps": [
                "Step 1: Take LCM of 12 and 24 = 24 total units of work.",
                "Step 2: A's efficiency = 24 / 12 = 2 units/day.",
                "Step 3: B's efficiency = 24 / 24 = 1 unit/day.",
                "Step 4: Combined efficiency = 2 + 1 = 3 units/day.",
                "Step 5: Total days = 24 units / 3 units/day = 8 days."
            ],
            "answer": "Time taken together = 8 days."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Successive Percentage Changes",
            "warning": "If a salary increases by 20% and then decreases by 20%, the net result is NOT zero! Formula: x + y + xy/100 = +20 - 20 - (20×20/100) = -4% net loss."
        }
    ]
}

# GA Chapter 1: Analytical & Spatial Reasoning
CHAPTERS_DB_CN_GA[("GA", 1)] = {
    "sub_id": "GA",
    "chap_idx": 1,
    "title": "Analytical & Spatial Reasoning - Blood Relations, Clocks & Cubes",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: Folding a Cardboard Box (Spatial Reasoning)",
            "text": (
                "When you unfold a cubic cardboard box into a 2D cross pattern, two faces that are separated by one intervening face can NEVER touch: they will become opposite faces when folded back up into a 3D cube."
            )
        }
    ],
    "foundations": [
        {
            "number": "37.1",
            "title": "Clock Angle Formula",
            "content": (
                "The angle θ between the Hour hand and Minute hand at H hours and M minutes is:<br/>"
                "• <b>θ = | 30 H - (11/2) M |</b>.<br/>"
                "• Speed of minute hand = 6° per minute.<br/>"
                "• Speed of hour hand = 0.5° per minute."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: If the calculated angle θ > 180°, subtract from 360° to find the smaller interior angle between the hands!"
        },
        {
            "number": "37.2",
            "title": "Painted Cube Slicing Formulas",
            "content": (
                "A large cube painted on all sides is cut into n × n × n small unit cubes:<br/>"
                "• <b>3 faces painted (Corners):</b> ALWAYS <b>8 cubes</b> (for any n ≥ 2).<br/>"
                "• <b>2 faces painted (Edges):</b> <b>12 × (n - 2)</b>.<br/>"
                "• <b>1 face painted (Surfaces):</b> <b>6 × (n - 2)^2</b>.<br/>"
                "• <b>0 faces painted (Interior core):</b> <b>(n - 2)^3</b>."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: Notice the multipliers 8, 12, 6, 1 correspond directly to the geometry of a cube: 8 corners, 12 edges, 6 faces, 1 core!"
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Angle Between Clock Hands",
            "problem": "Find the angle between hour hand and minute hand at 3:30.",
            "steps": [
                "Step 1: Use formula: θ = | 30 H - 5.5 M | with H = 3, M = 30.",
                "Step 2: 30 × 3 = 90.",
                "Step 3: 5.5 × 30 = 165.",
                "Step 4: θ = | 90 - 165 | = |-75| = 75°."
            ],
            "answer": "Angle at 3:30 = 75°."
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Leap Year Exception",
            "warning": "Century years are leap years ONLY if divisible by 400! For example, the year 2000 was a leap year, but 1900 was NOT a leap year."
        }
    ]
}

# GA Chapter 2: Verbal Aptitude
CHAPTERS_DB_CN_GA[("GA", 2)] = {
    "sub_id": "GA",
    "chap_idx": 2,
    "title": "Verbal Aptitude - Grammar, Concord & Critical Reasoning",
    "real_life_examples": [
        {
            "title": "Real-Life Example 1: The Team Captain Dilemma (Subject-Verb Agreement)",
            "text": (
                "Look at this sentence: 'The captain, along with all of his players, (is / are) arriving now.'\n"
                "Most students see 'players' (plural) and pick 'are'. That is INCORRECT!\n"
                "Phrases like 'along with', 'as well as', 'together with' are merely parenthetical descriptions. The true grammatical subject is 'The captain' (singular), so the correct verb is 'is'!"
            )
        }
    ],
    "foundations": [
        {
            "number": "38.1",
            "title": "Subject-Verb Agreement (Concord) Rules",
            "content": (
                "• <b>Singular Indefinite Pronouns:</b><br/>"
                "&nbsp;&nbsp;Words like <i>Everyone, Everybody, Neither, Either, Each, None</i> take a <b>SINGULAR VERB</b>.<br/>"
                "&nbsp;&nbsp;- Correct: 'Each of the students <b>is</b> ready' (NOT 'are ready').<br/><br/>"
                "• <b>Either... Or / Neither... Nor:</b><br/>"
                "&nbsp;&nbsp;The verb agrees with the <b>SUBJECT CLOSEST TO IT</b>!<br/>"
                "&nbsp;&nbsp;- 'Neither the teacher nor the students <b>were</b> present.'<br/>"
                "&nbsp;&nbsp;- 'Neither the students nor the teacher <b>was</b> present.'"
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: In 'Neither A nor B', the verb always matches B (the closest subject)!"
        },
        {
            "number": "38.2",
            "title": "Common Word Confusions in GATE",
            "content": (
                "• <b>Affect vs Effect:</b><br/>"
                "&nbsp;&nbsp;- <i>Affect</i> is usually a VERB (to influence: 'Smoking will affect your health').<br/>"
                "&nbsp;&nbsp;- <i>Effect</i> is usually a NOUN (a result: 'The effect was immediate').<br/><br/>"
                "• <b>Principal vs Principle:</b><br/>"
                "&nbsp;&nbsp;- <i>Principal:</i> College head / primary sum of money.<br/>"
                "&nbsp;&nbsp;- <i>Principle:</i> A fundamental rule or moral value."
            ),
            "crucial_rule": "GOLDEN RULE FOR GATE: In reading comprehension, never assume facts outside the passage! An inference is valid only if it is strictly entailed by the explicit sentences in the text."
        }
    ],
    "worked_examples": [
        {
            "title": "Step-by-Step Solved Problem: Grammar Correction",
            "problem": "Choose correct option: 'A bouquet of yellow roses (lend / lends) color to the room.'",
            "steps": [
                "Step 1: Identify the true grammatical subject.",
                "Step 2: 'of yellow roses' is a prepositional phrase modifying the noun.",
                "Step 3: The actual subject is 'A bouquet' (singular).",
                "Step 4: Singular subject requires a singular verb with 's': 'lends'."
            ],
            "answer": "Correct: 'A bouquet of yellow roses lends color to the room.'"
        }
    ],
    "exam_traps": [
        {
            "title": "GATE Trap: Dangling Modifiers",
            "warning": "In 'Walking into the room, the smoke was choking': The introductory participle 'Walking' accidentally modifies 'the smoke' (as if smoke was walking!). Correct: 'Walking into the room, I found the smoke choking.'"
        }
    ]
}
