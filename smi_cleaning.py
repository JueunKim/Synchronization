# 2. Data cleaning for .smi
# remove unnecessary lines, <br> tag
import sys

def main():

    #Encoding Unicode to UTF-8
    reload(sys)
    sys.setdefaultencoding("utf-8")
    for i in range(1,26):
        if i <= 9:
            input_file_name = "friends.s06e0"+str(i)+".uncut.dvdrip.xvid-saints-english.smi"
            print input_file_name
        if i > 9:
            input_file_name = "s06_e"+str(i)+"_smi.txt"
            print input_file_name

        output_file_name = "s06_e"+str(i)+"_smi.txt"

        # output_file_name = "s06_e2_smi.txt"

        f_out = open(output_file_name, 'w')

        with open(input_file_name) as f_in:
            # remove blank lines
            lines = filter(None, (line.rstrip() for line in f_in))

            # remove unnecessary lines and write it to a new file
            for idx, line in enumerate(lines):
                if input_file_name.endswith('.smi'):
                    if line.startswith('-->') or line.startswith('</') or line.startswith('<body>') or line.startswith('<head>') or line.startswith('<title>'):
                        continue
                    # Merge two lines that were distinguished by a '<br>' tag
                    if line.endswith('<br>'):
                        line = line[:-4]
                        line = line + ' '
                        f_out.write(line)
                        continue
                    # split into two caption
                    if line.startswith('-'):
                        line = "\n" + lines[idx + 1] + "\n" + lines[idx - 2] + "\n" + line.replace("-", "<p class=KRCC>")
                        # f_out.write(line)
                        # print line
                    f_out.write(line + '\r\n')

        f_in.close()
        f_out.close()

if __name__ == "__main__":
    main()