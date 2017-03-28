[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> `#load data
resp = nsfg.ReadFemResp()
#review data
resp.head()
#subset data
resp['numkdhh'].dtype
#plot subsetted data
resp['numkdhh'].hist()
#calculate and plot PMF for data
resp_pmf = thinkstats2.Pmf(resp['numkdhh'])
thinkplot.Hist(resp_pmf)

#Select only data from children in class & plot histogram
df_resp = resp['numkdhh']
nots = df_resp != 0
df_resp = df_resp[nots]
df_resp.hist()
#calculate and plot PMF
dfresp_pmf = thinkstats2.Pmf(df_resp)
thinkplot.Hist(dfresp_pmf)

