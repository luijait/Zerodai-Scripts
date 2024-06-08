try:
    from googlesearch import search

except ImportError:
    print("")
import time
counter = 15
def dorks(dork):
    counter = 15
    data_list = []
    for results in search(dork, tld="com", lang="en", num=5, start=0, stop=None, pause=2):
        counter = counter + 1
        print("[+]", counter, results)
        time.sleep(0.1)
        data = (counter, results)
        data_list.append(data)

    return data_list
