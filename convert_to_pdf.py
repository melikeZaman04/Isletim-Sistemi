import os
import glob
import subprocess

def main():
    # Klasördeki tüm .md dosyalarını bul
    md_files = glob.glob("*.md")
    
    if not md_files:
        print("Bulunacak .md dosyası yok.")
        return

    print(f"{len(md_files)} adet Markdown dosyası bulundu. PDF'e dönüştürülüyor...\n")

    for md_file in md_files:
        print(f"Dönüştürülüyor: {md_file} -> {md_file.replace('.md', '.pdf')}")
        # npx md-to-pdf komutu ile çevirme işlemini gerçekleştir
        subprocess.run(["npx", "md-to-pdf", md_file], shell=True)

    print("\nTüm dönüştürme işlemleri başarıyla tamamlandı. PDF dosyaları bulunduğunuz klasörde yer alıyor.")

if __name__ == "__main__":
    main()
