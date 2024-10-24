class Document:
    def __init__(self):
        self.__content = ""  # Encapsulated attribute

    def add_text(self, text):
        self.__content += text

    def save(self):
        with open("document.txt", "w") as file:
            file.write(self.__content)
        print("Document saved.")

    def display(self):
        return self.__content[:100]  # Display only the first 100 characters

# Using the Document class
doc = Document()
doc.add_text("Hello, this is a sample text for the document. ")
doc.add_text("Only a portion of this text will be displayed.")
print("Document Content Preview:", doc.display())  # Display a preview of the content
doc.save()  # Save the document