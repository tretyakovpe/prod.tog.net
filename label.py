from labelFields import labelFields
import code128
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A5
from reportlab.lib.units import mm

class label:
# Список линий для печати бирки
# X1 | Y1 | X2 | Y2
# Линия рисуется из точки (X1,Y1) в точку (X2,Y2)
#

    borders = [ [5, 5, 205, 5],
            [5, 30, 205, 30],
            [5, 55, 205, 55],
            [5, 80, 205, 80],
            [5, 105, 205, 105],
            [5, 130, 205, 130],
            [5, 140, 205, 140],
            [105, 42, 205, 42],
            [5, 5, 5, 140],
            [105, 5, 105, 55],
            [138, 42, 138, 55],
            [171, 42, 171, 55],
            [105, 80, 105, 140],
            [205, 5, 205, 140]
        ]

    def __init__(self):
        pass

    def make(self,file = "label.pdf"):
        """
        Makes a PDF file of shipping label
        """
        c = canvas.Canvas(file, landscape(A5), 0)
        # Draw the table lines
        for l in self.borders:
            c.line(l[0]*mm,l[1]*mm,l[2]*mm,l[3]*mm)
        # Fill data in template
        for f in labelFields:
            # If barcode is needed, add related fields
            if f[4]:
                self._fillForm(c,f[0],f[1],f[2],f[3],f[4],f[5])
            else:
                self._fillForm(c,f[0],f[1],f[2],f[3])
        c.showPage()
        c.save()
    
    def _fillForm(self, c: canvas, x, y, description, value, barcode = False, startChar = None):
        c.setFont('Helvetica',8)
        c.drawString(x*mm,y*mm,description)
        c.setFont('Helvetica-Bold',16)
        c.drawString((x+1)*mm, (y+5)*mm, value)
        if barcode:
            bc = code128.image(startChar+value,100,4,False)
            c.drawInlineImage(bc, 60+x*mm, y*mm, 160, 30, True)