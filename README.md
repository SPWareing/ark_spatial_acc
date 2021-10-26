# <p align='center'> Convert Survey </p>
---

## Usage

This script is designed to work in conjunction with the QGIS Plugin [Ark Spatial](https://github.com/lparchaeology/ArkSpatial). It takes a CSV format file from a GPS unit and processes the raw X,Y,Z data into lines and polygons, which can then be directly imported to Ark Spatial

## Running the Script

As it stands the script can either:
+ Run directly in the QGIS Python Console
+ Be added to a startup.py file

Familiarity is required with the ARK Spatial codelist for features, as these will be need to be used in the GPS unit when surveying. 
Point IDs should be used in a continuous manner as they are used as a composite key alongside the feature code to group feature geometries.

For example
>  When surveying a Section line
> GPS code should be 'SEC', POINT ID should be prefixed SEC<#section number>.01 .02 etc



### To do
- [] Add Sample CSV
- [x] Add startup.py example
- [] add point functionality
