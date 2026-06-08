import fitz  # PyMuPDF
import os

def extract_slides_from_pdf(pdf_path, output_folder="extracted_slides", slides_to_extract=None):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the PDF file
    try:
        pdf_document = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error opening PDF: {e}")
        return

    total_slides = len(pdf_document)

    # Determine which pages to process
    if slides_to_extract is None:
        # If no specific list is provided, extract everything
        pages_to_process = range(total_slides)
        print(f"Successfully opened {pdf_path}. Extracting all {total_slides} slides...")
    else:
        # Convert user's 1-based slide numbers to Python's 0-based page index
        pages_to_process = []
        for slide_num in slides_to_extract:
            if 1 <= slide_num <= total_slides:
                pages_to_process.append(slide_num - 1)
            else:
                print(f"Warning: Slide {slide_num} does not exist in this {total_slides}-page PDF. Skipping.")
        
        print(f"Successfully opened {pdf_path}. Extracting {len(pages_to_process)} specific slide(s)...")

    # Iterate through the selected pages
    for page_number in pages_to_process:
        page = pdf_document.load_page(page_number)

        # Set the resolution (zoom factor). 
        zoom_x = 2.0
        zoom_y = 2.0
        matrix = fitz.Matrix(zoom_x, zoom_y)

        # Render the page to an image (pixmap)
        pix = page.get_pixmap(matrix=matrix)

        # Format the filename with leading zeros based on the actual slide number
        slide_label = page_number + 1
        filename = f"slide_{slide_label:03d}.png"
        output_path = os.path.join(output_folder, filename)

        # Save the image
        pix.save(output_path)
        print(f"Saved: {filename}")

    pdf_document.close()
    print("Extraction complete!")

# --- How to use ---
if __name__ == "__main__":
    pdf_file_path = "Chapter_4_combined.pdf" #change to correct chapter PDF file path
    
    # Put the exact slide numbers you want in this list (e.g., slides 1, 4, 5, and 12)
    my_slides = [3, 4, 5, 6, 7, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 30, 31, 32, 33]

    my_slides_l1 = [8, 17, 19, 25, 28, 30, 32, 43, 48, 51]

    my_slides_l2 = [18, 61, 83, 84, 88, 89, 99, 106, 113]

    my_slides_l3 = [12, 22, 23, 26, 37, 39, 41, 45, 47, 49]

    my_slides_l4 = [11, 13, 21, 35, 49, 51, 62, 64, 67, 77, 78]

    my_slides_l5 = []

    my_slides_l6 = []

    my_slides_l7 = []


    # Run the function with the specific list
    extract_slides_from_pdf(
        pdf_path=pdf_file_path, 
        output_folder="lecture_4", 
        slides_to_extract=my_slides_l4
    )
    
    # NOTE: If you ever want to go back to extracting ALL slides, 
    # just remove the `slides_to_extract` part like this:
    # extract_slides_from_pdf(pdf_file_path, output_folder="all_slides")