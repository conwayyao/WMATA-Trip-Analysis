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

- 170 subway trips
  - 111 entries, 59 transfers from bus-to-subway
  - Boarded from 32 origination stations [map of frequency] 
  - Traveled to 29 destination stations [map of frequency] 
- $273.10 total cost
  - Average fare of $1.61
  - Max fare of $4.65 (Pentagon to Vienna) 
  - [histogram of cost value_counts]
- Subway trips by weekday [histogram] 
- Subway trips by month [histogram]
- Boardings by period of day: 
  - 11 morning (6am-11am)
  - 56 midday (11am-5pm)
  - 48 evening (5pm-10pm)
  - 58 night (10pm-6am)
- 43 peak-fare trips:
  - $1.81 average fare
  - 21m 40s average duration
- 127 off-peak trips
  - $1.54 average fare
  - 25m 26s average duration
- 2 days, 21 hours, 24 minutes total time
  - Average duration: 24 minutes, 29 seconds
  - Median duration: 21 minutes
  - 75% duration: 27 minutes
  - Shortest trip: 7 minutes (Pentagon to National Airport)
  - Longest trip: 1 hour, 15 minutes (New York Avenue to Pentagon)

## Bus trips

Filtered the trips by [Operator = Metrobus, DASH, or FFC]:

- 250 bus trips 
  - 149 entries, 101 transfers from subway-to-bus or bus-to-bus
  - Boarded 41 routes [map of frequency] 
- $304.95 total cost
  - Average fare of $1.22
  - Max fare of $7.00 (Greenbelt to BWI) 
  - [histogram of cost value_counts]
- Subway trips by weekday [histogram] 
- Subway trips by month [histogram]
- Boardings by period of day: 
  - 28 morning (5am-11am)
  - 44 midday (11am-5pm)
  - 54 evening (5pm-10pm)
  - 124 night (10pm-5am)