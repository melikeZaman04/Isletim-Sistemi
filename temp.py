import base64

content = b"""IyBCw7Zsw7xtIDQ6IMWeIFBhcsOnYWPEsWtsYXLEsSAoVGhyZWFkcykgdmUgw4dvayDDh2VraXJkZWtsaSBQcm9ncmFtbGFtYQoKQEBAQEA="""

with open(r"C:\Users\zaman\OneDrive\Desktop\ders\İşletim Sistemi\Thread.md", "w", encoding="utf-8") as f:
    f.write(base64.b64decode(content).decode("utf-8"))
