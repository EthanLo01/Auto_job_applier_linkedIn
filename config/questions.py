'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.29.12.30
'''


###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = r"C:\Chi\work\resume\AI Engineer_v6.docx"      # (In Development)

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience? 
years_of_experience = "2"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "No"               # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = "https://github.com/EthanLo01"                        # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/elo1729/"       # "https://www.linkedin.com/in/example" or "" and so on...

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "U.S. Citizen/Permanent Resident"



## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 150000          # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 90000            # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
# currency = "INR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 30                   # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "Full Stack Developer with Masters in Data Analysis and Visualization and 2+ years of experience" # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
AI/ML engineer with 3+ years in machine learning and NLP, specializing in Python, TensorFlow, and LLMs (RAG, prompt engineering). Experienced in JPMC LLM testing.
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Cover Letter
"""
##> ------ Dheeraj Deshwal : dheeraj9811 Email:dheeraj20194@iiitd.ac.in/dheerajdeshwal9811@gmail.com - Feature ------

# Your user_information_all letter in quotes, use \n to add line breaks if using single quotes "user_information_all".You can skip \n if using triple quotes """user_information_all""" (This question makes sense though)
# We use this to pass to AI to generate answer from information , Assuing Information contians eg: resume  all the information like name, experience, skills, Country, any illness etc. 
user_information_all ="""
### Personal Information
- Name: [Ethan Lo]  
- Contact: [ethanlowork7@gmail.com]  
- LinkedIn: https://www.linkedin.com/in/elo1729/

### Work Experience
- **Analyst - Global Fund Services Bank Loan Administration**
  - Organization: JPMorgan Chase & Co.
  - Duration: 2024/03/25 - Present
  - Location: New York City, New York
  - Details: Managed trade instruction capture, settlements, and lifecycle events for bank loan assets. Improved processing efficiency by 20% through Python and VBA automation. Collaborated with global teams to design internal LLM models for reporting.
- **Syndicated Loan Administrator**
  - Organization: First Commercial Bank, Ltd.
  - Duration: 2023/01/17 - 2024/03/22
  - Location: New York City, New York
  - Details: Oversaw 55 syndicated and 30 bilateral loans, reducing operational time by 30% with automation. Contributed to a clean 2022 FRB audit.
- **Information Technology Officer**
  - Organization: First Commercial Bank, Ltd.
  - Duration: 2022/05/09 - 2023/10/31
  - Location: New York City, New York
  - Details: Managed hardware/software systems and developed AML VBA scripts, improving monitoring efficiency by 15%. Supported 2022 FRB inspection.
- **Internship - AI and Deep Learning Application Talent Development Class**
  - Organization: Industrial Technology Research Institute
  - Duration: 2021/05 - 2021/07
  - Location: Taipei, Taiwan
  - Details: Developed deep learning models for traffic sign classification, achieving 95% accuracy with VGG19 and custom CNN. Reduced development cycle by 20%.

### Education
- **Master of Science in Data Analysis and Visualization**
  - Institution: The Graduate School and University Center of the City University of New York
  - Duration: 2022/02/01 - 2024/02/29
  - Location: New York City, New York
- **Bachelor of Business Administration**
  - Institution: National Taipei University of Business
  - Duration: 2016/09/01 - 2018/06/30
  - Location: Taipei, Taiwan
- **Associate of Management Science**
  - Institution: National Taipei University of Business
  - Duration: 2011/09/01 - 2016/06/30
  - Location: Taipei, Taiwan

### Skills
- **Technical Skills**: Proficient in Python, TensorFlow, Keras, PyTorch, SQL, VBA, Git, and AI/ML (LSTM, GRU, NLP with FinBERT, ChatGPT).
- **Data Processing**: Experienced with Matplotlib, Seaborn, Tableau, and web scraping for financial data visualization.
- **Financial Skills**: Expertise in quantitative trading, derivative prediction (E-Mini S&P 500), and syndicated loan processing using ClearPar and LSTA Par.
- **Languages**: Native Mandarin, proficient English, applied in NLP and financial communication.

### Projects
- **E-Mini S&P 500 Derivatives Price Forecasting**
  - Description: Built a stacked RNN model with 55% directional accuracy and R² of 0.912752, integrating NLP (FinBERT) and economic data.
- **Advanced Deep Learning for Traffic Sign Classification**
  - Description: Achieved 95% accuracy on a 45-class dataset using VGG19 and custom MCNN, with transferable Fintech applications.
- **Optiver Realized Volatility Prediction**
  - Description: Developed a LightGBM model for stock volatility prediction in a Kaggle competition.
- **Deep Q-learning Trading Robot**
  - Description: Implemented a DQN-based trading system in TensorFlow for automated trading.
- **The Journey of Amazon**
  - Description: Scraped Amazon Q4 2020 sales data and visualized with an interactive Tableau dashboard.
- **Interactive Options Trading Dashboard**
  - Description: Built a D3.js web application for options trading visualization.
- **Automatic Advertising Information System - Facebook**
  - Description: Designed a Python web crawler for automated Facebook ad delivery.


"""
##<
'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Name of your most recent employer
recent_employer = "JPMorgan Chase & Co" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "7"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = True         # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive







############################################################################################################
'''
THANK YOU for using my tool 😊! Wishing you the best in your job hunt 🙌🏻!

Sharing is caring! If you found this tool helpful, please share it with your peers 🥺. Your support keeps this project alive.

Support my work on <PATREON_LINK>. Together, we can help more job seekers.

As an independent developer, I pour my heart and soul into creating tools like this, driven by the genuine desire to make a positive impact.

Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

Gratefully yours 🙏🏻,
Sai Vignesh Golla
'''
############################################################################################################