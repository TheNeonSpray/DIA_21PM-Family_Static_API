
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7,13,22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10,14,3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] = self._generateId()
        member["last_name"] = self.last_name
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        eliminado = False
        for member in self._members:
            if member["id"] == id: 
                self._members.remove(member)
                eliminado = True
        return eliminado

## loop the list and replace the member with the given id
        #recorro la lista
        # "x" se refiere al objeto al que quiero cambiar
        # El "member" después del = se refiere al member que recibo como parametro

        #En caso de la manera actual en funcionamiento, "x" es el objeto, ".update es un método/función" y "(member)" es el parámetro que recibo.
    def update_member(self, id, member):
        modificado = False
        for x in self._members:
            if x["id"] == id: 
                x.update(member)
                modificado = True
            #    x["first_name"] = member["first_name"]
            #    x["age"] = member["age"]
            #    x["lucky_numbers"] = member["lucky_numbers"]
            
        return modificado

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id: 
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
