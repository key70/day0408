#연습)
#Data폴더의 users.dat, movies.dat, ratings.dat 파일을
#읽어들여 하나의 DataFrame으로 만들어 봅니다.

#movies.dat
# 1::Toy Story (1995)::Animation|Children's|Comedy
# movieid::title::ganre


#users.dat
# 1::F::1::10::48067
# userid::gender::age::job::zipcode

#ratings
#17::3457::3::978158845
#userid::movieid::rating::timestamp



import numpy as np
import pandas as pd

# scores = pd.read_csv("../Data/scores.csv")
# print(scores)
# print(type(scores))

# movies = pd.read_csv("../ml-1m/movies.dat")
# print(movies)
# read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer', names=None,
# help(pd.read_csv)


movies = pd.read_csv("../ml-1m/movies.dat", sep="::",header=None,
                        names=['movieid','title','ganre'], engine='python')


users = pd.read_csv("../ml-1m/users.dat", sep="::",header=None,
                        names=['userid','gender','age','job', 'zipcode'], engine='python')


ratings = pd.read_csv("../ml-1m/ratings.dat", sep="::",header=None,
                        names=['userid','movieid','rating', 'timestamp'], engine='python')

df = pd.merge( pd.merge(movies, ratings), users)
print(df.head(1))

#    movieid             title                        ganre  ...  age  job  zipcode
# 0        1  Toy Story (1995)  Animation|Children's|Comedy  ...    1   10    48067


# help(pd.merge)


# print(users)
# print(ratings)

















