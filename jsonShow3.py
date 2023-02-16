import json
import datetime
import matplotlib.pyplot as plt
import numpy as np

def parse_json_date(json_date):
    millis = int(json_date[6:-2])
    dt = datetime.datetime.fromtimestamp(millis/1000)
    return dt.strftime('%d/%m/%y')

# Open the JSON file and load its contents
with open("yucataplays.json") as f:
    data = json.load(f)

# Extract the required information
points = []
dates = []
for item in data["data"]:
    point_result = item["PointResult"]
    date = parse_json_date(item["FinishedOn"])
    points.append(point_result)
    dates.append(date)

# Create the scatter plot
plt.scatter(dates, points)
plt.title("LessLucid's Innovation Game Scores")
plt.xlabel("Date")
plt.ylabel("Points")

# Add a line of best fit
x = np.arange(len(dates))
coefficients = np.polyfit(x, points, 1)
p = np.poly1d(coefficients)
plt.plot(dates, p(x), color='red')

# Display the plot
plt.show()
