import nfl_data_py as nfl 


years = [2018, 2019, 2020]


qbr = nfl.import_qbr(years = years, level = 'nfl', frequency = 'season')

print(qbr.head())
