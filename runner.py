# Punch card ML recognition with Edge Impulse runner on LattePanda IOTA
# Roni Bandini 12/2025 MIT License

import subprocess
import time
import os

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('clear') 

clear_screen()

print(" _________________________________________________________________________")
print("/ Punched card ML recognition Edge Impulse & LattePanda IOTA              |")
print("|          ________________________________________________               |")
print("|   12  / [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]             |")
print("|   11 |  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]             |")
print("|    0 |  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]             |")
print("|    1 |  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]             |")
print("|    2 |  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]             |")
print("|    3 |  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]             |")
print("|    4 |  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]             |")
print("|    5 |  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]             |")
print("|    6 |  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]             |")
print("|    7 |  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]             |")
print("|    8 |  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]             |")
print("|    9 |  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]             |")
print("|      |__________________________________________________________________|")
print("|       1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ... 80         |")
print("|_________________________________________________________________________|")

RUNNER_PATH = "edge-impulse-linux-runner"
OUTPUT_FILE = "output.txt"

output_file_handle = open(OUTPUT_FILE, "w")
subprocess.Popen([RUNNER_PATH], stdout=output_file_handle, stderr=subprocess.STDOUT)

print("\nRoni Bandini 12/2025\n")

scores = {}
is_collecting = False

with open(OUTPUT_FILE, "r") as f:
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.01)
            continue

        raw = line.strip()

        # Inicio de bloque de inferencia
        if "classifyRes" in raw:
            scores = {}
            is_collecting = True
            continue

        if is_collecting:
            # Fin de bloque
            if "}" in raw:
                is_collecting = False
                if scores:
                    best_letter = max(scores, key=scores.get)
                    best_score = scores[best_letter]
                    print(f"best: {best_letter} {best_score}")
                continue

            # Extracción de pares clave: valor
            if ":" in raw:
                try:
                    parts = raw.split(":")
                    label = parts[0].strip().replace("'", "").replace('"', '')
                    value = float(parts[1].strip().replace(",", ""))
                    scores[label] = value
                except (ValueError, IndexError):
                    continue