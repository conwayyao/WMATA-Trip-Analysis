# WMATA Trip Analysis


Analysis of WMATA performance using Conway's own SmarTrip data

.

# Data Collection and Munging:

## Excel steps

1. Log into SmarTrip 
2. Navigate to usage history for the SmarTrip card
3. For each calendar month, export to Excel
4. Copy and paste rows of data to a master Excel sheet
4. Station name corrections ("Rosslyn East" to "Rosslyn", "Capitol S" to "Capitol South", etc.)
5. Change format of all cells in the "Change" and "Balance" columns to numbers rather than currency
4. If SmartBenefits is used, separate SmartBenefits balance and changes from SmarTrip balance and changes
5. Create new columns for "Month" and "Weekday"
4. Convert time into Month and Weekday using Excel format changes
4. Export whole file as CSV

## Python Steps

1. Convert time strings to timestamps using pandas.to_datetime()
2. Sort by time ascending (oldest trips to newest)
3. Group by trips: 
  1. Iterate through rows; if "Description" is "Entry", then add one to the trip number and append to a list
  2. Add list to DataFrame as new column "Trip"


# Data Analysis

- 688 rows of data. Each row represents one swipe of the SmarTrip card.
- 282 entries, 179 transfers, 179 exits, 48 reloads/others
- $606 spent

## Overall Trip Data

- 282 trips

## Circulator Usage

Filtered the data with [Operator = DC Circulator]:

- 29 boardings (pie chart)
  - 20 Georgetown- Union Station
  - 7 Rosslyn- Dupont Circle
  - 1 Union Station- Navy Yard
  - 1 Woodley Park- Adams Morgan
- 19 originations, 10 transfers
- $14.00 total cost

## Subway Trips

Filtered the trips by [Operator = Metrorail]:
- 173 subway trips
  - 111 entries, 62 transfers from bus-to-subway
  - Boarded from 32 origination stations [map of frequency]
  - Traveled to 29 destination stations [map of frequency]
- $276.00 total cost
  - Average of $1.60
  - Max cost of $4.65 (Pentagon to Vienna)
  - [histogram of cost value_counts]
- Subway trips by weekday [histogram]
- Subway trips by month [histogram]
- Boardings by period of day:
  - 11 morning (6am-11am)
  - 56 midday (11am-5pm)
  - 48 evening (5pm-10pm)
  - 58 night (10pm-6am)
- 3 days, 3 hours, and 31 minutes total time
  - Average duration: 24 minutes, 59 seconds
  - Shortest trip: 7 minutes (Pentagon to National Airport)
  - Longest trip: 1 hour, 15 minutes (New York Avenue to Pentagon)





