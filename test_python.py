# Import necessary libraries\n",
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read in data
#Google mobility data
goog_mob = pd.read_csv("./Region_Mobility_Report_CSVs/2020_CA_Region_Mobility_Report.csv")

#Ontario COVID Public Health Unit Data - Cases Status,
ont_phu_status = pd.read_csv("./cases_by_status_and_phu.csv")

#Ontario COVID Public Health Unit Data - Daily increase in cases
ont_phu_incr = pd.read_csv("./daily_change_in_cases_by_phu.csv")

# Filter for Ontario Data
ont_goog_mob = goog_mob[goog_mob['sub_region_1'] == 'Ontario']

# Plot some variable",
sns.relplot(data = ont_goog_mob, x = 'date', y = 'residential_percent_change_from_baseline', kind = 'line')
plt.show()