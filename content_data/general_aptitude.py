# General Aptitude Content Module for GATE 2027
# Weightage: 15 Marks (Mandatory Section for all papers)

SUBJECT_META = {
    "id": "GA",
    "name": "General Aptitude",
    "folder": "11_General_Aptitude",
    "weightage": "15 Marks",
    "topics": [
        "Verbal Aptitude: Grammar, Vocabulary, Reading comprehension, Narrative sequencing",
        "Quantitative Aptitude: Data interpretation, numerical computation, percentages, ratios, permutations, series, geometry",
        "Analytical Aptitude: Logic (deduction/induction), analogy, numerical relations and reasoning",
        "Spatial Aptitude: Transformation of shapes, translation, rotation, mirroring, paper folding, cutting in 2D/3D"
    ]
}

CHAPTERS = [
    {
        "title": "Verbal Aptitude - Grammar, Vocabulary & Comprehension",
        "hinglish": "Verbal aptitude me tenses, subject-verb agreement, vocabulary in context, aur reading comprehension ke direct 4-5 marks aate hain.",
        "theory": (
            "<b>1. Basic English Grammar:</b><br/>"
            "• <b>Subject-Verb Agreement:</b> Singular subject takes singular verb; plural subject takes plural verb.<br/>"
            "  - Words joined by 'along with', 'as well as', 'together with' do NOT affect subject number.<br/>"
            "  - With 'Either... or' / 'Neither... nor', verb agrees with the NEAREST subject.<br/>"
            "• <b>Tenses:</b> Present perfect vs Past simple, conditional clauses (If + had + V3, would have + V3).<br/>"
            "• <b>Prepositions & Collocations:</b> 'depend on', 'abstain from', 'comply with', 'congruent with'.<br/><br/>"
            "<b>2. Vocabulary & Word Groups:</b><br/>"
            "• Words commonly tested: Ephemeral (transient), Ubiquitous (omnipresent), Pragmatic (practical), Mitigate (alleviate), Ambivalent (conflicted), Resilient (tough).<br/>"
            "• Verbal Analogies: Analyze the exact grammatical and semantic relationship between the prompt pair (e.g. Cause-Effect, Worker-Tool, Degree of Intensity).<br/><br/>"
            "<b>3. Reading Comprehension & Narrative Sequencing:</b><br/>"
            "• Identify the primary thesis vs supporting evidence.<br/>"
            "• Avoid extreme options ('always', 'never', 'solely') unless explicitly asserted by the author.<br/>"
            "• Sentence Ordering: Look for transition markers (However, Therefore, Furthermore), chronological anchors, and pronoun antecedents."
        ),
        "callouts": [
            ("Neither... Nor Agreement", "Example: 'Neither the teacher nor the students WERE present' (agrees with plural 'students'). 'Neither the students nor the teacher WAS present' (agrees with singular 'teacher').", "tip"),
            ("Unwarranted Assumptions", "In critical reasoning and comprehension questions, never import outside real-world knowledge that is not supported by the passage text!", "warn")
        ],
        "tables": []
    },
    {
        "title": "Quantitative Aptitude - Arithmetic, Algebra & Mensuration",
        "hinglish": "Percentages, ratios, time and work (efficiency method), speed and distance, permutations, aur 2D/3D mensuration se quantitative section banta hai.",
        "theory": (
            "<b>1. Ratios, Percentages & Profit/Loss:</b><br/>"
            "• Successive Percentage Change: Net change = a + b + (ab / 100)%.<br/>"
            "• If price increases by r%, consumption must decrease by [r / (100 + r)] * 100% to keep expenditure constant.<br/>"
            "• Efficiency Method for Time & Work: Total Work = LCM of individual times. Efficiency = Work / Time.<br/><br/>"
            "<b>2. Permutations, Combinations & Probability:</b><br/>"
            "• n distinct items in a circle: (n - 1)! ways.<br/>"
            "• Total handshakes among n people: C(n, 2) = n(n - 1) / 2.<br/>"
            "• Derangements: D_n = n! [1 - 1/1! + 1/2! - 1/3! + ... + (-1)^n/n!]. D_1=0, D_2=1, D_3=2, D_4=9, D_5=44.<br/><br/>"
            "<b>3. Geometry & Mensuration:</b><br/>"
            "• Circle: Area = π r^2, Circumference = 2 π r.<br/>"
            "• Sphere: Volume = (4/3) π r^3, Surface Area = 4 π r^2.<br/>"
            "• Cylinder: Volume = π r^2 h, Curved Surface = 2 π r h, Total Surface = 2 π r (r + h).<br/>"
            "• Cone: Volume = (1/3) π r^2 h, Slant height l = sqrt(r^2 + h^2), Curved Surface = π r l."
        ),
        "callouts": [
            ("Relative Speed Rule", "Two objects moving towards each other: Relative Speed = S1 + S2. Moving in same direction: Relative Speed = |S1 - S2|.", "formula"),
            ("Mensuration Scaling", "If linear dimensions of a 3D object are scaled by factor k, its surface area scales by k^2 and its volume scales by k^3!", "tip")
        ],
        "tables": []
    },
    {
        "title": "Analytical & Spatial Aptitude - Logic, Reasoning & 2D/3D Shapes",
        "hinglish": "Analytical aptitude me syllogisms and deduction aate hain. Spatial aptitude me paper folding, reflection/mirroring, aur 3D blocks rotation questions hote hain.",
        "theory": (
            "<b>1. Analytical Logic & Deduction:</b><br/>"
            "• <b>Syllogisms (Venn Diagram Method):</b><br/>"
            "  - 'All A are B' (Subset: A ⊆ B).<br/>"
            "  - 'Some A are B' (Intersection: A ∩ B ≠ ∅).<br/>"
            "  - 'No A is B' (Disjoint: A ∩ B = ∅).<br/>"
            "• A conclusion is VALID only if it holds true across ALL possible Venn diagram representations!<br/>"
            "• Seating Arrangements: Linear and circular. Fix the position of the person with the most constraints first.<br/><br/>"
            "<b>2. Spatial Aptitude (Official Syllabus Focus):</b><br/>"
            "• <b>Transformations:</b> Translation (shifting), Rotation (clockwise/counter-clockwise by θ degrees), Scaling (enlargement/reduction).<br/>"
            "• <b>Mirror Imaging:</b> Left and right invert; top and bottom remain unchanged (horizontal flip).<br/>"
            "• <b>Water Imaging:</b> Top and bottom invert; left and right remain unchanged (vertical flip).<br/>"
            "• <b>Paper Folding & Cutting:</b> Trace backward from the final fold! Unfolding is equivalent to reflecting the pattern across each crease fold line sequentially.<br/>"
            "• <b>3D Cube Nets:</b> A standard cube has 6 faces. In a flat net, alternating faces along a strip are OPPOSITE faces and can never be adjacent in the assembled cube!"
        ),
        "callouts": [
            ("Cube Net Opposite Face Rule", "In a cross or linear strip net of a cube, faces separated by exactly one intervening face are ALWAYS OPPOSITE to each other in 3D!", "tip"),
            ("Spatial Unfolding Sequence", "When solving paper punch problems, always reverse the punch operations in the exact reverse chronological order of folds!", "warn")
        ],
        "tables": []
    }
]

PRACTICE_QUESTIONS = [
    {
        "id": "GA-Q01",
        "type": "MCQ",
        "marks": 1,
        "text": "Choose the most appropriate word from the options given below to complete the following sentence:<br/>The committee could not reach a consensus because the members had __________ views on the proposal.",
        "options": {
            "A": "divergent",
            "B": "congruent",
            "C": "complacent",
            "D": "transient"
        },
        "answer": "A",
        "explanation": "'Divergent' means differing or moving apart in direction, which directly explains why the committee could not reach a consensus. 'Congruent' means agreeing, 'complacent' means self-satisfied, and 'transient' means temporary.",
        "is_pyq": True,
        "year": 2023,
        "difficulty": "Easy"
    },
    {
        "id": "GA-Q02",
        "type": "NAT",
        "marks": 2,
        "text": "A vessel contains a mixture of milk and water in the ratio 7 : 3. If 10 liters of the mixture is removed and replaced with pure water, the new ratio of milk to water becomes 7 : 5. What was the initial quantity of the mixture (in liters)?",
        "answer": "60",
        "explanation": "Let initial total volume = V liters. Initial milk = (7/10) V.<br/>When 10 liters of mixture is removed, milk removed = (7/10) * 10 = 7 liters.<br/>Remaining milk = (7/10) V - 7.<br/>10 liters of pure water is added, so total volume remains V.<br/>In the new ratio 7:5, milk fraction = 7 / (7+5) = 7/12.<br/>Equation: (7/10) V - 7 = (7/12) V.<br/>Divide both sides by 7: (1/10) V - 1 = (1/12) V.<br/>(1/10 - 1/12) V = 1 => [(6 - 5) / 60] V = 1 => (1/60) V = 1 => V = 60 liters.",
        "is_pyq": True,
        "year": 2022,
        "difficulty": "Medium"
    },
    {
        "id": "GA-Q03",
        "type": "MCQ",
        "marks": 2,
        "text": "Consider the following statements and conclusions:<br/>Statements:<br/>1. Some engineers are writers.<br/>2. All writers are dreamers.<br/>Conclusions:<br/>I. Some dreamers are engineers.<br/>II. All dreamers are writers.<br/>Which of the conclusions logically follows?",
        "options": {
            "A": "Only conclusion I follows",
            "B": "Only conclusion II follows",
            "C": "Both conclusion I and II follow",
            "D": "Neither conclusion follows"
        },
        "answer": "A",
        "explanation": "Since Some Engineers are Writers, and All Writers are Dreamers, those Engineers who are writers must also be Dreamers. Therefore, 'Some dreamers are engineers' definitely follows (Conclusion I is valid). Conclusion II ('All dreamers are writers') does not necessarily follow because there can be dreamers who are not writers. Thus, only conclusion I follows.",
        "is_pyq": True,
        "year": 2021,
        "difficulty": "Easy"
    },
    {
        "id": "GA-Q04",
        "type": "MCQ",
        "marks": 1,
        "text": "A square sheet of paper is folded in half horizontally from top to bottom, and then in half vertically from left to right. A triangular hole is punched at the center of the folded paper. How many triangular holes will appear when the paper is completely unfolded?",
        "options": {
            "A": "2",
            "B": "4",
            "C": "8",
            "D": "16"
        },
        "answer": "B",
        "explanation": "Each fold doubles the number of layers of paper. First horizontal fold creates 2 layers. Second vertical fold creates 2 * 2 = 4 layers. Punching a hole through all 4 layers produces exactly 4 holes when completely unfolded.",
        "is_pyq": True,
        "year": 2021,
        "difficulty": "Easy"
    },
    {
        "id": "GA-Q05",
        "type": "NAT",
        "marks": 2,
        "text": "In how many distinct ways can 4 letters be placed into 4 addressed envelopes such that NO letter goes into its correct envelope (total derangements D_4)?",
        "answer": "9",
        "explanation": "The number of derangements of n objects is given by D_n = n! [1 - 1/1! + 1/2! - 1/3! + 1/4!].<br/>For n = 4: D_4 = 4! [1/2 - 1/6 + 1/24] = 24 [12/24 - 4/24 + 1/24] = 24 * (9/24) = 9.",
        "is_pyq": True,
        "year": 2020,
        "difficulty": "Easy"
    }
]
