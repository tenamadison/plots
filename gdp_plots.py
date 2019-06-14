
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

    # display the plot
    plt.show()

    #set some plot
    ax.set_xlabel("YEar")
    ax.set_yLabel ("GDP per capita")
    #set the x locations and lebels
    ax.set_xticks(range(len(data.index)))
    ax.set_xtickslabels(data.index, rotation =45)

    #display the plot
    split_name=filename.split(".")
    save_name=split_name[0] + "png"    
    pit.savefig (save_name)
