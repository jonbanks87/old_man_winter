import csv
import codecs
import urllib.request
import urllib.error
import sys
import pandas as pd

def check_weather(Location,StartDate,EndDate):
    '''Required Imports:
    import csv
    import codecs
    import urllib.request
    import urllib.error
    import sys
    import pandas as pd'''
    
    BaseURL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

    ApiKey='KHJY9L7H4AJAACFQ9CYDHHGCV'
    UnitGroup='us'
    
    ContentType="csv"
    Include="days"
    #basic query including location
    ApiQuery=BaseURL + Location

    #append the start and end date if present
    if (len(StartDate)):
        ApiQuery+="/"+StartDate
        if (len(EndDate)):
            ApiQuery+="/"+EndDate

    #Url is completed. Now add query parameters (could be passed as GET or POST)
    ApiQuery+="?"

    #append each parameter as necessary
    if (len(UnitGroup)):
        ApiQuery+="&unitGroup="+UnitGroup

    if (len(ContentType)):
        ApiQuery+="&contentType="+ContentType

    if (len(Include)):
        ApiQuery+="&include="+Include

    ApiQuery+="&key="+ApiKey


    print(' - Running query URL: ', ApiQuery)

    try: 
        CSVBytes = urllib.request.urlopen(ApiQuery)
    except urllib.error.HTTPError  as e:
        ErrorInfo= e.read().decode() 
        print('Error code: ', e.code, ErrorInfo)
        sys.exit()
    except  urllib.error.URLError as e:
        ErrorInfo= e.read().decode() 
        print('Error code: ', e.code,ErrorInfo)
        sys.exit()
    CSVText = csv.reader(codecs.iterdecode(CSVBytes, 'utf-8'))
    df = pd.DataFrame(CSVText)
    df.columns = df.iloc[0]
    df = df.drop(0)
    return df