# R code implementing simple random walk metropolis Hastings on the logit dataset in mcmc package


rm(list=ls())
data(logit,package="mcmc")

Y <- logit$y
X <- data.matrix(logit[,2:5])
N=1e5
d=4
s=20
f <- function(beta) prod(dbinom(Y,size=1,prob=1/(1+exp(-X%*%beta))))*prod(dnorm(beta,0,s))

# markov chain
beta = matrix(0,nrow=N,ncol=d)
acc.prob = numeric(N)

## NON-ADAPTIVE MCMC
for(i in 2:N){
  if(i%%1e3==0) print(i/1e3)
  y =rnorm(d,0,0.48) + beta[i-1,]
  alpha = min(1, f(y)/f(beta[i-1,]))
  if(log(runif(1))<log(alpha)){
    beta[i,] = y
    acc.prob[i] = 1
  }else{
    beta[i,] = beta[i-1,]
  }
}
mean(acc.prob)
plot(cumsum(acc.prob)/(1:N),col="red",type="l",xlab="",ylab="")
abline(h=0.23,col="blue",lty=2)
