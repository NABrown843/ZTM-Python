import PyPDF2
import sys
import os

parent_dir = os.getcwd()
file_folder = os.path.join(parent_dir, sys.argv[1])
watermark_file = os.path.join(parent_dir, sys.argv[2])

def pdf_combine_watermark(file_folder, watermark_file):

	pdf_list = []
	for file in os.listdir(file_folder):
		pdf_list.append(f'{file_folder}{file}')

	watermark_file = PyPDF2.PdfFileReader(open(watermark_file, 'rb'))	

	pdf_writer = PyPDF2.PdfFileWriter()
	for pdf in pdf_list:
		pdf_reader = PyPDF2.PdfFileReader(open(pdf, 'rb'))
		for page in range(pdf_reader.getNumPages()):
			page = pdf_reader.getPage(page)
			page.mergePage(watermark_file.getPage(0))
			pdf_writer.addPage(page)

			with open('watermarked_pdf.pdf', 'wb') as out:
				pdf_writer.write(out)


pdf_combine_watermark(file_folder, watermark_file)