# machine-learing-peoject2

question 3:

 The goal of this problem is to implement multivariate linear regression from scratch using gradient descent and validate it.
a. Implement a function for learning the parameters of a linear model for a given tranining data with user-specified learning rate η and number of epochs T. Note: you cannot use existing libraries such as sklearn; you need to write it out yourself.

b. Validate your algorithm on the glucose dataset discussed in Lecture 2. Confirm that the model obtained by running your code gets similar R2 values as the one produced by sklearn.


question 4:

In this lab, we will illustrate the use of multiple linear re- gression for calibrating robot control. The robot data for the lab is taken from TU Dortmund’s Multiple Link Robot Arms Project. We will focus on predicting the current drawn into one of the joints as a function of the robot motion. Such models are essential in predicting the overall robot power consumption.

a. Read in the data in the attached exp_train.csv file; check that the data that you read actually corresponds to the data in the .csv file. In Python, you can use the commands given at the end of this document.

b. Create the training data:
• Labels y: A vector of all the samples in the ‘I2’ column
• Data X : A matrix of the data with the columns: [‘q2’,‘dq2’,‘eps21’,
‘eps22’, ‘eps31’, ‘eps32’,‘ddq2’]

c. Fit a linear model between X and y (using sklearn, or any other library of your choice). Report the MSE of your model.

d. Using the linear model that you trained above, report the MSE on the test data contained in the attached exp_test.csv file.
