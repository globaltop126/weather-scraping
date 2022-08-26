from wwo_hist import retrieve_hist_data
from datetime import datetime, timedelta
import os
os.chdir(".\doc")
frequency=24
start_date = '01-01-2022'
end_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
end_date = end_date[8:10] + '-' + end_date[5:7] + '-' + end_date[0:4] 

api_key = '80f403e537ec46c189c33825222207'
location_list = ['Arica', 'Tarapaca', 'Antofagasta', 'Atacama', 'Coquimbo', 'Valparaiso', 'Santiago', "O'Higgins", 'Maule', 'Araucania', 'chillan', 'Valdivia', 'montt', 'Coyhaique', 'Concepcion', 'Punta']

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)

