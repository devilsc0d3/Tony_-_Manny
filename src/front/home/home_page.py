# def home_page():
#     import tkinter as tk
#     from tkinter import ttk
#
#     # Couleurs
#     BG_COLOR = "#f0f0f0"
#     BUTTON_COLOR = "#2c3e50"
#     TEXT_COLOR = "#777"
#
#     # Fenêtre principale
#     window = tk.Tk()
#     window.title("Création d'un compte")
#     window.geometry("400x300")
#     window.configure(bg=BG_COLOR)
#
#     # Cadre principal
#     main_frame = ttk.Frame(window, padding=20)
#     main_frame.pack()
#
#     # Titre
#     title_label = ttk.Label(main_frame, text="Tonny & Manny", font=("Arial", 18), foreground=BUTTON_COLOR)
#     title_label.pack()
#
#     title_label = ttk.Label(main_frame, text="create account", font=("Arial", 14), foreground=BUTTON_COLOR)
#     title_label.pack()
#
#     # Champs de saisie
#     username_label = ttk.Label(main_frame, text="name:", foreground=TEXT_COLOR)
#     username_entry = ttk.Entry(main_frame)
#
#     first_name_label = ttk.Label(main_frame, text="first name:", foreground=TEXT_COLOR)
#     first_name_entry = ttk.Entry(main_frame)
#
#     tel_label = ttk.Label(main_frame, text="tel:", foreground=TEXT_COLOR)
#     tel_entry = ttk.Entry(main_frame)
#
#     # Bouton de création
#     create_button = ttk.Button(main_frame, text="Créer un compte", style="Accent.TButton")
#
#     # Fonction de création de compte
#     def create_account():
#         username = username_entry.get()
#         first_name = first_name_entry.get()
#         tel = tel_entry.get()
#
#         print(f"Username: {username}")
#         print(f"First Name: {first_name}")
#         print(f"Tel: {tel}")
#
#         # Traitement des données saisies (ici, simulation)
#         print(f"Le compte a été créé avec succès!")
#
#         # Affichage d'un message de confirmation
#         confirmation_label = ttk.Label(main_frame, text="Compte créé avec succès!", foreground="green")
#         confirmation_label.pack()
#     # Disposition des widgets
#     username_label.pack(pady=5)
#     username_entry.pack()
#     username_entry.insert(0, "Enter any Text")
#
#     first_name_label.pack(pady=5)
#     first_name_entry.pack()
#
#     tel_label.pack(pady=5)
#     tel_entry.pack()
#
#     create_button.pack(pady=10)
#
#     # Lancement de la boucle principale
#     window.mainloop()
#
#
# home_page()
import tkinter as tk
from logging import root
from tkinter import ttk, messagebox
from tkinter.ttk import Button

import top

# Couleurs
BG_COLOR = "#f0f0f0"
BUTTON_COLOR = "#2c3e50"
TEXT_COLOR = "#777"

# Fenêtre principale
window = tk.Tk()
window.title("Création d'un compte")
window.geometry("400x300")
window.configure(bg=BG_COLOR)

# Cadre principal
main_frame = ttk.Frame(window, padding=20)
main_frame.pack()

# Titre
title_label = ttk.Label(main_frame, text="Créer un compte", font=("Arial", 18), foreground=BUTTON_COLOR)
title_label.pack()

# Champs de saisie
username_label = ttk.Label(main_frame, text="Nom d'utilisateur:", foreground=TEXT_COLOR)
username_entry = ttk.Entry(main_frame)

email_label = ttk.Label(main_frame, text="Email:", foreground=TEXT_COLOR)
email_entry = ttk.Entry(main_frame)

password_label = ttk.Label(main_frame, text="Mot de passe:", foreground=TEXT_COLOR)
password_entry = ttk.Entry(main_frame, show="*")


# Fonction de création de compte
def create_account():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Traitement des données saisies (ici, simulation)
    print(f"Création du compte pour {username} ({email}) avec le mot de passe {password}")

    # Affichage d'un message de confirmation
    confirmation_label = ttk.Label(main_frame, text="Compte créé avec succès!", foreground="green")
    confirmation_label.pack()


def helloCallBack():
    msg = messagebox.showinfo("Hello Python", "Hello World")


# Bouton de création
create_button = ttk.Button(main_frame, text="Créer un compte", style="Accent.TButton", command=helloCallBack)

# Disposition des widgets
username_label.pack(pady=5)
username_entry.pack()

email_label.pack(pady=5)
email_entry.pack()

password_label.pack(pady=5)
password_entry.pack()

create_button.pack(pady=10)


# Fonction de validation (optionnelle)
def validate_email(email):
    # TODO: Implémenter une logique de validation d'email plus robuste
    return "@" in email


# Fonction d'enregistrement (optionnelle)
def save_user(username, email, password):
    # TODO: Implémenter la logique de connexion à la base de données et d'enregistrement des utilisateurs
    pass


# Ajout de la validation et de l'enregistrement (optionnel)
create_button.configure(command=lambda: [validate_email(email_entry.get()),
                                         save_user(username_entry.get(), email_entry.get(), password_entry.get())])

# Lancement de la boucle principale
window.mainloop()
