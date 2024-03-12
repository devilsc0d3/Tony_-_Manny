def home_page():
    import tkinter as tk
    from tkinter import ttk, messagebox

    # Couleurs
    BG_COLOR = "#f0f0f0"
    BUTTON_COLOR = "#2c3e50"
    TEXT_COLOR = "#777"

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

    # Bouton de création
    create_button = ttk.Button(main_frame, text="Créer un compte", style="Accent.TButton", command=create_account)

    # Disposition des widgets
    username_label.pack(pady=5)
    username_entry.pack()

    email_label.pack(pady=5)
    email_entry.pack()

    password_label.pack(pady=5)
    password_entry.pack()

    create_button.pack(pady=10)

    # Lancement de la boucle principale
    window.mainloop()
