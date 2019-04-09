import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import bitUtil

df = bitUtil.getMovies()

# unstack
# index==> columns

# r1 = df.pivot_table(values='rating', index='gender', aggfunc='mean')
# print(r1)
#
# r2  = r1.unstack()
# print(r2)

#
# r1 = df.pivot_table(values='rating', index=['gender','age'], aggfunc='mean')
#
# print(r1)
# r2 = r1.unstack()
# print(r2)
#
# # unstack
# # index가 2개 일때
# # 2번째 index를 column으로 표현하여 가독성을 높일 수 있습니다.
#
#
# r3 = r2.stack()         #column --->index
# print(r3)
#


# help(pd.DataFrame.pivot_table)
#연습) 나이대별, 성별별로 별점의 평균과 합을 출력해 봅니다.
#혹시 오류가 나면 그것을 해결해 봅니다.
# r = df.pivot_table(values='rating', index='age', columns='gender',
#                     aggfunc=['mean', 'sum'])
# print(r)

# r = df.pivot_table(values='rating', index='age', columns='gender',
#                     aggfunc=[np.mean, np.sum])
# print(r)
# 때에따라 numpy 함수를 요구할 수도 있어요
# numpy 함수를 명시해 주세요.


#나이대별, 성별 별점의 평균을 구해봅시다.

r1 = df.pivot_table(values='rating', index='age', columns='gender', aggfunc='mean')


#나이대별, 성별 별점의 합을 구해봅시다.
r2 = df.pivot_table(values='rating', index='age', columns='gender', aggfunc='sum')


# print(r1)
# print(r2)

#두개의 데이터 프레임을 서로 이어붙이기 위해서는 concat을 이용합니다.


# r3 = pd.merge(r1,r2)
# print(r3)


r3 =  pd.concat([r1,r2])
print(r3)


r4 = pd.concat([r1,r2],axis=1)
print(r4)












