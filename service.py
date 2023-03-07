import markdown

def convert_to_html(path):
    file = open(path)
    md = markdown.Markdown()
    html_string = md.convert(file.read())
    file.close()
    return html_string

def create_html_file(html, path):
    file = open(path+"README.html", 'w')
    file.write(html)
    file.close()
