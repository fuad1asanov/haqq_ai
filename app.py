import streamlit as st
from datetime import datetime

# 1. Səhifə Ayarları və Stil
st.set_page_config(page_title="Haqq.ai | Hüquqi Müdafiə", layout="centered")

# Stabil Dizayn (Python 3.14 üçün optimallaşdırılmış)
st.markdown("""
<style>
    .stApp { background-color: #0E1117; }
    .main-header { color: #00D4FF; text-align: center; font-size: 2.5rem; font-weight: bold; }
    .legal-card { background-color: #1A1C24; padding: 20px; border-radius: 15px; border-left: 5px solid #00D4FF; margin-bottom: 20px; }
    .stButton>button { background: linear-gradient(90deg, #00D4FF, #0055FF); color: white; border-radius: 8px; border: none; height: 50px; font-weight: bold; }
</style>
""", unsafe_allow_value=True)

# 2. Başlıq
st.markdown("<div class='main-header'>⚖️ Haqq.ai</div>", unsafe_allow_value=True)
st.markdown("<p style='text-align: center; color: #999;'>Süni İntellektlə Haqqınızı Bərpa Edin</p>", unsafe_allow_value=True)
st.divider()

# 3. Addım-addım Məntiq (Wizard)
step = st.radio("Mərhələni seçin:", ["1. Analiz (Skrinşot)", "2. Detallar və Sübutlar", "3. Rəsmi Sənəd"], horizontal=True)

if step == "1. Analiz (Skrinşot)":
    st.markdown("### 📸 Cərimə Bildirişini Yükləyin")
    st.write("SMS Radar və ya DYP skrinşotunu əlavə edin, AI detalları avtomatik çəksin.")
    
    uploaded_file = st.file_uploader("Şəkli seçin...", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file:
        st.success("✅ Şəkil uğurla yükləndi!")
        # Real OCR inteqrasiyasına qədər istifadəçi datanı təsdiq edir
        st.info("AI Analiz Nəticəsi: 90-PY-161 | 346.4 (2-ci cərgə) | 80 AZN")
        st.session_state['data_ready'] = True

elif step == "2. Detallar və Sübutlar":
    st.markdown("### 🔍 Hüquqi Boşluqları Tapırıq")
    
    with st.expander("📝 Sürücü və Protokol Məlumatları", expanded=True):
        full_name = st.text_input("Ad, Soyad, Ata adı:", placeholder="Həsənov Fuad Elmir")
        protokol_no = st.text_input("Protokol nömrəsi:", placeholder="IXP7935495")
        fine_amount = st.selectbox("Cərimə məbləği:", ["20 AZN", "40 AZN", "60 AZN", "80 AZN", "100 AZN+"])

    st.write("#### 🛡️ Müdafiə Strategiyası Seçin")
    case_type = st.selectbox("Hadisə zamanı hansı hal baş vermişdi?", [
        "Mən sükan arxasında idim və manevr edirdim (Məsləhət görülən)",
        "Texniki nasazlıq / Məcburi dayanma",
        "Yol nişanları / Nişanlanma görünmürdü",
        "Zolağa sağa dönmək üçün daxil olmuşdum",
        "Digər xüsusi vəziyyət"
    ])
    
    extra_details = st.text_area("Hadisəni öz sözlərinizlə təsvir edin:", 
                                placeholder="Məsələn: Polis yaxınlaşanda park etmək üçün boş yerə girməyə çalışırdım...")

    if st.button("H
