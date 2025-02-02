import os

def alkol_kontrol():
    try:
        yas = int(input("Yaşınızı girin: "))

        # Dosyaya yaş bilgisini kaydet
        with open("veri.txt", "a") as dosya:
            dosya.write(f"Yaş: {yas}\n")

        # Alkol alma kontrolü
        if yas >= 18:
            print("Alkol alabilirsiniz.")
        else:
            print(f"Alkol almak için yaşınız uygun değil. {18 - yas} yıl sonra gelin.")

    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

def verileri_goster():
    if os.path.exists("veri.txt"):
        with open("veri.txt", "r") as dosya:
            print("\nÖnceki yaş girişleri:")
            print(dosya.read())
    else:
        print("Henüz veri yok.")

# Fonksiyonları çağır
alkol_kontrol()
verileri_goster()
