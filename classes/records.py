def checkRecord():
    # Open the record file
    recordFile = open("records.txt","r")
    
    # Read lines
    lines = recordFile.readlines()

    # Save the data into variables
    userRecord = lines[2]
    moneyRecord = lines[3]

    if userRecord == 'noRecord' or moneyRecord == 'noRecord':
        return "Theres no records"
    else:
        return f'Record by user: {userRecord}the final money was: ${moneyRecord}'

def stablishRecord(user,record):

    # Open the record file
    with open("records.txt", "r") as recordFile:
        lines = recordFile.readlines()

    # Rewrite the file with the new content
    lines[2] = user + "\n" 
    lines[3] = str(record) + "\n" 

    # Save the file
    with open("records.txt", "w") as recordFile:
        recordFile.writelines(lines)