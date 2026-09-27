from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, ListFlowable, ListItem


def build_resume_pdf(output_path="Shanvi_Chaudhary_Resume.pdf"):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "Title",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=24,
        textColor=colors.black,
        alignment=1,
        spaceAfter=4,
    )
    heading_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=14,
        textColor=colors.HexColor("#1f4e79"),
        spaceBefore=12,
        spaceAfter=8,
        borderWidth=1,
        borderColor=colors.HexColor("#dfe4ea"),
        borderPadding=4,
        borderBottom=1,
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=colors.black,
        spaceAfter=4,
    )
    small_style = ParagraphStyle(
        "Small",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#495463"),
    )

    story = []

    story.append(Paragraph("Shanvi Chaudhary", title_style))
    story.append(Paragraph("B.Tech Computer Science Engineering (CSE) | Batch 2029", small_style))
    story.append(Paragraph("Madan Mohan Malaviya University of Technology, Gorakhpur", small_style))
    story.append(Paragraph("Cybersecurity & Embedded Systems Enthusiast", ParagraphStyle("Badge", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=8, leading=10, textColor=colors.HexColor("#1f4e79"), spaceBefore=6, spaceAfter=8, borderWidth=1, borderColor=colors.HexColor("#d5e4f7"), borderPadding=4, backColor=colors.HexColor("#eaf2fb"), alignment=1)))
    story.append(Spacer(1, 10))

    contact_table = Table(
        [[Paragraph("Phone: 9696809253"), Paragraph("Email: ak84159156@gmail.com")]],
        colWidths=[140, 200],
        style=[
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ],
    )
    story.append(contact_table)
    story.append(Spacer(1, 12))

    story.append(Paragraph("Career Objective", heading_style))
    story.append(
        Paragraph(
            "Motivated and academically driven B.Tech CSE student with a strong interest in cybersecurity, embedded systems, and semiconductor design. "
            "Eager to deepen technical expertise in problem-solving, system design, and secure engineering practices while contributing to innovation through NXP's Women in Tech (WIT) Program.",
            body_style,
        )
    )

    story.append(Paragraph("Education", heading_style))
    education_data = [
        [Paragraph("<b>Examination</b>"), Paragraph("<b>Institution / Board</b>"), Paragraph("<b>Year</b>"), Paragraph("<b>Score</b>")],
        ["B.Tech (CSE) - 1st Year", "MMMUT, Gorakhpur", "2025-26", "9.1 CGPA"],
        ["Class XII", "Carmel Girls Inter College", "2025", "86.4%"],
        ["Class X", "Carmel Girls Inter College", "2023", "92.2%"],
    ]
    edu_table = Table(education_data, colWidths=[55 * mm, 60 * mm, 22 * mm, 25 * mm])
    edu_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eaf2fb")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#dfe4ea")),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(edu_table)

    story.append(Paragraph("Technical Skills", heading_style))
    skill_items = [
        "C",
        "C++",
        "Python",
        "Java",
        "Data Structures",
        "Programming Logic",
        "Cybersecurity Fundamentals",
        "Embedded Systems",
        "IoT Basics",
    ]
    skill_list = ListFlowable(
        [ListItem(Paragraph(item, body_style), bulletType="bullet", bulletColor=colors.HexColor("#1f4e79")) for item in skill_items],
        bulletType="bullet",
        leftIndent=18,
        spaceBefore=0,
        spaceAfter=2,
    )
    story.append(skill_list)

    story.append(Paragraph("Projects", heading_style))
    for title, desc in [
        ("Student/Management System (C Language)", "Console-based system to add, search, update, and delete records; file handling and structured programming."),
        ("Mini Game (C Language)", "Interactive game using logic building, loops, and conditional programming."),
        ("Phone-Controlled Robotic Car (ESP32 / IoT)", "Robotic car controlled via mobile phone, built during a college robotics workshop on IoT fundamentals."),
    ]:
        story.append(Paragraph(f"<b>{title}</b>", body_style))
        story.append(Paragraph(desc, body_style))
        story.append(Spacer(1, 4))

    story.append(Paragraph("Certifications & Achievements", heading_style))
    certs = [
        "Completed an 80-hour AI Bootcamp",
        "Participated in college-level Hackathon (team ranked 4th)",
        "Attended a college workshop on Robotics and IoT (ESP32-based)",
    ]
    story.append(ListFlowable([ListItem(Paragraph(c, body_style), bulletType="bullet", bulletColor=colors.HexColor("#1f4e79")) for c in certs], bulletType="bullet", leftIndent=18, spaceBefore=0, spaceAfter=2))

    story.append(Paragraph("Extracurricular Activities", heading_style))
    story.append(ListFlowable([ListItem(Paragraph("Member, Fine Arts Club, College (1st Year)", body_style), bulletType="bullet", bulletColor=colors.HexColor("#1f4e79"))], bulletType="bullet", leftIndent=18, spaceBefore=0, spaceAfter=2))

    story.append(Paragraph("Strengths", heading_style))
    strengths = [
        "Strong foundation in Data Structures and Programming Logic",
        "Quick learner, keen interest in VLSI, Embedded Systems, and Semiconductor Design",
        "Good analytical and problem-solving skills",
    ]
    story.append(ListFlowable([ListItem(Paragraph(s, body_style), bulletType="bullet", bulletColor=colors.HexColor("#1f4e79")) for s in strengths], bulletType="bullet", leftIndent=18, spaceBefore=0, spaceAfter=2))

    doc.build(story)
    print(f"PDF generated: {output_path}")


if __name__ == "__main__":
    build_resume_pdf()
