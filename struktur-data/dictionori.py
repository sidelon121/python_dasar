pemain = {
    "nama": "Cristiano Ronaldo",
    "tim": "Manchester United",
    "nomor": 7,
    "posisi": "Penyerang",
    "negara": "Portugal"
}
print(pemain)
print(pemain["nama"])
print(pemain["tim"])
print(pemain["nomor"])
print(pemain["posisi"])
print(pemain["negara"])

del pemain["negara"]
print(pemain)

pemain["alamat"] = "Indonesia"
print(pemain)

for key in pemain:
    print(key, ":", pemain[key])
    
for key, value in pemain.items():
    print(key, ":", value)