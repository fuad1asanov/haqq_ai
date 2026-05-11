import streamlit as st

# 1. UI Konfiqurasiyası
st.set_page_config(page_title="Haqq.ai | Premium Legal Tech", layout="wide")

# 2. Daha stabil dizayn (Python 3.14 dostu)
custom_css = """
<style>
    .stApp { background-color: #0A192F; color: #E6F1FF; }
    .main-title { color: #64FFDA; text-align: center; font-size: 40px; font-weight: bold; }
    .stButton>button {
        background: #64FFDA;
        color: #0A192F;
        border-radius: 10px;
        font-weight: bold;
        width: 100%;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_value=True)

# 3. Sidebar - Sürücü Profili
with st.sidebar:
    st.title("👤 Sürücü Paneli")
    name = st.text_input("Ad, Soyad:", placeholder="Əli Əliyev")
    car_plate = st.text_input("Avtomobil nömrəsi:", placeholder="99-XX-000")
    st.info("Profil məlumatlarınız rəsmi ərizəyə avtomatik əlavə olunacaq.")

# 4. Əsas Ekran
st.markdown("<h1 class='main-title'>⚖️ Haqq.ai</h1>", unsafe_allow_value=True)
st.write("---")

col1, col2 = st.columns(2)

with col1:
    category = st.selectbox("Xətanın növü:", [
        "Sürət həddinin aşılması (Maddə 327.1 - 328)",
        "Qırmızı işıq / Stop nişanı (Maddə 327.2)",
        "Dayanma, durma və parklanma (Maddə 346)",
        "Yol nişanlarının tələblərinə əməl etməmə",
        "Sərxoş vəziyyətdə idarəetmə (Maddə 333)"
    ])

with col2:
    date = st.date_input("Hadisə tarixi:")

details = st.text_area("Hadisənin təfərrüatları (arqumentləriniz):", 
                      placeholder="Məs: Nişan görünmürdü, radar xətası var idi...")

if st.button("🚀 PREMİUM ƏRİZƏNİ HAZIRLA"):
    if details and name and car_plate:
        st.success("✅ Rəsmi ərizəniz Azərbaycan qanunvericiliyinə uyğun hazırlandı!")
        
        # Sənədin önbaxışı
        doc_preview = f"""
        AZƏRBAYCAN RESPUBLİKASI DAXİLİ İŞLƏR NAZİRLİYİ
        DÖVLƏT YOL POLİSİ İDARƏSİNƏ
        
        Müraciət edən: {name}
        Avtomobil nömrəsi: {car_plate}
        
        ŞİKAYƏT ƏRİZƏSİ
        
        Mən bildirirəm ki, {date} tarixində tərəfimə tətbiq olunmuş {category} üzrə cərimə ilə razı deyiləm. 
        Səbəb: {details}
        
        Qanunvericiliyin tələblərinə əsasən işə yenidən baxılmasını xahiş edirəm.
        """
        st.text_area("Ərizə Mətni:", doc_preview, height=250)
        st.download_button("📥 Sənədi Yüklə", doc_preview, file_name="haqq_ai_erize.txt")
    else:
        st.error("Xahiş olunur bütün xanaları (ad, nömrə, detal) doldurun.")
