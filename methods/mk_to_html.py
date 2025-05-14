from markdown import markdown


def mk_to_html(markdown_file):
    text = ""
    html_output = markdown(text, extensions=['extra'])
    return html_output

