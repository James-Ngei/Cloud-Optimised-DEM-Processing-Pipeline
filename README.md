# Cloud-Optimised Digital Elevation Model (DEM) Pipeline

**Overview**

This project implements a reproducible, cloud-native pipeline for processing and serving large Digital Elevation Model (DEM) rasters efficiently over HTTP. The workflow converts a raw GeoTIFF DEM into a Cloud-Optimized GeoTIFF (COG), validates its internal structure, and verifies real-time access performance in a web mapping client.

**Problem**

Raw DEM GeoTIFFs are often stored as monolithic files, leading to inefficient data access patterns in web-based GIS systems. Without internal tiling, overviews, and HTTP range-request compatibility, even simple map interactions require excessive data transfer.

**Solution**

A containerised Python pipeline that:
1. Inspects raster structure and metadata
2. Converts the DEM into a valid COG with internal tiling and overviews
3. Validates compliance with the COG specification
4. Serves the raster via a lightweight HTTP server
5. Confirms correct behaviour in a browser-based map client

**Tech Stack**

- Python 3.11
- GDAL
- rio-cogeo
- Docker
- Leaflet (frontend validation)

**Repository structure**
```
project-01-dem-cog-pipeline/
│
├── data/
│   ├── raw/
│   │   └── srtm_raw.tif
│   └── cog/
│       └── srtm_cog.tif
│
├── scripts/
│   ├── inspect_raster.py
│   ├── convert_to_cog.py
│   └── validate_cog.py
│
├── frontend/
│   └── index.html
│
├── Dockerfile
├── requirements.txt
└── README.md
```


