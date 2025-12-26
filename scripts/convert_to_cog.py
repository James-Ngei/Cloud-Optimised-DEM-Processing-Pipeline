import sys
import os
from rio_cogeo.cogeo import cog_translate
from rio_cogeo.profiles import cog_profiles

def convert_to_cog(src_path, dst_path):
    """Convert raster to Cloud-Optimized GeoTIFF"""
    
    if not os.path.exists(src_path):
        print(f"Error: Source file not found: {src_path}")
        sys.exit(1)
    
    print("\n" + "="*60)
    print("CONVERTING TO COG")
    print("="*60 + "\n")
    print(f"Input:  {src_path}")
    print(f"Output: {dst_path}")
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    
    # Get COG profile (DEFLATE compression)
    profile = cog_profiles.get("deflate")
    
    # Customize profile
    profile.update({
        "blocksize": 512,
        "overview_level": 5,
        "overview_resampling": "cubic"
    })
    
    print("\nProcessing...")
    print(f"  Compression: DEFLATE")
    print(f"  Block size: 512x512")
    print(f"  Overview levels: 5")
    print(f"  Resampling: cubic")
    
    # Convert
    cog_translate(
        src_path,
        dst_path,
        profile,
        nodata=None,
        quiet=False
    )
    
    print(f"\n✓ COG created successfully")
    
    # Compare file sizes
    input_size = os.path.getsize(src_path) / (1024 * 1024)  # MB
    output_size = os.path.getsize(dst_path) / (1024 * 1024)  # MB
    reduction = ((input_size - output_size) / input_size) * 100
    
    print(f"\nFile size comparison:")
    print(f"  Original: {input_size:.2f} MB")
    print(f"  COG:      {output_size:.2f} MB")
    print(f"  Reduction: {reduction:.1f}%")
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_to_cog.py <input_raster> <output_cog>")
        print("Example: python convert_to_cog.py data/raw/srtm_raw.tif data/cog/srtm_cog.tif")
        sys.exit(1)
    
    convert_to_cog(sys.argv[1], sys.argv[2])