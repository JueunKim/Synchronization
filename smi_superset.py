# 3. make superset for all possible uttrance case.
import re
import pickle


def main():

    season = 6
    episode = 26
    for i in range(1, episode):
        input_file_name = "s06_e"+str(i)+"_smi.txt"
        output_file_name = "smi_superset_"+str(season)+"_"+str(i)+".txt"


        # Initialize list
        myList = []
        myList2 = []
        myList3 = []

        with open(input_file_name) as f_in:
            s_content = f_in.readlines()

            # remove whitespace character
            s_content = [x.strip() for x in s_content]

            for index, line in enumerate(s_content):
                if line.startswith('<p class=KRCC>'):
                    # trans = line.strip('<p class=KRCC>')
                    trans = re.sub('<.*?>', '', line)
                    start_t = int(re.search(r'\d+', s_content[index - 1]).group())
                    end_t = int(re.search(r'\d+', s_content[index + 1]).group())

                    myTuple = (trans, start_t, end_t)
                    myList.append(myTuple)

            # combine tuple to make superset
            # ex) [(1),(2),(3), (1,2) (2,3) (3,4)] .....
            trans, start_t, end_t = zip(*myList)
            for i in range(len(myList)):
                if i == len(myList) - 1:
                    break;
                else:
                    # print((' '.join((trans[i], trans[i+1])), start_t[i], end_t[i + 1]))
                    new_trans = trans[i] + trans[i + 1]
                    start_tt = int(start_t[i])
                    end_tt = int(end_t[i + 1])

                    myTuple2 = (new_trans, start_tt, end_tt)
                    myList2.append(myTuple2)

            for i in range(len(myList)):
                if i == len(myList) - 2:
                     break;
                else:
                    trans3 = trans[i] + trans[i + 1] + trans[i + 2]
                    startt = int(start_t[i])
                    endtt = int(start_t[i + 2])
                    myTuple3 = (trans3, startt, endtt)
                    myList3.append(myTuple3)

            # combine three list
            myList = myList + myList2 + myList3
            with open(output_file_name, 'wb') as fp:
                pickle.dump(myList, fp)

    # concatenate_superset(season)


def concatenate_superset(season):
    objs = []
    objs2 = []
    input1 = "smi_superset_"+str(season)+"_1.txt"

    for i in range(1, 26):
        input2 = "smi_superset_"+str(season)+"_"+str(i)+".txt"

        with open(input2, 'rb') as smi_data:
            objs = pickle.load(smi_data)

        with open(input1, 'rb') as standard:
            objs2 = pickle.load(standard)

        objs2 = objs2 + objs

        with open(input1, 'wb') as standard:
            pickle.dump(objs2, standard)




if __name__ == "__main__":
    main()
