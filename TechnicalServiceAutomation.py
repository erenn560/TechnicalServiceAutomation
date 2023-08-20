import tkinter as tk
from tkinter import Toplevel, Label, Text, Button, Listbox, StringVar, OptionMenu, Entry

# Teknik Servis Yetkilisi Uygulaması
class TeknikServisYetkilisiApp:
    def __init__(self, root):
        # Arayüzün başlatılması
        self.root = root
        self.root.title("Teknik Servis Yetkilisi Arayüzü")
        self.root.geometry("800x600")
        self.messages = []
        self.root.iconbitmap("Icon.ico")
        self.root.configure(bg="lightgray")

        # Mesajları görüntüleme düğmesi
        self.view_messages_button = Button(root, text="Mesajları Görüntüle", command=self.view_messages, bg="blue", fg="white", font=("Helvetica", 14))
        self.view_messages_button.pack(fill=tk.BOTH, padx=20, pady=10)

        # Onarım aşamaları çerçevesi
        self.onarim_asamalari_frame = tk.Frame(root, bg="lightgray")
        self.onarim_asamalari_frame.pack(fill=tk.BOTH, padx=20, pady=10)
        onarim_label = Label(self.onarim_asamalari_frame, text="Onarım Aşamaları:", font=("Helvetica", 16), bg="lightgray")
        onarim_label.pack(pady=10)
        self.create_onarim_buttons()

    # Onarım aşama düğmelerini oluşturma
    def create_onarim_buttons(self):
        onarim_button_1 = Button(self.onarim_asamalari_frame, text="Aşama 1", bg="red", fg="white", font=("Helvetica", 14))
        onarim_button_1.pack(fill=tk.BOTH, padx=20, pady=5)

        onarim_button_2 = Button(self.onarim_asamalari_frame, text="Aşama 2", bg="orange", fg="white", font=("Helvetica", 14))
        onarim_button_2.pack(fill=tk.BOTH, padx=20, pady=5)

        onarim_button_3 = Button(self.onarim_asamalari_frame, text="Aşama 3", bg="yellow", fg="black", font=("Helvetica", 14))
        onarim_button_3.pack(fill=tk.BOTH, padx=20, pady=5)

        onarim_button_4 = Button(self.onarim_asamalari_frame, text="Montaj Aşaması", bg="green", fg="white", font=("Helvetica", 14))
        onarim_button_4.pack(fill=tk.BOTH, padx=20, pady=5)

        onarim_button_5 = Button(self.onarim_asamalari_frame, text="Hazırlık Aşaması", bg="blue", fg="white", font=("Helvetica", 14))
        onarim_button_5.pack(fill=tk.BOTH, padx=20, pady=5)

    # Mesajları görüntüleme penceresi
    def view_messages(self):
        messages_window = Toplevel(self.root)
        messages_window.title("Teknik Servis Mesajları")
        messages_window.geometry("800x600")

        messages_label = Label(messages_window, text="Teknik Servis Mesajları", font=("Helvetica", 18))
        messages_label.pack(pady=10)

        messages_listbox = Listbox(messages_window, width=70, height=15, font=("Helvetica", 14))
        messages_listbox.pack(padx=20, pady=20)

        for message in self.messages:
            messages_listbox.insert(tk.END, message)

        view_details_button = Button(messages_window, text="Detayları Görüntüle", command=lambda: self.view_message_details(messages_listbox), bg="green", fg="white", font=("Helvetica", 14))
        view_details_button.pack(fill=tk.BOTH, padx=20, pady=10)

    # Mesaj detaylarını görüntüleme penceresi
    def view_message_details(self, listbox):
        selected_index = listbox.curselection()
        if selected_index:
            message_index = selected_index[0]
            message = self.messages[message_index]

            details_window = Toplevel(self.root)
            details_window.title("Mesaj Detayları")
            details_window.geometry("600x400")

            details_label = Label(details_window, text="Mesaj Detayları", font=("Helvetica", 18))
            details_label.pack(pady=10)

            details_text = Text(details_window, width=60, height=10, font=("Helvetica", 14))
            details_text.pack(padx=20, pady=20)

            details_text.insert(tk.END, message)

    # Mesaj alma işlemi
    def receive_message(self, message):
        self.messages.append(message)

    # Ana döngüyü başlatma
    def main(self):
        self.root.mainloop()

# Teknik Servis Uygulaması
class TeknikServisApp:
    def send_message(self):
        # Mesaj gönderme işlemi
        message = self.message_text.get("1.0", tk.END)
        self.teknik_servis_yetkilisi.receive_message(message)
        self.show_message_popup(message)  # Mesaj penceresi gösterimi

    # Gönderilen mesaj penceresi gösterimi
    def show_message_popup(self, message):
        message_popup = Toplevel(self.root)
        message_popup.title("Gönderilen Mesaj")
        message_popup.geometry("400x300")

        message_label = Label(message_popup, text="Gönderilen Mesaj:", font=("Helvetica", 18))
        message_label.pack(pady=10)

        message_text = Text(message_popup, width=40, height=10, font=("Helvetica", 14))
        message_text.pack(padx=20, pady=20)

        message_text.insert(tk.END, message)

    # Ana döngüyü başlatma
    def main(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    # Pencere kapatıldığında tetiklenen olay
    def on_closing(self):
        if self.message_sending:
            self.root.after(100, self.on_closing)
        else:
            self.root.destroy()

    # Constructor
    def __init__(self, root, teknik_servis_yetkilisi):
        self.root = root
        self.root.title("Teknik Servis Otomasyonu")
        self.root.geometry("1000x800")

        # Arayüz özellikleri
        self.root.iconbitmap("Icon.ico")
        self.devices = []
        self.arizalar = []
        self.root.configure(bg="lightgray")

        # Cihaz etiketi ve seçenek menüsü
        self.device_label = Label(root, text="Cihaz:", font=("Helvetica", 16), bg="lightgray")
        self.device_label.pack(padx=20, pady=10)

        self.device_var = StringVar()
        self.device_var.set("Seçiniz")
        self.device_optionmenu = OptionMenu(root, self.device_var, "Bilgisayar", "Telefon", "Tablet", "Yazıcı", "Diğer")
        self.device_optionmenu.config(font=("Helvetica", 14), width=15)
        self.device_optionmenu.pack(padx=20, pady=5, fill=tk.BOTH)

        # Cihaz ekleme düğmesi
        self.add_device_button = Button(root, text="Cihaz Ekle", command=self.add_device, bg="green", fg="white", font=("Helvetica", 14))
        self.add_device_button.pack(fill=tk.BOTH, padx=20, pady=10)

        # Seçilen cihazın etiketi
        self.selected_device_label = Label(root, text="", font=("Helvetica", 18, "bold"), bg="lightgray", fg="blue")
        self.selected_device_label.pack(padx=20, pady=10)

        # Arıza etiketi ve seçenek menüsü
        self.ariza_label = Label(root, text="Arıza:", font=("Helvetica", 16), bg="lightgray")
        self.ariza_label.pack(padx=20, pady=10)

        self.ariza_var = StringVar()
        self.ariza_var.set("Seçiniz")
        self.ariza_optionmenu = OptionMenu(root, self.ariza_var, "Ekran sorunu", "Pil sorunu", "Şarj sorunu", "Yazılım sorunu", "Diğer")
        self.ariza_optionmenu.config(font=("Helvetica", 14), width=15)
        self.ariza_optionmenu.pack(padx=20, pady=5, fill=tk.BOTH)

        # Arıza ekleme düğmesi
        self.add_ariza_button = Button(root, text="Ekle", command=self.add_ariza, bg="green", fg="white", font=("Helvetica", 14))
        self.add_ariza_button.pack(fill=tk.BOTH, padx=20, pady=10)

        # Arıza kaydı etiketi
        self.ariza_kaydi_label = Label(root, text="", font=("Helvetica", 18, "bold"), bg="lightgray", fg="red")
        self.ariza_kaydi_label.pack(padx=20, pady=10)

        # Arıza listesi
        self.ariza_listbox = Listbox(root, width=70, height=10, font=("Helvetica", 14))
        self.ariza_listbox.pack(padx=20, pady=10)

        # Durumu güncelleme düğmesi
        self.update_status_button = Button(root, text="Servis Durumunu Güncelle", command=self.show_onarim_asamalari, bg="green", fg="white", font=("Helvetica", 14))
        self.update_status_button.pack(fill=tk.BOTH, padx=20, pady=10)

        # Arıza çeşitleri düğmesi
        self.ariza_cesitleri_button = Button(root, text="Arıza Çeşitleri", command=self.show_ariza_cesitleri, bg="green", fg="white", font=("Helvetica", 14))
        self.ariza_cesitleri_button.pack(fill=tk.BOTH, padx=20, pady=10)

        # Mesaj gönderme düğmesi
        self.message_button = Button(root, text="Teknik Servise Mesaj Gönder", command=self.open_message_window, bg="blue", fg="white", font=("Helvetica", 14))
        self.message_button.pack(fill=tk.BOTH, padx=20, pady=10)
        self.teknik_servis_yetkilisi = teknik_servis_yetkilisi
        self.message_sending = False

    # Cihaz ekleme işlemi
    def add_device(self):
        device_name = self.device_var.get()
        if device_name and device_name != "Seçiniz":
            self.devices.append(device_name)
            self.device_var.set("Seçiniz")
            self.selected_device_label.config(text=f"Seçilen Cihaz: {device_name}")

    # Arıza ekleme işlemi
    def add_ariza(self):
        ariza_desc = self.ariza_var.get()
        if ariza_desc and ariza_desc != "Seçiniz":
            self.arizalar.append((ariza_desc, "Beklemede"))
            self.ariza_listbox.insert(tk.END, ariza_desc)
            self.ariza_var.set("Seçiniz")
            self.ariza_kaydi_label.config(text=f"Arıza Kaydı Eklendi: {ariza_desc}", fg="red")

    # Durumu güncelleme işlemi
    def update_status(self):
        selected_index = self.ariza_listbox.curselection()
        if selected_index:
            ariza_index = selected_index[0]
            ariza_desc = self.ariza_listbox.get(ariza_index)
            self.arizalar[ariza_index] = (ariza_desc, "Tamamlandı")

    # Arıza çeşitleri penceresini gösterme
    def show_ariza_cesitleri(self):
        ariza_cesitleri_window = Toplevel(self.root)
        ariza_cesitleri_window.title("Arıza Çeşitleri")
        ariza_cesitleri_window.geometry("400x300")

        ariza_cesitleri_label = Label(ariza_cesitleri_window, text="Arıza Çeşitleri", font=("Helvetica", 18))
        ariza_cesitleri_label.pack(pady=10)

        ariza_cesitleri_text = tk.Text(ariza_cesitleri_window, width=40, height=10, font=("Helvetica", 14))
        ariza_cesitleri_text.pack(padx=20, pady=20)

        ariza_cesitleri_text.insert(tk.END, "1. Ekran sorunu\n2. Pil sorunu\n3. Şarj sorunu\n4. Yazılım sorunu\n5. Diğer")

    # Onarım aşamaları penceresini gösterme
    def show_onarim_asamalari(self):
        onarim_asamalari_window = Toplevel(self.root)
        onarim_asamalari_window.title("Onarım Aşamaları")
        onarim_asamalari_window.geometry("400x300")

        onarim_asamalari_label = Label(onarim_asamalari_window, text="Onarım Aşamaları", font=("Helvetica", 18))
        onarim_asamalari_label.pack(pady=10)

        onarim_asamalari_text = tk.Text(onarim_asamalari_window, width=40, height=10, font=("Helvetica", 14))
        onarim_asamalari_text.pack(padx=20, pady=20)

        onarim_asamalari_text.insert(tk.END, "1. Onarım Aşaması 1\n2. Onarım Aşaması 2\n3. Onarım Aşaması 3\n4. Montaj Aşaması\n5. Hazırlık Aşaması")

    # Mesaj gönderme penceresini açma
    def open_message_window(self):
        message_window = Toplevel(self.root)
        message_window.title("Teknik Servise Mesaj Gönder")
        message_window.geometry("400x400")

        message_label = Label(message_window, text="Mesajınızı Girin:", font=("Helvetica", 18))
        message_label.pack(pady=10)

        self.message_text = Text(message_window, width=40, height=10, font=("Helvetica", 14))
        self.message_text.pack(padx=20, pady=20)

        send_button = Button(message_window, text="Mesajı Gönder", command=self.send_message, bg="green", fg="white", font=("Helvetica", 14))
        send_button.pack(fill=tk.BOTH, padx=20, pady=10)

    # Mesaj gönderme işlemi
    def send_message(self):
        if self.message_sending:
            return

        message = self.message_text.get("1.0", tk.END)
        if message.strip():
            self.message_sending = True
            self.message_button.config(text="Gönderiliyor...", state=tk.DISABLED)
            self.teknik_servis_yetkilisi.receive_message(message)
            self.message_text.delete("1.0", tk.END)
            self.show_message_popup(message)
            self.message_sending = False
            self.message_button.config(text="Teknik Servise Mesaj Gönder", state=tk.NORMAL)

    # Pencere kapatıldığında tetiklenen olay
    def on_closing(self):
        if self.message_sending:
            self.root.after(100, self.on_closing)
        else:
            self.root.destroy()

    # Giriş penceresini açma
    def open_login_window(self):
        self.logged_in = False
        self.root.title("Kullanıcı Girişi")
        self.root.geometry("300x200")

        self.login_window = tk.Toplevel(self.root)
        login_screen = LoginScreen(self.login_window, self)

    # Giriş hatası gösterme
    def show_login_error(self):
        error_label = Label(self.login_window, text="Hatalı giriş. Tekrar deneyin.", font=("Helvetica", 12), fg="red")
        error_label.pack(pady=5)

    # Ana pencereyi açma
    def open_main_window(self):
        self.logged_in = True
        self.root.title("Teknik Servis Otomasyonu")
        self.root.geometry("1000x800")
        self.login_window.destroy()  # Giriş penceresini kapat

    # Ana döngüyü başlatma
    def main(self):
        self.open_login_window()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

# Giriş ekranı
class LoginScreen:
    def __init__(self, root, app):
        self.root = root
        self.root.title("Kullanıcı Girişi")
        self.root.geometry("300x200")
        self.app = app

        self.username_label = Label(root, text="Kullanıcı Adı:", font=("Helvetica", 14))
        self.username_label.pack(pady=10)

        self.username_entry = Entry(root, font=("Helvetica", 14))
        self.username_entry.pack(padx=20, pady=5)

        self.password_label = Label(root, text="Şifre:", font=("Helvetica", 14))
        self.password_label.pack(pady=10)

        self.password_entry = Entry(root, show="*", font=("Helvetica", 14))
        self.password_entry.pack(padx=20, pady=5)

        self.login_button = Button(root, text="Giriş Yap", command=self.perform_login, bg="green", fg="white", font=("Helvetica", 14))
        self.login_button.pack(fill=tk.BOTH, padx=20, pady=10)

    # Giriş işlemi
    def perform_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "12345":
            self.app.open_main_window()
            self.root.destroy()
        else:
            self.app.show_login_error()

# Ana program
if __name__ == "__main__":
    root = tk.Tk()

    teknik_servis_yetkilisi_root = tk.Tk()
    teknik_servis_yetkilisi_app = TeknikServisYetkilisiApp(teknik_servis_yetkilisi_root)

    app = TeknikServisApp(root, teknik_servis_yetkilisi_app)
    app.main()
