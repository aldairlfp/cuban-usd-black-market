import random
import statistics
import json
import sys

# Opening JSON files
with open("eltoquedataECU1000.json") as euro_file, open("eltoquedataMLC1000.json") as mlc_file, open("eltoquedataUSD1000.json") as usd_file:
    euro_data = json.load(euro_file)
    mlc_data = json.load(mlc_file)
    usd_data = json.load(usd_file)


last_values_mean_euro = [i['avg'] for i in euro_data[len(euro_data)-7:]]
last_values_mean_mlc = [i['avg'] for i in mlc_data[len(mlc_data)-7:]]
last_values_mean_usd = [i['avg'] for i in usd_data[len(usd_data)-7:]]

last_values_median_euro = [i['median'] for i in euro_data[len(euro_data)-7:]]
last_values_median_mlc = [i['median'] for i in mlc_data[len(mlc_data)-7:]]
last_values_median_usd = [i['median'] for i in usd_data[len(usd_data)-7:]]

# Random reference to increase or decrease values 
states=[-1,0,1]

# k is index of fake value
def Simulate_Mean(last_values_mean,k, day):
    value_random = random.choice(states)
    if day%5==0:
        last_values_mean[0]+=k
    if day%6==0:
        last_values_mean[0]-=k
    if value_random == -1:
        last_values_mean[day%7]= int(statistics.mean(last_values_mean) - 5)
    elif value_random == 1:
        last_values_mean[day%7]= int(statistics.mean(last_values_mean) + 5)
    else:
        last_values_mean[day%7]= int(statistics.mean(last_values_mean))
    return last_values_mean[day%7]

def Simulate_Median(last_values_median, k, day):
    value_random = random.choice(states)
    if day%5==0:
            last_values_median[0]+=k
    if day%6==0:
        last_values_median[0]-=k
    if value_random == -1:
        last_values_median[day%7]= int(statistics.median(last_values_median)-5)
    elif value_random == 1:
        last_values_median[day%7]= int(statistics.median(last_values_median)+5)
    else: 
        last_values_median[day%7]= int(statistics.median(last_values_median))
    return last_values_median[day%7]

def simulate(day_until):
    day = 0
    print('This is using the mean:')
    while day < day_until:
        print('Euro: ', Simulate_Mean(last_values_mean_euro, 5, day))
        print('USD:  ', Simulate_Mean(last_values_mean_usd,  5, day))
        print('MLC:  ', Simulate_Mean(last_values_mean_mlc,  5, day))
        day += 1

    day = 0
    print('This is using the median:')
    while day < day_until:
        print('Euro: ', Simulate_Mean(last_values_mean_euro, 5, day))
        print('USD:  ', Simulate_Mean(last_values_mean_usd,  5, day))
        print('MLC:  ', Simulate_Mean(last_values_mean_mlc,  5, day))
        day += 1

day_until = 100
if len(sys.argv) == 2:
    day_until = int(sys.argv[1])

simulate(day_until)