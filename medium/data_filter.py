# Create a script that uses the attached countries_by_area.txt file as data source
# and prints out the top 5 most densely populated countries
import pandas

file = "/Users/hubertarciszewski/Downloads/countries-by-area.txt"

df = pandas.read_csv(file)
population = [x for x in df["population_2013"]]
area_sqkm = [x for x in df["area_sqkm"]]

zipped = (zip(population, area_sqkm))
zipped = list(zipped)

population_divde_by_area = []
for x in zipped:
    population_divde_by_area.append(x[0] / x[1])

df2 = df.assign(column_x=population_divde_by_area)
df2 = df2.nlargest(5, ["column_x"])

for x in df2["country"]:
    print(x)
