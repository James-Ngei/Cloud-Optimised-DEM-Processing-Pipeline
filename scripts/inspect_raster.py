import sys
from osgeo import gdal

def inspect_raster(filepath):
    """Inspect raster properties"""
    dataset = gdal.Open(filepath)
    
    if dataset is None:
        print(f"Error: Could not open {filepath}")
        sys.exit(1)
    
    print("\n" + "="*60)
    print(f"RASTER INSPECTION: {filepath}")
    print("="*60 + "\n")
    
    print(f"Driver: {dataset.GetDriver().ShortName}")
    print(f"Size: {dataset.RasterXSize} x {dataset.RasterYSize} pixels")
    print(f"Bands: {dataset.RasterCount}")
    print(f"Projection: {dataset.GetProjection()[:80]}...")
    
    # Geotransform
    gt = dataset.GetGeoTransform()
    print(f"\nGeotransform:")
    print(f"  Origin: ({gt[0]:.6f}, {gt[3]:.6f})")
    print(f"  Pixel size: ({gt[1]:.6f}, {gt[5]:.6f})")
    
    # Band info
    band = dataset.GetRasterBand(1)
    print(f"\nBand 1:")
    print(f"  Data type: {gdal.GetDataTypeName(band.DataType)}")
    print(f"  Block size: {band.GetBlockSize()}")
    print(f"  Overviews: {band.GetOverviewCount()}")
    
    # Check tiling
    block_x, block_y = band.GetBlockSize()
    if block_x == dataset.RasterXSize:
        print(f"  Layout: STRIP-BASED (inefficient for random access)")
    else:
        print(f"  Layout: TILED ({block_x}x{block_y})")
    
    # Compression
    metadata = band.GetMetadata("IMAGE_STRUCTURE")
    compression = metadata.get("COMPRESSION", "None")
    print(f"  Compression: {compression}")
    
    # Statistics
    try:
        stats = band.GetStatistics(True, True)
        print(f"\nStatistics:")
        print(f"  Min: {stats[0]:.2f}")
        print(f"  Max: {stats[1]:.2f}")
        print(f"  Mean: {stats[2]:.2f}")
        print(f"  StdDev: {stats[3]:.2f}")
    except:
        print(f"\nStatistics: Not available")
    
    dataset = None
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python inspect_raster.py <path_to_raster>")
        print("Example: python inspect_raster.py data/raw/srtm_raw.tif")
        sys.exit(1)
    
    inspect_raster(sys.argv[1])