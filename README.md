# pdcompare

[![PyPI Latest Release](https://img.shields.io/pypi/v/pdcompare.svg)](https://pypi.org/project/pdcompare/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Used to compare two pandas DataFrame objects to see how they changed.

```
pip install pdcompare
```
## Requirements
The DataFrames must have the same index to compare correctly. An error will be thrown if the index data-types do not match, and a warning will be thrown if the index names are different.

## STEPS

Initialize and call the ```compare()``` method:
```py
from pdcompare import Compare

compare_object = Compare(df1,df2)
compare_object.compare()
```

To get a dictionary of the resulting comparison data call:
```py
compare_object.output()
```
## Output Details

Once you call the .output() method, you will receive a dictionary object in return. This dictionary has the following keys and associated values:
  
| KEY       | VALUE     | VALUE Data Type | 
| :------------- | :----------: | :----------: | 
|  SUMMARY | high-level overview of differences   | pd.DataFrame | 
| ADDED   | list of all index values that were added | pd.Series |
| ADDED_cols   | list of all columns that were added | pd.Series |
| REMOVED   | list of all index values that were removed | pd.Series |
| REMOVED_cols  | list of all columns that were added | pd.Series |
| CHANGED   | (see below for details) | pd.DataFrame |

### CHANGED output data
This data has the following columns
| Column Header | Data | 
| :------------- | :---------- |
| ID | Index value by which we tracked the alterations |
| COLUMN | Column that we saw an index change values |
| from | Value of specified column & index in the first table (old) |
| to | Value of specified column & index in the second table (new) |


## Examples
### ScreamingFrog Crawl Comparison (SEO)
This is a great tool to compare crawls from different dates. Simply export the CSV files from ScreamingFrog. Then run this Google Colab notebook to create a Report in Google Sheets. 
<p align="center">
  <a href=https://colab.research.google.com/drive/11QKyGo5xjw7RF9KnZbiP9yYNqvc9Qx6H?usp target="_blank"><b>ScreamingFrog Crawl Compare in Colab</b></a>
</p>
By default the code to connect to Google Sheets and do all the formatting is hidden, but feel free to peep behind the curtain to see how it was done. You can display the first block of code by opening using the drop-down triangle on the far left side of the block. 


### Weed Price Comparison
For a simple, get acquainted quickly example, use this. Thanks to <a href=https://veekaybee.github.io/2018/07/23/small-datasets/ target="_blank">Vicki</a> for pointing me in the direction of these small datasets; and thanks to <a href=https://github.com/frankbi/price-of-weed target="_blank">Frank BI</a> for supplying the free datasets. I used Frank's weed price data from 2004 and compared them to 2005 across the 50 states. The example can be found in this repo's example folder.

## Thanks for using my code
<p align="center">
If you found this library useful, I'd appreciate a coffee. 
<br>
<br>
<a href="https://www.buymeacoffee.com/jaceiverson" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
</p>

