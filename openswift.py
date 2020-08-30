import webbrowser
from datetime import date 

startDate = date(2020, 7, 27)
swiftDay = (date.today() - startDate).days + 1

url = 'https://www.hackingwithswift.com/100/' + str(swiftDay)

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

webbrowser.get(chrome_path).open(url)
