import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Modern To-Do List")
app.geometry("900x550")
app.resizable(False, False)

# ================= SIDEBAR ===================
sidebar = ctk.CTkFrame(app, width=180, corner_radius=0)
sidebar.pack(side="left", fill="y")

title = ctk.CTkLabel(
    sidebar, text="📘 TO-DO APP", 
    font=("Poppins", 23, "bold")
)
title.pack(pady=25)

# ================= MAIN AREA ==================
main_area = ctk.CTkFrame(app)
main_area.pack(side="right", expand=True, fill="both")

# --------- Create 3 pages (Frames) ----------
home_page = ctk.CTkFrame(main_area, fg_color="transparent")
tasks_page = ctk.CTkFrame(main_area, fg_color="transparent")
about_page = ctk.CTkFrame(main_area, fg_color="transparent")

# Put all pages in same place (stacking)
for page in (home_page, tasks_page, about_page):
    page.place(relx=0, rely=0, relwidth=1, relheight=1)

# ============= PAGE CHANGER FUNCTION =============
def show_page(page):
    page.tkraise()

# ================= HOME PAGE =====================
home_label = ctk.CTkLabel(
    home_page, 
    text="🏠 Welcome to Your Modern To-Do App",
    font=("Poppins", 26, "bold")
)
home_label.pack(pady=40)

home_desc = ctk.CTkLabel(
    home_page,
    text="Stay organized. Stay productive.\nClick on Tasks to begin!",
    font=("Poppins", 16),
)
home_desc.pack()

# ================= TASKS PAGE ====================
heading = ctk.CTkLabel(tasks_page, text="Your Tasks", font=("Poppins", 30, "bold"))
heading.pack(pady=20)

task_entry = ctk.CTkEntry(
    tasks_page, 
    placeholder_text="Enter a new task...",
    width=520, height=40,
    corner_radius=15, font=("Poppins", 14)
)
task_entry.pack(pady=10)

# Store tasks
tasks = []

task_frame = ctk.CTkFrame(tasks_page, fg_color="#101315", corner_radius=12)
task_frame.pack(pady=15, padx=20, fill="both", expand=True)

def add_task():
    text = task_entry.get().strip()
    if text:
        row = ctk.CTkFrame(task_frame, fg_color="#1e2326", corner_radius=10)
        row.pack(fill="x", pady=5, padx=10)

        label = ctk.CTkLabel(row, text=text, font=("Poppins", 15))
        label.pack(side="left", padx=10, pady=8)

        delete_btn = ctk.CTkButton(
            row, text="❌", width=40,
            fg_color="#d02020", hover_color="#a11818",
            command=lambda r=row: delete_task(r)
        )
        delete_btn.pack(side="right", padx=10)

        tasks.append(row)
        task_entry.delete(0, 'end')

def delete_task(row):
    row.destroy()
    tasks.remove(row)

add_btn = ctk.CTkButton(
    tasks_page, text="➕ Add Task",
    command=add_task, width=200, height=45,
    corner_radius=20, fg_color="#00a8ff",
    hover_color="#007acc", font=("Poppins", 16, "bold")
)
add_btn.pack()

# ================= ABOUT PAGE =====================
about_label = ctk.CTkLabel(
    about_page,
    text="ℹ️ About This App",
    font=("Poppins", 28, "bold")
)
about_label.pack(pady=40)

about_desc = ctk.CTkLabel(
    about_page,
    text="This To-Do software is built by Arun_Verma.\n\n"
         "• Modern Windows-style UI\n"
         "• Fast, minimal & clean\n"
         "• Fully customizable\n",
    font=("Poppins", 15),
    justify="left"
)
about_desc.pack()

# ============== SIDEBAR BUTTONS ==================
home_btn = ctk.CTkButton(sidebar, text="🏠 Home", width=160,
                         command=lambda: show_page(home_page))
home_btn.pack(pady=10)

task_btn = ctk.CTkButton(sidebar, text="📝 Tasks", width=160,
                         command=lambda: show_page(tasks_page))
task_btn.pack(pady=10)

about_btn = ctk.CTkButton(sidebar, text="ℹ️ About", width=160,
                          command=lambda: show_page(about_page))
about_btn.pack(pady=10)

# Start on Home Page
show_page(home_page)

app.mainloop()
