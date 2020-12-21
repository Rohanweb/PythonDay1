import json

strs='''
    {
        "resources": [
            
                         {
                            "name":"USD/INR",
                            "price":"0.3344"
                            }
                
        ]
    }
'''


mydata=json.loads(strs)
print(mydata)
print(mydata["resources"][0]["price"])

with open("liststates.json","r") as f:

    data=json.load(f)
    print(data)
    for item in data["states"]:
        print(item['area_codes'][0])

    for state in data["states"]:
        del state['area_codes']

    with open("newliststates.json","w") as fw:
        json.dump(data,fw,indent=2,sort_keys=True)


