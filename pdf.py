from fpdf import FPDF


class PDF(FPDF):
    # Method to add a line with line break for long strings
    def multi_cell_line(self, w, h, txt, border=0, align='L'):
        """
        This method allows the addition of a cell with the possibility of line breaks.
        It will split the `txt` into lines if it's too long.
        """
        # Split the text by lines and then by words to wrap within our width limit.
        lines = txt.split("\n")
        for line in lines:
            words = line.split()
            line = ''
            for word in words:
                line_with_word = f"{line} {word}".strip()
                if self.get_string_width(line_with_word) > w:
                    self.multi_cell(w, h, line, border=border, align=align)
                    line = word
                else:
                    line = line_with_word
            if line:
                self.multi_cell(w, h, line, border=border, align=align)

    # Method to draw a dashed line
    def dashed_line(self, x1, y1, x2, y2, dash_length=1, space_length=1):
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.2)
        x = x1
        y = y1
        if (x2 - x1) > (y2 - y1):  # Horizontal line
            while x < x2:
                x2_temp = x + dash_length if x + dash_length < x2 else x2
                self.line(x, y, x2_temp, y)
                x = x + dash_length + space_length
        else:  # Vertical line
            while y < y2:
                y2_temp = y + dash_length if y + dash_length < y2 else y2
                self.line(x, y, x, y2_temp)
                y = y + dash_length + space_length