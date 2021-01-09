#!usr/bin/python3
"""
    This is the module for
    text_indentation

"""


def text_indentation(text):
    """
        text_indentation
    """
    final = ""
    c = 0
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    while c < len(text):
        if text[c] == '.' or text[c] == '?' or text[c] == ':':
            final = final + text[c] + "\n\n"
            c += 2
        else:
            final = final + text[c]
            c += 1
    print(final)
