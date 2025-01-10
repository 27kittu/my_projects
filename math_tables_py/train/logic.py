import random
import os
import json
import datetime

from pathlib import Path
root_dir= (Path('.')).joinpath('..')

class Tables:
    def __init__(self, n = None):
    #give any number while instantiation to avoid tables from 12-19, if 'n' is given, tables can be 12-n
        if n is None:
            self.tables = range(12, 19)
        self.tables = range(12, n)
        self.numbers =[2,3,4,5,6,7,8,9,10]
        self.start_line = "Let's start the tables"
        self.corr_perc = None
        self.record = []#list of recorded table lists

    def call(self):
        r_table = random.choice(self.tables)
        r_number = random.choice(self.numbers)
        r = []
        r.extend([r_table, r_number])
        i = self.collect_input(r)
        r.append(i)  
        self.record.append(r)
        

    def collect_input(self, rec):
        s = f'{rec[0]} x {rec[1]} = '
        try:
            i = int(input(s))
        except ValueError:
            i = 0
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt caught! Exiting gracefully.")
        return i

    def check_correct(self, assess_list):
        for i in assess_list:
            #this is to analyse which response is correct and wrong
            if i[0]*i[1] ==i[2]:
                i.append(True)
            else:
                i.append(False)
        counter =0
        for j in assess_list:
            if j[3]== True:
                counter+=1
        correct = counter
        self.corr_perc = (correct/30)*100
        print(f'Correct: {correct}/30  {self.corr_perc:.2f}')



def form_json(trnd_list):
    if 'rec_response.json' not in root_dir.iterdir():
        json_file = root_dir / 'rec_response.json'
        json_file.touch(exist_ok=True)
        with open(json_file,'w') as w:
            w.write('{}')        
    
    # ensure to have json string contains {days_record:{
    # date:{time:[], time:[]}, date = {time:[],time:[], time:[]} 
    #    }
    #}
    from datetime import datetime, time, date
    date = datetime.today().date().isoformat()
    date_t = datetime.today().date().isoformat()
    time_t = datetime.today().time().isoformat()
    if json_file:
        with open(json_file,'r') as f:
            json_s = json.load(f)
            if 'days_record' not in json_s:
                json_s['days_record'] = {}
            elif date_t not in json_s['days_record']:
                json_s['days_record'][date_t]={}
            elif time_t not in json_s['days_record'][date_t]:
                json_s['days_record'][date_t][time_t] = trnd_list
    else:
        print('no json in the directory')

def ret_json():
    json_file = root_dir / 'rec_response.json'
    if json_file:
        with open(json_file, 'r') as k:
            r = json.load(k)
            print(r)
