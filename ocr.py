import cv2
import pytesseract
import os

os.environ['TESSDATA_PREFIX'] = '/content/ocr/tessdata'

def extract_tables_and_ocr(png_file):
  # Türkçe dil modelini kullanarak tesseract OCR'ı yapılandırın
  custom_config = r'--oem 3 --psm 6 -l tur'
  pytesseract.pytesseract.tesseract_cmd = 'tesseract'
       
  # Dosyayı OpenCV ile okuyun
  img = cv2.imread(png_file)
       
  # Görüntüyü gri tonlamaya dönüştürün
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       
  # Gürültüyü azaltmak için görüntüyü bulanıklaştırın
  #blur = cv2.GaussianBlur(gray, (5, 5), 0)
       
  # Görüntüyü OCR ile metne dönüştürün
  text = pytesseract.image_to_string(gray, config=custom_config)
       
  return text

# PNG dosyasının adı
png_file = "sonuc.png"

# Tabloları çıkartmak ve OCR ile metin çıkartmak için fonksiyonu çağırın
ocr_text = extract_tables_and_ocr(png_file)

# Elde edilen metni yazdırın
print(ocr_text)