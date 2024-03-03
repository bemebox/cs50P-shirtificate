from sys import exit
from pdf import PDF

def main():
    try:
        input_name = input("Name: ").strip()

        # create PDF page with portrait orientation and A4 format
        pdf = PDF(orientation="portrait", format="A4")

        # add new PDF page with default font family and size, with white background color
        pdf.set_font(pdf.DEFAULT_FONT_FAMILY, size=pdf.DEFAULT_FONT_SIZE)
        pdf.set_page_background(pdf.WHITE_COLOR)
        pdf.add_page()

        # add centered text title to the PDF page
        pdf.add_title(
            title_text="CS50 Shirtificate",
            font_size=48
        )

        # add image with text to the PDF page
        pdf.add_image_with_text(
            image_path="shirtificate.png",
            image_text=input_name + " took CS50",
            font_size=24
        )

        # save the PDF file
        pdf.output("shirtificate.pdf")

    except ValueError:
        exit("Error: Something went wrong.")


if __name__ == "__main__":
    main()
