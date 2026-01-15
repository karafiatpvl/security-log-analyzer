"""
Security Log Analyzer - Brute Force Detection
Autor: karafiatpvl
Popis: Skript analyzuje neúspěšné pokusy o přihlášení a generuje vizuální report.
"""
import matplotlib.pyplot as plt

# Konfigurace
LOG_FILE = "server_logs.txt"
REPORT_FILE = "attack_report.png"
THRESHOLD = 3  # Práh alarmu pro Brute Force

failed_attempts = {}

# Otevření a analýza souboru
try:
    with open(LOG_FILE, "r") as file:
        for line in file:
            if "Status: Failed" in line:
                # Získání IP adresy z formátu: "... , IP: 192.168.1.5, ..."
                parts = line.split(",")
                ip_address = parts[1].replace(" IP: ", "").strip()
                failed_attempts[ip_address] = failed_attempts.get(ip_address, 0) + 1
except FileNotFoundError:
    print(f"Chyba: Soubor '{LOG_FILE}' nebyl nalezen!")
    exit()

# Vizualizace výsledků
if failed_attempts:
    ips = list(failed_attempts.keys())
    counts = list(failed_attempts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(ips, counts, color='crimson')
    plt.axhline(y=THRESHOLD, color='black', linestyle='--', label='Práh alarmu')
    
    plt.title('Report: Detekce pokusů o Brute Force')
    plt.xlabel('IP Adresa')
    plt.ylabel('Počet selhání')
    plt.legend()

    # Uložení a potvrzení
    plt.savefig(REPORT_FILE)
    print(f"Analýza hotova. Report uložen jako '{REPORT_FILE}'.")
    # plt.show() # Zakomentováno pro běh v prostředí bez GUI
else:
    print("Žádné útoky k zobrazení.")
