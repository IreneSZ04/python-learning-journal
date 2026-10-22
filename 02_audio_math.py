# Calculadora técnica de tiempos para audio
bpm = float(input("Introduce el tempo de la obra (BPM): "))

# 1 minuto = 60.000 ms. Calculamos la duración de una negra (quarter note)
ms_por_negra = 60000 / bpm
ms_por_corchea = ms_por_negra / 2
ms_por_semicorchea = ms_por_negra / 4

print("\n--- TABLA DE TIEMPOS DE DELAY / REVERB ---")
print(f"Tempo: {bpm} BPM")
print(f"Negra (1/4): {ms_por_negra:.2f} ms")
print(f"Corchea (1/8): {ms_por_corchea:.2f} ms")
print(f"Semicorchea (1/16): {ms_por_semicorchea:.2f} ms")