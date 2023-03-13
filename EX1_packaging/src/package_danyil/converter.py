from pyproj import Transformer

def convert_wgs_to_est(lat, lon) -> tuple:
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:3301")
    x, y = transformer.transform(lat, lon)

    return round(x, 2), round(y, 2)


def convert_est_to_wgs(lat, lon) -> tuple:
    transformer = Transformer.from_crs("EPSG:3301", "EPSG:4326")
    x, y = transformer.transform(lat, lon)

    return round(x, 6), round(y, 6)