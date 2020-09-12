from sklearn.text.feature_extraction import TfidfVectorizer

vect = TfidfVectorizer()

# переводим документ из локальной БД в вектор
local_doc = vect.fit_transform("local_document.txt")

# парсим этот же документ с Консультант плюс и векторизуем
updated_doc = vect.transform("parsed_doc.txt")

# рассчитаем 
