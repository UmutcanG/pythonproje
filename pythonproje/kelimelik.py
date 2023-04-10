import random

# Kelime listesi dosyası
kelime_dosyasi = "kelimeler.txt"

def kelime_yukle(kelime_dosyasi):
    """Kelime dosyasından kelimeleri yükle"""
    with open(kelime_dosyasi, "r", encoding="utf-8") as dosya:
        kelimeler = dosya.readlines()
        kelimeler = [kelime.strip().lower() for kelime in kelimeler]
    return kelimeler

def kelime_sec(kelimeler):
    """Kelime listesinden rastgele bir kelime seç"""
    return random.choice(kelimeler)

def gizli_kelime_olustur(kelime):
    """Gizli kelimeyi "_" karakterleri ile oluştur"""
    return "_" * len(kelime)

def kelime_bulmaca():
    # Kelime listesi yükle
    kelimeler = kelime_yukle(kelime_dosyasi)

    # Oyun parametrelerini belirle
    tahmin_hakki = int(input("Tahmin hakkı: "))
    kelime_uzunlugu = int(input("Kelime uzunluğu: "))

    # Seçilen uzunlukta rastgele bir kelime seç
    kelime = ""
    while len(kelime) != kelime_uzunlugu:
        kelime = kelime_sec(kelimeler)

    gizli_kelime = gizli_kelime_olustur(kelime)

    while tahmin_hakki > 0 and gizli_kelime != kelime:
        print(gizli_kelime)
        tahmin = input("Bir harf tahmin et: ").lower()
        if len(tahmin) != 1 or not tahmin.isalpha():
            print("Lütfen tek bir harf girin!")
            continue
        if tahmin in kelime:
            for i in range(len(kelime)):
                if kelime[i] == tahmin:
                    gizli_kelime = gizli_kelime[:i] + tahmin + gizli_kelime[i+1:]
        else:
            tahmin_hakki -= 1
            print("Yanlış tahmin! Kalan tahmin hakkın:", tahmin_hakki)

    if tahmin_hakki == 0:
        print("Tahmin hakkın bitti. Gizli kelime:", kelime)
    else:
        print("Tebrikler! Gizli kelimeyi doğru tahmin ettin.")

kelime_bulmaca()