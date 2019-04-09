import numpy as np
import pandas as pd
import bitUtil
import matplotlib.pyplot as plt

df = bitUtil.getMovies()
# print(df.head())

#연습)
#성별별로 별점의 평균을 알고 싶어요
#select gender, avg(rating) from df group by gender
#           ===> pivot_table
# help(pd.DataFrame.pivot_table)
# pivot_table(self, values=None, index=None, columns=None, aggfunc='mean', fill_value=None,

# gender_mean = df.pivot_table(values='rating', index='gender')
# gender_mean2 = df.pivot_table(values='rating', index='gender', aggfunc="mean")
# gender_sum = df.pivot_table(values='rating', index='gender', aggfunc="sum")
# gender_max = df.pivot_table(values='rating', index='gender', aggfunc="max")
# gender_min = df.pivot_table(values='rating', index='gender', aggfunc="min")
# print(gender_mean)
# print(gender_mean2)
# print(gender_sum)
# print(gender_max)
# print(gender_min)



# 연습) 나이별로 별점의 평균을 출력해 봅니다.

# select age, avg(rating) from df group by age
# age_mean = df.pivot_table(values='rating', index='age', aggfunc='mean')
# print(age_mean)


#연습)    나이대별, 성별별로 rating의 평균을  다음과 같이 보여주세요.
'''
       rating
age     F           M     
1    3.549520   3.549520
18   3.507573   3.549520
25   3.545235   3.549520
35   3.618162   3.549520
45   3.638062   3.638062   
50   3.714512   3.638062
56   3.766632   3.638062
'''




# r = df.pivot_table(values='rating', index='age', columns='gender',
#                                  aggfunc='mean')
# print(age_mean_gender)


# gender_mean_age = df.pivot_table(values='rating', index='gender', columns='age',
#                                  aggfunc='mean')
# print(gender_mean_age)

# print(r)
# print(type(r))
#
# r.index = ["under 18","18-24","25-34","35-44","45-49","50-55","56+"]
#
# print(r)
# r.plot(kind="bar")
# plt.show()



# r = df.pivot_table(values='rating', index='gender', aggfunc='mean')
# print(r)

# 나이대별, 성별별로 별점의 평균을 알고 싶어요!
# r = df.pivot_table(values='rating', index='gender', aggfunc='mean', columns='age')
# print(r)

# r = df.pivot_table(values='rating', index='age', aggfunc='mean', columns='gender')
# print(r)


# r = df.pivot_table(values='rating', index=['age','gender'], aggfunc='mean')
# print(r)
#
# r2 = df.pivot_table(values='rating', index=['gender','age'], aggfunc='mean')
# print(r2)


#연습) 직업별, 성별, 나이대별 평균평점을 알려주세요.
#단 결측치는 0으로 채워주세요


# r = df.pivot_table(values='rating', index=['gender','age'], columns='job', fill_value=0)
# print(r)
#
# r = df.pivot_table(values='rating', index=['job','age'], columns='gender', fill_value=0)
# print(r)
#
# r = df.pivot_table(values='rating', index=['age','job'], columns='gender', fill_value=0)
# print(r)

#pivot_table 시에
#어떤것을 index로 하고 어떤것을 columns으로 하는지에 대한 제약은 없지만
#항목의 수가 많은 것을 column으로 두는것이 읽기가 쉬운것 같아요.


# r = df.pivot_table(values='rating', index='gender', columns='age', aggfunc='mean')
# print(r)

r2 = df.pivot_table(values='rating', index='age', columns='gender', aggfunc='mean')
print(r2)


#unstack()          ==> column ---> 첫번째 index
r3 = r2.unstack()
print(r3)

















