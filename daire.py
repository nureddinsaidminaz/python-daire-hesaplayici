pi=3.14592653589793238462
while True:
    print("\n------Daire Hesaplama Programı---")
    print("1 Yarıçapı girerek alan ve çevre hesaplama")
    print("2 Alanı girerek yarıçap ve çevre hesaplama")
    print("3 Çevreyi girerek yarıçap ve alan hesaplama")
    print("4 Çıkış")
    secim = input("Seçiminizi yapınız (1-4): ")
    if secim == "4":
        print("Programdan çıkılıyor...")
        break
    try:
        if secim == "1":
            yaricap = float(input("Yarıçapı giriniz: "))
            if yaricap < 0:
                print("Yarıçap negatif olamaz. Lütfen pozitif bir değer giriniz.")
                continue
            alan = pi * (yaricap ** 2)
            cevre = 2 * pi * yaricap
            print(f"Alan: {alan:.2f}, Çevre: {cevre:.2f}")
        elif secim == "2":
            alan = float(input("Alanı giriniz: "))
            if alan < 0:
                print("Alan negatif olamaz. Lütfen pozitif bir değer giriniz.")
                continue
            yaricap = (alan / pi) ** 0.5
            cevre = 2 * pi * yaricap
            print(f"Yarıçap: {yaricap:.2f}, Çevre: {cevre:.2f}")
        elif secim == "3":
            cevre = float(input("Çevreyi giriniz: "))
            if cevre < 0:
                print("Çevre negatif olamaz. Lütfen pozitif bir değer giriniz.")
                continue
            yaricap = cevre / (2 * pi)
            alan = pi * (yaricap ** 2)
            print(f"Yarıçap: {yaricap:.2f}, Alan: {alan:.2f}")
        else:
            print("Geçersiz seçim. Lütfen 1-4 arasında bir değer giriniz.")
    except ValueError:
        print("Geçersiz giriş. Lütfen sayısal bir değer giriniz.")
        print("------------------------------------------------------")
        