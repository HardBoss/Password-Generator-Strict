# 🔒 Generator și Analizor de Parole Securizate

### Descriere

Acest proiect este o aplicație de tip **CLI (Command-Line Interface)** dezvoltată în **Python** pentru a genera și a analiza parole securizate. Aplicația respectă o serie de reguli stricte pentru a asigura o complexitate ridicată a parolelor generate și oferă o funcționalitate de analiză de bază pentru seturi de parole.

Proiectul a fost structurat folosind principii de **Programare Orientată pe Obiecte (OOP)**, cu logica încapsulată într-o clasă `PasswordGenerator`.

### Funcționalități

* **Generare de Parole Securizate**: Creează parole cu o lungime specificată, care conțin o distribuție echilibrată de litere mici, litere mari, cifre și simboluri.
* **Reguli de Securitate**: Parolele generate încep cu o literă mică și nu conțin mai mult de două caractere consecutive din aceeași categorie (ex: `aBc1@2De#4`).
* **Analiză de Bază**: Poate genera un set de parole și le poate evalua complexitatea, clasificându-le ca **"Strong"** sau **"Super Strong"** pe baza repetării caracterelor.
* **Interfață cu Utilizatorul**: O interfață simplă bazată pe consolă, cu un meniu interactiv pentru a alege între diferite funcționalități.
* **Gestionarea Erorilor**: Aplicația include excepții pentru a gestiona input-uri invalide din partea utilizatorului.

### Tehnologii Utilizate

* **Python**: Limbajul de programare de bază.
* **OOP (Programare Orientată pe Obiecte)**: Utilizarea unei clase pentru a organiza și a încapsula logica proiectului.
* **Module Standard**: `random`, `string`, `time`.
* **Data Science Elementară**: O abordare simplă de **Exploratory Data Analysis (EDA)** pentru analiza parolelor generate.

### Cum să Rulezi Proiectul

Pentru a rula aplicația, trebuie să ai instalat Python pe sistemul tău.

1.  Clonează acest repository:
    ```bash
    git clone https://github.com/HardBoss/Password-Generator-Strict.git
    ```

2.  Lansează scriptul direct din terminal:
    ```bash
    python main.py
    ```
