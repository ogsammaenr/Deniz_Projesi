from data.dataExplorer import DataExplorer
from data.SeaDataFetcher import SeaDataFetcher
from data.WeatherDataFetcher import WeatherDataFetcher
import xarray as xr
import numpy as np

# Farklı yol denemesi
FILE_PATH = "src/data/copernicus_data/"

weatherfetcher = WeatherDataFetcher()
weatherfetcher.fetch_data()

explorer = DataExplorer(FILE_PATH)
explorer.show_basic_info()
explorer.show_folder_summary()
