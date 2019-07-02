high_income=True
good_credit=False
criminal_record=False
if high_income and good_credit:
    print('Eligible for loan')
elif good_credit and criminal_record:
    print('Work hard')
elif high_income and not criminal_record:
    print('Nice person')
else:
    print('Do something in your life')
