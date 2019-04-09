import numpy as np
import pandas as pd
import bitUtil
import matplotlib.pyplot as plt


df = bitUtil.getMovies()

#연습) 영화별로 별점을 받은 건수를 출력
title_count = df.pivot_table(values='rating',index='title',aggfunc='count')
# print(title_count)


#연습) 평가건수가 500개 이상인 영화제목을 출력
# print(title_count['rating']>=100)
title_500 = title_count[ title_count['rating']>=500  ]
# print(title_100)


#연습) 평가건수가 500개 이상인 영화제목을 내림차순 정렬
title_500_sort = title_500.sort_values(by="rating", ascending=False)
print(title_500_sort)








