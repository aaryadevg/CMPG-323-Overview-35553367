# This is totally overkill but, there is a reason this is the most accurate estimate
# I can come up with for a burn down chart
import matplotlib.pyplot as plt
import numpy as np

# effort = (allocated - (badges + class time))
# classTime = 2* 1.75 * nWeeks
# allocated = nWeeks * 11
nWeeks = np.array([2,5,4,4,3], dtype=np.uint8) # Acquired from study guide
allocated = nWeeks * 11 # 11 Hours a week * number of weeks the project goes on
classTime = 2 * 1.75 * nWeeks # 2 classes a week, 1h45 according to the time table
badges = np.array([2.16777, 8.36, 3.5, 5, 8.25]) # from the required badges

# Time spent working on project should be the 
# time allocated according to study guide - the time taken by badges and time spent in class
# Not perfect but should be a reasonable estimate 
effort = allocated - (badges + classTime) 

# No actual work hours tracked thus these are purely guesses
actual = np.array([12, 30, 27, 25, 12.5])

xAxis = [1,2,3,4,5]


plt.figure(figsize=(12,7))
plt.style.use("seaborn-deep")
plt.plot(xAxis, effort, label="Estimated effort", marker="o")
plt.plot(xAxis, actual, label="Actual effort", marker="o", ls="-.")
plt.xticks(xAxis)
plt.legend(loc="upper right")
plt.title("Burndown chart")
plt.xlabel("Project number")
plt.ylabel("effort (Hours)")
plt.grid()
plt.savefig("BurndownChart.png", dpi=300)