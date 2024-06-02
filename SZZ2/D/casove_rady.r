library(forecast)

souvenir <- scan("http://robjhyndman.com/tsdldata/data/fancy.dat")
souvenirtimeseries <- ts(souvenir, frequency=12, start=c(1987,1))
souvenirtimeseries

# to csv
write.csv(souvenirtimeseries, file = "souvenirtimeseries.csv")

plot.ts(souvenirtimeseries)

souvenir_decomposition <- decompose(souvenirtimeseries, type = "additive")
plot(souvenir_decomposition)

souvenir_decomposition <- decompose(souvenirtimeseries, type = "multiplicative")
plot(souvenir_decomposition)
