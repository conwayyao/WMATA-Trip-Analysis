# WMATA Trip Analysis
Analysis of WMATA performance using Conway's own SmarTrip data

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
