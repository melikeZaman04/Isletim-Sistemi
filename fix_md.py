import shutil
import glob
files = glob.glob("*al*sma*md") + glob.glob("*al*sma*MD") + glob.glob("*.md")
target_file = None
for f in files:
    if "al" in f and "sma" in f and f.endswith(".md"):
        target_file = f
        break

if target_file:
    print(f"Buldum: {target_file}")
    with open(target_file, 'rb') as f:
        data = f.read()
    
    # Try different encodings
    for enc in ['utf-8-sig', 'utf-8', 'utf-16', 'windows-1254', 'cp1254']:
        try:
            text = data.decode(enc)
            print(f"{enc} ile basarili cozuldu, karakter uzunlugu:", len(text))
            if len(text) > 100:
                with open("calisma_temp.md", 'w', encoding='utf-8') as out:
                    out.write(text)
                print("calisma_temp.md olustu.")
                break
        except:
            pass
else:
    print("Dosya bulunamadi!")
