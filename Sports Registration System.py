import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from datetime import datetime


# =========================================================
# COLORS
# =========================================================
WHITE = "#FFFFFF"
BLACK = "#000000"
BG = "#F7F9FC"

BLUE = "#D6EAF8"
BLUE_DARK = "#2874A6"

GREEN = "#D5F5E3"
GREEN_DARK = "#239B56"

YELLOW = "#FCF3CF"
YELLOW_DARK = "#F39C12"

PURPLE = "#E8DAEF"
PURPLE_DARK = "#8E44AD"

RED = "#FADBD8"
RED_DARK = "#E74C3C"

GREY = "#E5E7E9"
GREY_DARK = "#5D6D7E"

LIGHT_BLUE = "#EBF5FB"


# =========================================================
# MYSQL CONNECTION
# =========================================================
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Omkamthe@03",
    database="sports_registration"
)

cur = con.cursor()


# =========================================================
# MAIN WINDOW
# =========================================================
root = tk.Tk()
root.title("Sports Registration System")
root.geometry("1100x750")
root.minsize(1000, 650)
root.configure(bg=WHITE)


# =========================================================
# CLEAR SCREEN
# =========================================================
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


# =========================================================
# TITLE
# =========================================================
def create_title(parent, text, bg_color=WHITE):
    frame = tk.Frame(
        parent,
        bg=bg_color,
        highlightbackground="#D5D8DC",
        highlightthickness=1
    )
    frame.pack(fill="x", padx=10, pady=(10, 5))

    label = tk.Label(
        frame,
        text=text,
        font=("Arial", 22, "bold"),
        bg=bg_color,
        fg=BLACK
    )
    label.pack(pady=15)

    return frame


# =========================================================
# BUTTON
# =========================================================
def create_button(parent, text, command, bg_color, width=20):
    button = tk.Button(
        parent,
        text=text,
        command=command,
        font=("Arial", 12, "bold"),
        bg=bg_color,
        fg=BLACK,
        activebackground=bg_color,
        activeforeground=BLACK,
        relief="flat",
        cursor="hand2",
        width=width,
        height=2,
        bd=0
    )
    return button


# =========================================================
# LOGIN
# =========================================================
def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "admin" and password == "admin123":
        open_dashboard()
    else:
        messagebox.showerror(
            "Login Failed",
            "Invalid Username or Password!"
        )


# =========================================================
# DASHBOARD
# =========================================================
def open_dashboard():
    clear_screen()

    root.configure(bg=WHITE)

    # Header
    header = tk.Frame(
        root,
        bg=BLUE,
        height=75,
        highlightbackground="#AED6F1",
        highlightthickness=1
    )
    header.pack(fill="x")

    tk.Label(
        header,
        text="🏆  Sports Registration System",
        font=("Arial", 24, "bold"),
        bg=BLUE,
        fg=BLACK
    ).pack(side="left", padx=25, pady=18)

    tk.Label(
        header,
        text="Admin",
        font=("Arial", 12, "bold"),
        bg=BLUE,
        fg=BLACK
    ).pack(side="right", padx=25)

    # Dashboard title
    tk.Label(
        root,
        text="Dashboard",
        font=("Arial", 25, "bold"),
        bg=WHITE,
        fg=BLACK
    ).pack(pady=25)

    # Buttons frame
    button_frame = tk.Frame(root, bg=WHITE)
    button_frame.pack()

    # Row 1
    b1 = create_button(
        button_frame,
        "➕  Add Registration",
        add_registration,
        GREEN,
        25
    )
    b1.grid(row=0, column=0, padx=10, pady=10)

    b2 = create_button(
        button_frame,
        "📋  View Records",
        view_records,
        BLUE,
        25
    )
    b2.grid(row=0, column=1, padx=10, pady=10)

    # Row 2
    b3 = create_button(
        button_frame,
        "🔍  Search Player",
        search_registration,
        YELLOW,
        25
    )
    b3.grid(row=1, column=0, padx=10, pady=10)

    b4 = create_button(
        button_frame,
        "✏  Update Registration",
        update_registration,
        PURPLE,
        25
    )
    b4.grid(row=1, column=1, padx=10, pady=10)

    # Row 3
    b5 = create_button(
        button_frame,
        "🗑  Delete Registration",
        delete_registration,
        RED,
        25
    )
    b5.grid(row=2, column=0, padx=10, pady=10)

    b6 = create_button(
        button_frame,
        "↪  Logout",
        logout,
        GREY,
        25
    )
    b6.grid(row=2, column=1, padx=10, pady=10)

    # Bottom information
    bottom = tk.Frame(
        root,
        bg=LIGHT_BLUE,
        highlightbackground="#AED6F1",
        highlightthickness=1
    )
    bottom.pack(fill="x", padx=40, pady=35)

    tk.Label(
        bottom,
        text="🏆",
        font=("Arial", 35),
        bg=LIGHT_BLUE,
        fg=BLUE_DARK
    ).pack(side="left", padx=30, pady=15)

    tk.Label(
        bottom,
        text="Play   •   Compete   •   Achieve",
        font=("Arial", 20, "bold"),
        bg=LIGHT_BLUE,
        fg=BLACK
    ).pack(pady=(15, 2))

    tk.Label(
        bottom,
        text="Your Game, Your Opportunity",
        font=("Arial", 12),
        bg=LIGHT_BLUE,
        fg=BLACK
    ).pack(pady=(0, 15))


# =========================================================
# ADD REGISTRATION
# =========================================================
def add_registration():
    clear_screen()

    create_title(
        root,
        "➕  Add New Sports Registration",
        GREEN
    )

    form = tk.Frame(root, bg=WHITE)
    form.pack(pady=20)

    # Variables
    name_var = tk.StringVar()
    phone_var = tk.StringVar()
    age_var = tk.StringVar()
    gender_var = tk.StringVar(value="Male")
    sport_var = tk.StringVar()
    category_var = tk.StringVar()
    registration_date_var = tk.StringVar()
    status_var = tk.StringVar(value="Registered")

    # Player Name
    tk.Label(
        form, text="Player Name",
        font=("Arial", 11, "bold"),
        bg=WHITE, fg=BLACK
    ).grid(row=0, column=0, sticky="w", padx=15, pady=8)

    name_entry = tk.Entry(
        form, textvariable=name_var,
        font=("Arial", 11), width=28,
        fg=BLACK, bg=WHITE
    )
    name_entry.grid(row=1, column=0, padx=15, pady=5)

    # Phone
    tk.Label(
        form, text="Phone",
        font=("Arial", 11, "bold"),
        bg=WHITE, fg=BLACK
    ).grid(row=0, column=1, sticky="w", padx=15, pady=8)

    phone_entry = tk.Entry(
        form, textvariable=phone_var,
        font=("Arial", 11), width=28,
        fg=BLACK, bg=WHITE
    )
    phone_entry.grid(row=1, column=1, padx=15, pady=5)

    # Age
    tk.Label(
        form, text="Age",
        font=("Arial", 11, "bold"),
        bg=WHITE, fg=BLACK
    ).grid(row=2, column=0, sticky="w", padx=15, pady=8)

    age_entry = tk.Entry(
        form, textvariable=age_var,
        font=("Arial", 11), width=28,
        fg=BLACK, bg=WHITE
    )
    age_entry.grid(row=3, column=0, padx=15, pady=5)

    # Gender
    tk.Label(
        form, text="Gender",
        font=("Arial", 11, "bold"),
        bg=WHITE, fg=BLACK
    ).grid(row=2, column=1, sticky="w", padx=15, pady=8)

    gender_combo = ttk.Combobox(
        form,
        textvariable=gender_var,
        values=["Male", "Female", "Other"],
        state="readonly",
        width=26,
        font=("Arial", 11)
    )
    gender_combo.grid(row=3, column=1, padx=15, pady=5)

    # Sport
    tk.Label(
        form, text="Sport",
        font=("Arial", 11, "bold"),
        bg=WHITE, fg=BLACK
    ).grid(row=4, column=0, sticky="w", padx=15, pady=8)

    sport_combo = ttk.Combobox(
        form,
        textvariable=sport_var,
        values=[
            "Cricket",
            "Football",
            "Basketball",
            "Volleyball",
            "Badminton",
            "Tennis",
            "Athletics",
            "Kabaddi",
            "Chess",
            "Other"
        ],
        state="readonly",
        width=26,
        font=("Arial", 11)
    )
    sport_combo.grid(row=5, column=0, padx=15, pady=5)

    # Category
    tk.Label(
        form, text="Category",
        font=("Arial", 11, "bold"),
        bg=WHITE, fg=BLACK
    ).grid(row=4, column=1, sticky="w", padx=15, pady=8)

    category_combo = ttk.Combobox(
        form,
        textvariable=category_var,
        values=[
            "Under 14",
            "Under 17",
            "Under 19",
            "Senior"
        ],
        state="readonly",
        width=26,
        font=("Arial", 11)
    )
    category_combo.grid(row=5, column=1, padx=15, pady=5)

    # Registration Date
    tk.Label(
        form, text="Registration Date (YYYY-MM-DD)",
        font=("Arial", 11, "bold"),
        bg=WHITE, fg=BLACK
    ).grid(row=6, column=0, sticky="w", padx=15, pady=8)

    date_entry = tk.Entry(
        form, textvariable=registration_date_var,
        font=("Arial", 11), width=28,
        fg=BLACK, bg=WHITE
    )
    date_entry.grid(row=7, column=0, padx=15, pady=5)

    # Status
    tk.Label(
        form, text="Status",
        font=("Arial", 11, "bold"),
        bg=WHITE, fg=BLACK
    ).grid(row=6, column=1, sticky="w", padx=15, pady=8)

    status_combo = ttk.Combobox(
        form,
        textvariable=status_var,
        values=[
            "Registered",
            "Confirmed",
            "Participated",
            "Cancelled"
        ],
        state="readonly",
        width=26,
        font=("Arial", 11)
    )
    status_combo.grid(row=7, column=1, padx=15, pady=5)

    # Save
    def save_registration():
        player_name = name_var.get().strip()
        phone = phone_var.get().strip()
        age = age_var.get().strip()
        gender = gender_var.get()
        sport = sport_var.get()
        category = category_var.get()
        registration_date = registration_date_var.get().strip()
        status = status_var.get()

        # Required validation
        if not all([
            player_name,
            phone,
            age,
            gender,
            sport,
            category,
            registration_date
        ]):
            messagebox.showwarning(
                "Validation",
                "Please fill all fields!"
            )
            return

        # Phone validation
        if not phone.isdigit() or len(phone) != 10:
            messagebox.showwarning(
                "Invalid Phone",
                "Phone number must contain exactly 10 digits!"
            )
            return

        # Age validation
        if not age.isdigit() or int(age) <= 0 or int(age) > 100:
            messagebox.showwarning(
                "Invalid Age",
                "Age must be a valid number between 1 and 100!"
            )
            return

        # Date validation
        try:
            datetime.strptime(registration_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning(
                "Invalid Date",
                "Date must be in YYYY-MM-DD format!"
            )
            return

        try:
            query = """
            INSERT INTO sports_registrations
            (player_name, phone, age, gender, sport,
             category, registration_date, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                player_name,
                phone,
                int(age),
                gender,
                sport,
                category,
                registration_date,
                status
            )

            cur.execute(query, values)
            con.commit()

            messagebox.showinfo(
                "Success",
                "Sports registration added successfully!"
            )

            add_registration()

        except Exception as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    button_frame = tk.Frame(root, bg=WHITE)
    button_frame.pack(pady=20)

    create_button(
        button_frame,
        "💾  Save Registration",
        save_registration,
        GREEN,
        22
    ).grid(row=0, column=0, padx=10)

    create_button(
        button_frame,
        "←  Back to Dashboard",
        open_dashboard,
        GREY,
        22
    ).grid(row=0, column=1, padx=10)


# =========================================================
# VIEW RECORDS
# =========================================================
def view_records():
    clear_screen()

    create_title(
        root,
        "📋  Sports Registration Records",
        BLUE
    )

    frame = tk.Frame(root, bg=WHITE)
    frame.pack(fill="both", expand=True, padx=20, pady=10)

    columns = (
        "ID",
        "Player",
        "Phone",
        "Age",
        "Gender",
        "Sport",
        "Category",
        "Date",
        "Status"
    )

    tree = ttk.Treeview(
        frame,
        columns=columns,
        show="headings"
    )

    for col in columns:
        tree.heading(col, text=col)

    tree.column("ID", width=50)
    tree.column("Player", width=140)
    tree.column("Phone", width=110)
    tree.column("Age", width=60)
    tree.column("Gender", width=80)
    tree.column("Sport", width=110)
    tree.column("Category", width=100)
    tree.column("Date", width=110)
    tree.column("Status", width=110)

    scrollbar = ttk.Scrollbar(
        frame,
        orient="vertical",
        command=tree.yview
    )

    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    try:
        cur.execute("""
            SELECT id, player_name, phone, age, gender,
                   sport, category, registration_date, status
            FROM sports_registrations
            ORDER BY id
        """)

        records = cur.fetchall()

        for row in records:
            tree.insert("", "end", values=row)

    except Exception as e:
        messagebox.showerror(
            "Database Error",
            str(e)
        )

    create_button(
        root,
        "←  Back to Dashboard",
        open_dashboard,
        GREY,
        22
    ).pack(pady=15)


# =========================================================
# SEARCH REGISTRATION
# =========================================================
def search_registration():
    clear_screen()

    create_title(
        root,
        "🔍  Search Sports Registration",
        YELLOW
    )

    search_frame = tk.Frame(root, bg=WHITE)
    search_frame.pack(pady=20)

    tk.Label(
        search_frame,
        text="Enter Player Name or Phone",
        font=("Arial", 12, "bold"),
        bg=WHITE,
        fg=BLACK
    ).pack(pady=5)

    search_entry = tk.Entry(
        search_frame,
        font=("Arial", 12),
        width=40,
        fg=BLACK,
        bg=WHITE
    )
    search_entry.pack(pady=10)

    result_frame = tk.Frame(root, bg=WHITE)
    result_frame.pack(fill="both", expand=True, padx=30)

    columns = (
        "ID",
        "Player",
        "Phone",
        "Sport",
        "Category",
        "Age",
        "Date",
        "Status"
    )

    tree = ttk.Treeview(
        result_frame,
        columns=columns,
        show="headings"
    )

    for col in columns:
        tree.heading(col, text=col)

    tree.column("ID", width=60)
    tree.column("Player", width=150)
    tree.column("Phone", width=120)
    tree.column("Sport", width=120)
    tree.column("Category", width=110)
    tree.column("Age", width=70)
    tree.column("Date", width=120)
    tree.column("Status", width=130)

    tree.pack(
        fill="both",
        expand=True
    )

    def search():
        value = search_entry.get().strip()

        if not value:
            messagebox.showwarning(
                "Search",
                "Please enter player name or phone!"
            )
            return

        for item in tree.get_children():
            tree.delete(item)

        try:
            query = """
            SELECT id, player_name, phone,
                   sport, category, age,
                   registration_date, status
            FROM sports_registrations
            WHERE player_name LIKE %s
               OR phone LIKE %s
            """

            search_value = "%" + value + "%"

            cur.execute(
                query,
                (search_value, search_value)
            )

            records = cur.fetchall()

            if not records:
                messagebox.showinfo(
                    "Search Result",
                    "No sports registration record found!"
                )
                return

            for row in records:
                tree.insert(
                    "",
                    "end",
                    values=row
                )

        except Exception as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    create_button(
        search_frame,
        "🔍  Search",
        search,
        YELLOW,
        22
    ).pack(pady=10)

    create_button(
        root,
        "←  Back to Dashboard",
        open_dashboard,
        GREY,
        22
    ).pack(pady=15)


# =========================================================
# UPDATE REGISTRATION
# =========================================================
def update_registration():
    clear_screen()

    create_title(
        root,
        "✏  Update Sports Registration",
        PURPLE
    )

    main_frame = tk.Frame(root, bg=WHITE)
    main_frame.pack(pady=15)

    id_var = tk.StringVar()

    tk.Label(
        main_frame,
        text="Registration ID",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=BLACK
    ).grid(row=0, column=0, padx=10, pady=10)

    id_entry = tk.Entry(
        main_frame,
        textvariable=id_var,
        font=("Arial", 11),
        width=25,
        fg=BLACK,
        bg=WHITE
    )
    id_entry.grid(row=0, column=1, padx=10)

    player_var = tk.StringVar()
    phone_var = tk.StringVar()
    age_var = tk.StringVar()
    gender_var = tk.StringVar(value="Male")
    sport_var = tk.StringVar()
    category_var = tk.StringVar()
    date_var = tk.StringVar()
    status_var = tk.StringVar(value="Registered")

    # Load Record
    def load_record():
        registration_id = id_var.get().strip()

        if not registration_id.isdigit():
            messagebox.showwarning(
                "Invalid ID",
                "Please enter a valid Registration ID!"
            )
            return

        try:
            cur.execute(
                """
                SELECT player_name, phone, age, gender,
                       sport, category, registration_date, status
                FROM sports_registrations
                WHERE id = %s
                """,
                (int(registration_id),)
            )

            record = cur.fetchone()

            if not record:
                messagebox.showinfo(
                    "Not Found",
                    "Sports registration record not found!"
                )
                return

            player_var.set(record[0])
            phone_var.set(record[1])
            age_var.set(record[2])
            gender_var.set(record[3])
            sport_var.set(record[4])
            category_var.set(record[5])
            date_var.set(str(record[6]))
            status_var.set(record[7])

        except Exception as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    create_button(
        main_frame,
        "🔍  Load Record",
        load_record,
        BLUE,
        18
    ).grid(row=0, column=2, padx=10)

    # Form
    form = tk.Frame(root, bg=WHITE)
    form.pack(pady=15)

    # Player
    tk.Label(
        form,
        text="Player Name",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=BLACK
    ).grid(row=0, column=0, sticky="w", padx=15, pady=5)

    player_entry = tk.Entry(
        form,
        textvariable=player_var,
        font=("Arial", 11),
        width=28,
        fg=BLACK,
        bg=WHITE
    )
    player_entry.grid(row=1, column=0, padx=15)

    # Phone
    tk.Label(
        form,
        text="Phone",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=BLACK
    ).grid(row=0, column=1, sticky="w", padx=15, pady=5)

    phone_entry = tk.Entry(
        form,
        textvariable=phone_var,
        font=("Arial", 11),
        width=28,
        fg=BLACK,
        bg=WHITE
    )
    phone_entry.grid(row=1, column=1, padx=15)

    # Age
    tk.Label(
        form,
        text="Age",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=BLACK
    ).grid(row=2, column=0, sticky="w", padx=15, pady=5)

    age_entry = tk.Entry(
        form,
        textvariable=age_var,
        font=("Arial", 11),
        width=28,
        fg=BLACK,
        bg=WHITE
    )
    age_entry.grid(row=3, column=0, padx=15)

    # Gender
    tk.Label(
        form,
        text="Gender",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=BLACK
    ).grid(row=2, column=1, sticky="w", padx=15, pady=5)

    gender_combo = ttk.Combobox(
        form,
        textvariable=gender_var,
        values=["Male", "Female", "Other"],
        state="readonly",
        width=26,
        font=("Arial", 11)
    )
    gender_combo.grid(row=3, column=1, padx=15)

    # Sport
    tk.Label(
        form,
        text="Sport",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=BLACK
    ).grid(row=4, column=0, sticky="w", padx=15, pady=5)

    sport_combo = ttk.Combobox(
        form,
        textvariable=sport_var,
        values=[
            "Cricket",
            "Football",
            "Basketball",
            "Volleyball",
            "Badminton",
            "Tennis",
            "Athletics",
            "Kabaddi",
            "Chess",
            "Other"
        ],
        state="readonly",
        width=26,
        font=("Arial", 11)
    )
    sport_combo.grid(row=5, column=0, padx=15)

    # Category
    tk.Label(
        form,
        text="Category",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=BLACK
    ).grid(row=4, column=1, sticky="w", padx=15, pady=5)

    category_combo = ttk.Combobox(
        form,
        textvariable=category_var,
        values=[
            "Under 14",
            "Under 17",
            "Under 19",
            "Senior"
        ],
        state="readonly",
        width=26,
        font=("Arial", 11)
    )
    category_combo.grid(row=5, column=1, padx=15)

    # Date
    tk.Label(
        form,
        text="Registration Date (YYYY-MM-DD)",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=BLACK
    ).grid(row=6, column=0, sticky="w", padx=15, pady=5)

    date_entry = tk.Entry(
        form,
        textvariable=date_var,
        font=("Arial", 11),
        width=28,
        fg=BLACK,
        bg=WHITE
    )
    date_entry.grid(row=7, column=0, padx=15)

    # Status
    tk.Label(
        form,
        text="Status",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=BLACK
    ).grid(row=6, column=1, sticky="w", padx=15, pady=5)

    status_combo = ttk.Combobox(
        form,
        textvariable=status_var,
        values=[
            "Registered",
            "Confirmed",
            "Participated",
            "Cancelled"
        ],
        state="readonly",
        width=26
    )
    status_combo.grid(row=7, column=1, padx=15)

    # Update
    def update_record():
        registration_id = id_var.get().strip()

        player_name = player_var.get().strip()
        phone = phone_var.get().strip()
        age = age_var.get().strip()
        gender = gender_var.get()
        sport = sport_var.get()
        category = category_var.get()
        registration_date = date_var.get().strip()
        status = status_var.get()

        if not registration_id.isdigit():
            messagebox.showwarning(
                "Invalid ID",
                "Enter a valid Registration ID!"
            )
            return

        if not all([
            player_name,
            phone,
            age,
            gender,
            sport,
            category,
            registration_date
        ]):
            messagebox.showwarning(
                "Validation",
                "Please fill all fields!"
            )
            return

        if not phone.isdigit() or len(phone) != 10:
            messagebox.showwarning(
                "Invalid Phone",
                "Phone number must contain exactly 10 digits!"
            )
            return

        if not age.isdigit() or int(age) <= 0 or int(age) > 100:
            messagebox.showwarning(
                "Invalid Age",
                "Age must be a valid number between 1 and 100!"
            )
            return

        try:
            datetime.strptime(
                registration_date,
                "%Y-%m-%d"
            )
        except ValueError:
            messagebox.showwarning(
                "Invalid Date",
                "Date must be in YYYY-MM-DD format!"
            )
            return

        try:
            query = """
            UPDATE sports_registrations
            SET player_name = %s,
                phone = %s,
                age = %s,
                gender = %s,
                sport = %s,
                category = %s,
                registration_date = %s,
                status = %s
            WHERE id = %s
            """

            values = (
                player_name,
                phone,
                int(age),
                gender,
                sport,
                category,
                registration_date,
                status,
                int(registration_id)
            )

            cur.execute(query, values)
            con.commit()

            if cur.rowcount == 0:
                messagebox.showinfo(
                    "Not Found",
                    "Registration ID not found!"
                )
                return

            messagebox.showinfo(
                "Success",
                "Sports registration updated successfully!"
            )

            open_dashboard()

        except Exception as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    button_frame = tk.Frame(root, bg=WHITE)
    button_frame.pack(pady=20)

    create_button(
        button_frame,
        "💾  Update Record",
        update_record,
        GREEN,
        22
    ).grid(row=0, column=0, padx=10)

    create_button(
        button_frame,
        "←  Back to Dashboard",
        open_dashboard,
        GREY,
        22
    ).grid(row=0, column=1, padx=10)


# =========================================================
# DELETE REGISTRATION
# =========================================================
def delete_registration():
    clear_screen()

    create_title(
        root,
        "🗑  Delete Sports Registration",
        RED
    )

    frame = tk.Frame(root, bg=WHITE)
    frame.pack(pady=50)

    tk.Label(
        frame,
        text="Enter Registration ID",
        font=("Arial", 12, "bold"),
        bg=WHITE,
        fg=BLACK
    ).pack(pady=10)

    id_entry = tk.Entry(
        frame,
        font=("Arial", 12),
        width=30,
        fg=BLACK,
        bg=WHITE
    )
    id_entry.pack(pady=10)

    def delete_record():
        registration_id = id_entry.get().strip()

        if not registration_id.isdigit():
            messagebox.showwarning(
                "Invalid ID",
                "Please enter a valid Registration ID!"
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this sports registration?"
        )

        if not confirm:
            return

        try:
            cur.execute(
                "DELETE FROM sports_registrations WHERE id = %s",
                (int(registration_id),)
            )

            con.commit()

            if cur.rowcount == 0:
                messagebox.showinfo(
                    "Not Found",
                    "Registration ID not found!"
                )
            else:
                messagebox.showinfo(
                    "Success",
                    "Sports registration deleted successfully!"
                )

                open_dashboard()

        except Exception as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    create_button(
        frame,
        "🗑  Delete Registration",
        delete_record,
        RED,
        25
    ).pack(pady=15)

    create_button(
        root,
        "←  Back to Dashboard",
        open_dashboard,
        GREY,
        22
    ).pack(pady=20)


# =========================================================
# LOGOUT
# =========================================================
def logout():
    answer = messagebox.askyesno(
        "Logout",
        "Are you sure you want to logout?"
    )

    if answer:
        create_login_screen()


# =========================================================
# LOGIN SCREEN
# =========================================================
def create_login_screen():
    clear_screen()

    root.configure(bg=WHITE)

    # Top header
    header = tk.Frame(
        root,
        bg=BLUE,
        height=90
    )
    header.pack(fill="x")

    tk.Label(
        header,
        text="🏆",
        font=("Arial", 35),
        bg=BLUE,
        fg=BLACK
    ).pack(pady=(10, 0))

    tk.Label(
        header,
        text="Sports Registration System",
        font=("Arial", 23, "bold"),
        bg=BLUE,
        fg=BLACK
    ).pack()

    # Login card
    card = tk.Frame(
        root,
        bg=WHITE,
        highlightbackground="#AED6F1",
        highlightthickness=2
    )
    card.pack(pady=50, ipadx=40, ipady=25)

    tk.Label(
        card,
        text="Login",
        font=("Arial", 25, "bold"),
        bg=WHITE,
        fg=BLACK
    ).pack(pady=15)

    # Username
    tk.Label(
        card,
        text="Username",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=BLACK
    ).pack(anchor="w", padx=20, pady=(10, 3))

    global username_entry
    username_entry = tk.Entry(
        card,
        font=("Arial", 12),
        width=35,
        fg=BLACK,
        bg=WHITE
    )
    username_entry.pack(padx=20, pady=5)

    # Password
    tk.Label(
        card,
        text="Password",
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=BLACK
    ).pack(anchor="w", padx=20, pady=(10, 3))

    global password_entry
    password_entry = tk.Entry(
        card,
        font=("Arial", 12),
        width=35,
        show="*",
        fg=BLACK,
        bg=WHITE
    )
    password_entry.pack(padx=20, pady=5)

    # Login button
    create_button(
        card,
        "🔐  LOGIN",
        login,
        BLUE,
        28
    ).pack(pady=25)

    tk.Label(
        card,
        text="Demo Login: admin / admin123",
        font=("Arial", 10),
        bg=WHITE,
        fg=GREY_DARK
    ).pack(pady=(0, 10))


# =========================================================
# START PROGRAM
# =========================================================
create_login_screen()

root.mainloop()


# =========================================================
# CLOSE DATABASE CONNECTION
# =========================================================
try:
    cur.close()
    con.close()
except:
    pass
