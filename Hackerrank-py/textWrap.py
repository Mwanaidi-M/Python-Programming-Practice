import textwrap 

def txtWrap(txt, wd):
    """Python has a textwrap Module that has two convenient methods; wrap() and fill()
       wrap() - Wraps a single paragraph of text, returning a list of wrapped lines.
                It returns a list of output lines.
       fill() - Reformat the single paragraph in 'text' to fit in lines of no more
        than 'width' columns. returns a single string containing the wrapped paragraph.

        given a string S and width W, your task is to wrap the string into a paragraph of width W.
    """

    return textwrap.fill(txt, wd) 

txtWrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4)