from pathlib import Path
from typing import Union

import salem
import xarray as xr

Raster = Union[xr.DataArray, xr.Dataset]
PathLike = Union[str, Path]


def extract_shp(in_ds: Raster, shp_file: PathLike) -> Raster:
    """Extract values using a shp file

    Args:
        in_ds (Raster): Input data
        shp_file (PathLike): Vector file

    Returns:
        Raster: Cropped data
    """
    shp_gdf = salem.read_shapefile(shp_file)
    bnds = shp_gdf.bounds.to_numpy()
    corners = ((bnds[0][0], bnds[0][1]), (bnds[0][2], bnds[0][3]))
    out_ds: Raster = in_ds.salem.subset(corners=corners, crs=shp_gdf.crs, margin=1)
    out_ds = out_ds.salem.roi(shape=shp_gdf, all_touched=True)

    return out_ds
