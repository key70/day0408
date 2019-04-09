import numpy as np
import pandas as pd
import bitUtil

df = bitUtil.getMovies()
cnt_500 = bitUtil.get_500_movie()

# print(cnt_500.columns)
# print(cnt_500.index)

#평가한 사람이 500명이상인 영화중에  영화별로 성별별로 별점의 평균을 출력
'''
            F              M
AAAAA       4.5          4.7
BBBBB       4.0          3.7
...
'''

# a = df.pivot_table(values='rating', index='title', columns='gender', aggfunc='mean')
# b = a.loc[cnt_500.index]
# b['diff'] = (b['F'] - b['M']).abs()
# c = b.sort_values(by='diff',ascending=False)
# print(c.head())

# print(b)
# print(len(cnt_500))


#연습) 성별별로 평점 평균의 차이가 가장 많이 나는 영화 5개를 출력해 봅니다.

#연습) 남자가 더 좋아하는 영화 5개
# a = df.pivot_table(values='rating', index='title', columns='gender', aggfunc='mean')
# b = a.loc[cnt_500.index]
#
# b['mdiff'] = b['M'] - b['F']
# c = b.sort_values(by='mdiff', ascending=False)
# print(c.head())


#연습) 여자가 더 좋아하는 영화 5개
# a = df.pivot_table(values='rating', index='title', columns='gender', aggfunc='mean')
# b = a.loc[cnt_500.index]
#
# b['wdiff'] = b['F'] - b['M']
# c = b.sort_values(by='wdiff', ascending=False)
# print(c.head())


#연습) 남여 모두 가장 좋아하는 영화 5개

# print(cnt_500.index)
# r = df.pivot_table(values='rating', index='title').sort_values(by='rating', ascending=False).head()
# print(r)




#연습) 남여 호불호가 갈리지 않는 5개의 영화

# a = df.pivot_table(values='rating', index='title', columns='gender', aggfunc='mean')
# # b = a.loc[cnt_500.index]
# # b['diff'] = (b['F'] - b['M']).abs()
# # c = b.sort_values(by='diff')
# # print(c.head())

# gender                                              F         M      diff
# title
# Jerry Maguire (1996)                         3.758315  3.759424  0.001109
# Trainspotting (1996)                         3.958974  3.960432  0.001457
# Dune (1984)                                  3.354331  3.356495  0.002165
# Fatal Attraction (1987)                      3.668050  3.670232  0.002182
# Indiana Jones and the Temple of Doom (1984)  3.674312  3.676568  0.002256


a = df.pivot_table(values='rating', index='title', columns='gender', aggfunc='mean')
b = a.loc[cnt_500.index]

b['fmadd'] = b['F'] + b['M']
c = b.sort_values(by='fmadd', ascending=False)
print(c.head())














