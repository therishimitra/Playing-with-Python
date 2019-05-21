from urllib import request


def downloader():
    url = input("URL of CSV file to be fetched:")  # 'http://www.etcs.ipfw.edu/~moor/128Lab/ResourceFiles/walk2.csv'

    response= request.urlopen(url)

    csv = response.read()
    csv_str=str(csv)

    lines = csv_str.split('\\n')

    fw= open('datafile.csv','w')

    for line in lines:
        fw.write(line+'\n')

    fw.close()


downloader()