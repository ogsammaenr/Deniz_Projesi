from data.seaData import _fetchSeaData
from data.printSeaData import printSeaData

_fetchSeaData()

FILE_PATH = "src/data/copernicus_data/merged_bgc_dataset.nc"

printSeaData(FILE_PATH)