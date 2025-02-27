import string
import secrets
import clipboard
import time
from colorama import Fore, Style

def generate_password(length, use_special_characters):
    characters = string.ascii_letters + string.digits
    if use_special_characters:
        characters += string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Tervehditään käyttäjää ja odotetaan hetki
print("Tervehdys! Olen salasanageneraattori, ja voin auttaa sinua luomaan uusia salasanoja.")
time.sleep(2)

# Pyydetään pituus käyttäjältä, ja tässä vaiheessa tarkistetaan, jos käyttäjä yrittää syöttää kirjaimia
# Aiemmin tästä seurasi katastrofi, ja ohjelma kaatui. Taklataan ongelma try:lla
while True:
    try:
        password_length = int(input("Toiveesi salasanan pituudelle? Pienin hyväksytty luku on 8!\n"))
        if password_length < 8:
            # Virheviesti ja muutos punaiseksi:
            print(Fore.RED + "Salasana on liian lyhyt! Vahvassa salasanassa on vähintään 8 merkkiä.")
            print(Style.RESET_ALL)
            continue

        # käyttäjän ei ole pakko käyttää erikoismerkkejä, mutta on suositeltavaa. Joka tapauksessa
        # tarjotaan mahdollisuutta käyttää tai olla käyttämättä.
        while True:
            use_special_characters_response = input("Haluatko käyttää erikoismerkkejä salasanassa? "
                                                    "Tämä on suositeltavaa, ja nostaa tietoturvatasoa! (k/e): ")
            if use_special_characters_response in ('k', 'e'):
                break
            else:
                print(Fore.RED + "Vastaa joko k tai e!")
                print(Style.RESET_ALL)
                continue

        if use_special_characters_response == 'k':
            use_special_characters = True
        elif use_special_characters_response == 'e':
            use_special_characters = False

        # Tässä muodostetaan salasana huomioiden kuitenkin käyttäjän valinta erikoismerkkien suhteen
        password = generate_password(password_length, use_special_characters)
        print("Salasana luotu: {}".format(password))
        # automaattinen kopiointi leikepöydälle
        clipboard.copy(password)

        # Salasana luotu, ja valmis käytettäväksi
        answer = input('Salasana kopioitu leikepöydälle. Paina Ctrl + V liittääksesi sen '
                       'haluamaasi paikkaan. Lopetetaanko ohjelma? (k/e):').lower()

        # tässä vaiheessa kaiken pitäisi olla OK, joten kysytään lopetetaanko ohjelma.
        if answer == 'k':
            print("Näkemiin!")
            break
        elif answer == 'e':
            continue
        else:
            print("Vastaa joko k tai e!")

    # Jos käyttäjä yrittää alussa syöttää kirjaimia kun pyydetään numeroita, niin ilmoitetaan siitä.
    except ValueError:

        # Virheviesti ja muutos punaiseksi:
        print(Fore.RED + "Et syöttänyt numeroa! Anna jokin luku, joka on suurempi tai yhtä suuri kuin 8!")
        print(Style.RESET_ALL)

        answer = input('Aloitetaanko alusta? (k/e):').lower()
        if answer == 'e':
            print("Näkemiin!")
            break
        elif answer == 'k':
            continue
        else:
            print("Vastaa joko k tai e!")