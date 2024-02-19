from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import base64
class PDF:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--headless")  # 无头模式
        self.driver = webdriver.Chrome(options=self.options)

    def generate_pdf(self, url, output_path):
        self.driver.get(url)
        result = self.driver.execute_cdp_cmd("Page.printToPDF", {
            "landscape": False,  # Portrait mode
            "displayHeaderFooter": False,  # No headers or footers
            "printBackground": True,  # Print background colors and images
            "paperWidth": 8.27,  # A4 width in inches
            "paperHeight": 11.69,  # A4 height in inches
            "marginTop": 0.39,  # Top margin in inches (10mm)
            "marginBottom": 0.39,  # Bottom margin in inches (10mm)
            "marginLeft": 0.39,  # Left margin in inches (10mm)
            "marginRight": 0.39,  # Right margin in inches (10mm)
        })
        pdf_content = base64.b64decode(result['data'])
        with open(output_path, "wb") as f:
            f.write(pdf_content)

    def __del__(self):
        self.driver.quit()



