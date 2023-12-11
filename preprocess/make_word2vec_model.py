from preprocess_test.tokenize_final import preprocess_tokenize
from gensim.models.word2vec import Word2Vec

def word2vec_model_making(trainval_txtpath, test_txtpath): #말뭉치 생성 #정제된 단어들로 txt를 만들자
    trainval = preprocess_tokenize(trainval_txtpath)
    test = preprocess_tokenize(test_txtpath)
    preprocessed_sent = trainval + test
    print(preprocessed_sent)
    model = Word2Vec(preprocessed_sent, vector_size=200, min_count=1, window=5)
    print('saving..')
    model.save('word2vec_model_4')
    print('done!')
    print(model)
    return


#word2vec_model_making('trainval.txt', 'test.txt')
