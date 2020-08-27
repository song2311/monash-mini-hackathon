import json

class lowest_cost:

    def __init__(self, team, tasks):
        self.__team = self.read_json(team)
        self.__tasks = self.read_json(tasks)
        self.qualified=[];
        
    #this method reads a json file and stores it in an variable, it will return a json string
    def read_json(self,json_file):
        with open(json_file) as f:
            json_string = json.load(f)
        f.close()
        return json_string

    #this function will find members in the team that are qualified for the task
    def find_qualified(self):
        task=self.__tasks[0]['Skills']
        team= self.__team
        print("Tasks:",task)
        for member in team:
            for skill in task:
                qualify=False
                for mem_skill in member['Skills']:
                    if mem_skill==skill:
                        skill_level=member['Skills'][skill]
                        skill_req=task[skill]
                        #if member meets skill requirements set qualify to true and break loop
                        if skill_level>=skill_req:
                            qualify=True
                            break
                #exit loop early if member did not meet one of the skill requirements
                if qualify==False:
                    break
            #only add member to qualified list if member meets all requirements
            if qualify==True:
                member_dict={'Name':member['Name'],
                             'Skills':{}}
                for skill in task:
                    member_dict['Skills'][skill]=member['Skills'][skill]
                self.qualified.append(member_dict)
        return self.qualified
                    
            
    
        
    


    
#for skill in task:
    #prints the rank of skill
        #print(task[skill])
#for member in team:
    #print(member['Name'])
    #for skill in member['Skills']:
         #print(skill,":",member['Skills'][skill])
