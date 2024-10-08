teamMember1 = "Francis Carlo S. De Guia"
teamMember2 = "Jerby Peralta"
teamMember3 = "Nicole T. Banez"
# Team members age
age_member1 = 21
age_member2 = 20
age_member3 = 21


# Team members lengths (assuming lengths in cm for this example)
allowanceMember1 = float(1000.00)
allowanceMember2 = float(1000.00)
allowanceMember3 = float(1000.00)

teamMember1_name_Length = len(teamMember1)
teamMember2_name_Length = len(teamMember2)
teamMember3_name_Length = len(teamMember3)

#addition
ageAddition_result = age_member1 + age_member2 + age_member3
print(ageAddition_result)

#Subtraction
ageSubtraction_result = age_member1 - (age_member2 - age_member3)
print(ageSubtraction_result)

#Multiplacation
ageMulti_result = age_member1 * age_member2 * age_member3
allowanceMulti_result = allowanceMember1 * allowanceMember2 * teamMember3_name_Length
print(ageMulti_result)
print(allowanceMulti_result)

#Compare Age
print(age_member1 == age_member2)
print(age_member2 == age_member3)

#Compare length
print(teamMember1_name_Length == teamMember2_name_Length)
print(teamMember2_name_Length == teamMember3_name_Length)