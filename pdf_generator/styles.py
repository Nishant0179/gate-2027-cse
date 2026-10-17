import os
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
from reportlab.pdfgen import canvas

# Palette
PRIMARY = HexColor("#1E3A8A")       # Deep Navy
SECONDARY = HexColor("#0D9488")     # Deep Teal
ACCENT = HexColor("#D97706")        # Warm Amber
DARK_TEXT = HexColor("#0F172A")     # Slate 900
MUTED_TEXT = HexColor("#475569")    # Slate 600
LIGHT_BG = HexColor("#F8FAFC")      # Slate 50
BORDER_COLOR = HexColor("#CBD5E1")  # Slate 300

TIP_BG = HexColor("#F0FDF4")        # Emerald 50
TIP_BORDER = HexColor("#16A34A")    # Emerald 600

WARN_BG = HexColor("#FEF2F2")       # Rose 50
WARN_BORDER = HexColor("#E11D48")   # Rose 600

NOTE_BG = HexColor("#EFF6FF")       # Blue 50
NOTE_BORDER = HexColor("#2563EB")   # Blue 600

CODE_BG = HexColor("#1E293B")       # Dark code block
CODE_TEXT = HexColor("#F1F5F9")

class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas to dynamically compute and print 'Page X of Y' 
    along with running headers and footers.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        # Don't draw running header/footer on cover page (page 1)
        if self._pageNumber == 1:
            return

        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(MUTED_TEXT)

        # Running Header
        header_text = getattr(self, "doc_header_title", "GATE 2027 CSE Preparation Library | IIT Madras Syllabus")
        self.drawString(54, 800, header_text)
        
        self.setStrokeColor(BORDER_COLOR)
        self.setLineWidth(0.5)
        self.line(54, 794, 541, 794)

        # Running Footer
        self.line(54, 45, 541, 45)
        self.setFont("Helvetica", 8)
        self.drawString(54, 32, "GATE 2027 CS/IT - Comprehensive Study System | Confidential & Authentic")
        page_str = f"Page {self._pageNumber} of {total_pages}"
        self.drawRightString(541, 32, page_str)

        self.restoreState()


def get_custom_stylesheet():
    styles = getSampleStyleSheet()

    # Modify Normal
    styles['Normal'].textColor = DARK_TEXT
    styles['Normal'].fontSize = 10
    styles['Normal'].leading = 14
    styles['Normal'].fontName = 'Helvetica'

    # Custom styles
    styles.add(ParagraphStyle(
        name='DocTitle',
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=PRIMARY,
        spaceAfter=10
    ))

    styles.add(ParagraphStyle(
        name='DocSubtitle',
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=SECONDARY,
        spaceAfter=15
    ))

    styles.add(ParagraphStyle(
        name='H1Custom',
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=PRIMARY,
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        name='H2Custom',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=SECONDARY,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        name='H3Custom',
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=DARK_TEXT,
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        name='BodyCustom',
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=DARK_TEXT,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name='BodyBold',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13.5,
        textColor=DARK_TEXT,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name='HinglishIntro',
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        leading=13.5,
        textColor=HexColor("#334155"),
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name='FormulaText',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=PRIMARY,
        alignment=1 # Centered
    ))

    styles.add(ParagraphStyle(
        name='CodeSnippet',
        fontName='Courier',
        fontSize=8.5,
        leading=11.5,
        textColor=CODE_TEXT
    ))

    styles.add(ParagraphStyle(
        name='CalloutTitle',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=PRIMARY,
        spaceAfter=4
    ))

    styles.add(ParagraphStyle(
        name='CalloutBody',
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=DARK_TEXT
    ))

    styles.add(ParagraphStyle(
        name='QuestionText',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13.5,
        textColor=DARK_TEXT,
        spaceAfter=4
    ))

    styles.add(ParagraphStyle(
        name='OptionText',
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=DARK_TEXT,
        leftIndent=12,
        spaceAfter=2
    ))

    styles.add(ParagraphStyle(
        name='SolutionText',
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=DARK_TEXT,
        spaceAfter=4
    ))

    return styles

def create_callout(title, text, callout_type="note", styles=None):
    if styles is None:
        styles = get_custom_stylesheet()

    if callout_type == "tip":
        bg_color = TIP_BG
        border_color = TIP_BORDER
        badge = "[PRO TIP]"
    elif callout_type == "warn":
        bg_color = WARN_BG
        border_color = WARN_BORDER
        badge = "[COMMON EXAM TRAP / MISTAKE]"
    elif callout_type == "formula":
        bg_color = HexColor("#FEF3C7")
        border_color = ACCENT
        badge = "[KEY FORMULA / RESULT]"
    else:
        bg_color = NOTE_BG
        border_color = NOTE_BORDER
        badge = "[EXPLANATION & CONCEPT]"

    content = [
        Paragraph(f"<b>{badge} {title}</b>", styles['CalloutTitle']),
        Paragraph(text, styles['CalloutBody'])
    ]

    t = Table([[content]], colWidths=[487])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg_color),
        ('BOX', (0,0), (-1,-1), 1, border_color),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    return t

def create_code_block(code_text, styles=None):
    if styles is None:
        styles = get_custom_stylesheet()
    
    # Escape HTML tags
    escaped_code = code_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    lines = escaped_code.split('\n')
    paras = [Paragraph(line.replace(' ', '&nbsp;'), styles['CodeSnippet']) for line in lines]

    t = Table([[paras]], colWidths=[487])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CODE_BG),
        ('BOX', (0,0), (-1,-1), 0.5, HexColor("#334155")),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    return t
