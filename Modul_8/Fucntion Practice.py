def heading_two(text):
    """
    return hearing two text of html
    :param text: Any kind of html
    :return: html tag
    """
    html = f'<h>{text}</h>'
    return html

# print(heading_two('This is heading tag'))
# print(heading_two.__doc__)

def html_tag(text, html_tag):
    """
    return Html Tag of any text
    :param text: any kind of string
    :param html_tag: what kind of html tag you want to generate
    :return: Html Tag of any text
    """
    html = f'<{html_tag}>{text}</{html_tag}>'
    return html

print(html_tag('This is paragaraph', 'strong'))