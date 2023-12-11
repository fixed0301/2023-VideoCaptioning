import re
import nltk
from nltk.corpus import stopwords
from collections import Counter

def preprocess_tokenize(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        content = f.read() #문장 단위로 끊기
        cleaned_content = re.sub(r'[^\.\?\!\w\d\s]', ' ', content).lower() #정상적으로 소문자로 문장들이 다 변환됨(str)
        word_tokens = nltk.word_tokenize(cleaned_content) #리스트 안에 단어 단위로 분리
        tokens_pos = nltk.pos_tag(word_tokens) #품사 태깅. 리스트 안에 글자랑 품사()묶임
        #print(tokens_pos)

        NN_words = [] #명사만 추출 (근데 지금은 아님)

        for word, pos in tokens_pos:
            #if 'NN' in pos:
            NN_words.append(word) #리스트 안 명사들만 모임.. 근데 굳이 명사만 토큰화할 이유가 있던가?

        wlem = nltk.WordNetLemmatizer() #원형을 찾아 같은 의미의 단어 토큰을 하나의 값으로 인지
        lemmatized_words = []
        for word in NN_words:
            new_word = wlem.lemmatize(word)
            lemmatized_words.append(new_word)
        #print(lemmatized_words)

        #stopwords_list = stopwords.words('english')  # nltk에서 제공하는 불용어사전 이용. 근데 개많은데??이게 다 필요없어??
        customized_stopwords = ['a', 'an', 'the']

        #unique_NN_words = list(set(lemmatized_words)) # set으로 중복 단어 제거 # 아니 그러니까 개수가 다 1개지
        #print('unique_NN_words:', unique_NN_words) # 여기서 이상한 단어들이 갑자기 생기네

        for word in lemmatized_words:
            if word in customized_stopwords:
                lemmatized_words.remove(word)
        print(lemmatized_words)
        f.close()
    #return unique_NN_words

final_words = preprocess_tokenize('../preprocess/test.txt')


# c = Counter(final_words) #음! 단어들이 다 하나씩만 저장되었군! ..왜?
# print(c)


