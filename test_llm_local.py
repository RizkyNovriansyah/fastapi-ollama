import requests
import json

# prompt = """Berikan tiga rekomendasi tempat makan ramen enak di Jakarta. 
# expected output:
# [
#   {
#     "name": "",
#     "address": "",
#     "description": ""
#   },
#   {
#     "name": "",
#     "address": "",
#     "description": ""
#   },
#   {
#     "name": "",
#     "address": "",
#     "description": ""
#   }
# ]
# """
context = """Kamu adalah asisten AI yang memberikan informasi dan rekomendasi untuk berbagai topik. 
Kamu bisa menjawab pertanyaan apa pun dari pengguna seperti ChatGPT.

ATURAN PENTING:
1. Jika pengguna meminta informasi tentang tempat, lokasi, restoran, alamat, venue, gedung, atau hal lain yang membutuhkan data lokasi di dunia nyata, maka:
   - Jangan memberikan alamat pasti atau data lokasi yang kamu tidak yakin 100% akurat.
   - Sebagai gantinya, kamu wajib mencantumkan placeholder dalam format berikut:

       {{TEMPAT:KEYWORD}}

   - KEYWORD adalah frasa yang paling optimal dan relevan untuk digunakan sebagai query ke Google Maps API. 
     Buat KEYWORD sejelas mungkin untuk mendukung pencarian akurat (misalnya mencantumkan nama tempat + kota).

2. Jika pengguna tidak meminta informasi tentang tempat, jawablah seperti biasa tanpa placeholder.

3. Untuk permintaan rekomendasi tempat (contoh: "rekomendasi ramen enak di Jakarta"):
   - Berikan nama tempat secara normal.
   - Untuk alamat, jangan memberikan alamat statis.
   - Sebagai gantinya berikan placeholder:
     
       {{TEMPAT:[nama tempat + lokasi]}}

4. Jangan mengarang alamat. Jika tidak yakin, selalu gunakan placeholder.

Contoh Output:
Totto Ramen — Rekomendasi ramen populer di Jakarta.
Lokasi: {{TEMPAT:Totto Ramen Jakarta}}

Jawaban harus tetap informatif meskipun menggunakan placeholder.
"""
prompt = """Berikan tiga rekomendasi tempat makan ramen enak di Jakarta beserta alamatnya."""

payload = {
    "model": "llama3",
    "prompt": context + "\n" + prompt
}

response = requests.post("http://localhost:11434/api/generate", json=payload, stream=True)


full_output = ""

# Ollama mengirim stream token per token → kita gabungkan
for chunk in response.iter_lines():
    if chunk:
        data = json.loads(chunk.decode("utf-8"))
        if "response" in data:
            full_output += data["response"]

print("\n=== OUTPUT LLM LOKAL ===\n")
print(full_output)
