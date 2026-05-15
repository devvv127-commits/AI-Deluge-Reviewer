# Main application entry point
from reviewer import review_script
from report_generator import generate_html_report

with open("sample_scripts/bad_script.dg", "r") as file:
    script = file.read()

result = review_script(script)
generate_html_report(result)

print("\n AI REVIEW REPORT \n")
print(result)