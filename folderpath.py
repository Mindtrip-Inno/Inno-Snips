import os

abs_path = os.path.dirname(__file__) # Python Kodunun Bulunduğu Dosya Yolunu
                                    # String Olarak abs_path değişkenine atar
## denemek istersen yorum kısmını sil 
# print(abs_path) // Örnek -> /home/mind/Downloads/pm5/bird opencv/

gerekli_dosya = "dosya/dosy.jpeg"
örnek_dosya = "dosya.xml"

dosya_yolu = os.path.join(abs_path, gerekli_dosya) # ikin stringi birleştirir
örnekdosyayolu =os.path.join(abs_path, örnek_dosya)
# print(dosya_yolu) // -> /home/mind/Downloads/pm5/bird opencv/dosya/dosy.jpeg
# print(örnekdosyayolu) /home/mind/Downloads/pm5/bird opencv/dosya.xml
