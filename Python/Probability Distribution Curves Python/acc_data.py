'''hello everyone!!! I am Pratyush and this is a basic matplotlib, panda and seaborn project to show the probability distribution curve of a 1-D data(i.e. we have counts of one variable only).

For this example we will be using the acceleration change in radial direction of stars catalougued in Gaia Space Mission DR2(Data release of information Gaia satellite got during the year 2014 to 2016).

We will be using panda to extract data from csv file and seaborn to show the histogram(probaability) curve aling with kde.

I used seaborn.histplot for this which takes the following parameters:
          
	1.Data: pandas.DataFrame, numpy.ndarray, mapping, or sequence

	2. x, y : vectors or keys in data
		Variables that specify positions on the x and y axes. It can also be done using matplotlib.pyplot also
		
	3.hue : vector or key in data
		Semantic variable that is mapped to determine the color of plot elements.
		
	4. weights : vector or key in data
		If provided, weight the contribution of the corresponding data points towards the count in each bin by these factors.
    
	5.stat : str
		Aggregate statistic to compute in each bin. Five types:

			(A)count: show the number of observations in each bin

			(B)frequency: show the number of observations divided by the bin width

			(C)probability: or proportion: normalize such that bar heights sum to 1

			(D)percent: normalize such that bar heights sum to 100

			(E)density: normalize such that the total area of the histogram equals 1

	6. bins : str, number, vector, or a pair of such values

        	Generic bin parameter that can be the name of a reference rule, the number of bins, or the breaks of the bins. Passed to numpy.histogram_bin_edges().
    
	7. binwidth : number or pair of numbers

		Width of each bin, overrides bins but can be used with binrange.
    
	8. binrange : pair of numbers or a pair of pairs

		Lowest and highest value for bin edges; can be used either with bins or binwidth. Defaults to data extremes. 	
	9. discrete : bool

		If True, default to binwidth=1 and draw the bars so that they are centered on their corresponding data points. This avoids “gaps” that may otherwise appear when using discrete (integer) data.
    
	10. cumulative : bool

		If True, plot the cumulative counts as bins increase.
    
	11. common_bins : bool

		If True, use the same bins when semantic variables produce multiple plots. If using a reference rule to determine the bins, it will be computed with the full dataset.
    
	12. common_norm :bool

		If True and using a normalized statistic, the normalization will apply over the full dataset. Otherwise, normalize each histogram independently.
    
	13. multiple :{“layer”, “dodge”, “stack”, “fill”}

		Approach to resolving multiple elements when semantic mapping creates subsets. Only relevant with univariate data.
    
	14. element :{“bars”, “step”, “poly”}

	Visual representation of the histogram statistic. Only relevant with univariate data.
	
	15. fill :bool

		If True, fill in the space under the histogram. Only relevant with univariate data.
    
	16. shrink :number

		Scale the width of each bar relative to the binwidth by this factor. Only relevant with univariate data.
    
	17. kde :bool

		If True, compute a kernel density estimate to smooth the distribution and show on the plot as (one or more) line(s). Only relevant with univariate data.
    
	18. kde_kws :dict

		Parameters that control the KDE computation, as in kdeplot().
    
	19. line_kws :dict

		Parameters that control the KDE visualization, passed to matplotlib.axes.Axes.plot().
	
	20. thresh :number or None

		Cells with a statistic less than or equal to this value will be transparent. Only relevant with bivariate data.
	
	21. pthresh :number or None

		Like thresh, but a value in [0, 1] such that cells with aggregate counts (or other statistics, when used) up to this proportion of the total will be transparent.
	
	22. pmax :number or None

		A value in [0, 1] that sets that saturation point for the colormap at a value such that cells below is constistute this proportion of the total count (or other statistic, when used).
	
	23. cbar :bool

		If True, add a colorbar to annotate the color mapping in a bivariate plot. Note: Does not currently support plots with a hue variable well.
    
	24. cbar_ax :matplotlib.axes.Axes

		Pre-existing axes for the colorbar.
    
	25. cbar_kws :dict

		Additional parameters passed to matplotlib.figure.Figure.colorbar().
    
	26. palette :string, list, dict, or matplotlib.colors.Colormap

		Method for choosing the colors to use when mapping the hue semantic. String values are passed to color_palette(). List or dict values imply categorical mapping, while a colormap object implies numeric mapping.
    
	27. hue_order :vector of strings

		Specify the order of processing and plotting for categorical levels of the hue semantic.
    
	28. hue_norm :tuple or matplotlib.colors.Normalize

		Either a pair of values that set the normalization range in data units or an object that will map from data units into a [0, 1] interval. Usage implies numeric mapping.
    
	28. color :matplotlib color

		Single color specification for when hue mapping is not used. Otherwise, the plot will try to hook into the matplotlib property cycle.
    
	30. log_scale :bool or number, or pair of bools or numbers

		Set axis scale(s) to log. A single value sets the data axis for univariate distributions and both axes for bivariate distributions. A pair of values sets each axis independently. Numeric values are interpreted as the desired base (default 10). If False, defer to the existing Axes scale.
	
	31. legend :bool

        	If False, suppress the legend for semantic variables.
    
	32. ax :matplotlib.axes.Axes

		Pre-existing axes for the plot. Otherwise, call matplotlib.pyplot.gca() internally.
	33. kw :args

		Other keyword arguments are passed to one of the following matplotlib functions:

            		matplotlib.axes.Axes.bar() (univariate, element=”bars”)

            		matplotlib.axes.Axes.fill_between() (univariate, other element, fill=True)

            		matplotlib.axes.Axes.plot() (univariate, other element, fill=False)

            		matplotlib.axes.Axes.pcolormesh() (bivariate)

'''

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sea

acc_data = pd.read_csv('acc_data.csv')       # extracting data

plt.figure(figsize=(10,6))

plt.title('acceleration curve', fontdict={'fontweight':'bold', 'fontsize': 18})

sea.histplot( x='Acceleration', data=acc_data, kde=True , stat='probability' ) # ploting the distribution with Kde

plt.xlabel('acceleration(cm/sec*year)')
plt.ylabel('Probability Density')

plt.savefig('acc.png', dpi=400)  #saving 

plt.show()
