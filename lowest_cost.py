import json

class lowest_cost(team, tasks):

    def __init__(self, team, tasks):
        self.team = self.read_json(team)
        self.tasks = self.read_json(tasks)
        
    #this method reads a json file and stores it in an variable, it will return a json string
    def read_json(self,json_file):
        with open('team.json') as f:
            json_string = json.load(f)
        f.close()
        return json_string
          
    

    
        
    


    
