#!/usr/bin/python3

class LogPeople(object):
    def __init__(self, people):
        self._dicts = people[0]

    def dicts(self):
        return self._dicts

    def maxAge(self):
        return [d
                for d in sorted(self._dicts, key='age')
                if d['age'] < 25]


people = [{'name':'Reuven', 'age':47, 'hobbies':['Python', 'cooking', 'reading']},
          {'name':'Atara', 'age':16, 'hobbies':['horses', 'cooking', 'art']},
          {'name':'Shikma', 'age':14, 'hobbies':['Python', 'piano', 'cooking']},
          {'name':'Amotz', 'age':11, 'hobbies':['biking', 'cooking']}]

info = LogPeople(people)
print("dicts: {}".format(info.dicts(), ))
#print("maxAge: {}".format(info.maxAge(), ))
