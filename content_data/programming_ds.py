# Programming & Data Structures Content Module for GATE 2027 CSE
# Weightage: 10-12 Marks

SUBJECT_META = {
    "id": "PDS",
    "name": "Programming and Data Structures",
    "folder": "04_Programming_Data_Structures",
    "weightage": "10 Marks",
    "topics": [
        "Programming in C: Operators, precedence, associativity, pointers, arrays, functions, recursion, structures",
        "Linear data structures: Arrays, address calculation, stacks, queues, linked lists",
        "Non-linear data structures: Trees, binary search trees (BST), binary heaps, graph representations"
    ]
}

CHAPTERS = [
    {
        "title": "Programming in C & Recursion Tracing",
        "hinglish": "C programming me pointers, pointer arithmetic, array indexing a[i] == *(a+i), aur recursive function calls ka execution tree draw karke output nikalna sabse common pattern hai.",
        "theory": (
            "<b>1. C Operators, Precedence & Associativity:</b><br/>"
            "• Highest precedence: Primary () [] -> . (Left to Right).<br/>"
            "• Unary operators: ++ -- ! ~ * & (type) sizeof (Right to Left!).<br/>"
            "• Arithmetic: * / % (L to R), followed by + - (L to R).<br/>"
            "• Bitwise shifts: &lt;&lt; &gt;&gt; (L to R).<br/>"
            "• Relational: &lt; &lt;= &gt; &gt;= followed by == !=.<br/>"
            "• Bitwise: & (AND), ^ (XOR), | (OR) in that order.<br/>"
            "• Logical: && (Logical AND - short-circuit!), || (Logical OR - short-circuit!).<br/>"
            "• Conditional Ternary: ?: (Right to Left).<br/>"
            "• Assignment: = += -= *= etc. (Right to Left).<br/>"
            "• Comma operator: , (Left to Right - lowest precedence).<br/><br/>"
            "<b>2. Pointers & Array Equivalence:</b><br/>"
            "• Name of an array decays into a constant pointer to its first element: a == &a[0].<br/>"
            "• Pointer subscript rule: a[i] ≡ *(a + i) ≡ *(i + a) ≡ i[a]! (All are identical in C).<br/>"
            "• For 2D array a[M][N]: Address of a[i][j] = Base + (i * N + j) * sizeof(element).<br/>"
            "• int *p vs int (*p)[N]: 'int *p' is pointer to int; 'int (*p)[N]' is pointer to an array of N ints.<br/><br/>"
            "<b>3. Recursion & Stack Activation:</b><br/>"
            "• Every recursive call pushes an Activation Record onto the call stack containing local variables, parameters, and return address.<br/>"
            "• Tail recursion: Recursive call is the absolute final statement executed in function (can be optimized into a loop)."
        ),
        "callouts": [
            ("Short-Circuit Evaluation Trap", "In expression (A && B): If A evaluates to FALSE (0), B is NEVER EXECUTED. In (A || B): If A evaluates to TRUE (≠0), B is NEVER EXECUTED! Watch out for side-effects like (x++ || y++)!", "warn"),
            ("Array Equivalence", "Because a[i] is defined as *(a+i), expression 2[a] is completely valid C syntax and equals a[2]!", "tip")
        ],
        "tables": []
    },
    {
        "title": "Linear Data Structures - Stacks, Queues & Linked Lists",
        "hinglish": "Stack applications jaise infix-to-postfix conversion, parenthesis matching, circular queue boundary conditions, aur linked list cycle detection (Floyd's Tortoise and Hare) exam me repeatedly aate hain.",
        "theory": (
            "<b>1. Stacks (LIFO - Last In First Out):</b><br/>"
            "• Standard operations: push(x), pop(), peek(), isEmpty() all in O(1) time.<br/>"
            "• Infix to Postfix conversion: Operands output immediately; operators pushed to stack based on precedence. Operator popped if stack top has higher or equal precedence (left-associative).<br/>"
            "• Evaluation of Postfix: Operands pushed to stack; on operator, pop 2 operands: result = (second popped) op (first popped); push result.<br/>"
            "• Total distinct stack permutations with n elements = Catalan Number: C_n = (1 / (n+1)) * (2n choose n).<br/><br/>"
            "<b>2. Queues (FIFO - First In First Out):</b><br/>"
            "• <b>Circular Queue:</b> Uses modulo arithmetic to avoid false overflow.<br/>"
            "  - Next rear: rear = (rear + 1) % Capacity.<br/>"
            "  - Next front: front = (front + 1) % Capacity.<br/>"
            "  - Queue Full condition: (rear + 1) % Capacity == front (leaving one empty slot).<br/>"
            "• Priority Queue: Implemented efficiently using Binary Heaps.<br/><br/>"
            "<b>3. Linked Lists:</b><br/>"
            "• Singly Linked List: Insertion/Deletion at head O(1); at tail O(n) without tail pointer, O(1) with tail pointer (deletion at tail is still O(n)!).<br/>"
            "• Floyd's Cycle Finding (Tortoise and Hare): Slow pointer moves 1 step, Fast pointer moves 2 steps. If they meet, cycle exists! Distance from head to cycle start equals distance from meeting point to cycle start."
        ),
        "callouts": [
            ("Catalan Numbers Formula", "Catalan number C_n = (2n)! / ((n+1)! * n!).<br/>C_1 = 1, C_2 = 2, C_3 = 5, C_4 = 14, C_5 = 42.<br/>Counts: Stack-sortable permutations, binary trees with n nodes, balanced parenthesis expressions.", "formula"),
            ("Tail Deletion in SLL", "Even if you maintain a tail pointer, deleting the last element in a Singly Linked List is O(n) because you must update the second-to-last node's next pointer to NULL!", "warn")
        ],
        "tables": []
    },
    {
        "title": "Trees, BST & Binary Heaps",
        "hinglish": "Binary Search Tree (BST) ka inorder traversal always STRICTLY ASCENDING sorted order deta hai. Heap me root par Min/Max element hota hai and Heapify takes O(n) time.",
        "theory": (
            "<b>1. Binary Tree Properties:</b><br/>"
            "• Maximum nodes at level i = 2^i (root at level 0).<br/>"
            "• Maximum nodes in binary tree of height h = 2^(h+1) - 1.<br/>"
            "• <b>Handshaking in Trees:</b> For any binary tree, number of leaf nodes n0 is related to number of nodes of degree 2 (n2) by: n0 = n2 + 1.<br/>"
            "• Tree Traversals: Inorder (LNR), Preorder (NLR), Postorder (LRN).<br/>"
            "  - To uniquely reconstruct a binary tree, you MUST have INORDER along with either PREORDER or POSTORDER.<br/><br/>"
            "<b>2. Binary Search Trees (BST):</b><br/>"
            "• Left subtree keys &lt; Node key &lt; Right subtree keys.<br/>"
            "• Inorder traversal of BST yields keys in strictly increasing sorted order!<br/>"
            "• Deletion in BST: Leaf -> delete directly; 1 child -> replace with child; 2 children -> replace with Inorder Predecessor (max of left) OR Inorder Successor (min of right).<br/><br/>"
            "<b>3. Binary Heaps:</b><br/>"
            "• Complete Binary Tree stored in array representation: For node at index i (1-based): Left child = 2i, Right child = 2i+1, Parent = ⌊i/2⌋.<br/>"
            "• <b>Max-Heap property:</b> A[Parent] ≥ A[Child]. Root holds global maximum.<br/>"
            "• <b>Building a Heap (Heapify):</b> Bottom-up approach takes O(n) time, NOT O(n log n)!<br/>"
            "• Extract Max: Swap root with last element, decrease size, Max-Heapify root in O(log n) time."
        ),
        "callouts": [
            ("Heap Build Complexity", "Building a heap of n elements using bottom-up build-heap is O(n) linear time, because nodes near leaves have very small heights: ∑ (h / 2^h) converges to 2!", "tip"),
            ("Unique Tree Condition", "Given only Preorder and Postorder traversals, a unique binary tree CANNOT be determined unless every internal node has strictly two children (Full Binary Tree)!", "warn")
        ],
        "tables": []
    }
]

PRACTICE_QUESTIONS = [
    {
        "id": "PDS-Q01",
        "type": "MCQ",
        "marks": 2,
        "text": "Consider the following C function:<br/>int fun(int n) {<br/>&nbsp;&nbsp;if (n <= 1) return 1;<br/>&nbsp;&nbsp;if (n % 2 == 0) return fun(n / 2);<br/>&nbsp;&nbsp;return fun(n / 2) + fun(n - 1);<br/>}<br/>What is the return value of fun(7)?",
        "options": {
            "A": "3",
            "B": "4",
            "C": "5",
            "D": "6"
        },
        "answer": "B",
        "explanation": "fun(7): 7 is odd => fun(3) + fun(6).<br/>• fun(6): 6 is even => fun(3).<br/>• fun(3): 3 is odd => fun(1) + fun(2).<br/>  - fun(1) = 1 (base case).<br/>  - fun(2): 2 is even => fun(1) = 1.<br/>  - So fun(3) = 1 + 1 = 2.<br/>• fun(6) = fun(3) = 2.<br/>• fun(7) = fun(3) + fun(6) = 2 + 2 = 4.",
        "is_pyq": True,
        "year": 2023,
        "difficulty": "Medium"
    },
    {
        "id": "PDS-Q02",
        "type": "NAT",
        "marks": 1,
        "text": "A full binary tree has 64 leaf nodes. What is the total number of internal nodes with degree 2 in this tree?",
        "answer": "63",
        "explanation": "In any binary tree, the number of leaf nodes n0 is related to nodes of degree 2 by: n0 = n2 + 1. Here n0 = 64. Hence n2 = 64 - 1 = 63.",
        "is_pyq": True,
        "year": 2021,
        "difficulty": "Easy"
    },
    {
        "id": "PDS-Q03",
        "type": "MSQ",
        "marks": 2,
        "text": "Which of the following array sequences CANNOT represent a valid MAX-HEAP? (1-based indexing)",
        "options": {
            "A": "[50, 40, 30, 20, 35, 25, 15]",
            "B": "[100, 60, 80, 50, 70, 40, 30]",
            "C": "[90, 80, 70, 60, 50, 40, 30]",
            "D": "[45, 30, 40, 25, 35, 10, 5]"
        },
        "answer": "B, D",
        "explanation": "In a Max-Heap, A[i] ≥ A[2i] and A[i] ≥ A[2i+1] for all valid indices.<br/>A: Root=50; children 40, 30; 40's children 20, 35 (both ≤40); 30's children 25, 15 (both ≤30). Valid!<br/>B: Root=100; children 60, 80. Node at index 2 is 60, its children are at index 4 (50) and index 5 (70). But 70 > 60! Violates Max-heap property. INVALID!<br/>C: Decreasing array is always a valid Max-heap. Valid!<br/>D: Node at index 2 is 30, its right child at index 5 is 35. But 35 > 30! Violates Max-heap. INVALID!<br/>Hence options B and D cannot represent a max-heap.",
        "is_pyq": False,
        "year": None,
        "difficulty": "GATE-Level"
    },
    {
        "id": "PDS-Q04",
        "type": "NAT",
        "marks": 2,
        "text": "The preorder traversal of a Binary Search Tree (BST) is: 15, 10, 8, 12, 20, 18, 25. What is the value of the node in the tree that is the Inorder Predecessor of 15?",
        "answer": "12",
        "explanation": "Inorder traversal of any BST is obtained by simply sorting its elements in ascending order: 8, 10, 12, 15, 18, 20, 25. In this sorted list, the element immediately preceding 15 is 12.",
        "is_pyq": False,
        "year": None,
        "difficulty": "Medium"
    },
    {
        "id": "PDS-Q05",
        "type": "MCQ",
        "marks": 1,
        "text": "What is the time complexity to find the minimum element in a MAX-HEAP of size n?",
        "options": {
            "A": "O(1)",
            "B": "O(log n)",
            "C": "O(n)",
            "D": "O(n log n)"
        },
        "answer": "C",
        "explanation": "In a Max-Heap, the maximum element is at the root in O(1). However, the minimum element must reside in one of the leaf nodes (indices ⌊n/2⌋ + 1 to n). There are ⌈n/2⌉ leaf nodes, so finding the minimum requires scanning all leaves in O(n) time.",
        "is_pyq": True,
        "year": 2020,
        "difficulty": "Easy"
    }
]
