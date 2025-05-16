from markdown import markdown

import re

def mk_to_html(markdown_file):
    markdown_file = re.sub(r'\n- ',r'\n\n- ',markdown_file,count=1)
    html_output = markdown(markdown_file, extensions=['extra'])
    return html_output
