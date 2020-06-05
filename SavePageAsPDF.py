from PIL import Image

class SavePageAsPDF():
  def __init__( self, driver, pdfName ):
    # create temporary image 
    driver.save_screenshot("tmp_save_page_as_pdf.png")
    
    # use temporary image to create definity pdf
    image1 = Image.open(".//tmp_save_page_as_pdf.png")
    im1 = image1.convert("RGB")
    im1.save( "{}.pdf".format( pdfName ) )