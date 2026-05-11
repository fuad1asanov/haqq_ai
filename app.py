import streamlit as st

# Saytın Başlığı və Dizaynı
st.set_page_config(page_title="Haqq.ai - Haqq Radarı", page_icon="⚖️", layout="centered")

st.markdown("<h1 style='text-align: center; color: #1A237E;'>⚖️ Haqq.ai</h1>", unsafe_allow_value=True)
st.markdown("<h3 style='text-align: center;'>Haqqınızı rəsmi və qanuni yolla bərpa edin</h3>", unsafe_allow_value=True)

st.divider()

# İSTİFADƏÇİ MƏLUMATLARININ YIĞILMASI
st.write("### 📞 Şikayət üçün məlumatları tamamlayın")
phone_number = st.text_input("Mobil nömrəniz (Təsdiq kodu üçün):", placeholder="050XXXXXXX")

if phone_number:
    st.write("---")
    st.write("### 🏎️ Cərimə detalları")
    
    option = st.selectbox("Cərimə maddəsini seçin:", 
                         ["Maddə 327.1 (Sürət həddi)", "Maddə 327.2 (Qırmızı işıq)", "Maddə 342 (Dayanma-durma)", "Digər"])
    
    user_text = st.text_area("Hadisə barədə rəsmi izahatınız (Məsələn: Yol nişanı ağacların arxasında qaldığı üçün görünmürdü):")
    
    if st.button("Rəsmi Şikayət Ərizəsini Hazırla ✨"):
        if len(user_text) > 10:
            st.success("✅ Rəsmi ərizəniz Azərbaycan İnzibati Xətalar Məcəlləsinə uyğun hazırlandı!")
            
            # SƏNƏDİN MƏTNİ (Rəsmi Ton)
            official_doc = f"""
            AZƏRBAYCAN RESPUBLİKASI DAXİLİ İŞLƏR NAZİRLİYİ
            BAKI ŞƏHƏR BAŞ POLİS İDARƏSİ DÖVLƏT YOL POLİSİ İDARƏSİNƏ
            
            Vətəndaş: (Nömrə: {phone_number}) tərəfindən
            
            ŞİKAYƏT ƏRİZƏSİ
            
            Mən, {phone_number} nömrəli istifadəçi, bildirirəm ki, tərəfimə tətbiq olunan {option} üzrə cərimə protokolu haqsızdır. 
            Səbəb: {user_text}. 
            Azərbaycan Respublikası İX Məcəlləsinin müvafiq maddələrinə əsasən bu protokolun ləğv edilməsini xahiş edirəm.
            """
            
            st.text_area("Ərizənin mətni:", official_doc, height=200)
            
            st.download_button("📥 PDF olaraq yüklə", official_doc, file_name="HaqqAI_Sikayet.txt")
            
            # ELEKTRON TƏLİMAT
            st.warning("ℹ️ **Növbəti addım:** Bu sənədi yükləyin və 'asan.gov.az' portalı vasitəsilə elektron müraciət bölməsinə əlavə edərək göndərin.")
        else:
            st.error("Zəhmət olmasa daha ətraflı məlumat yazın (minimum 10 hərf).")
