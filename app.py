import streamlit as st
from datetime import datetime

# 1. Səhifə Ayarları
st.set_page_config(page_title="Haqq.ai | Hüquqi Müdafiə", layout="centered")

# 2. Başlıq və Dizayn
st.title("⚖️ Haqq.ai")
st.markdown("#### Süni İntellektlə Haqqınızı Bərpa Edin")
st.info("Cərimə skrinşotunu yükləyin və ya detalları daxil edin.")

st.divider()

# 3. Addım-addım Məntiq
tab1, tab2, tab3 = st.tabs(["📸 Analiz", "📝 Detallar", "📄 Nəticə"])

with tab1:
    st.write("### Cərimə Şəklini Yükləyin")
    uploaded_file = st.file_uploader("SMS Radar və ya DYP skrinşotu", type=['png', 'jpg', 'jpeg'])
    if uploaded_file:
        st.success("✅ Şəkil qəbul olundu. AI analizə başladı...")
        st.session_state['ocr_done'] = True

with tab2:
    st.write("### Hüquqi Detallar")
    
    name = st.text_input("Ad, Soyad, Ata adı:", placeholder="Məs: Həsənov Fuad Elmir")
    protokol = st.text_input("Protokol nömrəsi:", placeholder="Məs: IXP7935495")
    
    reason_type = st.selectbox("Müdafiə növü:", [
        "Manevr edirdim (Parklanma/Sağa dönmə)",
        "Texniki nasazlıq / Məcburi dayanma",
        "Yol nişanları görünmürdü",
        "Zolağa məcburi daxil olmuşdum",
        "Polis tərəfindən yanlış qiymətləndirmə"
    ])
    
    user_story = st.text_area("Hadisə necə baş verdi?", placeholder="Məs: Polisin mənə yaxınlaşdığı an mən hələ hərəkətdə idim...")

    if st.button("Sənədi Formallaşdır"):
        if name and protokol and user_story:
            st.session_state['ready'] = True
            st.session_state['doc_name'] = name
            st.session_state['doc_protokol'] = protokol
            st.session_state['doc_reason'] = reason_type
            st.session_state['doc_story'] = user_story
            st.success("✅ Sənəd hazırlandı! 'Nəticə' bölməsinə keçin.")
        else:
            st.error("⚠️ Zəhmət olmasa bütün xanaları doldurun.")

with tab3:
    if 'ready' in st.session_state:
        st.write("### Hazır Şikayət Ərizəsi")
        
        # Ərizə mətni - Boşluq xətası olmaması üçün birbaşa formatda
        final_text = f"""AZƏRBAYCAN RESPUBLİKASI DAXİLİ İŞLƏR NAZİRLİYİ
DÖVLƏT YOL POLİSİ İDARƏSİNƏ

Müraciət edən: {st.session_state['doc_name']}
Protokol №: {st.session_state['doc_protokol']}

ŞİKAYƏT ƏRİZƏSİ

Bildirirəm ki, tərəfimə tətbiq olunmuş inzibati xəta protokolu ilə razı deyiləm. 
Hadisə zamanı müdafiə mövqeyim: {st.session_state['doc_reason']}.

Hadisənin təsviri: {st.session_state['doc_story']}

Azərbaycan Respublikası İnzibati Xətalar Məcəlləsinin müvafiq maddələrinə əsasən, işə yenidən baxılmasını və protokolun ləğv edilməsini xahiş edirəm.

Tarix: {datetime.now().strftime('%d.%m.%Y')}
İmza: {st.session_state['doc_name']}"""

        st.text_area("Ərizənin önbaxışı:", final_text, height=300)
        
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("📥 Sənədi Yüklə", final_text, file_name="haqq_ai_sikayet.txt")
        with c2:
            st.button("🚀 Birbaşa DYP-yə Göndər (2 AZN)")
    else:
        st.warning("Əvvəlcə 'Detallar' bölməsində məlumatları tamamlayın.")

# 4. Footer
st.divider()
st.caption("© 2026 Haqq.ai | Hüquqi Köməkçiniz")
