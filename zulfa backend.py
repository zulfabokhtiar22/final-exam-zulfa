# مشروع متجر ميكب - Backend

products = [
    ["أحمر شفاه", 10],
    ["كريم أساس", 20],
    ["ماسكارا", 30],
    ["آيشادو", 40],
    ["فرش مكياج", 50]
]

print("✨✨ مرحبًا بك في متجر الميكب ✨✨\n")

print ("قائمة المنتجات:")
for i in range(len(products)):
    print(f"{i+1} - {products[i][0]}")

choice = int(input("\nاختاري رقم المنتج: "))

if choice < 1 or choice > len(products):
    print("❌ رقم غير صحيح!")
else:
    price = products[choice-1][1]
    tax = price * 0.15
    total = price + tax
    print(f"\n💄 المنتج: {products[choice-1][0]}")
    print(f"💰 السعر قبل الضريبة: {price} ريال")
    print(f"🧾 الضريبة: {tax} ريال")
    print(f"✅ السعر النهائي: {total} ريال")