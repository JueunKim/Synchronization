# 4. compare with transcript/subtitle using fuzzy string matching algorithms.

import pickle
import json
import os
from fuzzywuzzy import fuzz


def timeconvert(mill):
    millis = float(mill)
    minutes = (millis/(1000*60))%60
    minutes = float(minutes)
    seconds = (millis/1000)%60
    minutes = minutes.__float__()
    seconds = seconds.__float__()
    # print ("00:%02d:%.3f" % (minutes,seconds))
    return minutes, seconds


json_file_name = "s06_e25_json.txt"     # file from json_cleaning.py
smi_file_name = "smi_superset_6_25.txt"  # file from smi_superset.py

final_result = "s06_e25.json"           # for writing result into json file
output_file_name = "____.txt"

# Output file
f_out = open("6x01.srt.txt", 'w')


# load transcript and subtitle
with open(json_file_name, 'rb') as t:
    with open(smi_file_name, 'rb') as s:
        t_content = pickle.load(t)  # transcript
        s_content = pickle.load(s)  # subtitle

# initialize
mylist=[]

# apply fuzzy string matching algorithms
for idx, i in enumerate(range(len(t_content))):
    best_score = 0
    t_best = " "
    for j in range(len(s_content)):
        score = fuzz.ratio(t_content[i][0], s_content[j][0])
        if score > best_score:
            best_score = score
            t_best = j
    mytuple = (timeconvert(s_content[t_best][1]), timeconvert(s_content[t_best][2]),t_content[i][1])
    mylist.append(mytuple)
    # f_out.write("scene_id :  " + str(t_content[i][3]) + "\n")
    f_out.write("00:%02d:%06.3f" % (timeconvert(s_content[t_best][1])))
    f_out.write(" --> ")
    f_out.write("00:%02d:%06.3f \n" % (timeconvert(s_content[t_best][2])))
    f_out.write(str(t_content[i][2]))
    f_out.write(": "+str(s_content[t_best][0]) + " \n")
    # f_out.write("transcript :  " + str(t_content[i][0]) + "\n")
    # f_out.write("%s %s" % (timeconvert(s_content[t_best][1]), timeconvert(s_content[t_best][2])))

    # f_out.write("\n")
    # f_out.write("score : " "%d\n" % best_score)
    # f_out.write("===================\n")

f_out.close()

with open(output_file_name, 'wb') as fp:
    pickle.dump(mylist, fp)

#===================================================================

with open(final_result, 'r') as json_data:
    with open(output_file_name) as result:
        data = json.load(json_data)
        result = pickle.load(result)

for r in data['episodes']:
    for s in r['scenes']:
        for u in s['utterances']:
            for j in range(len(result)):
                if u['utterance_id'] == result[j][2]:
                    u['with_description']['trans_sub_time'] = result[j][0], result[j][1]
            # print u['utterance_id'], u['with_description']['trans_sub_time']

os.remove(final_result)
with open(final_result, 'w') as f:
    json.dump(data, f, indent=4)

