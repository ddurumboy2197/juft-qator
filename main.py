def soz_qidir(fayl_ismi, soz):
    try:
        with open(fayl_ismi, 'r') as f:
            matn = f.read()
            sozlar = matn.split()
            qatorda_bor = matn.count(soz)
            return qatorda_bor
    except FileNotFoundError:
        return "Fayl topilmadi"
```

Kodni ishlatish uchun quyidagicha:

```python
print(soz_qidir("fayl.txt", "soz"))
```

Bunda "fayl.txt" - fayl nomi, "soz" - qidirilayotgan so'z.
