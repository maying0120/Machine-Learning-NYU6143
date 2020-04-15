# machine-learning-project3

question 2:

   The Boston Housing Dataset has been collected by the US Census Service and consists of 14 urban quality-of-life variables, with the last one being the median house price for a given town. Code for loading the dataset is provided at the end of this assignment. Implement a linear regression model with ridge regression that predicts median house prices from the other variables. Use 10-fold cross validation on 80-20 train-test splits and report the final R2 values that you discovered. (You may want to preprocess your data to the range [0, 1] in order to get meaningful results.)


question 4:

In this problem, we will implement logistic regression trained with GD/SGD and validate on synthetic training data.

   a. Suppose that the data dimension d equals 2. Generate two clusters of data points with 100 points each (so that the total data size is n = 200), by sampling from Gaussian distributions centered at (0.5, 0.5) and (−0.5, −0.5). Call the data points xi, and label them as yi = ±1 depending on which cluster they originated from. Choose the variance of the Gaussian to be small enough so that the data points are sufficiently well separated. Plot the data points on the 2D plane to confirm that this is the case.
   
   b. (Derive your own GD routines; do not use sklearn functions here.) Train a logistic regression model that tries to minimize:
   

![Alt text](https://github.com/maying0120/machine-learning-project3/blob/master/eq1.png)



using Gradient Descent (GD). Plot the decay of the training loss function as a function of
number of iterations.


   c. Train the same logistic regression model, but this time using Stochastic Gradient Descent (SGD). Demonstrate that SGD exhibits a slower rate of convergence than GD, but is faster per-iteration, and does not suffer in terms of final quality. You may have to play around a bit with the step-size parameters as well as mini-batch sizes to get reasonable answers.


   d. Overlay the original plot of data points on the 2D data plane with the two (final) models that you obtained above in parts b and c to visualize correctness of your implementation.
