def alkol_alabilir_mi(yas):
    if yas >= 18:
        return "Alkol satın alabilirsiniz."
    else:
        return "Alkol satın alamazsınız."

# Kullanıcıdan yaş bilgisini al
try:
    yas = int(input("Yaşınızı girin: "))
    sonuc = alkol_alabilir_mi(yas)
    print(sonuc)
except ValueError:
    print("Lütfen geçerli bir yaş girin.")
