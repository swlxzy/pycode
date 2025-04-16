sozluk = {
    "Bilim insanı": "Aziz Sancar",
    "Şair": "Mehmet Akif Ersoy",
    "Astronom": "Ali Kuşçu"
}

meslekler = sozluk.copy()
print("Meslekler sözlüğü:", meslekler)

print(len(sozluk))

sozluk.clear()
print(sozluk)

sozluk["Matematikçi"] = "Cahit Arf"
print(sozluk)

print("sanatçı" in sozluk)

sozluk["Bilim insanı"] = "Canan Dağdever"
print(sozluk)