from pdcompare.compare import Compare
from pandas import read_csv

# guarantee you won't have issues pulling this data
# this does not change permanant settings, only allows us to access
# raw data from Github without worrying about the settings
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# we will compare week prices, from Jan 1 2004 to Jan 1 2005

# thanks to Vicki for pointing me in the direct of these small datasets
# https://veekaybee.github.io/2018/07/23/small-datasets/
# and thanks to Frank BI for supplying the free datasets
# https://github.com/frankbi/price-of-weed

jan_04 = read_csv('https://raw.githubusercontent.com/frankbi/price-of-weed/master/data/weedprices01012014.csv',index_col=0)
jan_05 = read_csv('https://raw.githubusercontent.com/frankbi/price-of-weed/master/data/weedprices01012015.csv',index_col=0)

# init the Compare class with our 2 DFs
# then call the compare function
# it will output a small summary 

c = Compare(jan_04,jan_05)
c.compare()

# use the output to get the differences in a dict form

c.output()

# use results to just get the df of comparisons

c.results