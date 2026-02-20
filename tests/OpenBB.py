from openbb import obb
output = obb.equity.price.historical("UAL")
df = output.to_dataframe()
print(df)