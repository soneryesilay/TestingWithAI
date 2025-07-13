# Appium Test & AI Analysis

Bu proje, Android mobil uygulamalar için Appium tabanlı otomasyon testlerini çalıştıran ve test sonuçlarını Google Gemini AI ile analiz eden modern bir Tkinter arayüzü sunar. Test sonuçları ve AI analizleri kolayca kaydedilebilir.

## Özellikler
- **Appium ile Otomasyon:** Dört farklı test senaryosu (başarılı, hatalı, form doğrulama, navigasyon) ile Android uygulamalarını otomatik test etme.
- **Modern Tkinter Arayüzü:** Koyu tema, kolay kullanım, test logları ve sonuçlarının ayrı panellerde gösterimi.
- **AI Destekli Analiz:** Test sonuçlarını Google Gemini API ile analiz ederek QA uzmanı gibi özet ve öneriler sunar.
- **Sonuçları Kaydetme:** Test ve AI analiz sonuçlarını kolayca .txt dosyası olarak kaydedebilme.

## Kurulum

### Gereksinimler
- Python 3.8+
- Appium Server (localhost:4723)
- Android cihaz veya emülatör (API 14+ önerilir)
- Gerekli Python paketleri:
  - appium-python-client
  - requests
  - tkinter (çoğu Python dağıtımında yüklü gelir)

### Paketleri Yükleme
```bash
pip install appium-python-client requests
```

### Appium Server Kurulumu
- [Appium Desktop](https://appium.io/downloads.html) veya `npm install -g appium` ile Appium'u kurun.
- Appium server'ı başlatın ve cihazınızın/emülatörünüzün bağlı olduğundan emin olun.

## Kullanım
1. `AutomationWithAI.py` dosyasını açın ve çalıştırın:
   ```bash
   python AutomationWithAI.py
   ```
2. Arayüzde istediğiniz test senaryosunu seçin.
3. Test logları, sonuçlar ve AI analizi ilgili panellerde görüntülenecektir.
4. Sonuçları veya AI analizini kaydetmek için ilgili butonları kullanın.

## API Anahtarı
Google Gemini API anahtarı güvenlik nedeniyle koddan kaldırılmıştır. Kendi API anahtarınızı almak için:
1. [Google AI Studio](https://aistudio.google.com/app/apikey) üzerinden bir API anahtarı oluşturun.
2. `AutomationWithAI.py` dosyasında `get_ai_comment` fonksiyonundaki `api_key` değişkenine kendi anahtarınızı ekleyin:
   ```python
   api_key = "YOUR_API_KEY_HERE"
   ```

## Test Senaryoları
- **Başarılı Test:** Tüm kontrollerin başarıyla çalıştığı senaryo.
- **Hatalı Test:** Yanlış element ID'si ile hata alınan senaryo.
- **Form Validation:** Form alanlarının ve kontrollerinin doğrulandığı senaryo.
- **Navigation Test:** Uygulama içinde ileri-geri navigasyonun test edildiği senaryo.

## Ekran Görüntüsü
> Modern ve koyu temalı arayüz ile test ve analiz panelleri.
<img width="1196" height="862" alt="image" src="https://github.com/user-attachments/assets/cad87426-369b-4d7e-b610-5c929689d884" />

---

**Not:** API anahtarınızı kimseyle paylaşmayın ve kodunuzu herkese açık depolarda paylaşırken anahtarınızı gizli tutun.
