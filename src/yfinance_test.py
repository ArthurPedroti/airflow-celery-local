import yfinance

hist = yfinance.Ticker("AAPL").history(
  period = "1d",
  interval = "1h",
  start = "2023-01-03",
  end = "2023-01-10",
  prepost = True
)

print(hist)
