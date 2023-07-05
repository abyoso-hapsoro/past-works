# jika package pacman tidak ada, install terlebih dahulu
if (!require("pacman")) install.packages("pacman")

# load library pacman
library(pacman)

# gunakan fungsi pacman untuk load library
# jika library tersebut tidak ada, install terlebih dahulu
p_load(TSA, pastecs)

# load data
data(hours)
hours

# plot dots
plot(hours, type = 'o', ylab = 'Month hours')

# plot months
plot(hours, type = 'l', ylab = 'Month hours')
q <- season(hours)
points(y = hours, x = time(hours), pch = as.vector(q))

# quadratic trend least square modeling
hours.qm = lm(hours ~ time(hours) + I(time(hours)^2))
summary(hours.qm)

# time series plot of the standardized residuals
plot(y = rstandard(hours.qm), x = as.vector(time(hours)), type = 'l',
     ylab = 'Standardized Residuals', xlab = 'Time')
points(y = rstandard(hours.qm), x = as.vector(time(hours)),
       pch = as.vector(q))

# run test
runs(rstandard(hours.qm))

# calculate autocorrelation function
acf(rstandard(hours.qm))

# test for trend
trend.test(rstandard(hours.qm), R = 1)
