from fpdf import FPDF
from PIL import Image


class PDF(FPDF):

    def add_title(self, title, font_size: int = 30, font_family="Helvetica"):
        # set the font properties for the text that will be added to the PDF
        self.set_font(font_family, size=font_size)

        # calculate the width of the title text
        title_width = self.get_string_width(title)

        # calculate the position to horizontally center the text
        x_position = (self.w - title_width) / 2

        # set position and add the title text
        self.set_x(x_position)
        self.cell(title_width, 57, title, ln=True, align="C")

    def add_image_with_text(
        self, image_path, text, font_size: int = 30, font_family="Helvetica"
    ):
        # Calculate the center position for the image
        page_width = self.w - 2 * self.l_margin
        image_width = 0  # The width will be determined later

        # Get the size of the image
        with Image.open(image_path) as img:
            image_w, image_h = img.size
        aspect_ratio = image_w / image_h

        # Calculate the maximum width and height based on the page width and height
        max_width = page_width
        max_height = max_width / aspect_ratio

        # Adjust the image width and height if it exceeds the available space
        if max_height > self.h - 2 * self.t_margin:
            max_height = self.h - 2 * self.t_margin
            max_width = max_height * aspect_ratio

        image_width = max_width

        # Calculate the center position for the image
        x_position = (page_width - image_width) / 2 + self.l_margin

        # Add the image to the PDF
        self.image(image_path, x_position, 70, w=image_width)

        # Set font for the text
        self.set_font(font_family, size=font_size)
        self.set_text_color((255, 255, 255))

        # Add text in front of the image
        self.multi_cell(page_width, 138, text, align="C")

        # Restore text color to black (default)
        self.set_text_color(0, 0, 0)
