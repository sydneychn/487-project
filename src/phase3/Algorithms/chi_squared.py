import pandas as pd
from io import StringIO
from tabulate import tabulate
from scipy.stats import chi2_contingency

# CHI SQUARED
felonies = [
    'ROBBERY', 'RAPE', 'FELONY ASSAULT', 'ARSON', 'SEX CRIMES',
    'BURGLARY', "BURGLAR'S TOOLS", 'DANGEROUS WEAPONS',
    'OTHER OFFENSES RELATED TO THEF', 'CRIMINAL MISCHIEF & RELATED OF',
    'OFF. AGNST PUB ORD SENSBLTY &', 'POSSESSION OF STOLEN PROPERTY',
    'VEHICLE AND TRAFFIC LAWS', 'CRIMINAL TRESPASS', 'PETIT LARCENY',
    'MISCELLANEOUS PENAL LAW', 'DANGEROUS DRUGS',
    'MURDER & NON-NEGL. MANSLAUGHTE', 'ASSAULT 3 & RELATED OFFENSES',
    'OFFENSES INVOLVING FRAUD', 'OTHER TRAFFIC INFRACTION',
    'GRAND LARCENY', 'INTOXICATED & IMPAIRED DRIVING', 'FORGERY',
    'OFFENSES AGAINST PUBLIC ADMINI', 'PROSTITUTION & RELATED OFFENSES',
    'GRAND LARCENY OF MOTOR VEHICLE', 'NYS LAWS-UNCLASSIFIED FELONY',
    'OTHER STATE LAWS (NON PENAL LA', 'OFFENSES AGAINST THE PERSON',
    'FOR OTHER AUTHORITIES', 'UNAUTHORIZED USE OF A VEHICLE',
    'ALCOHOLIC BEVERAGE CONTROL LAW', 'ENDAN WELFARE INCOMP', 'FRAUDS',
    'OFFENSES AGAINST PUBLIC SAFETY', 'INTOXICATED/IMPAIRED DRIVING',
    'ANTICIPATORY OFFENSES', 'OTHER STATE LAWS', 'ADMINISTRATIVE CODE',
    'CANNABIS RELATED OFFENSES', 'THEFT-FRAUD', 'FRAUDULENT ACCOSTING',
    'GAMBLING', 'HARRASSMENT 2', 'THEFT OF SERVICES',
    'UNLAWFUL POSS. WEAP. ON SCHOOL', 'AGRICULTURE & MRKTS LAW-UNCLASSIFIED',
    'OFFENSES RELATED TO CHILDREN', 'DISORDERLY CONDUCT', 'FELONY SEX CRIMES',
    'HOMICIDE-NEGLIGENT,UNCLASSIFIE', 'KIDNAPPING & RELATED OFFENSES',
    'ESCAPE 3', 'ADMINISTRATIVE CODES', 'CHILD ABANDONMENT/NON SUPPORT',
    'MOVING INFRACTIONS', 'OTHER STATE LAWS (NON PENAL LAW)',
    'DISRUPTION OF A RELIGIOUS SERV', 'KIDNAPPING', 'PARKING OFFENSES'
]

misdemeanors = [
    'JOSTLING', 'CRIMINAL TRESPASS', 'PETIT LARCENY',
    'MISCELLANEOUS PENAL LAW', 'DANGEROUS DRUGS', 'ASSAULT 3 & RELATED OFFENSES',
    'OFFENSES AGAINST PUBLIC ADMINI', 'PROSTITUTION & RELATED OFFENSES',
    'NYS LAWS-UNCLASSIFIED FELONY', 'OTHER STATE LAWS (NON PENAL LAW)',
    'OFFENSES RELATED TO CHILDREN', 'DISORDERLY CONDUCT', 'MOVING INFRACTIONS',
    'OTHER STATE LAWS (NON PENAL LAW)', 'DISRUPTION OF A RELIGIOUS SERV',
    'PARKING OFFENSES'
]

def reassign_crime_type(crime_type):
    if crime_type in misdemeanors:
        return 'Misdemeanor'
    if crime_type in felonies:
        return 'Felony'
    

def chi_squared(crime_data):      
    output = StringIO()
    crime_data = crime_data[crime_data['PERP_SEX'] != 'U']

    contingency_table = pd.crosstab(crime_data['OFNS_DESC'].apply(reassign_crime_type), crime_data['PERP_SEX'], margins=True, margins_name='TOTAL')
    formatted_table = contingency_table.applymap(lambda x: f'{x:,.0f}' if x > 1000 else x)

    print(tabulate(formatted_table, headers='keys', tablefmt='grid'), file=output)

    chi2, p, _, _ = chi2_contingency(contingency_table)
    print(f"\nChi-square value: {chi2}",file=output)
    print(f"P-value: {p}",end=" ",file=output)

    if p < 0.05:
        print("(There is a significant association between gender and crime.)",file=output)
    else:
        print("(There is no significant association between gender and crime.)",file=output)
    return output.getvalue()
    
