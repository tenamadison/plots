
import sys #import library that works with CSV files
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

for filename in sys.argv[1:]:
    # load data and transpose so that country names are
    # the columns and their gdp data becomes the rows
    data = pandas.read_csv(filename, index_col = 'country').T

    # create a plot of the transposed data
    ax = data.plot(title=filename)

    #set some plot attributes
    ax.set_xlabel("Year")
    ax.set_ylabel ("GDP per capita")
    #set the x locations and lebels
    ax.set_xticks(range(len(data.index)))
    ax.set_xticklabels(data.index, rotation =45)

    #Save the plot with unique file name
    split_name=filename.split(".")
    save_name=split_name[0] + 'png'    
    plt.savefig (save_name)
