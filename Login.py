import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("iPhone Simulator - Perfect Replica")
app.geometry("460x760")
app.configure(fg_color="#0A0D14")
app.resizable(False, False)

# --- HLAVNÍ PLÁTNO PRO CELÝ TELEFON ---
canvas = ctk.CTkCanvas(
    master=app,
    width=320,
    height=650,
    bg="#0A0D14",
    highlightthickness=0
)
canvas.place(relx=0.5, rely=0.5, anchor="center")

# Funkce pro dokonale hladké zaoblené obdélníky (OPRAVENO: už žádné zmatené "=")
def draw_perfect_rounded_rect(canvas, x1, y1, x2, y2, r, fill_color, border_color="", border_width=1):
    canvas.create_arc(x1, y1, x1+2*r, y1+2*r, start=90, extent=90, fill=fill_color, outline="")
    canvas.create_arc(x2-2*r, y1, x2, y1+2*r, start=0, extent=90, fill=fill_color, outline="")
    canvas.create_arc(x2-2*r, y2-2*r, x2, y2, start=270, extent=90, fill=fill_color, outline="")
    canvas.create_arc(x1, y2-2*r, x1+2*r, y2, start=180, extent=90, fill=fill_color, outline="")
    canvas.create_rectangle(x1+r, y1, x2-r, y2, fill=fill_color, outline="")
    canvas.create_rectangle(x1, y1+r, x2, y2-r, fill=fill_color, outline="")
    
    if border_color:
        canvas.create_arc(x1, y1, x1+2*r, y1+2*r, start=90, extent=90, style="arc", outline=border_color, width=border_width)
        canvas.create_arc(x2-2*r, y1, x2, y1+2*r, start=0, extent=90, style="arc", outline=border_color, width=border_width)
        canvas.create_arc(x2-2*r, y2-2*r, x2, y2, start=270, extent=90, style="arc", outline=border_color, width=border_width)
        canvas.create_arc(x1, y2-2*r, x1+2*r, y2, start=180, extent=90, style="arc", outline=border_color, width=border_width)
        canvas.create_line(x1+r, y1, x2-r, y1, fill=border_color, width=border_width)
        canvas.create_line(x2, y1+r, x2, y2-r, fill=border_color, width=border_width)
        canvas.create_line(x1+r, y2, x2-r, y2, fill=border_color, width=border_width)
        canvas.create_line(x1, y1+r, x1, y2-r, fill=border_color, width=border_width)

# 1. Pozadí displeje uvnitř telefonu
draw_perfect_rounded_rect(canvas, 10, 10, 330, 670, r=45, fill_color="#0F121B")

# 2. Barevné kruhy na pozadí
canvas.create_oval(-30, 50, 180, 260, fill="#4E239B", outline="")   # Fialový
canvas.create_oval(160, 60, 350, 250, fill="#00A79D", outline="")   # Tyrkysový
canvas.create_oval(20, 500, 190, 670, fill="#D81B60", outline="")   # Růžový

# 3. PŘIHLASOVACÍ KARTA (Vykreslená až nad kruhy - rohy jsou čisté)
draw_perfect_rounded_rect(canvas, 30, 190, 310, 610, r=28, fill_color="#1F2433", border_color="#363F54", border_width=2)

# 4. VNĚJŠÍ SOUVISLÝ RÁM TELEFONU (Dokončený kolem dokola)
draw_perfect_rounded_rect(canvas, 10, 10, 330, 670, r=45, fill_color="", border_color="#3A4050", border_width=3)


# --- WIDGETY (TEXTY, VSTUPY A TLAČÍTKA) ---
status_time = ctk.CTkLabel(master=canvas, text="9:41", font=("Helvetica", 12, "bold"), text_color="#FFFFFF", bg_color="#0F121B")
status_time.place(x=38, y=24)

dynamic_island = ctk.CTkFrame(master=canvas, width=85, height=22, corner_radius=11, fg_color="#000000", border_width=0)
dynamic_island.place(relx=0.5, y=35, anchor="center")

status_icons = ctk.CTkLabel(master=canvas, text="📶 🚡 🔋", font=("Helvetica", 11), text_color="#FFFFFF", bg_color="#0F121B")
status_icons.place(x=248, y=24)

logo_bg = ctk.CTkFrame(master=canvas, width=42, height=42, corner_radius=14, fg_color="#2D374D", bg_color="#1F2433")
logo_bg.place(x=170, y=240, anchor="center")
logo_bg.pack_propagate(False)
logo = ctk.CTkLabel(master=logo_bg, text="⚡", font=("Arial", 18), text_color="#00C8FF")
logo.place(relx=0.5, rely=0.5, anchor="center")

title = ctk.CTkLabel(master=canvas, text="Welcome back", font=("Helvetica", 22, "bold"), text_color="#FFFFFF", bg_color="#1F2433")
title.place(x=170, y=295, anchor="center")

subtitle = ctk.CTkLabel(master=canvas, text="Sign in to continue your journey", font=("Helvetica", 11), text_color="#7E8B9B", bg_color="#1F2433")
subtitle.place(x=170, y=325, anchor="center")

email_input = ctk.CTkEntry(
    master=canvas, placeholder_text="Email (you@example.com)", width=230, height=42, corner_radius=10,
    fg_color="#141924", border_color="#2A3347", border_width=1.5, text_color="#FFFFFF", font=("Helvetica", 12), bg_color="#1F2433"
)
email_input.place(x=170, y=385, anchor="center")

password_input = ctk.CTkEntry(
    master=canvas, placeholder_text="Password", show="*", width=230, height=42, corner_radius=10,
    fg_color="#141924", border_color="#2A3347", border_width=1.5, text_color="#FFFFFF", font=("Helvetica", 12), bg_color="#1F2433"
)
password_input.place(x=170, y=445, anchor="center")

forgot_btn = ctk.CTkLabel(master=canvas, text="Forgot password?", font=("Helvetica", 10, "bold"), text_color="#00A2FF", bg_color="#1F2433")
forgot_btn.place(x=165, y=475)

login_btn = ctk.CTkButton(
    master=canvas, text="Sign In", width=230, height=44, corner_radius=10,
    font=("Helvetica", 13, "bold"), fg_color="#007AFF", hover_color="#0062CC", bg_color="#1F2433"
)
login_btn.place(x=170, y=525, anchor="center")

google_btn = ctk.CTkButton(
    master=canvas, text="Continue with Google", width=230, height=44, corner_radius=10,
    font=("Helvetica", 12), fg_color="#1F2433", border_color="#363F54", border_width=1.5,
    hover_color="#283146", text_color="#FFFFFF", bg_color="#1F2433"
)
google_btn.place(x=170, y=578, anchor="center")

app.mainloop()