# WMATA Trip Analysis

Analysis of WMATA performance using Conway's own SmarTrip data

# Data Analysis

- 700 rows of data. Each row represents one swipe of the SmarTrip card.
- 286 entries, 183 transfers, 183 exits, 48 reloads/others
- $627.75 spent

## Overall Trip Data

- 286 trips

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
  - 113 entries, 60 transfers from bus-to-subway
  - Boarded from 32 origination stations [map of frequency] 
  - Traveled to 29 destination stations [map of frequency] 
- $279.35 total cost
  - Average fare of $1.61
  - Max fare of $4.65 (Pentagon to Vienna) 
  - [histogram of cost value_counts]
- Subway trips by weekday [histogram] 
- Subway trips by month [histogram]
- Boardings by period of day: 
  - 11 morning (6am-11am)
  - 57 midday (11am-5pm)
  - 50 evening (5pm-10pm)
  - 55 night (10pm-6am)
- 46 peak-fare trips:
  - $1.81 average fare
  - 21m 20s average duration
- 127 off-peak trips
  - $1.54 average fare
  - 24m 43s average duration
- 2 days, 20 hours, 40 minutes total time
  - Average duration: 23 minutes, 49 seconds
  - Median duration: 21 minutes
  - 75% duration: 27 minutes
  - Shortest trip: 7 minutes (Pentagon to National Airport)
  - Longest trip: 1 hour, 15 minutes (New York Avenue to Pentagon)

## Bus trips

Filtered the trips by [Operator = Metrobus, DASH, or FFC]:

- 259 bus trips 
  - 154 entries, 105 transfers from subway-to-bus or bus-to-bus
  - Boarded 42 routes [map of frequency] 
- $317.45 total cost
  - Average fare of $1.23
  - Max fare of $7.00 (Greenbelt to BWI) 
  - [histogram of cost value_counts]
- Bus trips by weekday [histogram] 
- Bus trips by month [histogram]
- Boardings by period of day: 
  - 28 morning (5am-11am)
  - 47 midday (11am-5pm)
  - 57 evening (5pm-10pm)
  - 127 night (10pm-5am)

