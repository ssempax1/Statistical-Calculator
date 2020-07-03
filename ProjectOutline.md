 # Project Outline 
## Abstract 
	 The project  goal is to create a statistical calculator with the ability to to do statistical functions and ability to read data.
### Phase 1
We set up our project skeleton  with Dockerfile, integrated with travis for testing and with a central repository through Git 
We Create a basic Calculator that does  basic operations. 
Developmental Task
Create a Calculator folder that has a calculator module  to the Calculator folder and add basic operations as static methods each with its own file.
Addition subtraction multiplication division square and square root 
Ability to Pass Data to our Calculator module, create a CSV reader folder  with the ability to read  data files.
Create a Test folder  unit testing each of the basic operations 
If all the Tests are passed then we move on to the next Phase 
 
### Phase 2
Add functionality to the calculator that will enable it do statistical functions 
Like mean,Median,Mode We will extend the basic operations that allow us to do statistical operations to the statistical module.
 
 ##### Developmental Task
Create a statistical folder that has a statistics  module  to the folder and add basic statistics functions as static methods each with its own file.
Mean Standard Deviation and  Variance. 
Create a Test folder  unit testing each of the basic  statistics operations 
If all the Tests are passed then we move on to the next Phase 

### Phase 3 
Add functionality ability to carry out more complex statistics operations 
Sample Mean  Sample SD, Sample Variance
Population Mean, Population SD, Population Variance

##### Developmental Task
Add the functionality to   statistics  module  with 
Population  Mean Standard Deviation and  Variance, and Population Variance, 
Create a Test folder  unit testing each of the basic  statistics complex  operations 
If all the Tests are passed then we move on to the next Phase 


##### Definitions of Statistical terms

 **Population Mean**
The term population mean, which is the average score of the population on a given variable, is represented by:
μ = ( Σ Xi ) / N<br>
The symbol ‘μ’ represents the population mean.  The symbol ‘Σ Xi’ represents the sum of all scores present in the population (say, in this case) X1 X2 X3 and so on.  The symbol ‘N’ represents the total number of individuals or cases in the population. <br>
**Population Standard Deviation**
The population standard deviation is a measure of the spread (variability) of the scores on a given variable and is represented by:
σ = sqrt[ Σ ( Xi – μ )2 / N ]
The symbol ‘σ’ represents the population standard deviation.  The term ‘sqrt’ used in this statistical formula denotes square root.  The term ‘Σ ( Xi – μ )2’ used in the statistical formula represents the sum of the squared deviations of the scores from their population mean.<br>
  **Population Variance**
The population variance is the square of the population standard deviation and is represented by:
σ2 = Σ ( Xi – μ )2 / N <br>
The symbol ‘σ2’ represents the population variance.<br>
**Sample Mean**
The sample mean is the average score of a sample on a given variable and is represented by:
x_bar = ( Σ xi ) / n
The term “x_bar” represents the sample mean.  The symbol ‘Σ xi’ used in this formula represents the represents the sum of all scores present in the sample (say, in this case) x1 x2 x3 and so on.  The symbol ‘n,’ represents the total number of individuals or observations in the sample.
Sample Standard Deviation
The statistic called sample standard deviation, is a measure of the spread (variability) of the scores in the sample on a given variable and is represented by:
s = sqrt [ Σ ( xi – x_bar )2 / ( n – 1 ) ]
The term ‘Σ ( xi – x_bar )2’ represents the sum of the squared deviations of the scores from the sample mean.
Sample Variance
The sample variance is the square of the sample standard deviation and is represented by:
s2 = Σ ( xi – x_bar )2 / ( n – 1 )
The symbol ‘s2’ represents the sample variance.
Pooled Sample Standard Deviation
The pooled sample standard deviation is a weighted estimate of spread (variability) across multiple samples.  It is represented by:
sp = sqrt [ (n1 – 1) * s12 + (n2 – 1) * s22 ] / (n1 + n2 – 2) ]
The term ‘sp’ represents the pooled sample standard deviation.  The term ‘n1’ represents the size of the first sample, and the term ‘n2’ represents the size of the second sample that is being pooled with the first sample.  The term ‘s12’ represents the variance of the first sample, and ‘s22’ represents the variance of the second sample.
