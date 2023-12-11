import pickle
import numpy as np

from gensim.models.word2vec import Word2Vec

#load model
word_model = Word2Vec.load('word2vec_model_4')

word_dict = {}
#print(word_model.wv.key_to_index)
for word in word_model.wv.key_to_index.keys():
     word_dict[word] = word_model.wv[word]
#print('len_word_dict', len(word_dict))
print(word_dict.keys()) # 왜 딕셔너리에 숫자랑 언더바가 포함된건지 모르겠다 불용어 제거
     # word_dict: 알파벳!!이 임베딩되어있다 {'e': array([ 6.69453740e-02, -8.34109411e-02,..


# #save word_dict
# with open('word2vec_dict_1.pickle', 'wb') as f:
#     pickle.dump(word_dict, f)
# print('saved')
#
# # 200차원 임베딩 딕셔너리
# embeddings_index = {}
#
# word = 'man'
# for i in range(len(word)): # man이라는 단어가 있으면 3번, 즉 m, a, n 에 대한 임베딩 값을 찾겠지
#     embeddings = word_dict[word[i]]
#     coefs = np.asarray(embeddings, dtype='float32')
#     embeddings_index[word[i]] = coefs
#
# # embeddings_index는 딕셔너리 형태로 'm', 'a', 'n' 에 대한 200차원 임베딩 벡터를 담음
# #print(embeddings_index['m'].shape)


