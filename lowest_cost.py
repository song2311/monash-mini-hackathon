import json

class lowest_cost:

    def __init__(self, team, tasks):
        self.__team = self.read_json(team)
        self.__tasks = self.read_json(tasks)
        self.qualified=[];
        
    #this method reads a json file and stores it in an variable, it will return a json string
    def read_json(self,json_file):
        with open('team.json') as f:
            json_string = json.load(f)
        f.close()
        return json_string


    def find_qualified(self):
        task=self.__team[0]['Skills']
        print(task)
        for skill in task:
            print(task[skill])

    
        
    


    
