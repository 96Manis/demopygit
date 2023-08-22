from selenium import webdriver
import csv

# Set up the Selenium Edge webdriver
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True
edge_options.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'  # Replace with the actual path

# Initialize the WebDriver
driver = webdriver.Edge(options=edge_options)

# The URL of the website to scrape
url = 'https://www.bea.gov/'

# Open the webpage
driver.get(url)

# Find the topic
topic_element = driver.find_element("css selector", "h1")
topic = topic_element.text.strip() if topic_element else "No Topic Found"

# Find all the <p> elements
p_elements = driver.find_elements("css selector", "p")

# Extract the text from the <p> elements and remove empty paragraphs and the specific line
data = [p.text.strip() for p in p_elements if p.text.strip() and p.text.strip() != "An official website of the United States government"]

# Close the webdriver
driver.quit()

# Save the output to a CSV file
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Topic: " + topic])  # Write the topic as the first row

    for index, item in enumerate(data, start=1):
        writer.writerow([f"{index}. {item}"])  # Write each item as a separate row

print("Formatted output saved to output.csv")
