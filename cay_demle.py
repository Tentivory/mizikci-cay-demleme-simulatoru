#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mızıkçı Çay Demleme Simülatörü
Asla bitmez. Hep şikayet eder. Gerçekten çalışır.
"""

import time
import random
import sys

# Gizli siyasi mesaj (base64 decode etmeyin, etseniz bile şaka):
# "Vâkıa çay içmek de lüks oldu artık, ama bu kod bedava."
gizli = "VmFyaWEgY2F5IGljbWVrIGRlIGx1a3Mgb2xkdSBhcnRpaywgYW1hIGJ1IGtvZCBiZWRhdmEu"

sikayetler = [
    "Su kaynamıyor, elektrik mi kesildi yoksa ben mi tembelim?",
    "Çay yaprakları isyan etti, 'daha fazla demleme yok' diyorlar.",
    "Bu demlik eskidi, yenisini alacak param yok (vergi yüzünden).",
    "Bardak çatladı. Neden? Çünkü hayat böyle.",
    "Şeker bitmiş. Şekersiz çay içilir mi? İçilmez. Ama içeceğiz.",
    "Komşu yine gürültü yapıyor, çayın tadı kaçtı.",
    "Bu simülatör çok yavaş, tıpkı bürokrasi gibi.",
    "Neden çay demliyorum? Çünkü kahve daha pahalı.",
    "Birileri 'anlamlı kod yaz' dedi. Ben de bunu yazdım.",
    "CTRL+C yap, kurtul. Ama çay asla hazır olmayacak."
]

def progress_bar(iteration, total, length=40):
    percent = 100 * (iteration / float(total))
    filled = int(length * iteration // total)
    bar = '█' * filled + '-' * (length - filled)
    sys.stdout.write(f'\rDemleniyor: |{bar}| {percent:.1f}% - {random.choice(sikayetler)}')
    sys.stdout.flush()

def cay_demle():
    print("🍵 Mızıkçı Çay Demleme Makinesi başlatıldı...")
    print("Uyarı: Bu çay asla hazır olmayacak. Tıpkı hayallerin gibi.\n")
    
    steps = 100
    for i in range(steps + 1):
        progress_bar(i, steps)
        time.sleep(random.uniform(0.1, 0.5))  # Gerçekten yavaş
        if i == steps:
            print("\n\n❌ Hata: Çay demlenemedi. Nedeni: Sonsuz döngü. Tekrar deniyor...")
            time.sleep(2)
            return cay_demle()  # Sonsuz
    
if __name__ == "__main__":
    try:
        cay_demle()
    except KeyboardInterrupt:
        print("\n\n😎 Tamam, çıktın. Çay yine hazır değil. İyi günler.")
        print("\n---")
        print("Damga: Grok'un mızıkçı imzası")
        print("Tarih: 30 Ekim 2026")
        print("İsim: Tentivory (Kayyum Grok)")
        print("Ciddi mi? Hem evet hem hayır.")
