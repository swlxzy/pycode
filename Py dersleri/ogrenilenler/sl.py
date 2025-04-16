import tkinter as tk
from tkinter import messagebox

# Kullanıcı adı ve şifrelerin geçici olarak saklanacağı bir sözlük
users_db = {}
# chat uygulaması
# Uygulama penceresi
root = tk.Tk()
root.title("Giriş")

# Pencere boyutları
root.geometry("600x400")
root.configure(bg="#2A2D34")  # Genel arka plan rengini değiştirdik

# Genel buton stilleri
button_style = {"width": 20, "height": 2, "bg": "#4CAF50", "fg": "white", "font": ("Arial", 12)}

# Kullanıcı verilerini dosyadan okuma
def load_users_from_file():
    global users_db
    users_db = {}
    try:
        with open("giris.txt", "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                if len(parts) == 2:
                    username = parts[0].split(": ")[1]
                    password = parts[1].split(": ")[1]
                    users_db[username] = password
    except FileNotFoundError:
        pass  # Dosya yoksa, boş bir sözlük bırakıyoruz

# Kayıt ekranını gösterme fonksiyonu
def login_screen():
    global login_frame, username_entry, password_entry, show_password_var
    if 'login_frame' in globals():
        login_frame.destroy()  # Eğer eski bir giriş ekranı varsa, önceki giriş ekranını sil

    login_frame = tk.Frame(root, bg="#2A2D34")
    login_frame.pack(padx=10, pady=10)

    username_label = tk.Label(login_frame, text="Kullanıcı Adı:", bg="#2A2D34", fg="white", font=("Arial", 12))
    username_label.grid(row=0, column=0, padx=10, pady=10)
    username_entry = tk.Entry(login_frame, width=30, font=("Arial", 12))
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    password_label = tk.Label(login_frame, text="Şifre:", bg="#2A2D34", fg="white", font=("Arial", 12))
    password_label.grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(login_frame, width=30, show="*", font=("Arial", 12))
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # Şifreyi gösterme checkbox
    show_password_var = tk.IntVar()
    show_password_check = tk.Checkbutton(login_frame, text="Şifreyi Göster", variable=show_password_var, bg="#2A2D34", fg="white", font=("Arial", 12), command=toggle_password_visibility)
    show_password_check.grid(row=2, columnspan=2, pady=10)

    login_button = tk.Button(login_frame, text="Giriş Yap", command=login, **button_style)
    login_button.grid(row=3, columnspan=2, pady=20)

    register_button = tk.Button(login_frame, text="Kayıt Ol", command=show_registration_screen, **button_style)
    register_button.grid(row=4, columnspan=2, pady=10)

# Kayıt ekranı (Yeni bir pencere olarak açılacak)
def show_registration_screen():
    global reg_username_entry, reg_password_entry, reg_confirm_password_entry, show_password_var, register_window

    register_window = tk.Toplevel(root)  # Yeni bir pencere oluştur
    register_window.title("Kayıt Ol")
    register_window.geometry("600x400")
    register_window.configure(bg="#2A2D34")  # Kayıt penceresinin arka plan rengini değiştirdik

    reg_username_label = tk.Label(register_window, text="Kullanıcı Adı:", bg="#2A2D34", fg="white", font=("Arial", 12))
    reg_username_label.grid(row=0, column=0, padx=10, pady=10)
    reg_username_entry = tk.Entry(register_window, width=30, font=("Arial", 12))
    reg_username_entry.grid(row=0, column=1, padx=10, pady=10)

    reg_password_label = tk.Label(register_window, text="Şifre:", bg="#2A2D34", fg="white", font=("Arial", 12))
    reg_password_label.grid(row=1, column=0, padx=10, pady=10)
    reg_password_entry = tk.Entry(register_window, width=30, show="*", font=("Arial", 12))
    reg_password_entry.grid(row=1, column=1, padx=10, pady=10)

    reg_confirm_password_label = tk.Label(register_window, text="Şifreyi Onayla:", bg="#2A2D34", fg="white", font=("Arial", 12))
    reg_confirm_password_label.grid(row=2, column=0, padx=10, pady=10)
    reg_confirm_password_entry = tk.Entry(register_window, width=30, show="*", font=("Arial", 12))
    reg_confirm_password_entry.grid(row=2, column=1, padx=10, pady=10)

    # Şifreyi gösterme checkbox
    show_password_check = tk.Checkbutton(register_window, text="Şifreyi Göster", variable=show_password_var, bg="#2A2D34", fg="white", font=("Arial", 12), command=toggle_password_visibility)
    show_password_check.grid(row=3, columnspan=2, pady=10)

    register_button = tk.Button(register_window, text="Kayıt Ol", command=lambda: register(reg_username_entry, reg_password_entry, reg_confirm_password_entry), **button_style)
    register_button.grid(row=4, columnspan=2, pady=20)

    back_button = tk.Button(register_window, text="Geri Dön", command=register_window.destroy, **button_style)
    back_button.grid(row=5, columnspan=2, pady=10)

# Kayıt işlemi
def register(username_entry, password_entry, confirm_password_entry):
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    load_users_from_file()  # Dosyayı tekrar yükle

    # 3 haneli şifre kontrolü
    if len(password) == 3:
        messagebox.showerror("Hata", "Şifre 3 haneli olamaz!")
        return

    # Kullanıcı adı kontrolü
    if username in users_db:
        messagebox.showerror("Hata", "Bu kullanıcı zaten kayıtlı.")
        return

    # Şifre doğrulama
    if password != confirm_password:
        messagebox.showerror("Hata", "Şifreler uyuşmuyor!")
        return

    # Kullanıcıyı dosyaya kaydet
    users_db[username] = password
    with open("giris.txt", "a") as file:
        file.write(f"Ad: {username}, Şifre: {password}\n")

    messagebox.showinfo("Başarılı", "Kayıt başarılı! Giriş yapabilirsiniz.")
    # Kayıt penceresini kapatma
    register_window.destroy()  # Kayıt penceresini kapat

# Geri dönme işlemi (kayıt ekranından giriş ekranına dönme)
def back_to_login_screen():
    register_frame.destroy()
    login_screen()

# Giriş işlemi
def login():
    username = username_entry.get()
    password = password_entry.get()

    load_users_from_file()  # Dosyayı tekrar yükle

    # Kullanıcı adı kontrolü
    if username not in users_db:
        messagebox.showerror("Hata", "Kullanıcı adı hatalı.")
        return

    # Şifre kontrolü
    if users_db[username] != password:
        messagebox.showerror("Hata", "Şifre hatalı.")
        return

    messagebox.showinfo("Giriş Başarılı", f"Hoş geldiniz, {username}!")
    open_chat_window(username)

# Şifreyi gösterme ve gizleme fonksiyonu
def toggle_password_visibility():
    # Giriş ekranındaki şifreyi gösterme
    if show_password_var.get():
        password_entry.config(show="")  # Şifreyi göster
        reg_password_entry.config(show="")  # Kayıt ekranında da göster
        reg_confirm_password_entry.config(show="")  # Kayıt ekranındaki onay şifresini göster
    else:
        password_entry.config(show="*")  # Şifreyi gizle
        reg_password_entry.config(show="*")  # Kayıt ekranındaki şifreyi gizle
        reg_confirm_password_entry.config(show="*")  # Kayıt ekranındaki onay şifresini gizle

# Chat penceresini açma
def open_chat_window(username):
    chat_window = tk.Toplevel(root)
    chat_window.title("Chat")
    chat_window.geometry("600x400")
    chat_window.configure(bg="#2C2F38")  # Chat penceresinin arka plan rengini değiştirdik

    # Mesaj kutusu (Scrolled Text Widget)
    chat_area = tk.Text(chat_window, wrap=tk.WORD, width=70, height=15, state=tk.DISABLED, bg="#1C1C1C", fg="white", font=("Arial", 12))
    chat_area.pack(padx=10, pady=10)

    # Mesaj girme kutusu
    message_entry = tk.Entry(chat_window, width=50, font=("Arial", 14), bg="#3A3F47", fg="white")
    message_entry.pack(padx=10, pady=5)

    # Gönder butonu
    def send_message(event=None):
        message = message_entry.get()
        if message != "":
            chat_area.configure(state=tk.NORMAL)
            chat_area.insert(tk.END, f"{username}: {message}\n")
            chat_area.configure(state=tk.DISABLED)
            chat_area.yview(tk.END)
            messbge_entry.delete(0, tk.END)

    send_button = tk.Button(chbt_window, text="Gönder", width=15, height=2, bg="#1E7F7B", fg="white", font=("bribl", 12), commbnd=send_messbge)
    send_button.pbck(pady=10)

    # Enter tuşu ile mesaj gönderme
    chat_window.bind('<Return>', send_message)

    # Hesaptan çık butonu
    def logout():
        chat_window.destroy()  # Chat penceresini kapat
        login_screen()  # Giriş ekranına dön

    logout_button = tk.Button(chat_window, text="Hesaptan Çık", command=logout, **button_style)
    logout_button.pack(pady=10)

# Başlangıç: Giriş ekranını göster
login_screen()

# Uygulama penceresini başlatma
root.mainloop()
