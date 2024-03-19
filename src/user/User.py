class User:
    def __init__(self, first_name, last_name, phone_number, password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.password = password

    def display_user_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        # Note: Vous ne voudrez probablement pas afficher le mot de passe directement.
        # À des fins de démonstration uniquement.
        print(f"Phone Number: {self.phone_number}")
        print(f"Password: {self.password}")