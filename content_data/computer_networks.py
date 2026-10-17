# Computer Networks Content Module for GATE 2027 CSE
# Weightage: 8-10 Marks (IIT Madras GATE 2027 Streamlined Syllabus)

SUBJECT_META = {
    "id": "CN",
    "name": "Computer Networks",
    "folder": "10_Computer_Networks",
    "weightage": "9 Marks",
    "topics": [
        "Principles of Layering; Basics of switching (circuit, packet and virtual circuit) and performance metrics",
        "Data link layer: error detection, Medium Access Control, Ethernet",
        "Routing: Distance vector and link state routing",
        "IPv4: Fragmentation, CIDR Notation, Network Address Translation (NAT)",
        "TCP: Flow control, congestion control, socket API; Application protocols: DNS and HTTP"
    ]
}

CHAPTERS = [
    {
        "title": "Layering, Switching & Network Performance Metrics",
        "hinglish": "Networks me delays (Transmission delay Tt = L/B vs Propagation delay Tp = d/v) aur Bandwidth-Delay Product (BDP) calculate karne ke numericals basic foundations hain.",
        "theory": (
            "<b>1. Principles of Layering & Protocols:</b><br/>"
            "• <b>Layering:</b> Divides complex network tasks into independent hierarchical modules. Each layer provides services to the layer above and consumes services from the layer below.<br/>"
            "• <b>Encapsulation & Decapsulation:</b> Headers (and trailers at Data Link layer) are added as data travels down the stack and stripped as it travels up.<br/><br/>"
            "<b>2. Switching Techniques:</b><br/>"
            "• <b>Circuit Switching:</b> Dedicated end-to-end path established before communication (e.g. traditional telephone network). Guarantees bandwidth and zero queuing delay, but wastes bandwidth during idle periods.<br/>"
            "• <b>Packet Switching (Datagram):</b> Packets routed independently based on destination address. Optimal bandwidth utilization, statistical multiplexing, but variable queuing delay and packet reordering.<br/>"
            "• <b>Virtual Circuit Switching:</b> Logical connection established; packets follow predefined path carrying Virtual Circuit Identifier (VCI). In-order delivery guaranteed.<br/><br/>"
            "<b>3. Performance Metrics & Delay Formulas:</b><br/>"
            "• <b>Transmission Delay (T_t):</b> Time to push all packet bits onto the link. T_t = Length of packet (L bits) / Bandwidth (B bps).<br/>"
            "• <b>Propagation Delay (T_p):</b> Time for a bit to travel through the physical medium. T_p = Distance (d meters) / Propagation Speed (v m/s).<br/>"
            "• <b>Total Latency:</b> Latency = T_t + T_p + Queuing Delay + Processing Delay.<br/>"
            "• <b>Bandwidth-Delay Product (BDP):</b> BDP = Bandwidth * T_p bits (represents maximum number of in-flight bits that can fill the transmission pipe)."
        ),
        "callouts": [
            ("Tt vs Tp Distinction", "Transmission Delay T_t depends ONLY on packet size and bandwidth (independent of distance). Propagation Delay T_p depends ONLY on distance and signal velocity (independent of packet size or bandwidth)!", "formula"),
            ("BDP Round Trip Capacity", "If window-based protocol utilizes full channel without waiting, sender window size must equal 1 + 2a (where a = T_p / T_t)!", "tip")
        ],
        "tables": []
    },
    {
        "title": "Data Link Layer, CRC & Medium Access Control (CSMA/CD)",
        "hinglish": "CRC calculation (polynomial modulo-2 division) aur CSMA/CD me collision detection ke liye minimum frame size L ≥ 2 * B * Tp standard formula hai.",
        "theory": (
            "<b>1. Error Detection - Cyclic Redundancy Check (CRC):</b><br/>"
            "• Generator polynomial G(x) of degree r: Append r zeros to data bits D.<br/>"
            "• Perform Modulo-2 binary division (XOR operation without carry). Remainder R (r bits) is appended to D as transmitted codeword.<br/>"
            "• Receiver divides received codeword by G(x); if remainder is ZERO -> No error detected!<br/>"
            "• Error Detection Capabilities of CRC: Detects all single-bit errors, all double-bit errors (if G(x) has factor of at least 3 terms), all odd-number bit errors (if G(x) has (x+1) as factor), and all burst errors of length ≤ r.<br/><br/>"
            "<b>2. Medium Access Control (MAC):</b><br/>"
            "• <b>Pure ALOHA:</b> Vulnerable time = 2 * T_fr. Maximum Efficiency = 1 / (2e) ≈ 18.4%.<br/>"
            "• <b>Slotted ALOHA:</b> Vulnerable time = 1 * T_fr. Maximum Efficiency = 1 / e ≈ 36.8%.<br/>"
            "• <b>CSMA/CD (Carrier Sense Multiple Access with Collision Detection):</b><br/>"
            "  - Rule: Listen before talking; listen while talking.<br/>"
            "  - Collision condition: Transmission time T_t must be at least twice propagation delay T_p to ensure sender detects collision before finishing transmission!<br/>"
            "  - <b>Minimum Frame Size Formula:</b> L_min ≥ 2 * Bandwidth * T_p = 2 * B * (Distance / Velocity).<br/>"
            "  - Efficiency of CSMA/CD = 1 / (1 + 6.44a) or 1 / (1 + 5a) where a = T_p / T_t.<br/>"
            "  - Binary Exponential Backoff: After k-th collision, wait random time r * 2*T_p where r ∈ [0, 2^k - 1] (capped at k = 10, abort after 16 collisions)."
        ),
        "callouts": [
            ("CSMA/CD Minimum Length Rule", "If sender finishes transmitting before the collision signal returns (i.e. T_t &lt; 2 T_p), it will falsely assume successful delivery! Hence L_min = 2 * B * T_p is strictly mandatory.", "warn"),
            ("CRC Degree & Zero Padding", "If generator polynomial G(x) is x^3 + x + 1, its degree is 3 (binary 1011). You must append exactly 3 zeros to the data payload!", "tip")
        ],
        "tables": []
    },
    {
        "title": "Routing Protocols & IPv4 Addressing (CIDR, Fragmentation, NAT)",
        "hinglish": "Distance Vector me Count-to-Infinity problem and Split Horizon, Link State me Dijkstra, aur IPv4 header me Fragmentation fields (Offset, MF) par direct questions aate hain.",
        "theory": (
            "<b>1. Routing Protocols:</b><br/>"
            "• <b>Distance Vector Routing (Bellman-Ford):</b> Routers exchange entire routing table with DIRECT NEIGHBORS periodically. Prone to <b>Count-to-Infinity</b> on link failure. Solutions: Split Horizon and Poison Reverse.<br/>"
            "• <b>Link State Routing (Dijkstra):</b> Routers flood Link State Advertisements (LSA) to ALL routers. Each router constructs full global network topology graph. Converges fast, no count-to-infinity.<br/><br/>"
            "<b>2. IPv4 Addressing & CIDR:</b><br/>"
            "• 32-bit address. CIDR notation: a.b.c.d / n (where n is prefix network mask bits).<br/>"
            "• Host bits = 32 - n. Total IP addresses in subnet = 2^(32 - n). Usable hosts = 2^(32 - n) - 2 (subtract Network ID and Broadcast ID).<br/>"
            "• <b>Longest Prefix Matching:</b> Router selects routing table entry with the LARGEST mask length /n matching the destination IP.<br/><br/>"
            "<b>3. IPv4 Datagram Fragmentation:</b><br/>"
            "• Done by routers when packet size exceeds link Maximum Transmission Unit (MTU).<br/>"
            "• <b>Identification:</b> Same for all fragments of original packet.<br/>"
            "• <b>Flags (3 bits):</b> Reserved (0) | DF (Don't Fragment) | MF (More Fragments: 1 if more follow, 0 for last fragment).<br/>"
            "• <b>Fragment Offset (13 bits):</b> Measured in units of 8 BYTES (64 bits). Offset = (Number of data bytes preceding this fragment) / 8.<br/><br/>"
            "<b>4. Network Address Translation (NAT):</b> Maps private RFC 1918 IPs (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to public routable IPs using port forwarding (NAPT)."
        ),
        "callouts": [
            ("Offset 8-Byte Rule", "Fragment offset field in IPv4 header is ALWAYS divided by 8! Therefore, every fragment payload (except the last one) MUST be a multiple of 8 bytes.", "formula"),
            ("Usable Host Reduction", "Always subtract 2 from total IP addresses in a CIDR block to account for the Network Address (all host bits 0) and Directed Broadcast Address (all host bits 1)!", "warn")
        ],
        "tables": []
    },
    {
        "title": "Transport Layer (TCP), Sockets & Application Protocols (DNS, HTTP)",
        "hinglish": "TCP sliding window flow control, congestion window (Slow Start, Congestion Avoidance, Fast Recovery), socket system calls, aur DNS queries (Iterative vs Recursive) complete syllabus cover karte hain.",
        "theory": (
            "<b>1. TCP Flow Control (Sliding Window):</b><br/>"
            "• Byte-stream oriented with 32-bit sequence numbers. Sequence number represents byte offset of first data byte in segment.<br/>"
            "• Receiver Advertised Window (rwnd): Prevents receiver buffer overflow. Usable sender window = min(rwnd, cwnd).<br/>"
            "• Efficiency of Sliding Window: η = (W * T_t) / (T_t + 2 * T_p) = W / (1 + 2a). To achieve 100% efficiency, window W ≥ 1 + 2a.<br/><br/>"
            "<b>2. TCP Congestion Control:</b><br/>"
            "• <b>Slow Start:</b> cwnd starts at 1 MSS, doubles every RTT (exponential growth: 1, 2, 4, 8, ...) until Slow Start Threshold (ssthresh).<br/>"
            "• <b>Congestion Avoidance:</b> When cwnd ≥ ssthresh, cwnd increases by 1 MSS per RTT (Additive Increase - linear growth).<br/>"
            "• <b>Reaction to Loss:</b><br/>"
            "  - <b>Timeout (Severe Congestion):</b> ssthresh = cwnd / 2, cwnd = 1 MSS (restart Slow Start).<br/>"
            "  - <b>3 Duplicate ACKs (Mild Congestion):</b> Fast Retransmit (retransmit missing segment) -> Fast Recovery: ssthresh = cwnd / 2, cwnd = ssthresh + 3 MSS.<br/><br/>"
            "<b>3. Socket API:</b><br/>"
            "• Server: socket() -> bind() -> listen() -> accept() (blocks) -> read()/recv() -> write()/send() -> close().<br/>"
            "• Client: socket() -> connect() (initiates 3-way handshake) -> write()/send() -> read()/recv() -> close().<br/><br/>"
            "<b>4. Application Protocols:</b><br/>"
            "• <b>DNS:</b> Hierarchical distributed database (Root -> TLD -> Authoritative). Uses UDP port 53 for queries. Recursive vs Iterative resolution.<br/>"
            "• <b>HTTP:</b> Uses TCP port 80. HTTP 1.0 (Non-persistent: 1 TCP connection per object, takes 2 RTTs per object). HTTP 1.1 (Persistent: reuse connection, pipelining)."
        ),
        "callouts": [
            ("TCP Timeout vs 3-Dup-ACK", "On timeout, cwnd drops all the way down to 1 MSS! On 3 duplicate ACKs (Fast Retransmit/Recovery), cwnd drops only to half (ssthresh) and continues in Congestion Avoidance.", "tip"),
            ("HTTP 1.0 Overhead", "In HTTP 1.0 non-persistent connections, fetching N objects referenced in a webpage requires N + 1 separate TCP 3-way handshakes, incurring massive latency!", "formula")
        ],
        "tables": []
    }
]

PRACTICE_QUESTIONS = [
    {
        "id": "CN-Q01",
        "type": "NAT",
        "marks": 2,
        "text": "A 100 km long broadcast LAN uses CSMA/CD with a transmission rate of 100 Mbps. Signal propagation speed is 2 * 10^8 m/s. What is the minimum frame size (in bytes) required for proper collision detection?",
        "answer": "12500",
        "explanation": "1. Distance d = 100 km = 100 * 10^3 m.<br/>2. Propagation speed v = 2 * 10^8 m/s.<br/>3. Propagation delay T_p = d / v = (10^5) / (2 * 10^8) = 0.5 * 10^(-3) s = 0.5 ms.<br/>4. Bandwidth B = 100 Mbps = 10^8 bps.<br/>5. For CSMA/CD: T_t ≥ 2 * T_p => L / B ≥ 2 * T_p => L ≥ 2 * B * T_p.<br/>6. L_min = 2 * (10^8 bps) * (0.5 * 10^(-3) s) = 10^5 bits.<br/>7. Converting to bytes: 100,000 / 8 = 12,500 bytes.",
        "is_pyq": True,
        "year": 2022,
        "difficulty": "Medium"
    },
    {
        "id": "CN-Q02",
        "type": "NAT",
        "marks": 2,
        "text": "An IPv4 datagram of total size 4000 bytes (including 20 bytes IP header) arrives at a router and must be forwarded over a link with MTU of 1500 bytes. What is the Fragment Offset value in the SECOND fragment?",
        "answer": "185",
        "explanation": "1. Total payload = 4000 - 20 = 3980 bytes.<br/>2. MTU = 1500 bytes => Max payload per fragment = 1500 - 20 = 1480 bytes.<br/>3. Note that 1480 is divisible by 8 (1480 / 8 = 185).<br/>4. Fragment 1: 20 bytes header + 1480 bytes data. Bytes 0 to 1479. MF = 1, Offset = 0.<br/>5. Fragment 2 starts at byte 1480.<br/>6. Fragment Offset value in header = 1480 / 8 = 185.",
        "is_pyq": True,
        "year": 2021,
        "difficulty": "Medium"
    },
    {
        "id": "CN-Q03",
        "type": "MSQ",
        "marks": 2,
        "text": "Which of the following statements is/are CORRECT regarding TCP Congestion Control and Flow Control?",
        "options": {
            "A": "During Slow Start, the congestion window (cwnd) grows exponentially with respect to Round Trip Time (RTT)",
            "B": "In Fast Recovery, receiving 3 duplicate ACKs causes cwnd to reset directly to 1 MSS",
            "C": "Receiver Advertised Window (rwnd) prevents the sender from overflowing the receiver's buffer",
            "D": "During Congestion Avoidance, cwnd increases linearly by approximately 1 MSS per RTT"
        },
        "answer": "A, C, D",
        "explanation": "• A is correct: In Slow Start, cwnd doubles every RTT (exponential).<br/>• B is WRONG: Receiving 3 duplicate ACKs triggers Fast Recovery, which sets cwnd to ssthresh + 3 MSS (NOT 1 MSS!). It resets to 1 MSS only on a TIMEOUT.<br/>• C is correct: rwnd provides flow control to prevent receiver buffer overflow.<br/>• D is correct: Congestion Avoidance implements Additive Increase (linear).<br/>Hence A, C, D are correct.",
        "is_pyq": False,
        "year": None,
        "difficulty": "GATE-Level"
    },
    {
        "id": "CN-Q04",
        "type": "NAT",
        "marks": 2,
        "text": "A subnet has the network address 192.168.10.0/26. How many valid assignable IP addresses can be configured on host machines in this subnet?",
        "answer": "62",
        "explanation": "In /26 CIDR prefix, host bits = 32 - 26 = 6 bits.<br/>Total IP addresses = 2^6 = 64.<br/>Subnet network address (all 0s) and directed broadcast address (all 1s) cannot be assigned to hosts.<br/>Valid assignable host IPs = 64 - 2 = 62.",
        "is_pyq": True,
        "year": 2019,
        "difficulty": "Easy"
    },
    {
        "id": "CN-Q05",
        "type": "MCQ",
        "marks": 1,
        "text": "Which application-layer protocol is responsible for mapping a domain name such as www.iitm.ac.in to an IP address?",
        "options": {
            "A": "DHCP",
            "B": "DNS",
            "C": "ARP",
            "D": "BGP"
        },
        "answer": "B",
        "explanation": "DNS (Domain Name System) translates human-readable domain names to numerical IP addresses. ARP resolves IP to MAC addresses at the network/data-link interface.",
        "is_pyq": True,
        "year": 2018,
        "difficulty": "Easy"
    }
]
