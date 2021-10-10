# Bank Loan Modeling
<br>

# Objective:
The classification goal is to predict the likelihood of a liability customer buying personal loans.

# Context:
The bank has a growing customer base. The bank wants to increase borrowers (asset customers) base to bring in more loan business and earn more through the interest on loans. So , the bank wants to convert the liability based customers to personal loan customers (while retaining them as depositors). A campaign that the bank ran last year for liability customers showed a healthy conversion rate of over 9% success. The department wants to build a model that will help them identify the potential customers who have a higher probability of purchasing the loan. This will increase the success ratio while at the same time reduce the cost of the campaign.

# Attribute Information:
- ID: Customer ID
- Age: Customer's age in completed years
- Experience: #years of professional experience
- Income: Annual income of the customer ($000)
- ZIP Code: Home Address ZIP code.
- Family: Family size of the customer
- CCAvg: Avg. spending on credit cards per month ($000)
- Education: Education Level. 1: Undergrad; 2: Graduate; 3: Advanced/Professional
- Mortgage: Value of house mortgage if any. ($000)
- Personal Loan: Did this customer accept the personal loan offered in the last campaign?
- Securities Account: Does the customer have a securities account with the bank?
- CD Account: Does the customer have a certificate of deposit (CD) account with the bank?
- Online: Does the customer use internet banking facilities?
- Credit card: Does the customer use a credit card issued by the bank?

# Steps and tasks:
1. Importing the datasets and libraries, check datatype, statistical summary, shape, null values etc
2. Checking if we need to clean the data for any of the variables
3. EDA: Study the data distribution in each attribute and target variable.
- Number of unique in each column
- Number of people with zero mortgage
- Number of people with zero credit card spending per month
- Value counts of all categorical columns
- Univariate and Bivariate analysis
4. Applying necessary transformations for the feature variables
5. Normalising the data and splitting the data into training and test set in the ratio of 70:30 respectively
6. Using Logistic Regression model to predict the likelihood of a customer buying personal loans.
7. Displaying all the metrics related for evaluating the model performance
8. Building various other classification algorithms and comparing their performance
- Support Vector Machine
- K-Nearest Neighbors
- Naive Bayes Classifier
