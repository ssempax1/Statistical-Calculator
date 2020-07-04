Correlation coefficient, measures the strength of the linear association between variables measured on an interval or ratio scale.
Correlation coefficient describe the direction and the magnitude of the relationship between two variables.
Computing a product-moment correlation coefficient (r) is given below.

Product-moment correlation coefficient. The correlation r between two variables is:

r = Σ (xy) / sqrt [ ( Σ x2 ) * ( Σ y2 ) ]

where Σ is the summation symbol, x = xi - x, xi is the x value for observation i, x is the mean x value, y = yi - y, yi is the y value for observation i, and y is the mean y value.

The formula below uses population means and population standard deviations to compute a population correlation coefficient (ρ) from population data.

Population correlation coefficient. The correlation ρ between two variables is:

ρ = [ 1 / N ] * Σ { [ (Xi - μX) / σx ]

[ (Yi - μY) / σy ] }
where N is the number of observations in the population, Σ is the summation symbol, Xi is the X value for observation i, μX is the population mean for variable X, Yi is the Y value for observation i, μY is the population mean for variable Y, σx is the population standard deviation of X, and σy is the population standard deviation of Y.

The formula below uses sample means and sample standard deviations to compute a sample correlation coefficient (r) from sample data.

Sample correlation coefficient. The correlation r between two variables is:

r = [ 1 / (n - 1) ] * Σ { [ (xi - x) / sx ]

[ (yi - y) / sy ] }
where n is the number of observations in the sample, Σ is the summation symbol, xi is the x value for observation i, x is the sample mean of x, yi is the y value for observation i, y is the sample mean of y, sx is the sample standard deviation of x, and sy is the sample standard deviation of y.

The interpretation of the sample correlation coefficient depends on how the sample data are collected. With a large simple random sample, the sample correlation coefficient is an unbiased estimate of the population correlation coefficient.

Each of the latter two formulas can be derived from the first formula. Use the first or second formula when you have data from the entire population. Use the third formula when you only have sample data, but want to estimate the correlation in the population. When in doubt, use the first formula.

Fortunately, you will rarely have to compute a correlation coefficient by hand. Many software packages (e.g., Excel) and most graphing calculators have a correlation function that will do the job for you.