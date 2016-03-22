print 'Geef uw gewicht in kg: '
gewicht_kg = float(raw_input())
print 'Geef uw lengte in meters: '
lengte_meters = float(raw_input())
bmi = gewicht_kg / (lengte_meters * lengte_meters)
if bmi <= 18.5:
print 'Je BMI is ', bmi, 'wat betekent dat je ondergewicht hebt'
elif bmi > 18.5 and bmi <= 25:
print 'Je BMI is ', bmi, 'wat betekent dat je een gezond gewicht hebt'
elif bmi > 25 and bmi < 30:
print 'Je BMI is ', bmi, 'wat betekent dat je een overgewicht hebt'
elif bmi >= 30:
print 'Je BMI is ', bmi, 'wat betekent dat je zwaar overgewicht hebt'
