# 

# for i in range(100, 200, 10):
#     print(i)


# word = "book"
# number_of_letters = len(word) # Notice this can now work for any string

# for index in range(number_of_letters):
#     letter = word[index]
#     print(f"Index: {index} Letter: {letter}")

# value = 10
# while value < 20:
#    value = value + 1
# print(value)

# animal = "dog"
# while animal == "dog":
#    print("a")
#    animal = "cat"
#    print("b")
# print("c")

# while value < 20:
#    value = value + 1
# print(value)


# value = 20
# while value < 20:
#    value = value + 1
# print(value)
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
doc = Document()
sec = doc.sections[0]
sec.right_margin = Inches(0.35)

# Base font
styles = doc.styles
styles["Normal"].font.name = "Aptos"
styles["Normal"].font.size = Pt(8.5)
styles["Normal"].font.color.rgb = RGBColor(45,45,45)
styles["Normal"].paragraph_format.space_after = Pt(1.5)
styles["Normal"].paragraph_format.line_spacing = 1.0

DARK = "2F3236"
LIGHT = "E7E8E9"
WHITE = RGBColor(255,255,255)
ACCENT = RGBColor(47,50,54)

def set_cell_shading(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tcPr.append(shd)

def set_cell_margins(cell, top=70, start=100, bottom=70, end=100):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = tcPr.first_child_found_in("w:tcMar")
    if tcMar is None:
        tcMar = OxmlElement("w:tcMar")
        tcPr.append(tcMar)
    for m, v in [("top",top),("start",start),("bottom",bottom),("end",end)]:
        node = tcMar.find(qn(f"w:{m}"))
        if node is None:
            node = OxmlElement(f"w:{m}")
            tcMar.append(node)
        node.set(qn("w:w"), str(v))
        node.set(qn("w:type"), "dxa")

def remove_table_borders(table):
    tblPr = table._tbl.tblPr
    borders = tblPr.first_child_found_in("w:tblBorders")
    if borders is None:
        borders = OxmlElement("w:tblBorders")
        tblPr.append(borders)
    for edge in ("top","left","bottom","right","insideH","insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "nil")
        borders.append(el)

def header(cell, text):
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(text)
    r.bold = True
    r.font.name = "Aptos"
    r.font.size = Pt(10.5)
    r.font.color.rgb = WHITE
    set_cell_shading(cell, DARK)
    set_cell_margins(cell, 80, 130, 80, 130)

def add_line(cell, text, bold=False, size=8.5, space=1.5):
    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(space)
    p.paragraph_format.line_spacing = 1.0
    r = p.add_run(text)
    r.bold = bold
    r.font.name = "Aptos"
    r.font.size = Pt(size)
    return p

# Main two-column structure
table = doc.add_table(rows=1, cols=2)
table.autofit = False
remove_table_borders(table)
left, right = table.rows[0].cells
left.width = Inches(2.55)
right.width = Inches(4.65)
set_cell_margins(left, 120, 130, 80, 130)
set_cell_margins(right, 120, 150, 80, 150)
left.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
right.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP

# LEFT COLUMN — template-inspired
p = left.paragraphs[0]
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(3)
r = p.add_run("PHOTO")
r.bold = True
r.font.size = Pt(8)
r.font.color.rgb = RGBColor(130,130,130)

# Photo placeholder
photo = left.add_table(rows=1, cols=1)
photo.autofit = False
photo.cell(0,0).width = Inches(1.75)
photo.cell(0,0).height = Inches(1.65)
set_cell_shading(photo.cell(0,0), "F5F5F5")
set_cell_margins(photo.cell(0,0), 450, 50, 450, 50)
pp = photo.cell(0,0).paragraphs[0]
pp.alignment = WD_ALIGN_PARAGRAPH.CENTER
rr = pp.add_run("Insert photo")
rr.font.size = Pt(8)
rr.font.color.rgb = RGBColor(130,130,130)
remove_table_borders(photo)

# Name
p = left.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_before = Pt(8)
p.paragraph_format.space_after = Pt(1)
r = p.add_run("FAVOUR SAMUEL NYA")
r.bold = True
r.font.size = Pt(14)
r.font.color.rgb = ACCENT

p = left.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(9)
r = p.add_run("JUNIOR SOFTWARE DEVELOPER")
r.bold = True
r.font.size = Pt(8.5)

header(left, "✆  CONTACT")
add_line(left, "Email: favoursamuelnya@gmail.com")
add_line(left, "Phone: [ADD PHONE NUMBER]")
add_line(left, "Location: Lagos, Nigeria")
add_line(left, "LinkedIn: linkedin.com/in/favour-nya-a5b30525")
add_line(left, "GitHub: [ADD GITHUB URL]")

p = left.add_paragraph()
p.paragraph_format.space_before = Pt(8)
p.paragraph_format.space_after = Pt(3)
r = p.add_run("⚙  SKILLS")
r.bold = True
r.font.size = Pt(10.5)
r.font.color.rgb = WHITE
set_cell_shading(p._p.getparent().getparent().cells[0] if False else left, DARK)
# Undo: instead create a compact dark skill label via paragraph shading
pPr = p._p.get_or_add_pPr()
shd = OxmlElement("w:shd"); shd.set(qn("w:fill"), DARK); pPr.append(shd)
for label, value in [
    ("Languages", "Python, Go, SQL"),
    ("Backend", "REST APIs, HTTP, JSON, FastAPI"),
    ("Databases", "PostgreSQL, MySQL"),
    ("Data", "pandas, NumPy, Excel"),
    ("Tools", "Git, GitHub, Linux, Docker"),
    ("AI", "Prompt engineering, AI integration"),
]:
    add_line(left, f"{label}: {value}")

# RIGHT COLUMN
header(right, "👤  ABOUT ME")
add_line(right,
          "Junior software developer with hands-on experience building backend applications and "
          "data-driven tools using Python, Go, SQL, REST APIs, Git, Linux, and Docker. Currently "
          "completing intensive AI-native full-stack development training while pursuing a Bachelor’s "
          "degree in Information Technology. Experienced in data reconciliation, cleaning, reporting, "
          "and high-volume spreadsheet work through the Nigerian Civil Aviation Authority.")

header(right, "🎓  EDUCATION")
add_line(right, "Bachelor’s Degree, Information Technology", True, 9.0, 0.5)
add_line(right, "Brigham Young University–Pathway | Expected Mar 2029", size=8)
add_line(right, "Ordinary National Diploma, Computer Science & Information Technology", True, 9.0, 0.5)
add_line(right, "Petroleum Training Institute | Dec 2024", size=8)
add_line(right, "O’ Level", True, 9.0, 0.5)
add_line(right, "Federal Science and Technical College | Aug 2022", size=8)

header(right, "💼  WORK EXPERIENCE")
add_line(right, "AI-Native Full-Stack Development Fellow — Learn2Earn / 01 Edu", True, 9.0, 0.5)
add_line(right, "Feb 2026 – Present", size=8)
add_line(right, "• Build project-based applications with Python, Go, SQL, APIs, Git, Linux, Docker, and AI integration.")
add_line(right, "• Develop backend services and practice requirements analysis, debugging, and collaborative software development.")
add_line(right, "• Apply database design, REST API concepts, version control, and AI-assisted development workflows.")

add_line(right, "Data Analysis Intern — Nigerian Civil Aviation Authority (NCAA)", True, 9.0, 0.5)
add_line(right, "Internship", size=8)
add_line(right, "• Prepared and reconciled airline account, invoice, and passenger ticket-sales records.")
add_line(right, "• Cleaned, organized, and summarized high-volume Excel datasets for monthly revenue reporting.")
add_line(right, "• Analyzed national and international airline revenue data and produced reporting summaries.")

header(right, "🛠  PROJECTS")
add_line(right, "Task Management REST API | Go", True, 9.0, 0.5)
add_line(right, "• Built a backend API for creating, retrieving, and deleting tasks using Go’s standard HTTP tooling.")
add_line(right, "Ascii-Art-Web | Go", True, 9.0, 0.5)
add_line(right, "• Developed a web application using HTTP handlers and templates; containerized it with Docker.")
add_line(right, "Student Management System | Python + PostgreSQL", True, 9.0, 0.5)
add_line(right, "• Built a CLI student database and wrote SQL queries for filtering, grouping, aggregation, and statistics.")
add_line(right, "Mad Libs | Python", True, 9.0, 0.5)
add_line(right, "• Developed an interactive CLI program with multiple choices, case-insensitive input, and distinct outcomes.")

header(right, "📜  CERTIFICATIONS")
add_line(right, "DataCamp: Introduction to SQL • Introduction to Python • Intermediate Python • Prompt Engineering")

# Footer note
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_before = Pt(3)
r = p.add_run("Replace bracketed fields and add any missing information before submitting.")
r.italic = True
r.font.size = Pt(7.5)
r.font.color.rgb = RGBColor(110,110,110)

path = "jpeg(11)"
doc.save(path)
print(path)
