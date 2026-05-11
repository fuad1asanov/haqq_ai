import streamlit as st

# 1. UI Ayarları - Standart Streamlit elementləri ilə
st.set_page_config(page_title="Haqq.ai | Premium Legal Tech", layout="centered")

# 2. Başlıq və Təqdimat
st.title("⚖️ Haqq.ai")
st.subheader("Azərbaycanın ilk AI Hüquq Platforması")
st.info("Haqqınızı rəsmi və qanuni yolla bərpa edin. Bütün müraciətlər anonimdir.")

st.divider()

# 3. Sol Panel - Sürücü Profili
with st.sidebar:
    st.header("👤 Sürücü Paneli")
    name = st.text_input("Ad, Soyad:", placeholder="Məs: Əli Əliyev")
    car_plate = st.text_input("Avtomobil nömrəsi:", placeholder="Məs: 99-XX-000")
    st.write("---")
    st.caption("Profil məlumatlarınız rəsmi sənəd üçün istifadə olunur.")

# 4. Əsas Form
st.write("### 📝 Şikayət Formu")

col1, col2 = st.columns(2)

with col1:
    # Bütün maddələrin siyahısını bura yığırıq
    category = st.selectbox("Xəta maddəsini seçin:", [
        "Maddə 327.1 (Sürət həddinin aşılması - 10-20 km/saat)",
        "Maddə 328.1 (Sürət həddinin aşılması - 20-40 km/saat)",
        "Maddə 327.2 (Qırmızı işıqdan keçmə)",
        "Maddə 346.1 (Dayanma-durma qaydalarının pozulması)",
        "Maddə 329.1 (Təhlükəsizlik kəmərindən istifadə etməmə)",
        "Maddə 342.1.1 (Şüşələrə qanunsuz plyonka çəkilməsi)",
        "Digər (Mətn hissəsində qeyd edin)"
    ])

with col2:
    event_date = st.date_input("Hadisə tarixi:")

# Sürücü məlumatlarını əlavə etmək üçün təkmil bölmə
st.write("### 🔍 Hadisənin Təfərrüatları")
details = st.text_area("Niyə cərimə ilə razı deyilsiniz?", 
                      placeholder="Məsələn: Yol nişanı ağacların arxasında qaldığı üçün görünmürdü və ya radar xətası var idi...",
                      height=150)

# 5. Sənəd Yaradılması
if st.button("🚀 RƏSMİ ƏRİZƏNİ HAZIRLA"):
    if name and car_plate and details:
        with st.spinner('AI Azərbaycan qanunvericilik bazasını analiz edir...'):
            # Rəsmi Mətn Strukturunun yaradılması
            erize_metni = f"""
            AZƏRBAYCAN RESPUBLİKASI DAXİLİ İŞLƏR NAZİRLİYİ
            BAKI ŞƏHƏR BAŞ POLİS İDARƏSİ DÖVLƏT YOL POLİSİ İDARƏSİNƏ
            
            Müraciət edən: {name}
            Avtomobil nömrəsi: {car_plate}
            Tarix: {event_date}
            
            ŞİKAYƏT ƏRİZƏSİ
            
            Bildirirəm ki, tərəfimə tətbiq olunmuş {category} üzrə inzibati xəta protokolu ilə razı deyiləm. 
            
            Əsaslandırma: {details}
            
            Azərbaycan Respublikasının İnzibati Xətalar Məcəlləsinin və "Vətəndaşların müraciətləri haqqında"
