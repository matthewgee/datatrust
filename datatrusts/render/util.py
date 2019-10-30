
import pypandoc

#render readme in doc
#TODO: add rendering for html, ipynb

def to_docx(file):

    converted_file = pypandoc.convert(file, 'docx')

    if os.path.islink(converted_file):
        os.remove(converted_file)
    with open(converted_file, 'w') as out:
        out.write(converted_file)
    return converted_file

def to_rtf(file):

    converted_file = pypandoc.convert(file, 'rts')

    if os.path.islink(converted_file):
        os.remove(converted_file)
    with open(converted_file, 'w') as out:
        out.write(converted_file)
    return converted_file

