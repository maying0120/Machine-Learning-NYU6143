#  Machine Learning Homeworks for NYU-6143 
## There are 5 branches for 5 different prjects.





### machine-learning-project1

q3:
When we think of a Gaussian distribution (a bell-curve) in 1, 2, or 3 dimensions, the picture that comes to mind is a “blob” with a lot of mass near the origin and exponential decay away from the origin. However, the picture is very different in higher dimensions (and illustrates the counter-intuitive nature of high-dimensional data analysis). In short, we will show that Gaussian distributions are like soap bubbles: most of the mass is concentrated near a shell of a given radius, and is empty everywhere else.


a. Fix d = 3 and generate 10,000 random samples from the standard multi-variate Gaussian distribution defined in Rd.

b. Compute and plot the histogram of Euclidean norms of your samples. Also calculate the average and standard deviation of the norms.

c. Increase d on a coarsely spaced log scale all the way up to d = 1000 (say d = 50, 100, 200, 500, 1000), and repeat parts (a) and (b). Plot the variation of the average and the standard deviation of Euclidean norm of the samples with increasing d.

d. What can you conclude from your plot from part (c)?


q4: The goal of this problem is to implement a very simple text retrieval system. Given (as input) a database of documents as well as a query document (all provided in an attached .zip file), write a program, in a language of your choice, to find the document in the database that is the best match to the query. Specifically:

a. Write a small parser to read each document and convert it into a vector of words.

b. Compute tf-idf values for each word in every document as well as the query.

c. Compute the cosine similarity between tf-idf vectors of each document and the query.

d. Report the document with the maximum similarity value.
