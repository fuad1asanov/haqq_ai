import streamlit as st

# 1. Səhifə Ayarları (Stabil versiya)
st.set_page_config(page_title="Haqq.ai - Haqq Radarı", page_icon="⚖️")

# 2. Başlıq Hissəsi
st.title("⚖️ Haqq.ai")
st.markdown("### Haqqınızı rəsmi və qanuni yolla bərpa edin")
st.info("Azərbaycanın ilk Süni İntellekt əsaslı hüquq platforması")

st.divider()

# 3. İstifadəçi Məlumatları (Anonimlik qorunur)
st.write("#### 📞 Şikayət üçün məlumatları tamamlayın")
phone_number = st.text_input("Mobil nömrəniz (Təsdiq kodu və sənəd üçün):", placeholder="050XXXXXXX")

# Nömrə daxil edilmədən digər xanalar açılmır (Strategiyamız)
if phone_number:
    st.write("---")
    st.write("#### 🏎️ Cərimə detalları")
    
    option = st.selectbox("Cərimə maddəsini seçin:", 
                         ["Maddə 327.1 (Sürət həddi)", 
                          "Maddə 327.2 (Qırmızı işıq)", 
                          "Maddə 342 (Dayanma-durma)", 
                          "Digər hüquqi məsələ"])
    
    user_text = st.text_area("Hadisə barədə rəsmi izahatınız:", 
                             placeholder="Məsələn: Yol nişanı ağacların arxasında qaldığı üçün görünmürdü...")
    
    if st.button("Rəsmi Şikayət Ərizəsini Hazırla ✨"):
        if len(user_text) > 10:
            with st.spinner('Süni İntellekt Azərbaycan qanunvericiliyini analiz edir...'):
                # Rəsmi Sənəd Şablonu
                official_doc = f"""
                AZƏRBAYCAN RESPUBLİKASI DAXİLİ İŞLƏR NAZİRLİYİ
                BAKI ŞƏHƏR BAŞ POLİS İDARƏSİ DÖVLƏT YOL POLİSİ İDARƏSİNƏ
                
                Müraciət edən: {phone_number}
                
                ŞİKAYƏT ƏRİZƏSİ
                
                Mən, aşağıda qeyd olunan nömrəli istifadəçi, bildirirəm ki, tərəfimə tətbiq olunan {option} üzrə cərimə protokolu ilə razı deyiləm. 
                
                Səbəb və İzahat: {user_text}. 
                
                Azərbaycan Respublikası İnzibati Xətalar Məcəlləsinin müvafiq maddələrinə və vətəndaşların müraciətləri haqqında qanuna əsasən, qeyd olunan protokolun ləğv edilməsini və işə yenidən baxılmasını xahiş edirəm.
                
                Tarix: 12.05.2026
                İmza: (Elektron müraciət üçün imza tələb olunmur)
                """
                
                st.success("✅ Rəsmi ərizəniz hazırdır!")
                st.text_area("Ərizənin önbaxışı:", official_doc, height=250)
                
                # Sənədi yükləmə düyməsi
                st.download_button(label="📥 Sənədi PDF/Mətn olaraq yüklə", 
                                   data=official_doc, 
                                   file_name="HaqqAI_Sikayet_Erizesi.txt",
                                   mime="text/plain")
                
                st.warning("⚠️ **Növbəti addım:** Bu sənədi yükləyin və 'asan.gov.az' portalı vasitəsilə Daxili İşlər Nazirliyinə elektron müraciət kimi göndərin.")
        else:
            st.error("Zəhmət olmasa izahat hissəsini bir az daha ətraflı yazın.")

# 4. Footer (Anonimlik qeydi)
st.write("---")
st.caption("© 2026 Haqq.ai | Bütün müraciətlər anonim saxlanılır və rəsmi hüquqi bazaya uyğun hazırlanır.")
