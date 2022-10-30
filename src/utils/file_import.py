import csv

def import_csv(path_csv):
    """ 
    Reads the CSV file in the provided path
    Args: 
        path_csv: the csv file path
    Returns:
    A list of lists that contains the data from the CSV file 
 
    """
    with open(path_csv,"r") as csvfile:
        data=[]
        csvreader=csv.reader(csvfile,delimiter=",")
        next(csvreader)
        for row in csvreader:
            data.append(row)
    return data


