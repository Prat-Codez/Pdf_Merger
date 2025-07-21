import PyPDF2
print("Hello!!")
print("Welcome to PDF_Merger!!")
pdfiles=["Name of  pdf file 1","Name of  pdf file 2","Name of  pdf file 3","etc."]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdffiles = open(filename,"rb")
    pdfReader = PyPDF2.PdfReader(pdffiles)
    merger.append(pdfReader)
    pdffiles.close()
merger.write("merged.pdf")
print("Merged PDF file is ready to use.")
number_of_pages = len(merger.pages)
print(f"Number of pages: {number_of_pages}")
print("Thank you for using this program")