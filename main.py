import urllib.request
from bs4 import BeautifulSoup
import sched, time


def do_something(sc):
    print("Checking your Coupons...")

    try:
        request = urllib.request.Request(urlAddress, None, headers)  # The assembled request
        response = urllib.request.urlopen(request)
    except urllib.request.HTTPErrorProcessor as e:
        print(e.fp.read())

    html_doc = response.read()
    # Parse the html file
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Format the parsed html file
    strhtm = soup.prettify()

    if strhtm.find("0 Left") == -1:
        print(">>> COUPONS AVAILABLE!! <<<")
    else:
        print("No Coupons Available")
    s.enter(60, 1, do_something, (sc,))


print("COINGECKO BOT STARTS...")
urlAddress = "https://www.coingecko.com/account/rewards/15-off-ledger-nano-x"
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent': user_agent}

s = sched.scheduler(time.time, time.sleep)
s.enter(60, 1, do_something, (s,))
s.run()
