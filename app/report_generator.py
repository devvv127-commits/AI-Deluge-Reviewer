def generate_html_report(content):

    html = f"""
    <html>
    <body>
        <h1>AI Review Report</h1>
        <pre>{content}</pre>
    </body>
    </html>
    """

    with open("reports/report.html", "w") as file:
        file.write(html)# Report generation module
