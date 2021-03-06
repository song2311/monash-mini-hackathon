"""
Author: 
"""
import json
from performance import decorator
import time

class find_rank():
    total_times = []
    matching_times = []
    """
    Class constructor for find_rank
    Initializes the total_times to empty list
    Arguments:          None
    Time complexity:    Best case = O(1) time complexity
                        Worst case = O(1) time complexity
    Return: None
    """
    def __init__(self, team, tasks):
        total_times = []
        matching_times = []
        self.__call_count = 0
        self.__team = team
        self.__tasks = tasks
        self.__meet_req=[]
        self.__fail_req=[]
        self.__rank_skill=[]
        self.__rank_cost=[]
        self.__run_time = 0

    """
    Function that checks if the json file is empty after formatting it into a list  
    Arguments:          None
    Time complexity:    Best case = O(1) time complexity
                        Worst case = O(1) time complexity
    Return: true or false if the team or tasks list is empty
    """
    @decorator(total_times, matching_times, False) 
    def is_empty(self):
        return len(self.__team[0]) == 0 or len(self.__tasks[0]) == 0

    """
    Function that returns the ranks of the member by cost
    Returns an empty list if run() is not called yet 
    Arguments:          None
    Time complexity:    Best case = O(1) time complexity
                        Worst case = O(1) time complexity
    Return: List of members ranked by their cost
    """
    @decorator(total_times, matching_times, False) 
    def get_rank_cost(self):
        return self.__rank_cost

    """
    Function that returns the ranks of the member by their skills
    Returns an empty list if run() is not called yet 
    Arguments:          None
    Time complexity:    Best case = O(1) time complexity
                        Worst case = O(1) time complexity
    Return: List of members ranked by their skills
    """
    @decorator(total_times, matching_times, False) 
    def get_rank_skill(self):
        return self.__rank_skill

    """
    Function to return the list of tasks extracted from the task json file
    Arguments:          None
    Time complexity:    Best case = O(1) time complexity
                        Worst case = O(1) time complexity
    Return: the list of tasks
    """
    @decorator(total_times, matching_times, False) 
    def tasks(self):
        if self.is_empty():
            return []
        self.__call_count += 1
        return self.__tasks
               
    """
    Function that parses the json file, populate it in a dictionary and returns it
    Arguments:          json_file, the file to parse into a dictionary
    Time complexity:    Best case = O(N) time complexity
                        Worst case = O(N) time complexity
    Return: the json dictionary parsed from the json file
    """
    #this method reads a json file and stores it in an variable, it will return a json string
    @decorator(total_times, matching_times, False)
    def read_json(self,json_file):
        self.__call_count += 1
        with open(json_file) as f:
            json_string = json.load(f)
        f.close()
        return json_string
    
    """
    Function that filter skills unrelated to the tasks, and assigns them to different lists based on whether they meet the skill requirements
    A member without any skill required by a task will have an empty skill dictionary
    Arguments:          task, the task to filter with
    Time complexity:    Best case =  O(n*m), where n is the number of json elements in team json and m is the number of elements in tasks json
                        Worst case = O(n*m), where n is the number of json elements in team json and m is the number of elements in tasks json
    Return: the list of tasks
    """
    #this function will filter skills unrelated to the tasks, a member without any skill required by a task will have an empty skill dictionary
    #Worst time complexity is O(n*m), where n is the number of json elements in team json and m is the number of elements in tasks json
    @decorator(total_times, matching_times, False)
    def filter_skill(self,task):
        if self.is_empty():
            return
        self.__call_count += 1
        #empty lists before filtering skill because it is different for each task
        self.__meet_req=[]
        self.__fail_req=[]
        for member in self.__team:
            meet_req=True
            #the Skills dictionary will be empty if the member has 0 skill for the task
            member_dict={'Name':member['Name'],'Skills':{}}
            for skill in task:
                try:
                    #check if a member has the required skill
                    if member['Skills'][skill]:
                        member_dict['Skills'][skill]=member['Skills'][skill]
                    #member does not qualify for the task
                    if member['Skills'][skill]<task[skill]:
                        meet_req=False
                except KeyError:
                    #if skill cannot be found just continue
                    continue
            #only insert those that at least have all the required skills into the met_req list because those members will be higher rank than the others
            if len(member_dict['Skills'])==len(task):
                if meet_req:
                    self.__meet_req.append(member_dict)
                else:
                    self.__fail_req.append(member_dict)
            else:
                self.__fail_req.append(member_dict)
                

    """
    Function that takes in a list that contains the task and it will calculate the rank of members based on the difference of skill level requirements
    of a task and skill level of member and add them up to simulate the additional cost of a member compared to the task at hand.
    Arguments:          task, the task to check with skills of members in the team
    Time complexity:    Best case =  O(n*m), where n is the number of json elements in team json and m is the number of elements in tasks json
                        Worst case =  O(n*m), where n is the number of json elements in team json and m is the number of elements in tasks json
    Return: the list of members ranked by cost
    """
    @decorator(total_times, matching_times, True)
    def rank_by_cost(self, task):
        if self.is_empty():
            return
    
        for member in self.__meet_req:
            total_score=0
            for skill in task['Skills']:
                skill_req=task['Skills'][skill]
                skill_level=member['Skills'][skill]
                #find the balance to see how overqualified a member is in relation to the skill requirements
                total_score+=(skill_level-skill_req)
                member["Skill difference"]=total_score
        
        for member in self.__fail_req:
            total_score=0
            for skill in task['Skills']:
                try:
                    skill_req=task['Skills'][skill]
                    skill_level=member['Skills'][skill]
                    #find the absolute value because it does not matter if a member exceeds or did not meet skill level requirements, it is still not cost effective, so the difference is found out
                    #to determine the additional costs.                    total_score+=abs(skill_req-skill_level)
                except KeyError:
                    #add the skill requirements because if member does not have the skill required it will the cost to train up the member will be equivalent to the skill level requirement of the task
                    total_score+=skill_req
            member["Total score"]=total_score
        try:   
            self.__meet_req.sort(key=lambda e: e["Skill difference"])
            self.__fail_req.sort(key=lambda e: e['Total score'])
        except KeyError:
            pass
        
        self.__call_count += 1
        self.__rank_cost = self.__meet_req+self.__fail_req
        return self.__meet_req+self.__fail_req
    
    """
    Function that takes in a list that contains the task and it will calculate the rank of members based on the difference of skill level of member and skill level requirements
    of a task and add them up to find out how overqualified or underqualified is a member, members that do not have skill for a task will be deducted with the skill level requirements
    which results in a lower ranking. 
    Arguments:          task, the task to check with skills of members in the team
    Time complexity:    Best case =  O(n*m), where n is the number of json elements in team json and m is the number of elements in tasks json
                        Worst case = O(n*m), where n is the number of json elements in team json and m is the number of elements in tasks json
    Return: the list of members ranked by skill
    """
    @decorator(total_times, matching_times, True)
    def rank_by_skill(self,task):
        if self.is_empty():
            return
        for member in self.__meet_req:
            total_score=0
            for skill in task['Skills']:
                skill_req=task['Skills'][skill]
                skill_level=member['Skills'][skill]
                #find the balance to see how overqualified a member is in relation to the skill requirements
                total_score+=(skill_level-skill_req)
                member["Skill difference"]=total_score
        
        for member in self.__fail_req:
            #count the total differnce of all skill level and skill level requirements, lower means higher rank
            total_score=0
            for skill in task['Skills']:
                try:
                    skill_req=task['Skills'][skill]
                    skill_level=member['Skills'][skill]
                    #find the balance to see how overqualified/underqualified a member is in relation to the skill requirements
                    total_score+=(skill_level-skill_req)
                except KeyError:
                    total_score-=skill_req
            member["Total score"]=total_score
        try:
            #reverse sort because a higher score means better skill level
            self.__meet_req.sort(key=lambda e: e["Skill difference"],reverse=True)
            self.__fail_req.sort(key=lambda e: e['Total score'],reverse=True)
        except KeyError:
            pass
        
        self.__call_count += 1
        self.__rank_skill = self.__meet_req+self.__fail_req
        return self.__meet_req+self.__fail_req
    
    

    """
    Function that returns the number of times calls have been made in this class 
    Arguments:          None
    Time complexity:    Best case = O(1) time complexity
                        Worst case = O(1) time complexity
    Return: the number of times calls made in this class
    """
    def get_call_count(self):
        return self.__call_count

    """
    Function that returns the list of call elapsed time in milliseconds
    Arguments:          None
    Time complexity:    Best case = O(1) time complexity
                        Worst case = O(1) time complexity
    Return: the list of call elapsed time in milliseconds
    """
    def get_total_times(self):
        return find_rank.total_times

    """
    Function that performs filtering of team and tasks, 
    ranking by skill and cost of each member in the team
    and prints them out into the standard output
    Arguments:          None
    Time complexity:    Best case = 
                        Worst case = 
    Return: None
    """
    def run(self):
        open("log.txt", "w").close()
        start = time.time()
        self.__tasks = self.read_json(self.__tasks)
        self.__team = self.read_json(self.__team)
        for task in self.tasks():
            filtered_skill=self.filter_skill(task['Skills'])
            print("Tasks:",task)
            print("\nRank by skill\n")
            ranked_list=self.rank_by_skill(task)
            count=0
            for member in ranked_list:
                print("Rank",count,":",member['Name'],"Skills:",member['Skills'])
                count+=1
                
            print("\nRank by cost\n")
            ranked_list=self.rank_by_cost(task)
            count=0
            for member in ranked_list:
                print("Rank",count,":",member['Name'],"Skills:",member['Skills'])
                count+=1
            
            print("")
        end = time.time()
        self.__run_time = (end-start) * 1000

    """
    Function that logs the overall performance of the class into a text file
    Arguments:          None
    Time complexity:    Best case = O(1) time complexity
                        Worst case = O(1) time complexity
    Return: None
    """
    def log_performance(self):
        file = open("log.txt", "a+")
        file.write("-------Matching Performance-------\n")
        file.write("Mean matching call elapsed time in milliseconds : %f\n" %(sum(find_rank.matching_times) / len(find_rank.matching_times)))
        file.write("Maximum matching call elapsed time in milliseconds : %f\n" %max(find_rank.matching_times))
        file.write("Minimum matching call elapsed time in milliseconds : %f" %min(find_rank.matching_times))
        file.write("\n")
        file.write("-------Overall Performance-------\n")
        file.write("Total function calls made : %d\n" %(self.__call_count))
        file.write("Total elapsed time in milliseconds : %f\n" %(self.__run_time))
        if len(find_rank.total_times) == 0:
            file.write("Mean call elapsed time in milliseconds : 0\n")
            file.write("Maximum call elapsed time in milliseconds : 0\n")
            file.write("Minimum call elapsed time in milliseconds : 0")
        else:
            file.write("Mean call elapsed time in milliseconds : %f\n" %(sum(find_rank.total_times) / len(find_rank.total_times)))
            file.write("Maximum call elapsed time in milliseconds : %f\n" %max(find_rank.total_times))
            file.write("Minimum call elapsed time in milliseconds : %f" %min(find_rank.total_times))
        file.write("\n")
        file.close()
