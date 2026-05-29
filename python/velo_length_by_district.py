import geopandas as gpd
import pandas as pd

file_path = "all_velo_2025-12-12"

okrugs = [
    "ВАО", "ЗАО", "ЗелАО", "САО", "СВАО",
    "СЗАО", "ТиНАО", "ЦАО", "ЮАО", "ЮВАО", "ЮЗАО"
]

gdf = gpd.read_file(file_path)

filtered = gdf[gdf["OKRUG"].isin(okrugs)]

grouped = (
    filtered.groupby("OKRUG")["LEN"]
    .sum()
    .reindex(okrugs)  # Сохраняем нужный порядок
    .fillna(0) / 1000  # Переводим в километры
)

grouped["Общий итог"] = grouped.sum()

print(grouped.round(2))
