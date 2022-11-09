import pandas as pd

"""
convert file json to file csv and xlsx
"""
def json_to_excel(file):
    """
    convert file json to xlsx
    """
    data = pd.read_json(file)
    df = pd.DataFrame(data)
    df.to_excel(file[:-5]+'.xlsx')

def json_to_csv(file):
    """
    convert file json to csv
    """
    pdObj = pd.read_json(file, orient='index')
    pdObj.to_csv(file[:-5]+'.csv', index=False)

file_path = "folder/test.json"

json_to_excel(file_path)
json_to_csv(file_path)

print("Success")
