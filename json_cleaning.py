# 1. Data cleaning for .json
# extract ['transcript'], ['utterance_id], ['speaker'] element from json.

import json
import re
import pickle
import sys

def main():
    reload(sys)
    sys.setdefaultencoding("utf-8")

    input_file = "s06_e25.json"
    output_file = "s06_e25_json.txt"
    myList=[]

    with open(input_file,'r') as json_data:
        data = json.load(json_data)

        for r in data['episodes']:
            for s in r['scenes']:
                s_id = s['scene_id']
                for u in s['utterances']:
                    # print str
                    id = u['utterance_id']
                    str = u['with_description']['transcript']
                    speaker = u['speaker']

                    # remove (...) or [...] pattern using regular expression
                    pattern1 = re.compile(r'\(.*?\)')
                    pattern2 = re.compile(r'\[.*?\]')
                    if pattern1.findall(str):
                        str = re.sub(r'\(.*?\)', '', str)
                        # print str
                    if pattern2.findall(str):
                        str = re.sub(r'\[.*?\]', '', str)

                    if len(str) > 1:
                        mytuple = (str, id,speaker,s_id)
                        myList.append(mytuple)

    with open(output_file, 'wb') as fp:
        pickle.dump(myList, fp)

if __name__ == "__main__":
    main()
