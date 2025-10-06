dict1 = {'Name':'Ajay','Age':22}
dict2 = {'City':'Pune','Zip':123456}

dict1.update(dict2)

print(dict1)

nest_dict = {
    'Person' : {'Name':'Ajay','Age':22},
    'Address': {'City':'Pune','Zip':123456}
}

print(nest_dict['Person']['Name'])