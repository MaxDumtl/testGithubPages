import cdsapi

c = cdsapi.Client()

c.retrieve(
    'cams-global-reanalysis-eac4',
    {
        'date': '2003-01-01/2003-01-01',
        'format': 'grib',
        'variable': 'total_column_ozone',
        'time': '03:00',
    },
    'download.grib')