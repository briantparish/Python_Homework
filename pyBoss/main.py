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

input_file = 'employee_data.csv'
output_file = 'employee_data_out.csv'
with open(input_file, encoding='utf8') as input_csv, open(output_file,'w', newline='\n') as output_csv:
    employee_data = csv.DictReader(input_csv, delimiter=",")

    fieldnames =['Emp ID','Name','First Name','Last Name','DOB','SSN','State']
    employee_writer = csv.DictWriter(output_csv,fieldnames=fieldnames)
    employee_writer.writeheader()
    next(employee_data)     
    for emp in employee_data:
        date = emp['DOB'].split("-")
        emp['DOB'] = date[1] + "/" + date[2] + "/" + date[0]
        emp['SSN'] = "xxx-xx-" + emp['SSN'].split("-")[2]
        emp['State'] = us_state_abbrev[emp['State']]
        name = emp['Name'].split(" ")
        emp['First Name'] = name[0]
        emp['Last Name'] = name[1]
        del emp['Name']        
        employee_writer.writerow(emp)
