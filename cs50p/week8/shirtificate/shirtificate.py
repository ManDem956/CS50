from fpdf import FPDF

IMAGE_NAME = "shirtificate.png"
OUTPUT = "shirtificate.pdf"


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 30)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(50, 50, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)

    def chapter_body(self, image, message):
        self.set_fill_color(0, 0, 0)
        self.add_page()
        self.set_font("helvetica", "B", 30)
        self.image(image, x=10, y=70, w=190)
        self.set_text_color(255, 255, 255)
        self.cell(
                190,
                190,
                message,
                border=0,
                align="C",
        )


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def main() -> None:
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.chapter_body(IMAGE_NAME, f"{get_user_input("Name")} took CS50p")

    pdf.output(OUTPUT)


if __name__ == "__main__":
    main()
