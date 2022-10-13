import fitz


def extract_info(input_file: str):
    # Extracts file info
    # Open the PDF
    pdfDoc = fitz.open(input_file)
    output = {
        "File": input_file, "Encrypted": ("True" if pdfDoc.isEncrypted else "False")
    }


def highlight(page, duplicate_text, type):
    #To Highlight matching text
    
    match_found = 0
    # Loop throughout matching values
    for i in duplicate_text:
        match_found += 1
        matching_val_area = page.searchFor(i)
        # print("matching_val_area",matching_val_area)
        highlight = None
        if type == 'Highlight':
            highlight = page.addHighlightAnnot(matching_val_area)
        else:
            highlight = page.addHighlightAnnot(matching_val_area)
        highlight.update()
    return match_found