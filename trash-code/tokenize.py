import json
import re
from nltk import word_tokenize
from nltk.corpus import stopwords # 불용어 제거
from nltk.tokenize import RegexpTokenizer # 정규 표현식을 통한 토큰화
from gensim.models.word2vec import Text8Corpus
from gensim.models.word2vec import Word2Vec
from tqdm import tqdm

def get_captions(json_path, id):
    captions = []
    with open(json_path, 'r') as f:
        data = json.load(f)
        #print(data.keys()) #dict_keys(['info', 'videos', 'sentences'])
        #print(data['videos'][0].keys()) #dict_keys(['category', 'url', 'video_id', 'start time', 'end time', 'split', 'id'])

        for i in range(140200):
             if data['sentences'][i]['video_id'] == f'video{id}':
                 captions.append(data['sentences'][i]['caption'])
    return captions

def regex(sentence): # 정규표현식을 통한 단어 토큰화
    tokenizer = RegexpTokenizer("[\w']+") #시작 심볼과 끝 심볼 추가
    tokens = tokenizer.tokenize(sentence)
    return tokens


def stopword(tokens):
    english_stops = set(stopwords.words('english'))
    tokenized = [word for word in tokens if word not in english_stops]
    return tokenized

def word2vec_model_making(txt_filename): # 이거 안씀 #말뭉치 생성 #정제된 단어들로 txt를 만들자
    sentences = []

    with open (txt_filename, 'r', encoding='utf-8') as f:
        for line in f:
            sentence = line.strip()
            cleaned_sentence = re.sub(r'[^\.\?\!\w\d\s]', '', sentence).lower()
            sentences.append(cleaned_sentence)
    preprocessed_sent = [stopword(regex(c_sentence)) for c_sentence in cleaned_sentence]

    print(preprocessed_sent)
    model = Word2Vec(preprocessed_sent, vector_size=100, min_count=5, window=5)
    print('saving..')
    #model.save('word2vec_model_2')
    #print('done!')
    #print(model)
    #f.close()
    return

def all_sentences_txt(json_path):
    with open(json_path, 'r') as f:
        with open('../preprocess/test.txt', 'w', encoding='utf-8') as c:
            data = json.load(f)
            for i in range(20*2990):
                tmp = data['sentences'][i]['caption']
                c.write(f"{tmp}'")#단어 끝마다 구분자두기

json_path = '../videodata/test_videodatainfo_2017.json'
all_sentences_txt(json_path)
