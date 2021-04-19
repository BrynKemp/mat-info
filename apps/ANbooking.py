import re
from apps.snomedfind import retrievecoding
from re import search
import datetime as dt
from dateutil.parser import parse
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd


def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid  # key found

    return low

def findKClosestElements(arr, x, k):
    # find the insertion point using the binary search algorithm
    i = binarySearch(arr, x)
    left = i - 1
    right = i
    # run `k` times
    while k > 0:
        # compare the elements on both sides of the insertion point `i`
        # to get the first `k` closest elements
        if left < 0 or (right < len(arr) and abs(arr[left] - x) > abs(arr[right] - x)):
            right = right + 1
        else:
            left = left - 1
        k = k - 1
    # return `k` closest elements
    return arr[left + 1: right]


def getCentile(gender, weight, gaww):

    weights = pd.read_csv(r'Z:/2019/weightcentiles.csv')
    row = weights.index[weights['GA']==gaww][0]
    centiles = [0, 0.4, 2, 9, 25, 50, 75, 91, 98, 99.6, 100]
    cent = 'normal'

    if gender == 'female':
        tempc = findKClosestElements((weights.iloc[row, 1:12] * 1000), weight, 2)
        idx1 = float(((tempc[:].index)[0])[1:])
        idx2 = float(((tempc[:].index)[1])[1:])
        if max(idx1, idx2) <10 and min(idx1, idx2) >3:
            cent = 'sga10'
        if max(idx1, idx2) < 3 and min(idx1, idx2) > 0:
            cent = 'sga3'
        if min(idx1, idx2) > 97:
            cent = 'lfd97'

    elif gender == 'male':
        tempc = findKClosestElements((weights.iloc[row, 12:23] * 1000), weight, 2)
        idx1 = float(((tempc[:].index)[0])[1:])
        idx2 = float(((tempc[:].index)[1])[1:])
        if max(idx1, idx2) < 10 and min(idx1, idx2) > 3:
            cent = 'sga10'
        if max(idx1, idx2) < 3 and min(idx1, idx2) > 0:
            cent = 'sga3'
        if min(idx1, idx2) > 97:
            cent = 'lfd97'

    return cent

class delivery:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self):
        """ Create a new point at the origin """
        self.ga = 0
        self.deldate = ''
        self.delmode = ''
        self.lablength = 0
        self.babygender = 0
        self.babyweight = 0
        self.centile = 0
        self.labanal = ''
        self.delhospital = ''
        self.deloutcome = 0
        self.placenta = ''
        self.perineum = ''
        self.comment = ''


class problem:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self):
        """ Create a new point at the origin """
        self.date = ''
        self.name = ''
        self.snomed = ''
        self.pterms = ''


class procedure:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self):
        """ Create a new point at the origin """
        self.date = ''
        self.name = ''
        self.snomed = ''
        self.pterms = ''


anbooking = """
Personal Information 
Midwifery Team :   Rose
Maternity Booking History Obtained By :   Kemp , Bryn
1st Antenatal Assessment Date :   02/11/1995 WET 
Continuity of Carer Indicator :   No 
Later Booking :   No 
Staff Type First Contact :   General Medical Practitioner 
First Contact With NHS :   No 
NHS First Contact Date :   01/10/1995 BST 
Maternity Personal Info Provided By :   Woman 
Partnership :   Heterosexual Partnership 
Named Midwife :   Smith, Emma 
Born in United Kingdom :   Yes 
Woman Understands English :   Yes 
First Language :   English 
Difficulties Reading/Writing English :   No 
Woman Considers Herself to Be Disabled :   None 
Occupation :   Teacher 
Employment Status :   Part Time Paid 
Current Accommodation :   Permanent Accommodation - Own Home 
Kemp , Bryn - 02/11/1995 12:17 WET 
Height/Weight/Allergy 
Height/Length Measured :   169 cm(Converted to: 5 ft 7 in, 6 ft, 67 in)  
Weight Measured :   82 kg(Converted to: 180 lb 12 oz, 82,000 g, 181 lb, 2,892 oz)  
Body Mass Index Measured :   28.71 kg/m2 
Kemp , Bryn - 02/11/1995 12:17 WET 
(As Of: 02/11/1995 12:56:15 WET) 
Allergies (Active)
NKA 
Estimated Onset Date:   Unspecified ; Created By:   Kemp , Bryn; Reaction Status:   Active ; Category:   Drug ; Substance:   NKA ; Type:   Allergy ; Updated By:   Kemp , Bryn; Reviewed Date:   02/11/1995 12:23 WET
 

Husband/Partner's Information 
Woman able to provide info about Partner :   Yes 
Husband/Partner is Close Relative :   No 
Relationship to Husband/Partner :   Not Related 
Is Husband/ Partner the Baby's Father :   Yes 
Husband/Partner's Name :   Steven Jones 
Husband/Partner's DOB :   25/02/1977 WET 
Where was the biological father born? :   America - New York
Date arrived in the UK :   01/01/2006 WET date
Husband/Partner's Employment Status :   Full Time Paid 
Is the Husband/Partner living at the same address? :   Yes 
Husband/Partner's Occupation :   Senior Developer 
Kemp , Bryn - 02/11/1995 12:17 WET 
Obstetric History 
What is your Previous Pregnancy History? :   P1 SVD IOL for Sepsis 
Kemp , Bryn - 02/11/1995 12:17 WET 
Pregnancy History 
(As Of: 02/11/1995 12:56:15 WET) 
Gravida - 2, Para Fullterm - 1, Para Preterm - , Abortions - , Para Living - 1 
 
Delivery/Outcome Date: 03/06/2014 
 Gestation Age At Birth:   42 Weeks 0 Days ; Full Gestation ;  Delivery Method:   Spontaneous Vaginal Delivery ; Labor Duration:   36 hrs 0 mins ; Gender:   Male ; Birth Weight:   6lb 0oz / 2722g ; Anesthesia:   Epidural ; Delivery Hospital:   Hospital ; Neonate Outcome:   Live Birth ; Child Name:   James; Father Name:   Will ; Comment:   Sepsis in Labour - Johah In SCBU post delivery
 
"""
#############################################    Local Functions   #####################################################

anbooking2 = """
        Maternity Antenatal Booking Assessment Entered On:  02/11/1995 12:56 WET 
        Performed On:  02/11/1995 12:17 WET by Kemp , Bryn  
        Personal Information 
        Midwifery Team :   Rose
        Maternity Booking History Obtained By :   Kemp , Bryn
        1st Antenatal Assessment Date :   02/11/1995 WET 
        Continuity of Carer Indicator :   No 
        Later Booking :   No 
        Staff Type First Contact :   General Medical Practitioner 
        First Contact With NHS :   No 
        NHS First Contact Date :   01/10/1995 BST 
        Maternity Personal Info Provided By :   Woman 
        Partnership :   Heterosexual Partnership 
        Named Midwife :   Smith, Emma 
        Born in United Kingdom :   Yes 
        Woman Understands English :   Yes 
        First Language :   English 
        Difficulties Reading/Writing English :   No 
        Woman Considers Herself to Be Disabled :   None 
        Occupation :   Teacher 
        Employment Status :   Part Time Paid 
        Current Accommodation :   Permanent Accommodation - Own Home 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        Height/Weight/Allergy 
        Height/Length Measured :   169 cm(Converted to: 5 ft 7 in, 6 ft, 67 in)  
        Weight Measured :   82 kg(Converted to: 180 lb 12 oz, 82,000 g, 181 lb, 2,892 oz)  
        Body Mass Index Measured :   28.71 kg/m2 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        (As Of: 02/11/1995 12:56:15 WET) 
        Allergies (Active)
        NKA 
        Estimated Onset Date:   Unspecified ; Created By:   Kemp , Bryn; Reaction Status:   Active ; Category:   Drug ; Substance:   NKA ; Type:   Allergy ; Updated By:   Kemp , Bryn; Reviewed Date:   02/11/1995 12:23 WET
         
        
        Husband/Partner's Information 
        Woman able to provide info about Partner :   Yes 
        Husband/Partner is Close Relative :   No 
        Relationship to Husband/Partner :   Not Related 
        Is Husband/ Partner the Baby's Father :   Yes 
        Husband/Partner's Name :   Steven Jones 
        Husband/Partner's DOB :   25/02/1977 WET 
        Where was the biological father born? :   America - New York
        Date arrived in the UK :   01/01/2006 WET date
        Husband/Partner's Employment Status :   Full Time Paid 
        Is the Husband/Partner living at the same address? :   Yes 
        Husband/Partner's Occupation :   Senior Developer 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        
        Obstetric History 
        What is your Previous Pregnancy History? :   P1 SVD IOL for Sepsis 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        Pregnancy History 
        (As Of: 02/11/1995 12:56:15 WET) 
        Gravida - 2, Para Fullterm - 2, Para Preterm - , Abortions - , Para Living - 2 
         
        Delivery/Outcome Date: 03/06/2014 
         Gestation Age At Birth:   42 Weeks 0 Days ; Full Gestation ;  Delivery Method:   Spontaneous Vaginal Delivery ; Labor Duration:   36 hrs 0 mins ; Gender:   Male ; Birth Weight:   6lb 0oz / 2722g ; Anesthesia:   Epidural ; Delivery Hospital:   Hospital ; Neonate Outcome:   Live Birth ; Child Name:   James; Father Name:   Will ; Comment:   Sepsis in Labour - Johah In SCBU post delivery
         
        Delivery/Outcome Date: 28/03/2019 
         Gestation Age At Birth:   37 Weeks 0 Days ; Full Gestation ;  Delivery Method:   Spontaneous Vaginal Delivery ; Labor Duration:   12 hrs 14 mins ; Gender:   Male ; Birth Weight:   6lb 0oz / 2722g ; Anesthesia:   Epidural ; Delivery Hospital:   Hospital ; Neonate Outcome:   Live Birth ; Child Name:   James; Father Name:   Will ; Comment:   Sepsis in Labour - Johah In SCBU post delivery
         
        
        Problem & Diagnosis 
        (As Of: 02/11/1995 12:56:15 WET) 
        Problems(Active)  
        Pregnancy (SNOMED CT
        :429859012 ) 
        Name of Problem:   Pregnancy ; Onset Date:   01/09/1995 ; Recorder:   CMIS , Migrated Record; Confirmation:   Confirmed ; Code:   429859012 ; Last Updated:   30/10/1995 18:37 WET ; Life Cycle Status:   Active ; Responsible Provider:   CMIS , Migrated Record; Vocabulary:   SNOMED CT
         ; Comments:   
        
            30/10/1995 18:37 - CMIS , Migrated Record
        This woman's record with MRN No. 5127914  has been migrated from CMIS on 30 October 1995 18:37
         
        
        Diagnoses(Active)  
        Headache 
        Date:   02/11/1995 ; Diagnosis Type:   Working ; Confirmation:   Confirmed ; Clinical Dx:   Headache ; Classification:   No Flag ; Clinical Service:   Non-Specified ; Code:   SNOMED CT ; Probability:   0 ; Diagnosis Code:   41990019
         
        
        Procedure History 
          
         -  
        Procedure History 
        (As Of: 02/11/1995 12:56:15 WET) 
         
        Procedure Dt/Tm:   04/06/2015 12:33:00 BST ; Provider:   Longfield, Jane; Anesthesia Minutes:   0 ; Procedure Name:   Large loop excision of transformation zone ; Procedure Minutes:   0 ; Clinical Service:   Non-Specified
         
         
         
        Procedure Dt/Tm:   04/06/2015 12:33:00 BST ; Provider:   Longfield, Jane; Anesthesia Minutes:   0 ; Procedure Name:   Colposcopy of cervix ; Procedure Minutes:   0 ; Clinical Service:   Non-Specified
         
         
        
        Medication History 
        Medication List 
        (As Of: 02/11/1995 12:56:15 WET) 
        
        
        Blood Transfusion 
        Transfusion History :   No prior transfusion 
        Blood Transfusion Acceptable to Patient :   Yes 
        Consultant Referral Required? :   No 
        Anaesthetist Referral Required? :   No 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        Mental Health Status 
        Present Mental Health Illness :   No 
        Past Mental Health Illness :   Yes 
        Past Mental Health Illness Details :   Depression as teenager/twentities - medicated 
        Past Mental Health Agencies :   GP 
        Family Mental Health History :   No 
        Emotional Well-being :   No Concerns 
        Feeling Down, Depressed, Hopeless :   Not at all 
        Little Interest in Doing Things :   Not at all 
        Worrying/Feeling Anxious about Things :   No 
        Any Thoughts of Self Harm Recently :   No 
        Does Patient Need/Want Help :   No 
        GAD7 assessment needed :   No 
        Is a consultant referral required? :   No 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        Smoking / Alcohol Details 
        Are you able to perform CO Monitoring? :   No 
        Unable to perform Carbon Monoxide Comments :   Virtual booking 
        Smoking Status Mother at Booking :   Never Smoked 
        Lives with Someone Who Smokes :   No 
        Alcohol Units at Booking Per Week :   0  
        Alcohol Comments :   No Concenrs about Will and alcohol 
        Alcohol Referral Required? :   No 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        Substance Use 
        Substance Misuse Grid 
        Substance Misuse Status :   
        Never Used  
          
          
          
         
        Kemp , Bryn - 02/11/1995 12:17 WET 
        
        
        
        
        Social History 
        Support Status :   Full support of Partner 
        Number of People in Household :   2  
        Number of Adults in Household :   2  
        Number of Child in Household :   1  
        Safeguarding Concerns :   No 
        Routine Enquiry Completed :   Yes 
        Presence of Domestic Abuse :   No 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        Family History 
        Family History Grid 
        Childhood Hearing Loss :   Mother's Family 
        (Comment: Maternal father  [Kemp , Bryn - 02/11/1995 12:17 WET] ) 
        Diabetes :   Mother's Family 
        (Comment: Sister Gestational diabetes [Kemp , Bryn - 02/11/1995 12:17 WET] ) 
        Hypertension :   Mother's Family 
        (Comment: Maternal Father & Mother [Kemp , Bryn - 02/11/1995 12:17 WET] ) 
        Learning Difficulties :   Mother's Family 
        (Comment: Brother Aspergers [Kemp , Bryn - 02/11/1995 12:17 WET] ) 
        Mental Health Disorders :   Baby's Biological Father's Family 
        (Comment: Paternal mother depression historically [Kemp , Bryn - 02/11/1995 12:17 WET] ) 
        Multiple Fetal Pregnancy :   Mother's Family 
        (Comment: Maternal side [Kemp , Bryn - 02/11/1995 12:17 WET] ) 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        Does Husband/Partner have any Mental Health Issues :   No 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        Social Worker Information 
        Current Social Worker :   No 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        Antenatal Screening 
        EWS Category 
        Haemoglobin Test :   Offered and accepted 
        ABO Blood Group Test :   Offered and accepted 
        Rhesus Antibodies Test :   Offered and accepted 
        Hepatitis B Antigen Test :   Offered and accepted 
        Syphilis Test :   Offered and accepted 
        HIV Test :   Offered and accepted 
        Urine for Asymptomatic Bacteriuria :   Offered and accepted 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        Ultrasound and Blood Tests Grid 
        Dating Scan :   Offered and accepted 
        Anomaly Scan :   Offered and accepted 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        Haemoglobinopathy Test :   Offered and considering 
        Downs Syndrome Screening :   Offered and considering 
        Edwards' and Patau Syndromes Screening :   Offered and considering 
        Screening Information Shared :   Yes 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        Additional Screening at Booking assessment 
        Folic Acid Pre-pregnancy :   Taking Once Pregnancy Confirmed 
        Women/Partner from TB high R Countries :   No 
        Aspirin Recommended :   No 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        Female Genital Mutilation 
        Pregnancy Status :   Yes, unconfirmed 
        Patient had Mutilation to Genital Area :   No 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        Antenatal VTE 
        Antenatal Pre Existing/ Medical Factors :   Age over 35 years 
        Obstetric VTE Risk Factors :   None 
        Antenatal Sum :   7  
        Transient VTE Risk Factors :   None 
        Antenatal VTE Score :   Low risk 
        VTE Management Plan :   Low risk
         
        Kemp , Bryn - 02/11/1995 12:17 WET 
        Antenatal Information 
        Care Plan Type :   Antenatal Care Plan 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        Antenatal Information Grid 
        Pregnancy Care :   Yes 
        Antenatal Tests Discussed :   Yes 
        Place of Birth Discussed :   Yes 
        Flu Vaccinations Discussed :   Yes 
        Sharing of Contact Numbers Discussed :   Yes 
        Personalised Care Plan Discussed :   Yes 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        Risk Assessment 
        Antenatal Medical Factors :   None 
        Previous Obstetric History :   None 
        Antenatal Current Factors :   None 
        Antenatal gateway sum :   0  
        Antenatal Gateway Result :   Standard 
        Maternity Care Pathway :   Midwifery led care 
        Intended Place of Delivery :   NHS Alongside Midwifery Unit 
        Care Plan Type :   Antenatal Care Plan 
        Intended Delivery Location :   Royal Berkshire NHS Foundation Trust 
        Home Birth Team Referral Required? :   No 
        Consultant Referral Required? :   No 
        Anaesthetist Referral Required? :   No 
        Midwife Consultant Referral Required? :   No 
        Kemp , Bryn - 02/11/1995 12:17 WET 
        
        

"""

#############################################    Local Functions   #####################################################

bookinglist = anbooking.splitlines()
bookinglist2 = anbooking2.splitlines()

# trim white space
for i in range(len(bookinglist2)):
    bookinglist2[i] = (bookinglist2[i]).lstrip()
# remove empty lines
bookinglist2 = [x for x in bookinglist2 if len(x.strip()) > 0]

today = dt.date.today()

# Gestational age from EDD
edd_str = "04/04/2021"
edd = parse(edd_str, dayfirst=True)
edd = edd.date()

ga_today = 280 - (edd - today).days
gaw = ga_today // 7
gad = ga_today - gaw * 7

if gad == 1:
    ga_str = 'GA = %d weeks + %d day' % (gaw, gad)
elif gad == 0:
    ga_str = 'GA = %d weeks' % (gaw)
elif gad > 1:
    ga_str = 'GA = %d weeks + %d days' % (gaw, gad)

# Maternal age from DOB
dob_str = "30/05/1980"
dob = parse(dob_str, dayfirst=True)
dob = dob.date()
bdstr = (str(dob.day) + '/' + str(dob.month) + '/' + str(today.year))
bd = parse(bdstr, dayfirst=True)
bd = bd.date()

if (today - bd).days >= 0:
    age = today.year - dob.year
else:
    age = today.year - (dob.year + 1)


def get_items(str_lookup):
    bookinglist = anbooking2.splitlines()
    bookinglist = [x for x in bookinglist if len(x.strip()) > 0]
    for i in range(len(bookinglist)):
        bookinglist[i] = (bookinglist[i]).lstrip()
    itemvar = []
    for i in range(len(bookinglist)):
        if str_lookup in bookinglist2[i]:
            itemvar.append(i)
    return itemvar


def get_obshistory(obshx_temp):
    term = re.search('Para Fullterm -(.*?),', obshx_temp).group(1).strip()
    if term == '':
        term = 0
    else:
        term = int(term)

    preterm = re.search('Para Preterm -(.*?),', obshx_temp).group(1).strip()
    if preterm == '':
        preterm = 0
    else:
        preterm = int(preterm)

    termalive = (obshx_temp.split("Living -", 1)[1]).strip()
    if termalive == '':
        termalive = 0
    else:
        termalive = int(termalive)

    childloss = term - termalive

    obs_return = {
        'term': term,
        'preterm': preterm,
        'termalive': termalive,
        'rip': childloss
    }
    return obs_return


# Booking Date

lookupstrings = {
    'date_booking': '1st Antenatal Assessment Date',
    'latebooker': 'Later Booking',
    'mstatus': 'Partnership',
    'english_understands': 'Woman Understands English',
    'english_muttersprache': 'First Language',
    'disability': 'Herself to be Disabled',
    'occupation': 'Occupation',
    'employed': 'Employment Status',
    'height': 'Height/Length Measured',
    'weight': 'Weight Measured',
    'father_name': 'Husband/Partner\'s Name',
    'obshx_string': 'What is your Previous Pregnancy History?',
    'gravid_string': 'Gravida'
                     ''
}

obshx_temp = bookinglist2[get_items('Gravida')[0]]
deliveries = get_obshistory(obshx_temp)
parity = deliveries['term'] + deliveries['preterm']
delrows = get_items("Delivery/Outcome")
deldetailrows = [x + 1 for x in delrows]

temp1 = get_items('1st Antenatal Assessment Date')
temp2 = temp1[0]
bookingdate = (((bookinglist2[temp2]).split(":", 1)[1]).strip())[0:10]

height = re.search('Height/Length Measured :(.*?) cm', anbooking2).group(1).strip()
if height == '':
    height = 0
else:
    height = int(height)

weight = re.search('Weight Measured :(.*?) kg', anbooking2).group(1).strip()
if weight == '':
    weight = 0
else:
    weight = int(weight)

if weight != 0 and height != 0:
    bmi = weight / ((height / 100) ** 2)
else:
    bmi = 0

temp1 = get_items('Woman Understands English')
temp2 = temp1[0]
english_u = ((bookinglist2[temp2]).split(":", 1)[1]).strip()

temp1 = get_items('First Language :')
temp2 = temp1[0]
first_language = ((bookinglist2[temp2]).split(":", 1)[1]).strip()

for k in range(parity):
    exec(f'del_{k} = delivery()')

for k in range(len(delrows)):
    temp = bookinglist2[delrows[k]]
    temp2 = (temp.split(":", 1)[1]).strip()[0:10]
    exec(f'del_{k}.deldate = temp2')

    temp = bookinglist2[deldetailrows[k]]

    gaww = re.search('Gestation Age At Birth:(.*?) Weeks', temp).group(1)
    gaww = int(gaww.strip())
    gad = re.search('Weeks(.*?) Days', temp).group(1)
    gad = int(gad.strip())
    gadd = gaww * 7 + gad
    exec(f'del_{k}.ga = gadd')

    delm = re.search('Delivery Method:(.*?) ;', temp).group(1)
    delm = delm.strip()
    exec(f'del_{k}.delmode = delm')

    dels = re.search('Gender:(.*?) ;', temp).group(1)
    dels = delm.strip()
    exec(f'del_{k}.babygender = dels')

    delo = re.search('Neonate Outcome:(.*?) ;', temp).group(1)
    delo = delo.strip()
    exec(f'del_{k}.deloutcome = delo')

    delh = re.search('Delivery Hospital:(.*?) ;', temp).group(1)
    delh = delh.strip()
    exec(f'del_{k}.delhospital = delh')

    delw = re.search('Birth Weight:(.*?) ;', temp).group(1)
    delw = delw.strip()
    delw = (delw.split("/", 1)[1]).strip()
    delw = (delw.split("g", 1)[0]).strip()
    exec(f'del_{k}.babyweight = delw')

    delanal = re.search('Anesthesia:(.*?) ;', temp).group(1)
    delanal = delanal.strip()
    exec(f'del_{k}.labanal = delanal')

    delc = (temp.split("Comment:", 1)[1]).strip()
    delc = delc.strip()
    exec(f'del_{k}.comment = delc')

    lhrs = re.search('Labor Duration:(.*?) hrs', temp).group(1)
    lhrs = int(lhrs.strip())
    lmin = re.search('hrs(.*?) mins', temp).group(1)
    lmin = int(lmin.strip())
    lmmm = lhrs * 60 + lmin
    exec(f'del_{k}.lablength = lmmm')

# Medical History

lookuptemp1 = (get_items('Diagnoses(Active)'))[0]
lookuptemp2 = lookuptemp1 + 1
testrow = lookuptemp2
problem_row = []
problem_num = 0
procedure_num = 0

while bookinglist2[testrow].find("Procedure History") == -1 and bookinglist2[testrow].find("") == 0:
    problem_row.append(testrow)
    problem_num += 1
    testrow += 2

for k in range(len(problem_row)):
    trow = problem_row[k] + 1
    tproblem = problem()
    tproblem.date = re.search('Date:(.*?) ;', bookinglist2[trow].strip()).group(1).strip()
    tproblem.name = re.search('Clinical Dx:(.*?) ;', bookinglist2[trow].strip()).group(1).strip()
    tproblem.pterms, tproblem.snomed = retrievecoding(tproblem.name)
    exec(f'problem{k} = tproblem')

procedure_num = get_items('Procedure Dt/Tm')

for k in range(len(procedure_num)):
    prow = procedure_num[k]
    tprocedure = procedure()
    tprocedure.date = re.search('Dt/Tm:(.*?) ;', bookinglist2[prow].strip()).group(1).strip()[:10]
    tprocedure.name = re.search('Procedure Name:(.*?) ;', bookinglist2[prow].strip()).group(1).strip()
    tprocedure.pterms, tprocedure.snomed = retrievecoding(tprocedure.name)
    exec(f'procedure{k} = tprocedure')

bloodproducts = get_items('Blood Transfusion Acceptable to Patient :')[0]
blood_accept = ((bookinglist2[bloodproducts]).split("to Patient :", 1)[1]).strip()

# Substance use
temp = get_items('Smoking Status Mother at Booking :')[0]
smokingstatus = ((bookinglist2[temp]).split("Mother at Booking :", 1)[1]).strip()
temp = get_items('Lives with Someone Who Smokes :')[0]
smokehousestatus = ((bookinglist2[temp]).split("Someone Who Smokes :", 1)[1]).strip()

# Mental health
temp = get_items('Present Mental Health Illness :')[0]
mentalhealth_current = ((bookinglist2[temp]).split("Health Illness :", 1)[1]).strip()
temp = get_items('Past Mental Health Illnesss :')[0]
mentalhealth_past = ((bookinglist2[temp]).split("Health Illness :", 1)[1]).strip()
temp = get_items('Past Mental Health Illness Details :')[0]
mentalhealth_comment = ((bookinglist2[temp]).split("Illness Details :", 1)[1]).strip()

# Family History
fh_start = get_items('Family History Grid')[0]
fh_end = get_items('Social Worker Information')[0]

## Diabetes
diabetes = get_items('Diabetes')
diabetes.append(diabetes[:][0] + 1)
diabetes_fhx = []
diabetes_fdegree = 0

for i in range(len(diabetes)):
    if fh_end > diabetes[i] > fh_start:
        diabetes_fhx.append(bookinglist2[diabetes[i]])

family = ["mother ", "father ", "sister ", "brother ", "son ", "daughter ", "Mother ", "Father ", "Sister ", "Brother ",
          "Son ", "Daughter "]
for j in range(len(diabetes_fhx)):
    for k in range(len(family)):
        if diabetes_fhx[j].count(family[k]) > 0:
            diabetes_fdegree = 1

## PET
pet_fhx = 0
pet = []
if get_items('pre-eclampsia') != [] and fh_end > get_items('pre-eclampsia') > fh_start:
    pet.append(get_items('pre-eclampsia'))
if get_items('eclampsia') != [] and fh_end > get_items('eclampsia') > fh_start:
    pet.append(get_items('eclampsia'))
if get_items('eclamptic') != [] and fh_end > get_items('eclamptic') > fh_start:
    pet.append(get_items('eclamptic'))
if get_items('pet') != [] and fh_end > get_items('pet') > fh_start:
    pet.append(get_items('pet'))
if get_items('PET') != [] and fh_end > get_items('PET') > fh_start:
    pet.append(get_items('PET'))
if get_items('HELLP') != [] and fh_end > get_items('HELLP') > fh_start:
    pet.append(get_items('HELLP'))

pet = [item for sublist in pet for item in sublist]
if pet:
    pet_fhx = 1

#
# query_str = 'geatatieonal diabetes - diet'
# dm_match = []
#
# for a in range(len(d_dm)):
#     temp = fuzz.WRatio(query_str, d_dm[a + 1])
#     dm_match.append(temp)
