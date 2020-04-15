# machine-learning-project4

question2:

In this problem, we will implement the Perceptron algorithm discussed in class on synthetic training data.

   a. Suppose that the data dimension d equals 2. Generate two clusters of data points with 100 points each, by sampling from Gaussian distributions centered at (0.5, 0.5) and (−0.5, −0.5). Choose the variance of the Gaussian to be small enough so that the data points are sufficiently well separated. Plot the data points on the 2D plane to confirm that this is the case.

   b. Implement the Perceptron algorithm as discussed in class. Choose the initial weights to be zero and the maximum number of epochs as T = 100, and the learning rate α = 1. How quickly does your implementation converge?

   c. Now, repeat the above experiment with a second synthetic dataset; this time, increase the variance (radius) of the two Gaussians such that the generated data points from different classes now overlap. What happens to the behavior of the algorithm? Does it converge? Show the classification regions obtained at the end of T epochs.
   
   
question4:

The Fashion MNIST dataset is a database of (low-resolution) clothing images that is similar to MNIST but somewhat more challenging. You can load it in Colab using the Python code below.

   a. Load the dataset and display 10 representative images from each class.

   b. Implement the following classification methods: k-NN, logistic regression, and support vector machines (with linear and rbf kernels). You can use sklearn.

   c. Report best possible test-error performances by tuning hyperparameters in each of your methods.

   d. Report train- and test-running time of each of your methods in the form of a table, and comment on the relative tradeoffs across the different methods.

