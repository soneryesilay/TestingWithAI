import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from appium.webdriver.webdriver import WebDriver as Remote
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
import requests


# Test Case 1: Başarılı Test - Orijinal test
def test_case_successful(log_callback=None):
    try:
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.platform_version = "14"
        options.device_name = ""
        options.app_package = "io.appium.android.apis"
        options.app_activity = ".ApiDemos"
        options.no_reset = True
        options.udid = ""

        if log_callback:
            log_callback("✅ Başarılı Test Senaryosu Başlatıldı\n")
            log_callback("Appium sunucusuna bağlanılıyor...\n")
        
        driver = Remote("http://localhost:4723/wd/hub", options=options)
        time.sleep(1)
        
        if log_callback:
            log_callback("Views menüsüne tıklanıyor...\n")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
        
        if log_callback:
            log_callback("Controls'a scroll yapılıyor...\n")
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Controls"))'
        ).click()
        
        if log_callback:
            log_callback("1. Light Theme seçiliyor...\n")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Light Theme").click()
        
        if log_callback:
            log_callback("Metin kutusuna yazı yazılıyor...\n")
        edit_text = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/edit")
        edit_text.send_keys("Appium Test Başarılı!")
        
        if log_callback:
            log_callback("Checkbox işaretleniyor...\n")
        driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/check1").click()
        
        if log_callback:
            log_callback("RadioButton seçiliyor...\n")
        driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/radio1").click()
        
        if log_callback:
            log_callback("Spinner açılıyor...\n")
        spinner = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/spinner1")
        spinner.click()
        time.sleep(0.5)
        
        if log_callback:
            log_callback("Venus seçiliyor...\n")
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Venus")'
        ).click()
        
        time.sleep(0.5)
        driver.quit()
        return ("success", "✅ Başarılı Test: Tüm kontroller başarıyla test edildi!")
        
    except Exception as e:
        return ("error", f"❌ Test sırasında hata oluştu: {e}")


# Test Case 2: Hatalı Test - Yanlış element ID'si
def test_case_failing(log_callback=None):
    try:
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.platform_version = "14"
        options.device_name = ""
        options.app_package = "io.appium.android.apis"
        options.app_activity = ".ApiDemos"
        options.no_reset = True
        options.udid = ""

        if log_callback:
            log_callback("❌ Hatalı Test Senaryosu Başlatıldı\n")
            log_callback("Appium sunucusuna bağlanılıyor...\n")
        
        driver = Remote("http://localhost:4723/wd/hub", options=options)
        time.sleep(1)
        
        if log_callback:
            log_callback("Views menüsüne tıklanıyor...\n")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
        
        if log_callback:
            log_callback("Controls'a scroll yapılıyor...\n")
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Controls"))'
        ).click()
        
        if log_callback:
            log_callback("1. Light Theme seçiliyor...\n")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Light Theme").click()
        
        if log_callback:
            log_callback("⚠️ Yanlış element ID'si kullanılacak...\n")
        # Kasıtlı olarak yanlış ID kullanıyoruz
        edit_text = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/wrong_element_id")
        edit_text.send_keys("Bu çalışmayacak!")
        
        driver.quit()
        return ("success", "Test tamamlandı")
        
    except Exception as e:
        return ("error", f"❌ Hatalı Test: Element bulunamadı - {str(e)}")


# Test Case 3: Form Validation Test
def test_case_form_validation(log_callback=None):
    try:
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.platform_version = "14"
        options.device_name = ""
        options.app_package = "io.appium.android.apis"
        options.app_activity = ".ApiDemos"
        options.no_reset = True
        options.udid = ""

        if log_callback:
            log_callback("📝 Form Validation Test Başlatıldı\n")
            log_callback("Appium sunucusuna bağlanılıyor...\n")
        
        driver = Remote("http://localhost:4723/wd/hub", options=options)
        time.sleep(1)
        
        if log_callback:
            log_callback("Views menüsüne tıklanıyor...\n")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
        
        if log_callback:
            log_callback("Controls'a scroll yapılıyor...\n")
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Controls"))'
        ).click()
        
        if log_callback:
            log_callback("1. Light Theme seçiliyor...\n")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Light Theme").click()
        
        if log_callback:
            log_callback("Form alanları test ediliyor...\n")
        
        # Metin alanını test et
        edit_text = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/edit")
        edit_text.clear()
        edit_text.send_keys("Form Test - Özel Karakterler: @#$%^&*()")
        
        if log_callback:
            log_callback("Tüm kontroller test ediliyor...\n")
        
        # Checkbox durumunu kontrol et
        checkbox = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/check1")
        if not checkbox.is_selected():
            checkbox.click()
        
        # RadioButton gruplarını test et
        radio1 = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/radio1")
        radio2 = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/radio2")
        
        radio1.click()
        time.sleep(0.3)
        radio2.click()
        
        if log_callback:
            log_callback("Form validation tamamlandı...\n")
        
        driver.quit()
        return ("success", "✅ Form Validation Test: Tüm form kontrolleri başarıyla validate edildi!")
        
    except Exception as e:
        return ("error", f"❌ Form validation test hatası: {e}")


# Test Case 4: Navigation Test
def test_case_navigation(log_callback=None):
    try:
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.platform_version = "14"
        options.device_name = ""
        options.app_package = "io.appium.android.apis"
        options.app_activity = ".ApiDemos"
        options.no_reset = True
        options.udid = ""

        if log_callback:
            log_callback("🧭 Navigation Test Başlatıldı\n")
            log_callback("Appium sunucusuna bağlanılıyor...\n")
        
        driver = Remote("http://localhost:4723/wd/hub", options=options)
        time.sleep(1)
        
        if log_callback:
            log_callback("Animation menüsüne gidiliyor...\n")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Animation").click()
        time.sleep(1)
        
        if log_callback:
            log_callback("Default Layout Animations tıklanıyor...\n")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Default Layout Animations").click()
        time.sleep(1)
        
        if log_callback:
            log_callback("ADD BUTTON tıklanıyor...\n")
        driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/addNewButton").click()
        time.sleep(1)
        
        if log_callback:
            log_callback("DELETE BUTTON tıklanıyor...\n")
        driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/deleteButton").click()
        time.sleep(1)
        
        if log_callback:
            log_callback("Geri navigasyon yapılıyor...\n")
        driver.back()
        time.sleep(0.5)
        driver.back()
        
        driver.quit()
        return ("success", "✅ Navigation Test: Tüm navigasyon işlemleri başarıyla tamamlandı!")
        
    except Exception as e:
        return ("error", f"❌ Navigation test hatası: {e}")



def get_ai_comment(test_result):

    # API anahtarınızı buraya ekleyin
    api_key = "YOUR_API_KEY_HERE"  # <-- Buraya kendi Google Gemini API anahtarınızı girin
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}

    # Gelişmiş prompt: Daha net ve sınırlı bir görev tanımı veriyoruz
    prompt_text = (
        "Aşağıda bir mobil test raporu bulunmaktadır. Lütfen bu test sonucunu gerçek bir QA test uzmanı gibi değerlendir ama raporu test uzmanı gibi değerlendiriyorum diye başlama cümelelrin doğal olsun tamamdır diye de başlama direkt gir konuya:\n\n"
        f"{test_result}\n\n"
        "Analizinde aşağıdaki yapıyı izle:\n"
        "1. ✅ Test başarılıysa kısa bir özet ver. Gereksiz uzatma yapma.\n"
        "2. ❌ Başarısız test adımları varsa bunları net olarak belirt:\n"
        "   - Hangi adımda hata var?\n"
        "   - Muhtemel nedenleri neler olabilir?\n"
        "   - Hangi çözüm yolları önerilebilir?\n"
        "3. Test kapsamı yeterli mi? Eksik senaryo varsa belirt (kısa tut).\n"
        "4. Yorumlar sade, teknik ve doğrudan olmalı. Genel-geçer ifadelerden kaçın."
    )

    data = {
        "contents": [
            {"parts": [{"text": prompt_text}]}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=20)
        if response.status_code == 200:
            result = response.json()
            return result["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return f"AI API hatası: {response.status_code} - {response.text}"
    except Exception as e:
        return f"AI API çağrısı başarısız: {e}"



# Test fonksiyonları mapping
test_functions = {
    "successful": test_case_successful,
    "failing": test_case_failing,
    "form_validation": test_case_form_validation,
    "navigation": test_case_navigation
}


# Seçilen testi başlatan fonksiyon
def start_selected_test(test_type):
    def worker():
        # Tüm butonları devre dışı bırak
        for btn in test_buttons:
            btn.config(state=tk.DISABLED)
        
        # Arayüzü temizle
        txt_log.config(state=tk.NORMAL)
        txt_log.delete(1.0, tk.END)
        txt_result.config(state=tk.NORMAL)
        txt_result.delete(1.0, tk.END)
        txt_ai.config(state=tk.NORMAL)
        txt_ai.delete(1.0, tk.END)
        
        # Tag'leri temizle
        txt_result.tag_remove("error", "1.0", tk.END)
        txt_result.tag_remove("success", "1.0", tk.END)
        
        txt_result.insert(tk.END, "Test başlatıldı...\n")
        
        def log_callback(msg):
            txt_log.insert(tk.END, msg)
            txt_log.see(tk.END)
            root.update_idletasks()
        
        # Seçilen test fonksiyonunu çalıştır
        test_func = test_functions[test_type]
        status, test_result = test_func(log_callback)
        
        # Sonuçları göster
        txt_result.delete(1.0, tk.END)
        if status == "success":
            txt_result.insert(tk.END, test_result, "success")
        else:
            txt_result.insert(tk.END, test_result, "error")
        

        # AI yorumu al
        txt_result.insert(tk.END, "\n\n🤖 AI yorumu bekleniyor...\n")
        ai_comment = get_ai_comment(test_result)
        txt_ai.delete(1.0, tk.END)
        txt_ai.insert(tk.END, ai_comment)
        # Son AI analizini global değişkende tut
        global last_ai_comment, last_test_type
        last_ai_comment = ai_comment
        last_test_type = test_type

        # Arayüzü kilitle
        txt_log.config(state=tk.DISABLED)
        txt_result.config(state=tk.DISABLED)
        txt_ai.config(state=tk.NORMAL)

        # Butonları tekrar aktif et
        for btn in test_buttons:
            btn.config(state=tk.NORMAL)
    
    threading.Thread(target=worker, daemon=True).start()


# Modern Tkinter arayüzü
root = tk.Tk()
root.title("Appium Test & AI Analysis")
root.geometry("1200x800")
root.resizable(True, True)
root.configure(bg='#1e1e2e')

# Modern stil tanımlamaları
style = ttk.Style()
style.theme_use('clam')

# Koyu tema renkleri
style.configure('Modern.TFrame', background='#1e1e2e')
style.configure('Header.TLabel', 
                background='#1e1e2e', 
                foreground='#cdd6f4',
                font=("Segoe UI", 18, "bold"))
style.configure('SubHeader.TLabel', 
                background='#1e1e2e', 
                foreground='#a6adc8',
                font=("Segoe UI", 12))
style.configure('Modern.TButton', 
                font=("Segoe UI", 11, "bold"),
                padding=(15, 8))

# Üst başlık frame
frm_header = ttk.Frame(root, style='Modern.TFrame')
frm_header.pack(fill=tk.X, pady=(20, 10))

header = ttk.Label(frm_header, text="🚀  Appium Test & AI Analysis", style='Header.TLabel')
header.pack()

subtitle = ttk.Label(frm_header, text="Mobil test senaryoları için AI destekli analiz", style='SubHeader.TLabel')
subtitle.pack(pady=(5, 0))

# Test butonları frame
frm_buttons = ttk.Frame(root, style='Modern.TFrame')
frm_buttons.pack(fill=tk.X, pady=15)

# Ortalamak için iç frame
frm_buttons_inner = ttk.Frame(frm_buttons, style='Modern.TFrame')
frm_buttons_inner.pack(anchor='center')

# Test butonları
test_buttons = []

btn_successful = ttk.Button(frm_buttons_inner, text="✅ Başarılı Test", 
                           command=lambda: start_selected_test("successful"),
                           style='Modern.TButton')
btn_successful.pack(side=tk.LEFT, padx=10)
test_buttons.append(btn_successful)

btn_failing = ttk.Button(frm_buttons_inner, text="❌ Hatalı Test", 
                        command=lambda: start_selected_test("failing"),
                        style='Modern.TButton')
btn_failing.pack(side=tk.LEFT, padx=10)
test_buttons.append(btn_failing)

btn_form = ttk.Button(frm_buttons_inner, text="📝 Form Validation", 
                     command=lambda: start_selected_test("form_validation"),
                     style='Modern.TButton')
btn_form.pack(side=tk.LEFT, padx=10)
test_buttons.append(btn_form)

btn_navigation = ttk.Button(frm_buttons_inner, text="🧭 Navigation Test", 
                           command=lambda: start_selected_test("navigation"),
                           style='Modern.TButton')
btn_navigation.pack(side=tk.LEFT, padx=10)
test_buttons.append(btn_navigation)

# Ana içerik frame
frm_main = ttk.Frame(root, style='Modern.TFrame')
frm_main.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Sol panel - Test Logları
frm_left = ttk.Frame(frm_main, style='Modern.TFrame')
frm_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

lbl_log = ttk.Label(frm_left, text="📊 Test Logları", style='SubHeader.TLabel')
lbl_log.pack(anchor='w', pady=(0, 5))

txt_log = scrolledtext.ScrolledText(frm_left, 
                                   width=60, height=25, 
                                   font=("Consolas", 10),
                                   bg="#313244", fg="#cdd6f4",
                                   insertbackground="#cdd6f4",
                                   selectbackground="#585b70",
                                   bd=0, relief="flat")
txt_log.pack(fill=tk.BOTH, expand=True, pady=(0, 10))


# Sağ panel - Test Sonucu
frm_right = ttk.Frame(frm_main, style='Modern.TFrame')
frm_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(20, 0))

lbl_result = ttk.Label(frm_right, text="📋 Test Sonucu", style='SubHeader.TLabel')
lbl_result.pack(anchor='w', pady=(0, 5))

txt_result = scrolledtext.ScrolledText(frm_right, 
                                      width=50, height=10, 
                                      font=("Segoe UI", 11),
                                      bg="#313244", fg="#cdd6f4",
                                      insertbackground="#cdd6f4",
                                      selectbackground="#585b70",
                                      bd=0, relief="flat")
txt_result.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

# Test sonucunu kaydet butonu
def save_test_result():
    from tkinter import messagebox, filedialog
    import datetime
    result_text = txt_result.get(1.0, tk.END).strip()
    if not result_text:
        messagebox.showwarning("Uyarı", "Kaydedilecek bir test sonucu yok.")
        return
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    default_filename = f"Test_Sonucu_{now}.txt"
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Metin Dosyası", "*.txt")],
        initialfile=default_filename,
        title="Test Sonucunu Kaydet"
    )
    if not file_path:
        return
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(result_text)
        messagebox.showinfo("Başarılı", f"Test sonucu '{file_path}' olarak kaydedildi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Test sonucu dosyaya yazılamadı: {e}")

btn_save_result = ttk.Button(frm_right, text="📋 Test Sonucunu Kaydet", command=save_test_result, style='Modern.TButton')
btn_save_result.pack(anchor='e', pady=(0, 5))

# Renk tag'leri
txt_result.tag_configure("error", foreground="#f38ba8", font=("Segoe UI", 11, "bold"))
txt_result.tag_configure("success", foreground="#a6e3a1", font=("Segoe UI", 11, "bold"))


# AI Yorum paneli
lbl_ai = ttk.Label(frm_right, text="🤖 AI Analizi", style='SubHeader.TLabel')
lbl_ai.pack(anchor='w', pady=(10, 5))

txt_ai = scrolledtext.ScrolledText(frm_right, 
                                  width=50, height=12, 
                                  font=("Segoe UI", 11),
                                  bg="#313244", fg="#cdd6f4",
                                  insertbackground="#cdd6f4",
                                  selectbackground="#585b70",
                                  bd=0, relief="flat")
txt_ai.pack(fill=tk.BOTH, expand=True)

# AI analizini kaydet butonu
def save_ai_analysis():
    from tkinter import messagebox, filedialog
    import datetime
    global last_ai_comment, last_test_type
    try:
        comment = last_ai_comment
        test_type = last_test_type
    except Exception:
        comment = txt_ai.get(1.0, tk.END).strip()
        test_type = "test"
    if not comment.strip():
        messagebox.showwarning("Uyarı", "Kaydedilecek bir AI analizi yok.")
        return
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    default_filename = f"AI_QA_{test_type}_{now}.txt"
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Metin Dosyası", "*.txt")],
        initialfile=default_filename,
        title="AI Analizini Kaydet"
    )
    if not file_path:
        return  # Kullanıcı iptal etti
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(comment)
        messagebox.showinfo("Başarılı", f"AI analizi '{file_path}' olarak kaydedildi.")
    except Exception as e:
        messagebox.showerror("Hata", f"AI çıktısı dosyaya yazılamadı: {e}")

btn_save_ai = ttk.Button(frm_right, text="💾 AI Analizini Kaydet", command=save_ai_analysis, style='Modern.TButton')
btn_save_ai.pack(anchor='e', pady=(5, 10))

# Başlangıç mesajları
txt_log.insert(tk.END, "🔧 Test ortamı hazır. Bir test senaryosu seçin.\n")
txt_log.config(state=tk.DISABLED)

txt_result.insert(tk.END, "📱 Test sonuçları burada gösterilecek...\n")
txt_result.config(state=tk.DISABLED)

txt_ai.insert(tk.END, "🤖 AI analizi test tamamlandıktan sonra burada görüntülenecek...\n")
txt_ai.config(state=tk.DISABLED)

# Uygulama kapatma
def on_closing():
    root.quit()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()