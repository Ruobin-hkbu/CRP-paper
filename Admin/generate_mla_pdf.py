from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

SOURCE = Path(r"c:\Users\ruobin Yu\.vscode\CRP-paper-1\Admin\Research_Proposal_Marcuse_Haraway_AI_Poetry.md")
OUTPUT = Path(r"c:\Users\ruobin Yu\.vscode\CRP-paper-1\Admin\Research_Proposal_Marcuse_Haraway_AI_Poetry_MLA.pdf")

PAGE_W, PAGE_H = A4
MARGIN = 72  # 1 inch
FONT = "Times-Roman"
SIZE = 12
LEADING = 24  # double spacing

AUTHOR = "Ruobin Yu"
INSTRUCTOR = "Instructor Name"
COURSE = "Course Name"
DATE = "9 April 2026"
LAST_NAME = "Yu"

def strip_markdown(line: str) -> str:
    text = line.rstrip()
    if not text.strip():
        return ""

    # Remove heading markers
    text = text.lstrip("#").strip()

    # Convert markdown bullets to plain bullets
    if text.startswith("- "):
        text = "- " + text[2:].strip()

    # Remove emphasis markers
    for token in ("**", "*"):
        text = text.replace(token, "")

    return text


def wrap_text(text: str, max_width: float):
    words = text.split()
    if not words:
        return [""]

    lines = []
    current = words[0]

    for word in words[1:]:
        trial = current + " " + word
        if pdfmetrics.stringWidth(trial, FONT, SIZE) <= max_width:
            current = trial
        else:
            lines.append(current)
            current = word

    lines.append(current)
    return lines


def draw_header(c: canvas.Canvas, page_num: int):
    c.setFont(FONT, SIZE)
    c.drawRightString(PAGE_W - MARGIN, PAGE_H - MARGIN + 12, f"{LAST_NAME} {page_num}")


def new_page(c: canvas.Canvas, page_num: int):
    c.showPage()
    page_num += 1
    draw_header(c, page_num)
    return PAGE_H - MARGIN, page_num


def main():
    global FONT

    # Prefer true Times New Roman if available on Windows.
    tnr_path = Path(r"C:\Windows\Fonts\times.ttf")
    if tnr_path.exists():
        pdfmetrics.registerFont(TTFont("TimesNewRoman", str(tnr_path)))
        FONT = "TimesNewRoman"

    raw_lines = SOURCE.read_text(encoding="utf-8").splitlines()

    # Keep main prose; skip markdown title line and reference bullets for MLA body brevity
    body_lines = []
    in_refs = False
    for ln in raw_lines:
        if ln.strip().lower().startswith("## selected references"):
            in_refs = True
            continue
        if in_refs:
            continue
        cleaned = strip_markdown(ln)
        body_lines.append(cleaned)

    c = canvas.Canvas(str(OUTPUT), pagesize=A4)
    page_num = 1
    draw_header(c, page_num)

    y = PAGE_H - MARGIN
    text_width = PAGE_W - 2 * MARGIN

    c.setFont(FONT, SIZE)

    # MLA heading (double-spaced)
    heading = [AUTHOR, INSTRUCTOR, COURSE, DATE]
    for line in heading:
        c.drawString(MARGIN, y, line)
        y -= LEADING

    # Title centered, no bold/italics
    title = "The Machine Judges Before We Do: Iterative Human-AI Poetry Writing, One-Dimensionality, and the Pedagogy of Discernment"
    c.drawCentredString(PAGE_W / 2, y, title)
    y -= LEADING

    # Body paragraphs (double-spaced)
    for line in body_lines:
        if not line:
            y -= LEADING
            if y < MARGIN:
                y, page_num = new_page(c, page_num)
            continue

        wrapped = wrap_text(line, text_width)
        for out in wrapped:
            if y < MARGIN:
                y, page_num = new_page(c, page_num)
                c.setFont(FONT, SIZE)
            c.drawString(MARGIN, y, out)
            y -= LEADING

    c.save()
    print(f"Created: {OUTPUT}")


if __name__ == "__main__":
    main()
