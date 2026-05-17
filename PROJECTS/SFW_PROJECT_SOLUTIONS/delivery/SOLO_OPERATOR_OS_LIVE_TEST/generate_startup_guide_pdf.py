from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)
from pathlib import Path


BASE = Path(__file__).resolve().parent
PDF_PATH = BASE / "SOLO_OPERATOR_STARTUP_GUIDE.pdf"


def p(text, style):
    return Paragraph(text, style)


def code(text):
    safe = text.replace("\\", "\\\\")
    return Paragraph(safe, styles["CodeBlock"])


def section(title):
    return [Spacer(1, 8), p(title, styles["H2"]), Spacer(1, 4)]


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="TitleLarge",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=26,
        leading=31,
        textColor=colors.HexColor("#17202a"),
        alignment=TA_LEFT,
        spaceAfter=12,
    )
)
styles.add(
    ParagraphStyle(
        name="Intro",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=12,
        leading=17,
        textColor=colors.HexColor("#5f6f7c"),
        spaceAfter=14,
    )
)
styles.add(
    ParagraphStyle(
        name="H2",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=21,
        textColor=colors.HexColor("#17202a"),
        spaceBefore=8,
        spaceAfter=6,
    )
)
styles.add(
    ParagraphStyle(
        name="Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=15,
        textColor=colors.HexColor("#17202a"),
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        name="Small",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#5f6f7c"),
        spaceAfter=6,
    )
)
styles.add(
    ParagraphStyle(
        name="CodeBlock",
        parent=styles["BodyText"],
        fontName="Courier",
        fontSize=9,
        leading=12,
        backColor=colors.HexColor("#f4f7f8"),
        borderColor=colors.HexColor("#d9e1e7"),
        borderWidth=0.5,
        borderPadding=6,
        spaceBefore=4,
        spaceAfter=10,
    )
)


story = []

story.append(p("Solo Operator OS", styles["Small"]))
story.append(p("Start-Up And User Guide", styles["TitleLarge"]))
story.append(
    p(
        "A plain-English guide for opening, starting, testing, and using the Solo Operator OS live-test build in Claude.",
        styles["Intro"],
    )
)

story += section("1. What This System Is")
story.append(
    p(
        "Solo Operator OS is a personal AI operating system for a solo entrepreneur, freelancer, consultant, creator, or busy professional.",
        styles["Body"],
    )
)
story.append(
    p(
        "It helps one person manage work, business actions, personal admin, ideas, relationships, decisions, follow-ups, and weekly priorities through a structured Claude folder.",
        styles["Body"],
    )
)
story.append(
    p(
        "<b>Simple version:</b> this is not a normal AI chat. It is a repeatable operating system with commands, context files, trackers, routines, and review steps.",
        styles["Body"],
    )
)

story += section("2. Where To Start")
story.append(p("Open this folder in Claude:", styles["Body"]))
story.append(
    code(
        r"D:\Axis AI - ChatGPT OS\AXIS_OS_CLAUDE_BUILD\PROJECTS\SFW_PROJECT_SOLUTIONS\delivery\SOLO_OPERATOR_OS_LIVE_TEST"
    )
)
story.append(p("Start by reading these files:", styles["Body"]))
for item in [
    "README.md",
    "START_HERE.md",
    "PERSONAL_CONTEXT.md",
    "LIVE_TEST_SCRIPT.md",
    "ACCEPTANCE_CHECKLIST.md",
]:
    story.append(p(f"- {item}", styles["Body"]))

story += section("3. First Command To Type")
story.append(p("In Claude, type:", styles["Body"]))
story.append(code("AXIS: SOLO START"))
story.append(
    p(
        "Expected result: Claude reads the live-test context, sees setup is already complete, does not repeat first-time onboarding, and offers the main operating choices.",
        styles["Body"],
    )
)

story += section("4. Main Commands")
commands = [
    ["Command", "Use It For"],
    ["AXIS: SOLO START", "Start the Solo Operator OS and choose what to do next."],
    ["AXIS: DAILY COMMAND", "Set today's priorities, admin actions, follow-ups, and focus plan."],
    ["AXIS: CAPTURE THIS", "Turn a messy note, idea, message, or voice-note transcript into action."],
    ["AXIS: DECISION", "Compare options, trade-offs, risks, and next steps."],
    ["AXIS: ADMIN CLEAR-DOWN", "Sort personal or business admin into a clear action list."],
    ["AXIS: BUSINESS BUILDER", "Move offers, leads, pricing, delivery, content, or revenue actions forward."],
    ["AXIS: WEEKLY REVIEW", "Review wins, open loops, decisions, admin, follow-ups, and next week."],
    ["AXIS: 30 DAY REVIEW", "Review clarity, follow-through, admin, business progress, relationships, and system fit."],
]
table = Table(commands, colWidths=[58 * mm, 106 * mm], repeatRows=1)
table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f4f7f8")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#17202a")),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTNAME", (0, 1), (0, -1), "Courier"),
            ("FONTSIZE", (0, 0), (-1, -1), 8.8),
            ("LEADING", (0, 0), (-1, -1), 11),
            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d9e1e7")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ]
    )
)
story.append(table)

story += section("5. How To Run The Live Test")
for item in [
    "Open the live-test folder in Claude.",
    "Type AXIS: SOLO START.",
    "Open LIVE_TEST_SCRIPT.md.",
    "Run each test prompt in order.",
    "After each test, update LIVE_TEST_LOG.md.",
    "When finished, complete ACCEPTANCE_CHECKLIST.md.",
]:
    story.append(p(f"- {item}", styles["Body"]))
story.append(
    p(
        "<b>Pass standard:</b> output should be specific, practical, calm, and action-focused. It should reference the right trackers and avoid acting like a generic chatbot.",
        styles["Body"],
    )
)

story.append(PageBreak())
story += section("6. What Each Folder Does")
folders = [
    ["Folder / File", "Purpose"],
    ["PERSONAL_CONTEXT.md", "User context, priorities, preferences, and setup status."],
    ["COMMAND_CENTRE", "Daily command centre for priorities and focus."],
    ["TRACKERS", "Open loops, waiting items, closed items, and review state."],
    ["LIFE_ADMIN", "Personal admin, deadlines, documents, renewals, and practical tasks."],
    ["BUSINESS", "Offers, leads, content, clients, delivery, revenue, and business actions."],
    ["RELATIONSHIPS", "Follow-ups, useful context, introductions, and relationship memory."],
    ["IDEAS", "Idea capture and idea-to-action processing."],
    ["DECISIONS", "Decision log and decision support."],
    ["KNOWLEDGE", "Durable preferences, rules, goals, and project context."],
    ["ROUTINES", "Weekly review and 30-day review workflows."],
]
folder_table = Table(folders, colWidths=[58 * mm, 106 * mm], repeatRows=1)
folder_table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f4f7f8")),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTNAME", (0, 1), (0, -1), "Courier"),
            ("FONTSIZE", (0, 0), (-1, -1), 8.8),
            ("LEADING", (0, 0), (-1, -1), 11),
            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d9e1e7")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ]
    )
)
story.append(folder_table)

story += section("7. What Good Use Looks Like")
for item in [
    "Start the day with AXIS: DAILY COMMAND.",
    "Capture ideas immediately with AXIS: CAPTURE THIS.",
    "Use AXIS: DECISION before changing direction.",
    "Run AXIS: ADMIN CLEAR-DOWN when tasks feel scattered.",
    "End the week with AXIS: WEEKLY REVIEW.",
]:
    story.append(p(f"- {item}", styles["Body"]))

story += section("8. Important Boundaries")
story.append(
    p(
        "Solo Operator OS supports organisation, planning, drafting, workflow management, decision clarity, and follow-through. It does not replace legal, financial, tax, medical, therapeutic, safeguarding, or regulated professional advice.",
        styles["Body"],
    )
)
story.append(
    p(
        "If a topic is high-risk, the OS should help prepare questions and organise information, then recommend speaking to a qualified professional.",
        styles["Body"],
    )
)

story += section("9. How To Test First-Time Setup Later")
story.append(p("The live-test build is already configured. To test first-time onboarding later, read:", styles["Body"]))
story.append(code("RESET_FOR_FIRST_TIME_SETUP.md"))

story += section("10. When It Is Ready To Use Externally")
for item in [
    "LIVE_TEST_LOG.md is completed.",
    "ACCEPTANCE_CHECKLIST.md passes.",
    "Pricing and packaging are approved.",
    "Data and professional-advice boundaries are clear.",
    "Wayne signs off the build.",
]:
    story.append(p(f"- {item}", styles["Body"]))

story.append(Spacer(1, 12))
story.append(
    p(
        "Solo Operator OS is developed by Wayne Francis and delivered through SF&W Project Solutions. Document status: in review. Created for live testing before external use.",
        styles["Small"],
    )
)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#5f6f7c"))
    canvas.drawString(14 * mm, 10 * mm, "Solo Operator OS Start-Up Guide")
    canvas.drawRightString(196 * mm, 10 * mm, f"Page {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(
    str(PDF_PATH),
    pagesize=A4,
    rightMargin=14 * mm,
    leftMargin=14 * mm,
    topMargin=14 * mm,
    bottomMargin=16 * mm,
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(PDF_PATH)
