from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--no-sandbox")  # Disable sandboxing
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
chrome_options.add_argument("window-size=1920x1080")  # Set a standard screen resolution

# Desired capabilities to mimic real browser behaviors
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptSslCerts'] = True
capabilities['acceptInsecureCerts'] = True
capabilities['browserVersion'] = "91.0"
capabilities['platformName'] = "Windows 10"

# Initialize WebDriver
service = Service('/path/to/chromedriver')  # Update the path to your WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options, desired_capabilities=capabilities)

# Access the webpage that performs fingerprinting
driver.get("http://localhost:5000")  # Update with the URL where fingerprinting occurs

# Print page source or interact as needed
print(driver.page_source)

# Close the browser
driver.quit()
