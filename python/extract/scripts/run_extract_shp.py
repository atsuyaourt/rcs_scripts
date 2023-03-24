from pathlib import Path

import salem
from extract_shp import extract_shp

nc_file = Path("input/nc/obs_aphrodite_v1801_r1_pr_1998_2015.nc")
in_ds = salem.open_xr_dataset(nc_file)

shp_file = Path("input/shp/metromanila/MetroManila.shp")

out_ds = extract_shp(in_ds, shp_file)
