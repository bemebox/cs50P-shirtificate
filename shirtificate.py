from sys import exit
from pdf import PDF


def main():
    try:
        input_name = input("Name: ").strip()

        # create instance of FPDF class with portrait orientation and A4 format
        pdf = PDF(orientation="P", unit="mm", format="A4")

        # add a page
        pdf.add_page()

        # set the default font type and size
        pdf.set_font("Helvetica", size=12)

        # add a text title to the page
        pdf.add_title("CS50 Shirtificate", 48, "Helvetica")

        # add image to the page
        pdf.add_image_with_text(
            "shirtificate.png", f"{input_name} took CS50", 24, "Helvetica"
        )

        # save the pdf file
        pdf.output("shirtificate.pdf")

    except ValueError:
        exit("something went wrong")


if __name__ == "__main__":
    main()
