# Web-Scrapper-for-Australian-Bureau-of-Meteorology-Site
A web scraper that allows users to directly access data from www.bom.gov.au.

The Australian Government's Bureau of Meteorology Site provides a number of pages where users can access measurements taken at stations located around the country. This data can be useful for a number of purposes, such as studying whether patterns, but it's not provided in an easily accessible form. This web scraper makes it easy to extract and use data from the site.

Has 1 class: ExtractBOM

Initialized as : ExtractBOM(Region, Area, Location)

Region: an abbreviation of the region in which the desired area is located, can be found on http://www.bom.gov.au/places/
- SA for South Australia
- NSW for New South Wales
- WA for Western Australia
- TAS for Tasmania
- ACT for Australian Capital Territory
- NT for Northern Territory
- QLD for Queensland
- VIC for Victoria

Area - City/Town were location is located

Location - Specific location in Area

METHODS for this class:

*using map_to allows you to specify the type of the outputs, which are stings by default

extractByField(Field, map_to = None) - extract an array representing all the entries of a certain field currently shown on the site

extractByFieldTime(Field, datetime, map_to = None) - extracts the entry of a certain field based on a specified timestamp, which is [day in month]/[time]
 
dailyFieldTime(Field, Time, outfile) - extracts an entry from a specific field and time on a daily basis and writes it to a csv file

hourlyFieldTime(Field, Time, outfile) - extracts an entry from a specific field on an hourly basis and writes it to a csv file
