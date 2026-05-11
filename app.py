import streamlit as st

# 1. UI Ayarları
st.set_page_config(page_title="Haqq.ai | Screenshot-to-Appeal", layout="centered")

# 2. Başlıq
st.title("⚖️ Haqq.ai")
st.markdown("### Cərimə Skrinşotunu At, Şikayəti Hazırlayaq")
st.info("SMS Radar və ya DYP-dən gələn cərimə bildirişinin şəklini yükləyin.")

st.divider()

# 3. Ağıllı Analiz Bölməsi
st.write("### 📸 1. Şəkli Yükləyin")
upload_type = st.radio("Yükləyəcəyiniz sənəd növü:", ["SMS Radar / Bildiriş Skrinşotu", "Texpasport Şəkli"])
uploaded_img = st.file_uploader("Şəkli buraya yükləyin", type=['jpg', 'jpeg', 'png'])

# Demo Məlumatlar (Analiz simulyasiyası)
if uploaded_img:
    with st.spinner('AI mətni analiz edir və detalları çıxarır...'):
        st.success("✅ Məlumatlar tapıldı!")
        if "SMS" in upload_type:
            # Skrinşotdan gələn təxmini datalar
            auto_name = "Sürücü" 
            auto_plate = "99-UP-007"
            auto_madda = "Maddə 328.1 (Sürət)"
            auto_reason = "Radarda qeydə alınmış sürət həddi"
        else:
            auto_name = "Əliyev Vəli"
            auto_plate = "77-AA-111"
            auto_madda = "Seçilməyib"
            auto_reason = ""
else:
    auto_name, auto_plate, auto_madda, auto_reason = "", "", "", ""

st.divider()

# 4. Dinamik Form
st.write("### 📝 2. Məlumatları Təsdiqləyin")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Ad, Soyad:", value=auto_name)
    category = st.text_input("Cərimə Maddəsi:", value=auto_madda)
with col2:
    plate = st.text_input("Nömrə:", value=auto_plate)
    event_date = st.date_input("Hadisə tarixi:")

details = st.text_area("Etiraz səbəbiniz (Məs: Texniki xəta, nişan yoxluğu):", value=auto_reason)

# 5. Ödəniş və Yükləmə Məntiqi
if st.button("🚀 ŞİKAYƏT SƏNƏDİNİ GÖSTƏ"):
    if name and plate and details:
        st.markdown("---")
        st.subheader("📄 Hazırlanmış Ərizə (Önbaxış)")
        
        preview_text = f"""AZƏRBAYCAN RESPUBLİKASI DYP-nə
Müraciət edən: {name} ({plate})

ŞİKAYƏT ƏRİZƏSİ

Bildirirəm ki, {event_date} tarixində tərəfimə göndərilən {category} üzrə 
cərimə bildirişi ilə razı deyiləm. Səbəb: {details}.

İşə yenidən baxılmasını xahiş edirəm."""
        
        st.code(preview_text, language="text")
        
        # ÖDƏNİŞ TƏKLİFİ
        st.warning("💰 **Sənədi yükləmək üçün cəmi 1 AZN ödəniş tələb olunur.**")
        
        if st.button("💳 İndi Ödə və Yüklə"):
            st.info("Ödəniş sisteminə yönləndirilir... (Bu hissə real bank API-na qoşulacaq)")
    else:
        st.error("Zəhmət olmasa şəkli yükləyin və ya məlumatları tamamlayın.")

st.divider()
st.caption("Haqq.ai - Azərbaycanın ilk mobil hüquq köməkçisi.")
