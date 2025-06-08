from fpdf import FPDF

def create_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Financial Report", ln=True)
    pdf.cell(200, 10, txt="Goal Forecasting and Risk Analysis", ln=True)
    pdf.output("financial_report.pdf")