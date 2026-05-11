import streamlit as st

# 1. UI Ayarları
st.set_page_config(page_title="Haqq.ai | Pro Legal", layout="centered")

# 2. Başlıq
st.title("⚖️ Haqq.ai")
st.markdown("### Süni İntellektlə Texpasport Tanıma və Şikayət")
st.info("Texpasportun şəklini yükləyin, məlumatları AI doldursun.")

st.divider()

# 3. OCR Funksiyası (Simulyasiya və İnterfeys)
st.write("### 📸 1. Məlumatları Avtomatik Doldur")
uploaded_file = st.file_uploader("Texpasportun şəklini buraya yükləyin və ya çəkin", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    with st.spinner('AI şəkildəki məlumatları oxuyur...'):
        # Burada gələcəkdə real OCR (EasyOCR/Tesseract) modelini qoşacağıq
        # Hələlik istifadəçiyə prosesi göstərmək üçün demo data doldururuq
        st.success("✅ Məlumatlar uğurla tanındı!")
        demo_name = "Əliyev Məmməd"
        demo_plate = "99-BJ-001"
else:
    demo_name = ""
    demo_plate = ""

st.divider()

# 4. Form və Sürücü Paneli
st.write("### 📝 2. Şikayət Detalları")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Ad, Soyad:", value=demo_name, placeholder="Məs: Əli Əliyev")
with col2:
    car_plate = st.text_input("Avtomobil nömrəsi:", value=demo_plate, placeholder="Məs: 99-XX-000")

# Genişləndirilmiş Maddə Kitabxanası
category = st.selectbox("Xəta maddəsini seçin:", [
    "Maddə 327.1 (Sürət həddinin 10-20 km/saat aşılması) - 10 AZN",
    "Maddə 328.1 (Sürət həddinin 20-40 km/saat aşılması) - 50 AZN",
    "Maddə 327.2 (İşıqforun qırmızı işığında keçid) - 60 AZN + 3 Bal",
    "Maddə 346.1 (Dayanma-durma qaydalarının pozulması) - 20 AZN",
    "Maddə 329.1 (Təhlükəsizlik kəmərindən istifadə etməmə) - 40 AZN",
    "Digər xüsusi hal"
])

details = st.text_area("Haqsızlıq barədə qısa qeydiniz:", placeholder="Məs: Kamera görüntüsündə maşın mənə məxsus deyil...")

# 5. Sənədin Hazırlanması
if st.button("🚀 PREMİUM ŞİKAYƏT GENERASİYA ET"):
    if name and car_plate and details:
        erize_metni = f"""AZƏRBAYCAN RESPUBLİKASI DAXİLİ İŞLƏR NAZİRLİYİ
DÖVLƏT YOL POLİSİ İDARƏSİNƏ

Müraciət edən: {name}
Nəqliyyat vasitəsi: {car_plate}

ŞİKAYƏT ƏRİZƏSİ

Bildirirəm ki, tərəfimə tətbiq olunmuş {category} üzrə inzibati xəta protokolunu haqsız hesab edirəm. 

Səbəb: {details}

İnzibati Xətalar Məcəlləsinin müvafiq maddələrinə əsasən, işə obyektiv baxılmasını və cərimənin ləğvini xahiş edirəm.

Hörmətlə, {name}"""

        st.success("✅ Peşəkar ərizəniz hazırdır!")
        st.text_area("Sənədin Önbaxışı:", erize_metni, height=250)
        st.download_button("📥 Rəsmi Sənədi Yüklə (.txt)", erize_metni, file_name=f"Haqq_AI_{car_plate}.txt")
    else:
        st.error("⚠️ Zəhmət olmasa texpasportu yükləyin və ya xanaları əllə doldurun.")
