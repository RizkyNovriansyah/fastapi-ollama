import requests
import json
import os,re

from dotenv import load_dotenv
load_dotenv()

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
URL_OLLAMA = os.getenv("URL_OLLAMA")

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

def ask_llm(prompt):
    payload = {
        "model": "llama3",
        "prompt": context + "\n" + prompt
    }

    response = requests.post(f"{URL_OLLAMA}/api/generate", json=payload, stream=True)
    
    full_output = ""
    for chunk in response.iter_lines():
        if chunk:
            data = json.loads(chunk.decode("utf-8"))
            if "response" in data:
                full_output += data["response"]
    return full_output

def search_google_place(query: str) -> str:
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "key": GOOGLE_MAPS_API_KEY
    }

    response = requests.get(url, params=params).json()

    # Jika hasil ditemukan
    # print("\nGoogle Maps API Response:", response)
    if response.get("results"):
        place = response["results"][0]

        # Ambil place_id untuk URL maps resmi
        place_id = place.get("place_id", "")
        if place_id:
            maps_url = f"https://www.google.com/maps/place/?q=place_id:{place_id}"
            return maps_url

    # fallback: pakai query biasa jika gagal
    return f"https://www.google.com/maps/search/?api=1&query={query.replace(' ', '+')}"

def replace_tempat_placeholders(text: str) -> str:
        pattern = r"\{\{TEMPAT:(.*?)\}\}"

        def replacer(match):
            keyword = match.group(1).strip()
            print(f"Searching Google Maps for: {keyword}")
            url = search_google_place(keyword)
            return url  # replace full block dengan URL

        return re.sub(pattern, replacer, text)

def ask_ai(prompt_user):
    print("ASK AI")

    llm_output = ask_llm(prompt_user)
    print(llm_output)

    result = replace_tempat_placeholders(llm_output)
    # print(result)
    return result