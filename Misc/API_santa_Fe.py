import requests
import pandas as pd
import urllib.parse
import time
input_string = '1841034,1841035,1842928,1842929,1842930,1842931,1842932,1842933,1842934,1844823,1844824,1844825,1844826,1844827,1844828,1844829,1844830,1844831,1846720,1846721,1846722,1846723,1846724,1846725,1846726,1846727,1846728,1846729,1846730,1848617,1848618,1848619,1848620,1848621,1848622,1848623,1848624,1848625,1848626,1848627,1848628,1850519,1850520,1850521,1850522,1850523,1850524,1850525,1850526,1850527,1850528,1850529,1850530,1850531,1852420,1852421,1852422,1852423,1852424,1852425,1852426,1852427,1852428,1852429,1852430,1852431,1852432,1852433,1854300,1854301,1854302,1854303,1854304,1854305,1854306,1854307,1854308,1854309,1854310,1854311,1854312,1854313,1856180,1856181,1856182,1856183,1856184,1856185,1856186,1856187,1856188,1856189,1856190,1856191,1856192,1856193,1858064,1858065,1858066,1858067,1858068,1858069,1858070,1858071,1858072,1858073,1858074,1858075,1858076,1858077,1859948,1859949,1859950,1859951,1859952,1859953,1859954,1859955,1859956,1859957,1859958,1859959,1859960,1859961,1861836,1861837,1861838,1861839,1861840,1861841,1861842,1861843,1861844,1861845,1861846,1861847,1861848,1861849,1863725,1863726,1863727,1863728,1863729,1863730,1863731,1863732,1863733,1863734,1863735,1863736,1863737,1865641,1865642,1865643,1865644,1865645,1865646,1865647,1865648,1865649,1865650,1865651,1865652,1867558,1867559,1867560,1867561,1867562,1867563,1867564,1867565,1867566,1867567,1867568,1869501,1869502,1869503,1869504,1869505,1869506,1869507,1869508,1869509,1871444,1871445,1871446,1871447,1871448,1871449,1871450,1873392,1873393'
numbers = input_string.split(',')
elements_per_list = len(numbers) // 8
split_lists = [numbers[i * elements_per_list: (i + 1) * elements_per_list] for i in range(8)]
API_KEY = "xchNW9hSAWq9WoiQbzdRFtr0XXq75xjZUds8FTRw"
EMAIL = "CENSORED"
BASE_URL = "https://developer.nrel.gov/api/nsrdb/v2/solar/full-disc-download.json?"
POINTS = [
'1841034,1841035,1842928,1842929,1842930,1842931,1842932,1842933,1842934,1844823,1844824,1844825,1844826,1844827,1844828,1844829,1844830,1844831,1846720,1846721,1846722,1846723,1846724,1846725,1846726,1846727,1846728,1846729,1846730,1848617,1848618,1848619,1848620,1848621,1848622,1848623,1848624,1848625,1848626,1848627,1848628,1850519,1850520,1850521,1850522,1850523,1850524,1850525,1850526,1850527,1850528,1850529,1850530,1850531,1852420,1852421,1852422,1852423,1852424,1852425,1852426,1852427,1852428,1852429,1852430,1852431,1852432,1852433,1854300,1854301,1854302,1854303,1854304,1854305,1854306,1854307,1854308,1854309,1854310,1854311,1854312,1854313,1856180,1856181,1856182,1856183,1856184,1856185,1856186,1856187,1856188,1856189,1856190,1856191,1856192,1856193,1858064,1858065,1858066,1858067,1858068,1858069,1858070,1858071,1858072,1858073,1858074,1858075,1858076,1858077,1859948,1859949,1859950,1859951,1859952,1859953,1859954,1859955,1859956,1859957,1859958,1859959,1859960,1859961,1861836,1861837,1861838,1861839,1861840,1861841,1861842,1861843,1861844,1861845,1861846,1861847,1861848,1861849,1863725,1863726,1863727,1863728,1863729,1863730,1863731,1863732,1863733,1863734,1863735,1863736,1863737,1865641,1865642,1865643,1865644,1865645,1865646,1865647,1865648,1865649,1865650,1865651,1865652,1867558,1867559,1867560,1867561,1867562,1867563,1867564,1867565,1867566,1867567,1867568,1869501,1869502,1869503,1869504,1869505,1869506,1869507,1869508,1869509,1871444,1871445,1871446,1871447,1871448,1871449,1871450,1873392,1873393'
]

def main():
    input_data = {
        'attributes': 'dew_point,air_temperature,cloud_type,ghi,relative_humidity,surface_pressure,surface_albedo,solar_zenith_angle,total_precipitable_water,wind_direction,wind_speed',
        'interval': '30',
        'to_utc': 'false',
        
        'api_key': API_KEY,
        'email': EMAIL,
    }
    output_links = []
    all_locations = ','.join(numbers)
    
    for name in ['2021']:
        print(f"Processing name: {name}")
        for location_id in all_locations.split(','):
            input_data['names'] = [name]
            input_data['location_ids'] = location_id
            print(f'Making request for location {location_id}...')

            if '.csv' in BASE_URL:
                url = BASE_URL + urllib.parse.urlencode(data, True)
                # Note: CSV format is only supported for single point requests
                # Suggest that you might append to a larger data frame
                data = pd.read_csv(url)
                print(f'Response data (you should replace this print statement with your processing): {data}')
                # You can use the following code to write it to a file
                # data.to_csv('SingleBigDataPoint.csv')
            else:
                headers = {
                    'x-api-key': API_KEY
                }
                data = get_response_json_and_handle_errors(requests.post(BASE_URL, input_data, headers=headers))
                download_url = data['outputs']['downloadUrl']
                output_links.append(download_url)  # Save the resulting link to the list

                # Delay for 1 second to prevent rate limiting
                time.sleep(1)
                
            print(f'Processed')
            with open('resulting_links.txt', 'w') as file:
                file.write(','.join(output_links))


def get_response_json_and_handle_errors(response: requests.Response) -> dict:
    """Takes the given response and handles any errors, along with providing
    the resulting json

    Parameters
    ----------
    response : requests.Response
        The response object

    Returns
    -------
    dict
        The resulting json
    """
    if response.status_code != 200:
        print(f"An error has occurred with the server or the request. The request response code/status: {response.status_code} {response.reason}")
        print(f"The response body: {response.text}")
        exit(1)

    try:
        response_json = response.json()
    except:
        print(f"The response couldn't be parsed as JSON, likely an issue with the server, here is the text: {response.text}")
        exit(1)

    if len(response_json['errors']) > 0:
        errors = '\n'.join(response_json['errors'])
        print(f"The request errored out, here are the errors: {errors}")
        exit(1)
    return response_json

if __name__ == "__main__":
    main()