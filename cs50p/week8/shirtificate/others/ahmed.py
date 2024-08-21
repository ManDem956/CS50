from fpdf import FPDF


def main():

    name = input("Name: ")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 45)
    pdf.set_xy(80, 15)
    pdf.cell(50, 30, "CS50 Shirtificate", align='c')
    pdf.image("/workspaces/175999125/problem_set_8/shirtificate.png", 5, 60, 200)
    pdf.set_font(size=30)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.set_xy(75, 105)
    pdf.cell(60, 30, f"{name} took CS50", align='c')
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
