import streamlit as st

# 1. UI Ayarları
st.set_page_config(page_title="Haqq.ai | Premium Legal Tech", layout="centered")

# 2. Başlıq
st.title("⚖️ Haqq.ai")
st.subheader("Azərbaycanın ilk AI Hüquq Platforması")
st.info("Haqqınızı rəsmi və qanuni yolla bərpa edin.")

st.divider()

# 3. Sidebar
with st.sidebar:
    st.header("👤 Sürücü Paneli")
    name = st.text_input("Ad, Soyad:", placeholder="Məs: Əli Əliyev")
    car_plate = st.text_input("Avtomobil nömrəsi:", placeholder="Məs: 99-XX-000")

# 4. Form
st.write("### 📝 Şikayət Formu")
category = st.selectbox("Xəta maddəsini seçin:", [
    "Maddə 327.1 (Sürət həddinin aşılması - 10-20 km/saat)",
    "Maddə 328.1 (Sürət həddinin aşılması - 20-40 km/saat)",
    "Maddə 327.2 (Qırmızı işıqdan keçmə)",
    "Maddə 346.1 (Dayanma-durma qaydaları)",
    "Digər"
])

details = st.text_area("Niyə cərimə ilə razı deyilsiniz?", height=150)

# 5. Sənəd Yaradılması (Boşluq xətası düzəldildi)
if st.button("🚀 RƏSMİ ƏRİZƏNİ HAZIRLA"):
    if name and car_plate and details:
        # Mətn blokunu birbaşa sol kənardan başlayaraq qeyd edirik
        erize_metni = f"""AZƏRBAYCAN RESPUBLİKASI DAXİLİ İŞLƏR NAZİRLİYİ
DÖVLƏT YOL POLİSİ İDARƏSİNƏ

Müraciət edən: {name}
Avtomobil nömrəsi: {car_plate}

ŞİKAYƏT ƏRİZƏSİ

Bildirirəm ki, tərəfimə tətbiq olunmuş {category} üzrə protokolu qəbul etmirəm.

Əsaslandırma: {details}

Qanunvericiliyin tələblərinə uyğun olaraq, işə yenidən baxılmasını xahiş edirəm.

Hörmətlə, {name}"""

        st.success("✅ Ərizəniz hazırdır!")
        st.text_area("Önbaxış:", erize_metni, height=250)
        st.download_button("📥 Yüklə", erize_metni, file_name="haqq_ai_erize.txt")
    else:
        st.error("⚠️ Xanaları doldurun!")
