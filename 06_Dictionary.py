# Disctionary Data Type

# Key = Value
# Name = Server
# env = dev
# "us-east-1" : ["us-east-1a", "us-east-1b", "us-east-1c"]
# "us-west-1" : ["us-west-1a", "us-west-1b", "us-west-1c"]

"""
data = {"Name" : "Server", "env" : "dev"}
print(type(data))



data = {"us-east-1": ["us-east-1a", "us-east-1b", "us-east-1c"],
        "us-west-1": ["us-west-1a", "us-west-1b", "us-west-1c"],
        "us-southeast-1": "us-southeast-1a",
        20: "Twenty"}

print(type(data["us-west-1"]))
print(data["us-west-1"])
print(data["us-southeast-1"])
print(data[20])

for az in data["us-west-1"]:
    print("Availability Zone - " + az)



data = {"us-east-1": ["us-east-1a", "us-east-1b", "us-east-1c"],
        "us-west-1": ["us-west-1a", "us-west-1b", "us-west-1c"],
        "us-southeast-1": "us-southeast-1a",
        20: "Twenty"}

print(data.keys())
print(data.values())

for key in data.keys():
    print(key)

for val in data.values():
    print(val)



emp = {"name": "RNS Tech",
       "age": 12,
        "skills": ["AWS", "DevOps", "Python"],
        "salary": "2L"}

# Adding item in dictionary
emp["address"] = ["Flat", "Street", "City", "State", "Pincode"]
#print(emp)
#print(emp["address"])

emp["age"] = 30
emp["skills"] = ["AWS", "DevOps", "Python", "Docker"]
print(emp)

for skill in emp["skills"]:
    print(skill)


# Nested dictionary

emp = {"name": "RNS Tech",
       "age": 12,
        "skills": {"DevOps": ["Git", "Ansible", "Docker"], "Cloud": ["Azure", "AWS", "GCP"]},
        "salary": "2L"}

print(emp["skills"]["Cloud"])

"""


