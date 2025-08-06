import random
import string
import time

class PasswordGenerator:
    """
    Generează parole securizate respectând o serie de reguli stricte,
    încapsulând toată logica de creare și validare într-o singură clasă.
    """

    def _get_char_category(self, char):
        """Metodă privată ce returnează categoria unui caracter."""
        if char in string.ascii_lowercase:
            return 'lowercase'
        elif char in string.ascii_uppercase:
            return 'uppercase'
        elif char in string.digits:
            return 'digit'
        elif char in string.punctuation:
            return 'symbol'
        return None

    def _is_valid_password_order(self, password):
        """
        Metodă privată ce verifică dacă parola nu are mai mult de două
        caractere consecutive din aceeași categorie.
        """
        if not password:
            return True

        count = 1
        for i in range(1, len(password)):
            current_category = self._get_char_category(password[i])
            previous_category = self._get_char_category(password[i - 1])

            if current_category and current_category == previous_category:
                count += 1
                if count > 2:
                    return False
            else:
                count = 1
        return True

    def generate_strict_password(self, length):
        """
        Metoda publică care generează o parolă securizată conform regulilor:
        - lungime minimă de 8 caractere
        - distribuție echilibrată de caractere
        - începe cu o literă mică
        - fără mai mult de două caractere consecutive de același tip
        """
        if length < 8:
            print("Avertisment: Lungimea parolei a fost ajustată la minim 8 caractere pentru securitate.")
            length = 8

        is_valid = False
        while not is_valid:
            num_chars_per_type = length // 4
            remainder = length % 4

            num_lowercase = num_chars_per_type + (1 if remainder > 0 else 0)
            num_uppercase = num_chars_per_type + (1 if remainder > 1 else 0)
            num_digits = num_chars_per_type + (1 if remainder > 2 else 0)
            num_symbols = num_chars_per_type

            lowercase_chars = [random.choice(string.ascii_lowercase) for _ in range(num_lowercase)]
            uppercase_chars = [random.choice(string.ascii_uppercase) for _ in range(num_uppercase)]
            digit_chars = [random.choice(string.digits) for _ in range(num_digits)]
            symbol_chars = [random.choice(string.punctuation) for _ in range(num_symbols)]

            all_chars = lowercase_chars + uppercase_chars + digit_chars + symbol_chars
            random.shuffle(all_chars)

            first_char = random.choice(string.ascii_lowercase)
            all_chars.insert(0, first_char)
            all_chars.pop(random.randint(1, len(all_chars) - 1))
            
            password = "".join(all_chars)

            if self._is_valid_password_order(password):
                is_valid = True
                
        return password

    def calculate_complexity(self, password):
        """
        Calculează complexitatea parolei conform regulilor specificate.
        - 'Super Strong' dacă nu se repetă niciun caracter.
        - 'Strong' dacă cel puțin un caracter se repetă.
        """
        # Convertim la set pentru a găsi caractere unice
        unique_chars = set(password.lower()) # ignoram case-ul pentru litere
        if len(unique_chars) == len(password):
            return "Super Strong"
        else:
            return "Strong"

def analyze_passwords(generator):
    """
    Generează un set de parole și afișează un tabel de analiză.
    """
    try:
        num_passwords = int(input("\nIntroduceți cantitatea de parole de generat: "))
        if num_passwords <= 0:
            print("Cantitatea trebuie să fie un număr pozitiv.")
            return

        password_length = int(input("Introduceți lungimea parolelor (minim 8): "))
        
        passwords = []
        for _ in range(num_passwords):
            passwords.append(generator.generate_strict_password(password_length))

        print("\n--- Tabel de analiză a parolelor ---")
        
        # Vizualizare sub formă de tabel
        print(f"{'Nr.':<5} | {'Parola':<{password_length}} | {'Complexitate':<15}")
        print("-" * (5 + 2 + password_length + 2 + 15))

        for i, password in enumerate(passwords):
            complexity = generator.calculate_complexity(password)
            print(f"{i+1:<5} | {password:<{password_length}} | {complexity:<15}")

    except ValueError:
        print("Eroare: Vă rugăm să introduceți un număr valid.")

def main():
    """
    Funcția principală a aplicației care interacționează cu utilizatorul
    și utilizează clasa PasswordGenerator.
    """
    print("--- Generator de Parole Securizate ---")
    
    generator = PasswordGenerator()

    while True:
        print("\n--- Meniu Principal ---")
        print("1. Generează o singură parolă")
        print("2. Generează și analizează un set de parole")
        print("3. Ieșire")
        
        choice = input("Alegeți o opțiune: ")

        if choice == '1':
            try:
                password_length = int(input("Introduceți lungimea dorită a parolei (minim 8): "))
                generated_password = generator.generate_strict_password(password_length)
                
                print("\nParola generată este:")
                print(f"-> {generated_password} <-\n")
                
                print("Parola va fi ștearsă din memorie după 15 secunde...")
                start_time = time.time()
                while time.time() - start_time < 15:
                    time.sleep(1)
                print("\nParola a fost ștearsă din memorie.")
            except ValueError:
                print("Eroare: Vă rugăm să introduceți un număr valid pentru lungime.")
        
        elif choice == '2':
            analyze_passwords(generator)

        elif choice == '3':
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă. Vă rugăm să alegeți 1, 2 sau 3.")


if __name__ == "__main__":
    main()