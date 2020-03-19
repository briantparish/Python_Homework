import csv
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#label input and output files
input_file = 'employee_data.csv'
output_file = 'employee_data_out.csv'

#Open input reader and output writer
with open(input_file, encoding='utf8') as input_csv, open(output_file,'w', newline='\n') as output_csv:
    
    #Read input CSV file and store as a list of dictionaries
    employee_data = csv.DictReader(input_csv, delimiter=",")
    
    #Define dictionary keys for output
    fieldnames =['Emp ID','First Name','Last Name','DOB','SSN','State']
    
    #Write desired output CSV dictionary keys as header
    employee_writer = csv.DictWriter(output_csv,fieldnames=fieldnames)
    employee_writer.writeheader()
    
    for emp in employee_data:
        #split DOB by '-' to format date in different order
        date = emp['DOB'].split("-")
        emp['DOB'] = date[1] + "/" + date[2] + "/" + date[0]
        
        #remove first 5 digits of SSN and include the last 4 using split
        emp['SSN'] = "xxx-xx-" + emp['SSN'].split("-")[2]
        
        #Use state abbreviation dictionary to replace State with abbreviation
        emp['State'] = us_state_abbrev[emp['State']]
        
        #split the name by a space to seperate into first and last
        name = emp['Name'].split(" ")
        emp['First Name'] = name[0]
        emp['Last Name'] = name[1]
        
        #delete 'Name' key from dictionary
        del emp['Name']
        
        #Finally write the formatted dictionary to output csv file
        employee_writer.writerow(emp)
