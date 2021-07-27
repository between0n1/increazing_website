from google_trends import gtrends
from datetime import datetime
today = datetime.today().strftime('%Y%m%d')
google_trends = gtrends(date= today, country="GB")
print(google_trends)


