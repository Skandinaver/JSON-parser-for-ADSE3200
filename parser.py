import json 

# creating global lists and dictionaries
transposed_data = []
month_dict = {}
#function to group values in sets of 5
with open("95265.json") as file_stream:
    table_data = json.load(file_stream)
    month_dict = table_data["dataset"]["dimension"]["Tid"]["category"]["index"]
    counter = 0
    group = []
    for value in table_data["dataset"]["value"]:
        
        if counter == 5:
            transposed_data.append(group)
            group = []
            counter = 0
        group.append(value)
        counter += 1 

inv_month = {v: k for k, v in month_dict.items()}

""" Function to write the grouped values under relevant headers
adds the month data in front """

with open("processed data.csv", "w+") as writer:
    writer.write("Month,Enterprise bankruptcies,Personal bankruptcies,Forced sales in real estate,Forced sales in movables,Reg. execution proceedings\n")
    month_counter = 0
    for group in transposed_data:
        write_string = ""
        write_string =inv_month[month_counter]
        month_counter +=1
        for value in group:
            write_string += f",{value}"
        writer.write(write_string+"\n")
        


