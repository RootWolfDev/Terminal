from rich import print

# HTML tags guide with their simple definitions
htmlg = {
        'html': "<html> - Defines the start and end of an HTML document.",
        'head': "<head> - Contains metadata about the document, such as title and character set.",
        'body': "<body> - Contains the main content of the document like text, images, and other elements.",
        'title': "<title> - Specifies the title of the document, shown in the browser's title bar.",
        'h1-h6': "<h1> - <h6> - Defines headings, from <h1> (most important) to <h6> (least important).",
        'p': "<p> - Defines a paragraph of text.",
        'a': "<a> - Defines a hyperlink to another webpage or location in the same page. Uses 'href' attribute.",
        'img': "<img> - Embeds an image into the page. Requires the 'src' attribute to specify the image source.",
        'ul': "<ul> - Defines an unordered list (bulleted).",
        'ol': "<ol> - Defines an ordered list (numbered).",
        'li': "<li> - Defines a list item within a <ul> or <ol>.",
        'div': "<div> - Defines a block-level section to group other elements, often used with CSS.",
        'span': "<span> - Defines a small part of the content, usually for styling purposes, inline.",
        'table': "<table> - Defines a table for displaying data in rows and columns.",
        'tr': "<tr> - Defines a row within a table.",
        'td': "<td> - Defines a data cell within a table row.",
        'th': "<th> - Defines a header cell within a table.",
        'form': "<form> - Defines an HTML form for user input.",
        'input': "<input> - Defines an input field, used in forms.",
        'textarea': "<textarea> - Defines a multi-line text input field for forms.",
        'button': "<button> - Defines a clickable button within a form or elsewhere.",
        'label': "<label> - Defines a label for an input element in a form.",
        'select': "<select> - Defines a dropdown list of options in a form.",
        'option': "<option> - Defines an option within a <select> dropdown list.",
        'br': "<br> - Inserts a line break in the text.",
        'hr': "<hr> - Creates a horizontal rule (a dividing line) on the page.",
        'strong': "<strong> - Defines important text (usually displayed in bold).",
        'em': "<em> - Defines emphasized text (usually displayed in italics).",
        'i': "<i> - Defines text in italics.",
        'b': "<b> - Defines text in bold.",
        'code': "<code> - Defines a block of computer code.",
        'pre': "<pre> - Defines preformatted text, preserving spaces and line breaks.",
        'link': "<link> - Defines the relationship between the current document and an external resource (like a CSS file).",
        'meta': "<meta> - Provides metadata (information about the HTML document), such as charset and viewport settings.",
        'script': "<script> - Defines client-side JavaScript or links to an external script file.",
        'style': "<style> - Defines CSS styles within the HTML document.",
        'header': "<header> - Defines the header of a webpage or section, often containing a logo or navigation links.",
        'footer': "<footer> - Defines the footer of a webpage or section, often containing copyright info and contact links.",
        'nav': "<nav> - Defines a section for navigation links.",
        'article': "<article> - Defines content that is independent and reusable (like a blog post or news article).",
        'section': "<section> - Defines a section of related content within a document.",
        'aside': "<aside> - Defines content that is tangentially related to the main content, like a sidebar or additional information.",
        'figure': "<figure> - Defines content (like an image) with an optional caption.",
        'figcaption': "<figcaption> - Defines a caption for a <figure> element.",
        'address': "<address> - Defines contact information (email, phone number, etc.) for the document or author.",
        'mark': "<mark> - Highlights or marks text (usually displayed with a background color).",
        'q': "<q> - Defines a short inline quote.",
        'blockquote': "<blockquote> - Defines a block-level quote, typically used for long quotes from external sources.",
        'cite': "<cite> - Defines the source of a quote or reference.",
        'time': "<time> - Defines a date or time, often used with a specific time format.",
        'video': "<video> - Defines a video file to be played on the page, with various control options.",
        'audio': "<audio> - Defines an audio file to be played on the page.",
        'iframe': "<iframe> - Embeds another document or webpage inside the current page, essentially creating a 'window' to another content source.",
        '<!-- (just type - here) -->':'This is a comment in HTML'

    }
def help_b():
    global htmlg
    print(
            "Commands:\n"
            "start  → write HTML header\n"
            "begin → write HTML tag content\n"
            "end    → close HTML document\n"
            "exit   → stop writing\n"
            "show   → show all HTML tags and their definitions\n"
        )
    print('__________HTML guide with simple definition__________')
   
    # Print all tags with their definitions
    for key, value in htmlg.items():
        print(f'[red]{key}[/]: [green]{value}[/]')

# Start of the HTML post builder program
def one():
    print("HTML post builder...")
    print(r"""
 _   _ _____ __  __ _     
| | | |_   _|  \/  | |    
| |_| | | | | |\/| | |    
|  _  | | | | |  | | |___ 
|_| |_| |_| |_|  |_|_____| 
""")

    print("How to work!")
    print("Options:")
    print("1. Create a file")
    print("2. Modify a file")
    print("3. Help")
    print("4. Show HTML Tags")
    print("5. Use HTML tags directly")
    print("0. Exit")
# Function to directly add HTML tags to the document
def use_tags():
    global htmlg
    print("You can now add any HTML tag directly!")
    while True:
        tag = input("Enter HTML tag name (like 'p', 'h1', 'a', etc.): ").strip().lower()
        if tag in htmlg:
            if tag =='-':
                t= input('enter text:')
                print(f'<!-- {t} -->')
            if tag == 'a':
                url = input('Enter URL: ')
                name = input('Enter anchor text: ')
                print(f"<{tag} href=\"{url}\">{name}</{tag}>")
            elif tag == 'img':
                src = input('Enter image source (src): ')
                alt = input('Enter image alt text: ')
                print(f"<{tag} src=\"{src}\" alt=\"{alt}\">")
            else:
                content = input(f"Enter content for <{tag}>: ")
                print(f"<{tag}>{content}</{tag}>")
        elif tag=='exit':
            break
        else:
            print(f"[red]Invalid tag![/] Please try again.")
def first():
 

    answer = input("> ")

    if answer == "1":
        print("Path of file:")
        name = input("> ")
        with open(name, "w") as f:
            print(f"Creating file at path: {name}")
            writing(f)

    elif answer == "2":
        print("Write the file name to modify:")
        name = input("> ")
        with open(name, "a") as f:
            print(f"Modifying file: {name}")
            writing(f)

    elif answer == "3":
        help_b()

    elif answer == "4":
        help_b()

    elif answer == "5":
        use_tags()

    elif answer == "exit" or "0":
        print("Exiting...")
        return False  # Return False to stop the loop and exit

    else:
        print("Invalid choice! Please try again.")
    return True  # Keep the loop running unless the user chooses to exit

# Function to write the HTML content to a file
def writing(f):
    print("What can I help you with?")
    while True:
        answer = input("user: ").strip().lower()

        if answer == "start":
            title = input("Choose your title: ")
            f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body>
""")
            print("HTML start written ")

        elif answer == "begin":
            tag = input("Choose your tag (p, h1, div): ")
            if tag == 'hr':
                f.write(f"<{tag}>\n")
            elif tag == '-':
                texts=('enter text:')
                f.write(f'<!-- {t} -->')
            elif tag == 'a':
                url = input('url: ')
                name = input('name url: ')
                f.write(f"<{tag} href=\"{url}\">{name}</{tag}>")
            else:
                text = input("Write your text: ")
                f.write(f"<{tag}>{text}</{tag}>\n")
                print("Tag written ")
        elif answer == "end":
            f.write("""</body>
</html>
""")
            print("HTML closed ")

        elif answer == "exit":
            print("Stopping editor...")
            break

        else:
            print("Unknown command!")

# Run the program
def founct_ht():
    try:
        one()
        while True:
            if not first():  # Exit if user chooses 0
                break

    except Exception as e:
        print(f"[red]error:[/] {e}")
founct_ht()