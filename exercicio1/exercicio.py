### Introduction

import pandas as pd

df = pd.read_csv("movies.csv")


df.columns

df.head()

### Activities

##### 1. Create a new column `revenue`

revenue = df['gross'] - df['budget']
df.insert(7,column="revenue",value=revenue)


##### 2. Create a new column `percentage_profit`

# Try your code here
percentage_profit = (df['revenue'] / df['gross']) * 100
df.insert(len(df.columns)-1, "percentage_profit", percentage_profit)

##### 3. Create a new column `high_budget_movie`

highbudgetmovie = (df['budget']>100000000)
df.insert(len(df.columns)-1, "high_budget_movie", highbudgetmovie)

##### 4. Create a new column `successful_movie`

# Try your code here
succesful_movie = (df['percentage_profit']>50)
df.insert(len(df.columns)-1, "successful_movie", succesful_movie)

##### 5. High-Rated Movies

high_rated_movie = (df['score']>8)
df.insert(len(df.columns)-1, "high_rated_movie", high_rated_movie)

##### 6. Create a new column `is_new_release`

is_new_release = (df['year']>2020)
df.insert(len(df.columns)-1, "is_new_release", is_new_release)

##### 7. Create a new column `is_long_movie`

is_long_movie = (df['runtime']>150)
df.insert (len(df.columns)-1, "is_long_movie", is_long_movie)

##### 8. Drop unsuccessful movie.

df.drop(df[df['successful_movie'] == False].index, inplace=True)

##### 9. Drop high budget movie.

low_budget_df = df[df['budget'] <= 100000000]
low_budget_df

##### 10. Removing Low-Voted Movies

high_voted_df = df[df['votes'] >=1000].copy()
high_voted_df


##### 11. Drop the column `budget`

df.drop(columns='budget', inplace=True)

##### 12. Drop the `director` and `writer` columns from the dataframe.

new_df = df.drop(columns=['director', 'writer'], inplace=False)

##### 13. Drop Out Low-Rated and Low-Voted Movies

df.drop(df[(df['score'] <5) & (df['votes'] <1000)].index, inplace = True)

##### 14. Top High-Rated Movies

top_rated_movies = df.nlargest(5, 'score').sort_values(by='score', ascending=False).copy()

##### 15. Removing Specific Rows

df.drop(index=[2,10])

##### 16. Sci-Fi Blockbusters

sci_fi_blockbusters = df[(df['genre'] == 'Sci-Fi') & (df['gross'] > 150000000)]

##### 17. Age of Movies

age = 2024 - df['year']
df.insert(len(df.columns)-1, "age", age)

##### 18. Movies Released in Summer

summer_movies = df[df['released'].str.contains('June|July|August')]
