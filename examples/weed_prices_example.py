# guarantee you won't have issues pulling this data
# this does not change permanant settings, only allows us to access
# raw data from Github without worrying about the settings
import ssl

from pandas import DataFrame, read_csv
from pandas.api.types import is_object_dtype
from rich import print
from tabulate import tabulate

from pdcompare.compare import Compare

ssl._create_default_https_context = ssl._create_unverified_context

# we will compare week prices, from Jan 1 2004 to Jan 1 2005

# thanks to Vicki for pointing me in the direct of these small datasets
# https://veekaybee.github.io/2018/07/23/small-datasets/
# and thanks to Frank BI for supplying the free datasets
# https://github.com/frankbi/price-of-weed


def clean_dollar_values(df) -> DataFrame:
    """
    Cleans dollar values in the DataFrame by removing the dollar sign
    and converting the column to float type.
    """
    for col_name in df.columns:
        if is_object_dtype(df[col_name]):
            df[col_name] = df[col_name].str.replace("$", "").astype(float)
    return df


def main() -> None:
    # Load the data from CSV files
    jan_01 = read_csv(
        "https://raw.githubusercontent.com/frankbi/price-of-weed/master/data/weedprices01012014.csv",
        index_col=0,
    )
    jan_02 = read_csv(
        "https://raw.githubusercontent.com/frankbi/price-of-weed/master/data/weedprices01022014.csv",
        index_col=0,
    )

    # Clean dollar values in the DataFrames
    jan_01 = clean_dollar_values(jan_01)
    jan_02 = clean_dollar_values(jan_02)
    # for the example we want to validate that if a column changes from 0 to a value
    # we don't break. We will get a `inf%` change with how numpy does math
    jan_01.loc[:, ("LowQN")] = 0.0

    # Initialize the Compare class with the two DataFrames
    c = Compare(jan_01, jan_02)

    # Set change comparison to True to include differences in values
    # this will attempt to compare numerical values and will throw a warning
    # if it cannot do so (e.g., comparing strings)
    # this also creates a change and pct_change column in the output
    c.set_change_comparison(True)

    # Perform the comparison
    c.compare()

    # Output the results
    summary = c.output()["SUMMARY"]
    summary.index = ["SUMMARY"]
    print(tabulate(summary, headers="keys", tablefmt="psql"))
    print(c.change_detail.head(10))


if __name__ == "__main__":
    main()
