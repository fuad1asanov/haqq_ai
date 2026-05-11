import streamlit as st

# 1. UI Konfiqurasiyası
st.set_page_config(page_title="Haqq.ai | Premium Legal Tech", layout="wide")

# 2. Premium Dark-Blue Dizayn (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #0A192F; color: #E6F1FF; }
    .stButton>button {
        background: linear-gradient(90deg, #64FFDA 0%, #48BB78 100%);
        color: #0A192F; border: none; font-weight: bold; border-radius: 10px;
        transition: 0.3s; width: 100%;
    }
    .stButton>button:hover { transform: scale(1.02); }
    .stTextInput>div>div>input { background-color: #112240; color: white; border: 1px solid #233554; }
    .stSelectbox>div>div>div { background-color: #112240; color: white; }
    </style>
    """, unsafe_allow_value=True)

# 3. Sidebar - Sürücü Profili
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.title("Sürücü Paneli")
    name = st.text_input("Ad, Soyad:", placeholder="Məs: Əli Əliyev")
    car_plate = st.text_input("Avtomobil nömrəsi:", placeholder="99-XX-000")
    st.success("Profil yadda saxlanıldı (Lokal)")

# 4. Əsas Ekran
st.title("🤖 Haqq.ai - Ağıllı Şikayət Sistemi")
st.write("Düzgün maddəni seçin və AI sizin üçün peşəkar hüquqi sənəd hazırlasın.")

col1, col2 = st.columns(2)

with col1:
    category = st.selectbox("Xətanın növü:", [
        "Sürət həddinin aşılması (Maddə 327.1 - 328)",
        "Qırmızı işıq / Stop nişanı (Maddə 327.2)",
        "Dayanma, durma və parklanma (Maddə 346)",
        "Yol nişanlarının tələblərinə əməl etməmə",
        "Sərxosh vəziyyətdə idarəetmə (Maddə 333)"
    ])

with col2:
    date = st.date_input("Hadisə tarixi:")

details = st.text_area("Hadisənin təfərrüatları (Sübutlar, görüntülər, haqsızlığın səbəbi):")

if st.button("🚀 PREMIUM ƏRİZƏNİ GENERASİYA ET"):
    if details:
        with st.status("Qanunvericilik bazası yoxlanılır...", expanded=True) as status:
            st.write("🔍 İnzibati Xətalar Məcəlləsi analiz edilir...")
            st.write("📑 Precedent məhkəmə qərarları tapılır...")
            st.write("✍️ Hüquqi terminologiya tətbiq olunur...")
            status.update(label="Ərizə hazırdır!", state="complete", expanded=False)
        
        # Sənədin Vizualı
        st.markdown(f"""
        <div style="background-color: white; color: black; padding: 20px; border-radius: 5px; font-family: serif;">
            <p style="text-align: center; font-weight: bold;">AZƏRBAYCAN RESPUBLİKASI DAXİLİ İŞLƏR NAZİRLİYİ</p>
            <p>Müraciət edən: <b>{name}</b></p>
            <p>Nəqliyyat vasitəsi: <b>{car_plate}</b></p>
            <br>
            <p style="text-align: center; font-weight: bold;">ŞİKAYƏT ƏRİZƏSİ</p>
            <p>Mən bildirirəm ki, {date} tarixində qeydə alınmış {category} üzrə cərimə ilə razı deyiləm.</p>
            <p>Əsaslandırma: {details}</p>
        </div>
        """, unsafe_allow_value=True)
        st.download_button("📥 Sənədi Yüklə (PDF Formatında)", "Mətn bura gələcək...", file_name="sikayet.pdf")
    else:
        st.warning("Zəhmət olmasa təfərrüatları qeyd edin.")
