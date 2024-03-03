from fpdf import FPDF
from fpdf.enums import XPos, YPos, Align

class PDF(FPDF):

    _TOP_MARGIN = 20
    DEFAULT_FONT_FAMILY = "Helvetica"
    DEFAULT_FONT_SIZE = 12
    WHITE_COLOR = (255, 255, 255)
    BLACK_COLOR = (0, 0, 0)

    def add_title(
            self,
            title_text="",
            font_family=DEFAULT_FONT_FAMILY,
            font_size: int=DEFAULT_FONT_SIZE
    ):

        # set the font proprties for the text that will be added to PDF page
        self.set_font(font_family, size=font_size)
        self.set_text_color(self.BLACK_COLOR)

        # get the title text width to be horizontally centered
        title_text_width = self.get_string_width(title_text)

        # calculate the x position to set text horizontally center to the PDF page
        x_position = (self.w - title_text_width) / 2
        y_position = self.t_margin + self._TOP_MARGIN

        # set the text title position and add it to the PDF page
        self.set_y(y_position)
        self.set_x(x_position)
        self.cell(
            w=title_text_width,
            text=title_text,
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
            align=Align.C
        )

    def add_image_with_text(
            self,
            image_path="",
            image_text="",
            font_family=DEFAULT_FONT_FAMILY,
            font_size: int= DEFAULT_FONT_SIZE
    ):

        # calculate image position
        x_image_position = self.l_margin
        y_image_position = self.get_y() + self._TOP_MARGIN + 3

        # calculate image width size to fit in the PDF page
        page_width = self.w - (2 * self.l_margin)

        # add image to the PDF page
        self.image(
            x=x_image_position,
            y=y_image_position,
            name=image_path,
            w=page_width
        )

        # set PDF Y position equal to the image Y position
        self.set_y(y_image_position)

        # set the text font properties
        self.set_font(font_family, size=font_size)
        self.set_text_color(self.WHITE_COLOR)

        # get the text width to be horizontally centered
        text_width = self.get_string_width(image_text)

        # calculate text position
        x_text_position = (self.w - text_width) / 2
        y_text_position = self.get_y() + 62

        # set text position and add it to the PDF page
        self.set_y(y_text_position)
        self.set_x(x_text_position)
        self.cell(
            w=text_width,
            text=image_text,
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
            align=Align.C
        )