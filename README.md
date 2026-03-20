 # datanix 

A smart data cleaning package for Python!
Built for data scientists and ML engineers.

## Installation
pip install datanix

## Functions
- check()      - Finds all data problems
- prepare()    - Fixes everything automatically
- fix()        - Smart missing value fixing
- report()     - Full data summary report
- visualize()  - Beautiful charts and graphs

## Quick Start
import datanix as dx
import pandas as pd

df = pd.read_csv("your_data.csv")
dx.check(df)
dx.prepare(df)
dx.report(df)
dx.visualize(df)

## Author
Chandravardhan

## License
MIT License
