from rio_cogeo.cogeo import cog_validate

valid, errors, warnings = cog_validate("data/cog/srtm_cog.tif")

print("Valid COG:", valid)

if errors:
    print("Errors:")
    for e in errors:
        print("-", e)

if warnings:
    print("Warnings:")
    for w in warnings:
        print("-", w)
