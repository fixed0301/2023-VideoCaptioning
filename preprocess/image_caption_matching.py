# 캡션 중 최대 기리 찾고 토큰화된 1개 문장을 리스트에 넣어 im_cap 이라는 딕셔너리에 추가
# 각 이미지의 id가 딕셔너리의 키값

im_cap = dict()

max_len = 0

for i in range(7010): #trainval. test는 2990

