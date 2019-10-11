from polymer.main import run_atm_corr
from polymer.level2_nc import Level2_NETCDF
from polymer.level1_olci import Level1_OLCI
from glob import glob

s3_l1_filedir='<Your_path>/L1/S3*.SEN3'
s3_l2_outdir='<Your_path>/L2_POLYMER/'

for filename in glob(s3_l1_filedir):
    print(filename)
    print(s3_l2_outdir)
    run_atm_corr(Level1_OLCI(filename), Level2_NETCDF(outdir=s3_l2_outdir))
