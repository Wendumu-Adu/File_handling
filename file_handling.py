# Aufgabe 1
with open("system.log", "w", encoding="utf-8") as file:
    file.write("SYSTEM START \n")


# Aufgabe 2
with open("system.log", "a", encoding="utf-8") as file:
    file.write("[INFO] System läuft normal.\n")
    file.write("[WARNUNG] Speicherplatz fast voll.\n")

# Aufgabe 3
with open("system.log", "r", encoding="utf-8") as file:
    content = file.read()
    print("Inhalt von system.log")
    print(content)

# Aufgabe 4
with open("system.log", "r+", encoding="utf-8") as file:
    # Read existing content first
    print(file.read())

    # Write at the end of the file
    file.write("[SUCCESS] Überprüfung abgeschlossen.\n")


# Aufgabe 5 (Using the byte sequence for "Hello")
with open("data.bin", "wb") as file:
    file.write(b"Hello")

with open("data.bin", "rb") as file:
    binary_data = file.read()
    decoded_text = binary_data.decode('utf-8')
    print(f"Dekodierter Text: {decoded_text}")	

