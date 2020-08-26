#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    l=[]
    for i in range(0,len(patient_medical_speciality_list),2):
        l.append(patient_medical_speciality_list[i])
    i1=patient_medical_speciality_list.index(max(l))
    for  k,v in medical_speciality.items():
        if k==patient_medical_speciality_list[i1+1]:
            speciality=v
    return speciality
#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
