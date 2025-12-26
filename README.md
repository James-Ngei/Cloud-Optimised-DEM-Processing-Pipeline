# Cloud-Optimized Raster Processing & Delivery Pipeline

A reproducible, cloud-native pipeline for preparing, validating, and serving large raster datasets efficiently over the web.

## Problem Statement

Large raster datasets are typically stored as monolithic GeoTIFFs, making them inefficient to access, stream, or visualize in web-based GIS applications. This project demonstrates a production-ready pipeline for converting raw rasters into Cloud-Optimized GeoTIFFs (COGs) with validation and web delivery.

## Dataset

**SRTM Digital Elevation Model** - Kenya/Uganda Region
- Size: 28,721 × 33,677 pixels (~967 megapixels)
- Resolution: ~30m at equator
- Elevation range: -10m to 3,314m
- Original size: 417 MB (uncompressed)
- COG size: 524 MB (with compression + 5 overview levels)

## Quick Start

### Using Docker (Recommended)
```bash
# Build image
docker build -t dem-cog .

# Run pipeline
docker run --rm -v %cd%:/app dem-cog python3 scripts/inspect_raster.py data/raw/srtm_raw.tif
docker run --rm -v %cd%:/app dem-cog python3 scripts/convert_to_cog.py data/raw/srtm_raw.tif data/cog/srtm_cog.tif
docker run --rm -v %cd%:/app dem-cog python3 scripts/validate_cog.py data/cog/srtm_cog.tif

# Serve COG
docker run -p 8000:8000 -v %cd%:/app dem-cog python3 scripts/serve.py

# View in browser
http://localhost:8000/frontend/index.html
```

## Results

- ✅ Valid COG structure confirmed
- ✅ 512×512 internal tiling for efficient HTTP range requests
- ✅ 5 overview levels for multi-resolution access
- ✅ ~110x faster web access vs raw GeoTIFF
- ✅ 95% bandwidth reduction for typical viewport loads

See [Performance Comparison](docs/performance_comparison.md) for detailed analysis.

## Technical Stack

- **GDAL 3.9.2** - Raster processing
- **rio-cogeo** - COG validation
- **Python 3.11** - Pipeline orchestration
- **Leaflet + georaster** - Web visualization
- **Docker** - Reproducible environment
<<<<<<< HEAD
=======

## License

MIT
>>>>>>> 21596f7623209e661e233f5b65c7b63656d70612
