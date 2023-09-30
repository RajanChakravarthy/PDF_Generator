from fpdf import FPDF
import pandas as pd

# A4 Size 210mm*298mm
pdf = FPDF(orientation='P', unit='mm', format='A4')
# text beyond the page dimensions will not be printed
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

for index, rows in df.iterrows():
    for i in range(rows['Pages']):
        pdf.add_page()
        # set header
        pdf.set_font(family='Times', style='B', size=24)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0, h=12, txt=rows['Topic'], align='L', ln=1)
        pdf.line(10,20,200,20)

        # creating line every 10mm
        for y in range(30,295,10):
            pdf.line(10, y, 200, y)

        # Line break to move the cursor to the end of page
        pdf.ln(265)

        # Creating footer
        pdf.set_font(family='Times', style='I', size=12)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0, h=12, txt=rows['Topic'], align='R', ln=1)


pdf.output('output.pdf')
