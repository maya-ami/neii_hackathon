"""
Концепт автоматического обнаружения изменений в нормативных и законодательных актах.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import sys


def read_files(local_doc, updated_doc):
    with open(local_doc) as f:
        text_local = f.read()
    with open(updated_doc) as f:
        text_updated = f.read()
    return text_local, text_updated

# векторизуем документы и рассчитаем косинус угла между ними.
def cosine_sim(text1, text2):
    vect = TfidfVectorizer()
    tfidf = vect.fit_transform([text1, text2])
    return(((tfidf * tfidf.T).A)[0,1])

def main():
    text_local, text_updated = read_files(sys.argv[1], sys.argv[2])
    similarity =  cosine_sim(text_local, text_updated)
    if similarity < 1:
        print("В документе произошли изменения! Необходима актуализация локальной базы данных!")
    else:
        print("Локальная версия документа является актуальной.")

if __name__ == "__main__":
    main()
