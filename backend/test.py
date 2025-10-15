from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

# Değerleri oku
username = os.getenv("COPERNICUS_USERNAME")
password = os.getenv("COPERNICUS_PASSWORD")

# Kontrol et
print("🔍 .env Dosyası Test Ediliyor...")
print("-" * 50)

if username:
    print(f"✅ COPERNICUS_USERNAME: {username}")
else:
    print("❌ COPERNICUS_USERNAME bulunamadı!")

if password:
    print(f"✅ COPERNICUS_PASSWORD: {(password)}")
else:
    print("❌ COPERNICUS_PASSWORD bulunamadı!")

print("-" * 50)

# Diğer ayarları da test edebilirsiniz
cache_expire = os.getenv("CACHE_EXPIRE", "3600")
print(f"📦 CACHE_EXPIRE: {cache_expire}")