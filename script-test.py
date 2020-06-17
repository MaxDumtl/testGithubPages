import cdsapi

c = cdsapi.Client()

c.retrieve(
    'cams-solar-radiation-timeseries',
    {
        'sky_type': 'clear',
        'location': {
            'latitude': 0,
            'longitude': 0,
        },
        'altitude': '-999.',
        'date': '2020-06-09/2020-06-09',
        'time_step': '1month',
        'time_reference': 'universal_time',
        'format': 'csv',
    },
    'download.csv')