# analyzer.py - Jednoduchý detektor Brute Force útoků

# # Slovník, kam budeme ukládat počet selhání pro každou IP adresu
# failed_attempts = {}

# # Otevřeme soubor s logy
# with open("server_logs.txt", "r") as file:
#     for line in file:
#         # Pokud řádek obsahuje "Failed", analyzujeme ho
#         if "Status: Failed" in line:
#             # Získáme IP adresu z řádku (velmi zjednodušeně)
#             parts = line.split(",")
#             ip_address = parts[1].replace(" IP: ", "").strip()
            
#             # Přičteme pokus k dané IP adrese
#             failed_attempts[ip_address] = failed_attempts.get(ip_address, 0) + 1

# # Výpis podezřelých adres (více než 3 neúspěšné pokusy)
# print("--- BEZPEČNOSTNÍ REPORT ---")
# for ip, count in failed_attempts.items():
#     if count > 3:
#         print(f"ALARM: Podezření na Brute Force! IP: {ip} má {count} neúspěšných pokusů.")


############


import matplotlib.pyplot as plt

# Slovník pro ukládání neúspěšných pokusů
failed_attempts = {}

# Otevření souboru (teď už se správným názvem)
try:
    with open("server_logs.txt", "r") as file:
        for line in file:
            if "Status: Failed" in line:
                # Rozdělení řádku a získání IP adresy
                parts = line.split(",")
                ip_address = parts[1].replace(" IP: ", "").strip()
                failed_attempts[ip_address] = failed_attempts.get(ip_address, 0) + 1
except FileNotFoundError:
    print("Chyba: Soubor 'server_logs.txt' nebyl nalezen v aktuální složce!")
    exit()

# Vizualizace výsledků
if failed_attempts:
    ips = list(failed_attempts.keys())
    counts = list(failed_attempts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(ips, counts, color='crimson')
    plt.axhline(y=3, color='black', linestyle='--', label='Práh alarmu')
    
    plt.title('Report: Detekce pokusů o Brute Force')
    plt.xlabel('IP Adresa')
    plt.ylabel('Počet selhání')
    plt.legend()

    # Uložení a zobrazení
    plt.savefig("attack_report.png")
    print("Analýza hotova. Report uložen jako 'attack_report.png'.")
    plt.show()
else:
    print("Žádné útoky k zobrazení.")
