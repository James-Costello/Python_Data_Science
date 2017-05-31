import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj = Series([3,6,9,12])

# Series is like an array but indexed
obj.values
obj.index

ww2_cas = Series([8700000,4300000,3000000,2100000,400000],index=['USSR','Germany','China','Japan','USA'])

ww2_dict = ww2_cas.to_dict()
ww2_series = Series(ww2_dict)
# converting Series to dicts and the reverse


# DATAFRAMES
#

import webbrowser
website='https://en.wikipedia.org/wiki/NFL_win%E2%80%93loss_records'
webbrowser.open(website)
nfl_frame = pd.read_clipboard()
nfl_frame
# Pandas has converted our clipboard into a dataframe
nfl_frame.columns
nfl_frame.Rank

# If its more than one word
nfl_frame['First Season']

# Grabbing specific row information
nfl_frame.ix[3]

# Deleting entire column
del nfl_frame['Stadium']

# Dataframe methods
dframe.sum()

# adding rows instead of colunmns
dframe.sum(axis=1)

dframe.min()

# index for min value in column
dframe.idxmin()

# works for max as well
# accumulation sum
dframe.cumsum

# DESCRIBE METHOD
d.frame.describe()

# Info on correlation and covariance




