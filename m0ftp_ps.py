import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import ftplib
import os
import threading
from datetime import datetime

TRANSLATIONS = {
    "app_title": {
        "ar": "m0ftp-ps",
        "es": "m0ftp-ps",
        "en": "m0ftp-ps"
    },
    "connect": {
        "ar": "🔗 اتصال",
        "es": "🔗 Conectar",
        "en": "🔗 Connect"
    },
    "disconnect": {
        "ar": "🔌 قطع",
        "es": "🔌 Desconectar",
        "en": "🔌 Disconnect"
    },
    "refresh": {
        "ar": "🔄 تحديث",
        "es": "🔄 Actualizar",
        "en": "🔄 Refresh"
    },
    "upload": {
        "ar": "⬆ رفع",
        "es": "⬆ Subir",
        "en": "⬆ Upload"
    },
    "download": {
        "ar": "⬇ تحميل",
        "es": "⬇ Descargar",
        "en": "⬇ Download"
    },
    "delete": {
        "ar": "🗑️ حذف",
        "es": "🗑️ Eliminar",
        "en": "🗑️ Delete"
    },
    "new_folder": {
        "ar": "📁 مجلد جديد",
        "es": "📁 Nueva carpeta",
        "en": "📁 New folder"
    },
    "goto_data": {
        "ar": "📂 /data",
        "es": "📂 /data",
        "en": "📂 /data"
    },
    "path_label": {
        "ar": "المسار:",
        "es": "Ruta:",
        "en": "Path:"
    },
    "status_disconnected": {
        "ar": "🔌 غير متصل",
        "es": "🔌 Desconectado",
        "en": "🔌 Disconnected"
    },
    "status_connecting": {
        "ar": "⏳ جارٍ الاتصال بـ {host}:{port}...",
        "es": "⏳ Conectando a {host}:{port}...",
        "en": "⏳ Connecting to {host}:{port}..."
    },
    "status_connected": {
        "ar": "✅ متصل بـ {host}",
        "es": "✅ Conectado a {host}",
        "en": "✅ Connected to {host}"
    },
    "status_ready": {
        "ar": "✅ جاهز",
        "es": "✅ Listo",
        "en": "✅ Ready"
    },
    "status_uploading": {
        "ar": "⏫ جاري رفع {name}...",
        "es": "⏫ Subiendo {name}...",
        "en": "⏫ Uploading {name}..."
    },
    "status_downloading": {
        "ar": "⏬ جاري تحميل {name}...",
        "es": "⏬ Descargando {name}...",
        "en": "⏬ Downloading {name}..."
    },
    "status_refreshed": {
        "ar": "✅ تم التحديث - {count} عنصر",
        "es": "✅ Actualizado - {count} elementos",
        "en": "✅ Refreshed - {count} items"
    },
    "status_deleted": {
        "ar": "🗑️ تم حذف {name}",
        "es": "🗑️ Eliminado {name}",
        "en": "🗑️ Deleted {name}"
    },
    "status_renamed": {
        "ar": "✏️ تمت إعادة التسمية إلى {name}",
        "es": "✏️ Renombrado a {name}",
        "en": "✏️ Renamed to {name}"
    },
    "status_folder_created": {
        "ar": "📁 تم إنشاء مجلد {name}",
        "es": "📁 Carpeta creada {name}",
        "en": "📁 Folder created {name}"
    },
    "status_goto_data": {
        "ar": "📂 انتقلت إلى /data",
        "es": "📂 Navegado a /data",
        "en": "📂 Navigated to /data"
    },
    "menu_file": {
        "ar": "ملف",
        "es": "Archivo",
        "en": "File"
    },
    "menu_actions": {
        "ar": "عمليات",
        "es": "Acciones",
        "en": "Actions"
    },
    "menu_ps4": {
        "ar": "PS4",
        "es": "PS4",
        "en": "PS4"
    },
    "menu_language": {
        "ar": "اللغة",
        "es": "Idioma",
        "en": "Language"
    },
    "menu_exit": {
        "ar": "❌ خروج",
        "es": "❌ Salir",
        "en": "❌ Exit"
    },
    "menu_connect": {
        "ar": "اتصال",
        "es": "Conectar",
        "en": "Connect"
    },
    "menu_disconnect": {
        "ar": "قطع الاتصال",
        "es": "Desconectar",
        "en": "Disconnect"
    },
    "menu_refresh": {
        "ar": "تحديث",
        "es": "Actualizar",
        "en": "Refresh"
    },
    "menu_upload": {
        "ar": "رفع ملف",
        "es": "Subir archivo",
        "en": "Upload file"
    },
    "menu_download": {
        "ar": "تحميل ملف",
        "es": "Descargar archivo",
        "en": "Download file"
    },
    "menu_delete": {
        "ar": "حذف",
        "es": "Eliminar",
        "en": "Delete"
    },
    "menu_rename": {
        "ar": "إعادة تسمية",
        "es": "Renombrar",
        "en": "Rename"
    },
    "menu_new_folder": {
        "ar": "إنشاء مجلد",
        "es": "Crear carpeta",
        "en": "Create folder"
    },
    "menu_goto_data": {
        "ar": "الانتقال إلى /data",
        "es": "Ir a /data",
        "en": "Go to /data"
    },
    "dialog_title": {
        "ar": "اتصال بـ FTP",
        "es": "Conectar a FTP",
        "en": "FTP Connection"
    },
    "dialog_header": {
        "ar": "الاتصال بخادم FTP",
        "es": "Conectar al servidor FTP",
        "en": "Connect to FTP Server"
    },
    "label_host": {
        "ar": "عنوان IP:",
        "es": "Dirección IP:",
        "en": "IP Address:"
    },
    "label_port": {
        "ar": "المنفذ:",
        "es": "Puerto:",
        "en": "Port:"
    },
    "label_user": {
        "ar": "اسم المستخدم:",
        "es": "Usuario:",
        "en": "Username:"
    },
    "label_password": {
        "ar": "كلمة المرور:",
        "es": "Contraseña:",
        "en": "Password:"
    },
    "btn_connect": {
        "ar": "اتصال",
        "es": "Conectar",
        "en": "Connect"
    },
    "btn_cancel": {
        "ar": "إلغاء",
        "es": "Cancelar",
        "en": "Cancel"
    },
    "error_title": {
        "ar": "خطأ",
        "es": "Error",
        "en": "Error"
    },
    "warning_title": {
        "ar": "تحذير",
        "es": "Advertencia",
        "en": "Warning"
    },
    "info_title": {
        "ar": "ملاحظة",
        "es": "Nota",
        "en": "Note"
    },
    "success_title": {
        "ar": "تم",
        "es": "Éxito",
        "en": "Success"
    },
    "confirm_title": {
        "ar": "تأكيد",
        "es": "Confirmar",
        "en": "Confirm"
    },
    "msg_enter_host": {
        "ar": "الرجاء إدخال عنوان IP",
        "es": "Por favor ingrese la dirección IP",
        "en": "Please enter IP address"
    },
    "msg_connect_failed": {
        "ar": "فشل الاتصال: {error}",
        "es": "Falló la conexión: {error}",
        "en": "Connection failed: {error}"
    },
    "msg_not_connected": {
        "ar": "غير متصل",
        "es": "No conectado",
        "en": "Not connected"
    },
    "msg_connect_first": {
        "ar": "الرجاء الاتصال أولاً",
        "es": "Por favor conéctese primero",
        "en": "Please connect first"
    },
    "msg_already_connected": {
        "ar": "أنت متصل بالفعل. هل تريد إعادة الاتصال؟",
        "es": "Ya estás conectado. ¿Quieres reconectar?",
        "en": "Already connected. Do you want to reconnect?"
    },
    "msg_select_file": {
        "ar": "اختر ملفاً لتحميله",
        "es": "Seleccione un archivo para descargar",
        "en": "Select a file to download"
    },
    "msg_select_item": {
        "ar": "اختر عنصراً للحذف",
        "es": "Seleccione un elemento para eliminar",
        "en": "Select an item to delete"
    },
    "msg_select_rename": {
        "ar": "اختر عنصراً لإعادة تسميته",
        "es": "Seleccione un elemento para renombrar",
        "en": "Select an item to rename"
    },
    "msg_no_folder_download": {
        "ar": "لا يمكن تحميل مجلدات بشكل مباشر",
        "es": "No se pueden descargar carpetas directamente",
        "en": "Cannot download folders directly"
    },
    "msg_confirm_delete": {
        "ar": "هل أنت متأكد من حذف '{name}'؟",
        "es": "¿Estás seguro de eliminar '{name}'?",
        "en": "Are you sure you want to delete '{name}'?"
    },
    "msg_rename_prompt": {
        "ar": "أدخل الاسم الجديد لـ '{old}':",
        "es": "Ingrese el nuevo nombre para '{old}':",
        "en": "Enter new name for '{old}':"
    },
    "msg_new_folder_prompt": {
        "ar": "أدخل اسم المجلد:",
        "es": "Ingrese el nombre de la carpeta:",
        "en": "Enter folder name:"
    },
    "msg_upload_success": {
        "ar": "تم رفع {name} بنجاح",
        "es": "{name} subido con éxito",
        "en": "{name} uploaded successfully"
    },
    "msg_download_success": {
        "ar": "تم تحميل {name} بنجاح",
        "es": "{name} descargado con éxito",
        "en": "{name} downloaded successfully"
    },
    "msg_delete_success": {
        "ar": "تم حذف {name}",
        "es": "{name} eliminado",
        "en": "{name} deleted"
    },
    "msg_rename_success": {
        "ar": "تمت إعادة التسمية إلى {name}",
        "es": "Renombrado a {name}",
        "en": "Renamed to {name}"
    },
    "msg_folder_created": {
        "ar": "تم إنشاء مجلد {name}",
        "es": "Carpeta {name} creada",
        "en": "Folder {name} created"
    },
    "msg_upload_failed": {
        "ar": "فشل الرفع: {error}",
        "es": "Error al subir: {error}",
        "en": "Upload failed: {error}"
    },
    "msg_download_failed": {
        "ar": "فشل التحميل: {error}",
        "es": "Error al descargar: {error}",
        "en": "Download failed: {error}"
    },
    "msg_delete_failed": {
        "ar": "فشل الحذف: {error}",
        "es": "Error al eliminar: {error}",
        "en": "Delete failed: {error}"
    },
    "msg_rename_failed": {
        "ar": "فشل إعادة التسمية: {error}",
        "es": "Error al renombrar: {error}",
        "en": "Rename failed: {error}"
    },
    "msg_folder_failed": {
        "ar": "فشل إنشاء المجلد: {error}",
        "es": "Error al crear carpeta: {error}",
        "en": "Create folder failed: {error}"
    },
    "msg_navigate_failed": {
        "ar": "لا يمكن الانتقال إلى {path}: {error}",
        "es": "No se puede navegar a {path}: {error}",
        "en": "Cannot navigate to {path}: {error}"
    },
    "msg_list_failed": {
        "ar": "فشل جلب القائمة: {error}",
        "es": "Error al obtener lista: {error}",
        "en": "Failed to list directory: {error}"
    },
    "col_name": {
        "ar": "اسم الملف",
        "es": "Nombre de archivo",
        "en": "File name"
    },
    "col_size": {
        "ar": "الحجم",
        "es": "Tamaño",
        "en": "Size"
    },
    "col_type": {
        "ar": "النوع",
        "es": "Tipo",
        "en": "Type"
    },
    "col_perms": {
        "ar": "الصلاحيات",
        "es": "Permisos",
        "en": "Permissions"
    },
    "col_date": {
        "ar": "تاريخ التعديل",
        "es": "Fecha de modificación",
        "en": "Modified date"
    },
    "type_folder": {
        "ar": "مجلد",
        "es": "Carpeta",
        "en": "Folder"
    },
    "type_file": {
        "ar": "ملف",
        "es": "Archivo",
        "en": "File"
    },
    "context_open": {
        "ar": "📂 فتح",
        "es": "📂 Abrir",
        "en": "📂 Open"
    },
    "context_download": {
        "ar": "⬇ تحميل",
        "es": "⬇ Descargar",
        "en": "⬇ Download"
    },
    "context_delete": {
        "ar": "🗑️ حذف",
        "es": "🗑️ Eliminar",
        "en": "🗑️ Delete"
    },
    "context_rename": {
        "ar": "✏️ إعادة تسمية",
        "es": "✏️ Renombrar",
        "en": "✏️ Rename"
    }
}

class FTPConnectionDialog(tk.Toplevel):
    def __init__(self, parent, lang="ar"):
        super().__init__(parent)
        self.parent = parent
        self.lang = lang
        self.title(self.tr("dialog_title"))
        self.geometry("420x300")
        self.resizable(False, False)
        self.configure(bg="#1e1e1e")
        self.result = None
        self.default_host = "192.168.1.xxx"
        self.default_port = 2121
        tk.Label(self, text=self.tr("dialog_header"), font=("Segoe UI", 14, "bold"),
                 bg="#1e1e1e", fg="#e0e0e0").grid(row=0, column=0, columnspan=2, pady=(15, 10))
        labels = [self.tr("label_host"), self.tr("label_port"), self.tr("label_user"), self.tr("label_password")]
        entries = []
        for i, lbl in enumerate(labels):
            tk.Label(self, text=lbl, bg="#1e1e1e", fg="#aaaaaa", font=("Segoe UI", 10)).grid(
                row=i+1, column=0, padx=20, pady=5, sticky="e")
            entry = tk.Entry(self, width=25, bg="#2d2d2d", fg="#ffffff",
                             insertbackground="white", font=("Segoe UI", 10), relief="solid")
            entry.grid(row=i+1, column=1, padx=10, pady=5, sticky="w")
            entries.append(entry)
        self.host_entry, self.port_entry, self.user_entry, self.pass_entry = entries
        self.host_entry.insert(0, self.default_host)
        self.port_entry.insert(0, str(self.default_port))
        self.pass_entry.config(show="*")
        btn_frame = tk.Frame(self, bg="#1e1e1e")
        btn_frame.grid(row=5, column=0, columnspan=2, pady=20)
        connect_btn = tk.Button(btn_frame, text=self.tr("btn_connect"), command=self.on_connect,
                                bg="#3a3a3a", fg="#ffffff", font=("Segoe UI", 10),
                                padx=15, pady=5, relief="flat", cursor="hand2")
        connect_btn.pack(side="left", padx=10)
        connect_btn.bind("<Enter>", lambda e: e.widget.config(bg="#4a6fa5"))
        connect_btn.bind("<Leave>", lambda e: e.widget.config(bg="#3a3a3a"))
        cancel_btn = tk.Button(btn_frame, text=self.tr("btn_cancel"), command=self.destroy,
                               bg="#3a3a3a", fg="#ffffff", font=("Segoe UI", 10),
                               padx=15, pady=5, relief="flat", cursor="hand2")
        cancel_btn.pack(side="left", padx=10)
        cancel_btn.bind("<Enter>", lambda e: e.widget.config(bg="#6a3a3a"))
        cancel_btn.bind("<Leave>", lambda e: e.widget.config(bg="#3a3a3a"))
        self.grab_set()
        self.wait_window()

    def tr(self, key, **kwargs):
        text = TRANSLATIONS.get(key, {}).get(self.lang, key)
        if kwargs:
            text = text.format(**kwargs)
        return text

    def on_connect(self):
        host = self.host_entry.get().strip()
        try:
            port = int(self.port_entry.get().strip())
        except:
            port = 2121
        user = self.user_entry.get().strip()
        password = self.pass_entry.get().strip()
        if not host:
            messagebox.showerror(self.tr("error_title"), self.tr("msg_enter_host"))
            return
        self.result = (host, port, user, password)
        self.destroy()

class PS4FTPManagerPro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.lang = "ar"
        self.title(self.tr("app_title"))
        self.geometry("950x700")
        self.configure(bg="#1a1a1a")
        self.ftp = None
        self.current_path = "/"
        self.status_var = tk.StringVar(value=self.tr("status_disconnected"))
        self.progress_var = tk.DoubleVar(value=0.0)
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview",
                             background="#1e1e1e",
                             foreground="#e0e0e0",
                             fieldbackground="#1e1e1e",
                             font=("Segoe UI", 10),
                             rowheight=28)
        self.style.configure("Treeview.Heading",
                             background="#2d2d2d",
                             foreground="#e0e0e0",
                             font=("Segoe UI", 10, "bold"),
                             relief="flat")
        self.style.map("Treeview",
                       background=[("selected", "#4a6fa5")],
                       foreground=[("selected", "white")])
        self.style.configure("TProgressbar",
                             thickness=10,
                             background="#4a6fa5",
                             troughcolor="#2d2d2d")
        self.create_menu()
        self.create_toolbar()
        self.create_treeview()
        self.create_statusbar()
        self.bind("<Control-o>", lambda e: self.connect_dialog())
        self.bind("<F5>", lambda e: self.refresh_list())
        self.after(200, self.connect_dialog)

    def tr(self, key, **kwargs):
        text = TRANSLATIONS.get(key, {}).get(self.lang, key)
        if kwargs:
            text = text.format(**kwargs)
        return text

    def set_language(self, lang):
        self.lang = lang
        self.title(self.tr("app_title"))
        self.status_var.set(self.tr("status_disconnected") if not self.ftp else self.tr("status_connected", host="?"))
        self.rebuild_menus()
        self.rebuild_toolbar()
        self.update_statusbar_texts()
        self.update_treeview_headers()

    def rebuild_menus(self):
        self.config(menu="")
        self.create_menu()

    def rebuild_toolbar(self):
        for widget in self.toolbar.winfo_children():
            widget.destroy()
        self.build_toolbar_widgets()

    def update_statusbar_texts(self):
        pass

    def update_treeview_headers(self):
        self.tree.heading("#0", text=self.tr("col_name"), anchor="w")
        self.tree.heading("size", text=self.tr("col_size"))
        self.tree.heading("type", text=self.tr("col_type"))
        self.tree.heading("perms", text=self.tr("col_perms"))
        self.tree.heading("date", text=self.tr("col_date"))

    def create_menu(self):
        menubar = tk.Menu(self, bg="#1a1a1a", fg="#e0e0e0", font=("Segoe UI", 10))
        file_menu = tk.Menu(menubar, tearoff=0, bg="#1a1a1a", fg="#e0e0e0", font=("Segoe UI", 10))
        file_menu.add_command(label=self.tr("menu_connect"), command=self.connect_dialog, accelerator="Ctrl+O")
        file_menu.add_command(label=self.tr("menu_disconnect"), command=self.disconnect_ftp)
        file_menu.add_separator()
        file_menu.add_command(label=self.tr("menu_exit"), command=self.quit)
        menubar.add_cascade(label=self.tr("menu_file"), menu=file_menu)
        action_menu = tk.Menu(menubar, tearoff=0, bg="#1a1a1a", fg="#e0e0e0", font=("Segoe UI", 10))
        action_menu.add_command(label=self.tr("menu_refresh"), command=self.refresh_list, accelerator="F5")
        action_menu.add_command(label=self.tr("menu_upload"), command=self.upload_file)
        action_menu.add_command(label=self.tr("menu_download"), command=self.download_file)
        action_menu.add_command(label=self.tr("menu_new_folder"), command=self.create_folder)
        action_menu.add_command(label=self.tr("menu_rename"), command=self.rename_item)
        action_menu.add_command(label=self.tr("menu_delete"), command=self.delete_item)
        menubar.add_cascade(label=self.tr("menu_actions"), menu=action_menu)
        ps4_menu = tk.Menu(menubar, tearoff=0, bg="#1a1a1a", fg="#e0e0e0", font=("Segoe UI", 10))
        ps4_menu.add_command(label=self.tr("menu_goto_data"), command=self.goto_data)
        menubar.add_cascade(label=self.tr("menu_ps4"), menu=ps4_menu)
        lang_menu = tk.Menu(menubar, tearoff=0, bg="#1a1a1a", fg="#e0e0e0", font=("Segoe UI", 10))
        lang_menu.add_command(label="العربية", command=lambda: self.set_language("ar"))
        lang_menu.add_command(label="Español", command=lambda: self.set_language("es"))
        lang_menu.add_command(label="English", command=lambda: self.set_language("en"))
        menubar.add_cascade(label=self.tr("menu_language"), menu=lang_menu)
        self.config(menu=menubar)

    def create_toolbar(self):
        self.toolbar = tk.Frame(self, bg="#2d2d2d", height=45)
        self.toolbar.pack(fill="x", pady=(5, 0))
        self.build_toolbar_widgets()

    def build_toolbar_widgets(self):
        def make_btn(parent, text_key, command, side="left"):
            btn = tk.Button(parent, text=self.tr(text_key), command=command,
                            bg="#3a3a3a", fg="#e0e0e0", font=("Segoe UI", 10),
                            padx=8, pady=3, relief="flat", cursor="hand2")
            btn.pack(side=side, padx=2)
            btn.bind("<Enter>", lambda e: e.widget.config(bg="#4a6fa5"))
            btn.bind("<Leave>", lambda e: e.widget.config(bg="#3a3a3a"))
            return btn
        make_btn(self.toolbar, "connect", self.connect_dialog)
        make_btn(self.toolbar, "disconnect", self.disconnect_ftp)
        make_btn(self.toolbar, "refresh", self.refresh_list)
        make_btn(self.toolbar, "upload", self.upload_file)
        make_btn(self.toolbar, "download", self.download_file)
        make_btn(self.toolbar, "delete", self.delete_item)
        make_btn(self.toolbar, "new_folder", self.create_folder)
        make_btn(self.toolbar, "goto_data", self.goto_data)
        tk.Label(self.toolbar, text=self.tr("path_label"), bg="#2d2d2d", fg="#aaaaaa",
                 font=("Segoe UI", 10)).pack(side="left", padx=(20, 5))
        self.path_var = tk.StringVar(value="/")
        self.path_entry = tk.Entry(self.toolbar, textvariable=self.path_var, width=60,
                                   bg="#1a1a1a", fg="#e0e0e0", insertbackground="white",
                                   font=("Segoe UI", 10), relief="flat")
        self.path_entry.pack(side="left", padx=5, fill="x", expand=True)
        self.path_entry.bind("<Return>", lambda e: self.navigate_to_path())

    def create_treeview(self):
        tree_frame = tk.Frame(self, bg="#1a1a1a")
        tree_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.tree = ttk.Treeview(tree_frame, columns=("size", "type", "perms", "date"), show="tree headings")
        self.tree.heading("#0", text=self.tr("col_name"), anchor="w")
        self.tree.heading("size", text=self.tr("col_size"))
        self.tree.heading("type", text=self.tr("col_type"))
        self.tree.heading("perms", text=self.tr("col_perms"))
        self.tree.heading("date", text=self.tr("col_date"))
        self.tree.column("#0", width=350, anchor="w")
        self.tree.column("size", width=120, anchor="e")
        self.tree.column("type", width=100, anchor="center")
        self.tree.column("perms", width=110, anchor="center")
        self.tree.column("date", width=160, anchor="center")
        v_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        h_scroll = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
        self.tree.pack(side="left", fill="both", expand=True)
        v_scroll.pack(side="right", fill="y")
        h_scroll.pack(side="bottom", fill="x")
        self.tree.bind("<Double-1>", self.on_double_click)
        self.tree.bind("<Button-3>", self.show_context_menu)
        self.tree.tag_configure("odd", background="#252525")
        self.tree.tag_configure("even", background="#1e1e1e")

    def create_statusbar(self):
        status_frame = tk.Frame(self, bg="#1a1a1a", height=30)
        status_frame.pack(fill="x", side="bottom")
        self.status_label = tk.Label(status_frame, textvariable=self.status_var,
                                     bg="#1a1a1a", fg="#aaaaaa", font=("Segoe UI", 9))
        self.status_label.pack(side="left", padx=10)
        tk.Label(status_frame, text="© 2026 mansoo0x",
                 bg="#1a1a1a", fg="#555555", font=("Segoe UI", 8, "italic")).pack(side="left", padx=20)
        self.progress_bar = ttk.Progressbar(status_frame, variable=self.progress_var,
                                            maximum=100, length=180)
        self.progress_bar.pack(side="right", padx=5)
        self.progress_label = tk.Label(status_frame, text="0%",
                                       bg="#1a1a1a", fg="#e0e0e0", font=("Segoe UI", 9))
        self.progress_label.pack(side="right", padx=5)

    def connect_dialog(self):
        if self.ftp:
            reply = messagebox.askyesno(self.tr("confirm_title"), self.tr("msg_already_connected"))
            if not reply:
                return
            self.disconnect_ftp()
        dialog = FTPConnectionDialog(self, self.lang)
        if dialog.result:
            host, port, user, password = dialog.result
            self.status_var.set(self.tr("status_connecting", host=host, port=port))
            threading.Thread(target=self.connect_ftp, args=(host, port, user, password), daemon=True).start()

    def connect_ftp(self, host, port, user, password):
        try:
            self.ftp = ftplib.FTP()
            self.ftp.connect(host, port)
            if user:
                self.ftp.login(user, password)
            else:
                self.ftp.login()
            self.ftp.set_pasv(True)
            self.current_path = "/"
            self.after(0, lambda: self.status_var.set(self.tr("status_connected", host=host)))
            self.after(0, self.refresh_list)
        except Exception as e:
            self.after(0, lambda: messagebox.showerror(self.tr("error_title"),
                                                       self.tr("msg_connect_failed", error=str(e))))
            self.after(0, lambda: self.status_var.set(self.tr("status_disconnected")))

    def disconnect_ftp(self):
        if self.ftp:
            try:
                self.ftp.quit()
            except:
                pass
            self.ftp = None
        self.current_path = "/"
        self.path_var.set("/")
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.status_var.set(self.tr("status_disconnected"))
        self.progress_var.set(0)
        self.progress_label.config(text="0%")

    def refresh_list(self):
        if not self.ftp:
            messagebox.showwarning(self.tr("warning_title"), self.tr("msg_connect_first"))
            return
        try:
            for item in self.tree.get_children():
                self.tree.delete(item)
            files = []
            self.ftp.retrlines('LIST', files.append)
            row_index = 0
            for line in files:
                parts = line.split()
                if len(parts) < 9:
                    continue
                perms = parts[0]
                size = parts[4]
                date = " ".join(parts[5:8])
                name = " ".join(parts[8:])
                ftype = self.tr("type_folder") if perms.startswith('d') else self.tr("type_file")
                tag = "odd" if row_index % 2 == 0 else "even"
                self.tree.insert("", "end", text=name, values=(size, ftype, perms, date), tags=(tag,))
                row_index += 1
            self.path_var.set(self.current_path)
            self.status_var.set(self.tr("status_refreshed", count=len(self.tree.get_children())))
        except Exception as e:
            messagebox.showerror(self.tr("error_title"), self.tr("msg_list_failed", error=str(e)))

    def navigate_to_path(self):
        path = self.path_var.get().strip()
        if not path:
            return
        try:
            self.ftp.cwd(path)
            self.current_path = self.ftp.pwd()
            self.refresh_list()
        except Exception as e:
            messagebox.showerror(self.tr("error_title"), self.tr("msg_navigate_failed", path=path, error=str(e)))

    def on_double_click(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        item = selected[0]
        name = self.tree.item(item, "text")
        if self.tree.item(item, "values")[1] == self.tr("type_folder"):
            try:
                self.ftp.cwd(name)
                self.current_path = self.ftp.pwd()
                self.refresh_list()
            except Exception as e:
                messagebox.showerror(self.tr("error_title"), self.tr("msg_navigate_failed", path=name, error=str(e)))

    def upload_file(self):
        if not self.ftp:
            messagebox.showwarning(self.tr("warning_title"), self.tr("msg_not_connected"))
            return
        path = filedialog.askopenfilename()
        if not path:
            return
        filename = os.path.basename(path)
        threading.Thread(target=self._upload, args=(path, filename), daemon=True).start()

    def _upload(self, local_path, remote_name):
        try:
            self.after(0, lambda: self.status_var.set(self.tr("status_uploading", name=remote_name)))
            self.after(0, lambda: self.progress_var.set(0))
            size = os.path.getsize(local_path)
            uploaded = 0
            def update_progress(chunk):
                nonlocal uploaded
                uploaded += len(chunk)
                percent = (uploaded / size) * 100
                self.after(0, lambda: self.progress_var.set(percent))
                self.after(0, lambda: self.progress_label.config(text=f"{int(percent)}%"))
            with open(local_path, 'rb') as f:
                self.ftp.storbinary(f'STOR {remote_name}', f, callback=update_progress)
            self.after(0, lambda: messagebox.showinfo(self.tr("success_title"),
                                                       self.tr("msg_upload_success", name=remote_name)))
            self.after(0, self.refresh_list)
            self.after(0, lambda: self.status_var.set(self.tr("status_ready")))
            self.after(0, lambda: self.progress_var.set(0))
            self.after(0, lambda: self.progress_label.config(text="0%"))
        except Exception as e:
            self.after(0, lambda: messagebox.showerror(self.tr("error_title"),
                                                       self.tr("msg_upload_failed", error=str(e))))

    def download_file(self):
        if not self.ftp:
            messagebox.showwarning(self.tr("warning_title"), self.tr("msg_not_connected"))
            return
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning(self.tr("warning_title"), self.tr("msg_select_file"))
            return
        item = selected[0]
        name = self.tree.item(item, "text")
        if self.tree.item(item, "values")[1] == self.tr("type_folder"):
            messagebox.showinfo(self.tr("info_title"), self.tr("msg_no_folder_download"))
            return
        save_path = filedialog.asksaveasfilename(initialfile=name)
        if not save_path:
            return
        threading.Thread(target=self._download, args=(name, save_path), daemon=True).start()

    def _download(self, remote_name, local_path):
        try:
            self.after(0, lambda: self.status_var.set(self.tr("status_downloading", name=remote_name)))
            self.after(0, lambda: self.progress_var.set(0))
            size = None
            files = []
            self.ftp.retrlines('LIST', files.append)
            for line in files:
                parts = line.split()
                if len(parts) >= 9 and " ".join(parts[8:]) == remote_name:
                    size = int(parts[4])
                    break
            downloaded = 0
            def update_progress(chunk):
                nonlocal downloaded
                downloaded += len(chunk)
                if size:
                    percent = (downloaded / size) * 100
                    self.after(0, lambda: self.progress_var.set(percent))
                    self.after(0, lambda: self.progress_label.config(text=f"{int(percent)}%"))
            with open(local_path, 'wb') as f:
                self.ftp.retrbinary(f'RETR {remote_name}', f.write, callback=update_progress)
            self.after(0, lambda: messagebox.showinfo(self.tr("success_title"),
                                                       self.tr("msg_download_success", name=remote_name)))
            self.after(0, lambda: self.status_var.set(self.tr("status_ready")))
            self.after(0, lambda: self.progress_var.set(0))
            self.after(0, lambda: self.progress_label.config(text="0%"))
        except Exception as e:
            self.after(0, lambda: messagebox.showerror(self.tr("error_title"),
                                                       self.tr("msg_download_failed", error=str(e))))

    def delete_item(self):
        if not self.ftp:
            messagebox.showwarning(self.tr("warning_title"), self.tr("msg_not_connected"))
            return
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning(self.tr("warning_title"), self.tr("msg_select_item"))
            return
        item = selected[0]
        name = self.tree.item(item, "text")
        if not messagebox.askyesno(self.tr("confirm_title"), self.tr("msg_confirm_delete", name=name)):
            return
        try:
            if self.tree.item(item, "values")[1] == self.tr("type_folder"):
                self.ftp.rmd(name)
            else:
                self.ftp.delete(name)
            self.refresh_list()
            self.status_var.set(self.tr("status_deleted", name=name))
        except Exception as e:
            messagebox.showerror(self.tr("error_title"), self.tr("msg_delete_failed", error=str(e)))

    def rename_item(self):
        if not self.ftp:
            messagebox.showwarning(self.tr("warning_title"), self.tr("msg_not_connected"))
            return
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning(self.tr("warning_title"), self.tr("msg_select_rename"))
            return
        item = selected[0]
        old_name = self.tree.item(item, "text")
        new_name = simpledialog.askstring("Rename", self.tr("msg_rename_prompt", old=old_name))
        if not new_name:
            return
        try:
            self.ftp.rename(old_name, new_name)
            self.refresh_list()
            self.status_var.set(self.tr("status_renamed", name=new_name))
        except Exception as e:
            messagebox.showerror(self.tr("error_title"), self.tr("msg_rename_failed", error=str(e)))

    def create_folder(self):
        if not self.ftp:
            messagebox.showwarning(self.tr("warning_title"), self.tr("msg_not_connected"))
            return
        folder_name = simpledialog.askstring("New Folder", self.tr("msg_new_folder_prompt"))
        if not folder_name:
            return
        try:
            self.ftp.mkd(folder_name)
            self.refresh_list()
            self.status_var.set(self.tr("status_folder_created", name=folder_name))
        except Exception as e:
            messagebox.showerror(self.tr("error_title"), self.tr("msg_folder_failed", error=str(e)))

    def goto_data(self):
        if not self.ftp:
            messagebox.showwarning(self.tr("warning_title"), self.tr("msg_not_connected"))
            return
        try:
            self.ftp.cwd("/data")
            self.current_path = self.ftp.pwd()
            self.refresh_list()
            self.status_var.set(self.tr("status_goto_data"))
        except Exception as e:
            messagebox.showerror(self.tr("error_title"), self.tr("msg_navigate_failed", path="/data", error=str(e)))

    def show_context_menu(self, event):
        if not self.ftp:
            return
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            menu = tk.Menu(self, tearoff=0, bg="#2d2d2d", fg="#e0e0e0", font=("Segoe UI", 10))
            menu.add_command(label=self.tr("context_open"), command=lambda: self.on_double_click(None))
            menu.add_command(label=self.tr("context_download"), command=self.download_file)
            menu.add_command(label=self.tr("context_delete"), command=self.delete_item)
            menu.add_command(label=self.tr("context_rename"), command=self.rename_item)
            menu.tk_popup(event.x_root, event.y_root)

if __name__ == "__main__":
    app = PS4FTPManagerPro()
    app.mainloop()