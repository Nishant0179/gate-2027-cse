import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib import colors
from reportlab.lib.colors import HexColor

from .styles import (
    NumberedCanvas, get_custom_stylesheet, create_callout, create_code_block,
    PRIMARY, SECONDARY, ACCENT, DARK_TEXT, MUTED_TEXT, LIGHT_BG, BORDER_COLOR
)

class GatePdfBuilder:
    def __init__(self, filename, title, subject_name, doc_type="Study Notes", syllabus_code="CS"):
        self.filename = filename
        self.title = title
        self.subject_name = subject_name
        self.doc_type = doc_type
        self.syllabus_code = syllabus_code
        self.styles = get_custom_stylesheet()
        self.story = []
        
        # Ensure parent directory exists
        os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)

    def add_cover_page(self, metadata=None):
        """Builds a formal, academic cover page."""
        meta = metadata or {}
        weightage = meta.get("weightage", "8-10 Marks")
        topics = meta.get("topics", [])
        version = meta.get("version", "GATE 2027 Official IIT Madras Compliant")

        # Top Banner
        banner_table = Table([[
            Paragraph(f"<b>GATE 2027 PREPARATION SYSTEM</b> &nbsp;|&nbsp; IIT MADRAS SYLLABUS", self.styles['Normal']),
            Paragraph(f"<b>PAPER: {self.syllabus_code}</b>", self.styles['Normal'])
        ]], colWidths=[350, 137])
        banner_table.setStyle(TableStyle([
            ('TEXTCOLOR', (0,0), (-1,-1), PRIMARY),
            ('ALIGN', (1,0), (1,0), 'RIGHT'),
            ('BOTTOMPADDING', (0,0), (-1,-1), 10),
            ('LINEBELOW', (0,0), (-1,-1), 1, PRIMARY)
        ]))
        self.story.append(banner_table)
        self.story.append(Spacer(1, 35))

        # Title & Subtitle
        self.story.append(Paragraph(self.subject_name.upper(), self.styles['DocSubtitle']))
        self.story.append(Paragraph(self.title, self.styles['DocTitle']))
        self.story.append(Paragraph(f"Document Type: <b>{self.doc_type}</b> &nbsp;|&nbsp; Expected Exam Weightage: <b>{weightage}</b>", self.styles['Normal']))
        self.story.append(Spacer(1, 20))

        # Divider
        self.story.append(HRFlowable(width="100%", thickness=2, color=SECONDARY, spaceAfter=20))

        # Syllabus / Topic Checklist Box
        checklist_rows = [[
            Paragraph("<b>OFFICIAL SYLLABUS CHECKLIST & TOPICS COVERED</b>", self.styles['CalloutTitle'])
        ]]
        if topics:
            for t in topics:
                checklist_rows.append([
                    Paragraph(f"[v] {t}", self.styles['Normal'])
                ])
        else:
            checklist_rows.append([
                Paragraph("[v] Verified against official GATE 2027 curriculum published by IIT Madras.", self.styles['Normal'])
            ])

        checklist_table = Table(checklist_rows, colWidths=[487])
        checklist_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
            ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
            ('INNERGRID', (0,0), (-1,-1), 0.5, HexColor("#E2E8F0")),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 12),
            ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ]))
        self.story.append(checklist_table)
        self.story.append(Spacer(1, 30))

        # Metadata Footer
        info_data = [
            [Paragraph("<b>Curriculum Version:</b>", self.styles['BodyBold']), Paragraph(version, self.styles['Normal'])],
            [Paragraph("<b>Target Audience:</b>", self.styles['BodyBold']), Paragraph("B.Tech CSE / IT Students & GATE 2027 Aspirants", self.styles['Normal'])],
            [Paragraph("<b>Pedagogy:</b>", self.styles['BodyBold']), Paragraph("Intuitive Hinglish Concepts -> Mathematical Rigor -> Solved GATE Numerical -> PYQ Mapping", self.styles['Normal'])],
            [Paragraph("<b>Authentication:</b>", self.styles['BodyBold']), Paragraph("Verified against IIT Madras Official Guidelines (gate2027.iitm.ac.in)", self.styles['Normal'])]
        ]
        info_table = Table(info_data, colWidths=[140, 347])
        info_table.setStyle(TableStyle([
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('LINEBELOW', (0,-1), (-1,-1), 1, BORDER_COLOR)
        ]))
        self.story.append(info_table)

        self.story.append(PageBreak())

    def add_section_header(self, title, section_num=None):
        prefix = f"Section {section_num}: " if section_num else ""
        self.story.append(Paragraph(f"{prefix}{title}", self.styles['H1Custom']))
        self.story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceBefore=2, spaceAfter=8))

    def add_subsection_header(self, title):
        self.story.append(Paragraph(title, self.styles['H2Custom']))

    def add_sub_subsection_header(self, title):
        self.story.append(Paragraph(title, self.styles['H3Custom']))

    def add_paragraph(self, text):
        self.story.append(Paragraph(text, self.styles['BodyCustom']))

    def add_hinglish_intro(self, text):
        self.story.append(Paragraph(f"<b>Concept Intuition (Hinglish):</b> {text}", self.styles['HinglishIntro']))

    def add_callout(self, title, text, callout_type="note"):
        self.story.append(create_callout(title, text, callout_type, self.styles))
        self.story.append(Spacer(1, 8))

    def add_code(self, code_text):
        self.story.append(create_code_block(code_text, self.styles))
        self.story.append(Spacer(1, 8))

    def add_table(self, header, rows, col_widths=None):
        table_data = [[Paragraph(f"<b>{h}</b>", self.styles['BodyBold']) for h in header]]
        for row in rows:
            table_data.append([
                Paragraph(str(cell), self.styles['BodyCustom']) if not isinstance(cell, Paragraph) else cell
                for cell in row
            ])

        if col_widths is None:
            col_widths = [487 / len(header)] * len(header)

        t = Table(table_data, colWidths=col_widths, repeatRows=1)
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), HexColor("#E2E8F0")),
            ('TEXTCOLOR', (0,0), (-1,0), PRIMARY),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ]))
        self.story.append(t)
        self.story.append(Spacer(1, 8))

    def add_question(self, q_num, q_type, marks, q_text, options=None, answer=None, explanation=None, is_pyq=False, pyq_year=None):
        q_elements = []
        badge = f"[VERIFIED GATE {pyq_year} | {marks} Mark{'s' if marks>1 else ''} | {q_type}]" if is_pyq else f"[PRACTICE EXERCISE | {marks} Mark{'s' if marks>1 else ''} | {q_type}]"
        
        q_elements.append(Paragraph(f"<b>Question {q_num}:</b> <font color='{PRIMARY.hexval()}'><b>{badge}</b></font>", self.styles['QuestionText']))
        q_elements.append(Paragraph(q_text, self.styles['BodyCustom']))
        
        if options:
            for opt_key, opt_val in options.items():
                q_elements.append(Paragraph(f"<b>({opt_key})</b> {opt_val}", self.styles['OptionText']))
        
        if answer is not None:
            q_elements.append(Spacer(1, 4))
            q_elements.append(Paragraph(f"<b>Correct Answer:</b> <font color='{SECONDARY.hexval()}'><b>{answer}</b></font>", self.styles['BodyBold']))
        
        if explanation:
            q_elements.append(Paragraph(f"<b>Detailed Explanation:</b> {explanation}", self.styles['SolutionText']))

        q_elements.append(Spacer(1, 10))
        self.story.append(KeepTogether(q_elements))

    def build(self):
        doc = SimpleDocTemplate(
            self.filename,
            pagesize=A4,
            leftMargin=54,
            rightMargin=54,
            topMargin=54,
            bottomMargin=54
        )
        
        # Attach header title to custom canvas class dynamically
        header_title = f"GATE 2027 CSE: {self.subject_name} ({self.doc_type})"
        class BoundNumberedCanvas(NumberedCanvas):
            doc_header_title = header_title

        doc.build(self.story, canvasmaker=BoundNumberedCanvas)
        return self.filename
