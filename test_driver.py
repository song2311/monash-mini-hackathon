import unittest
import json
from find_rank import find_rank

class TestCase(unittest.TestCase):
    def test_empty(self):
        find_rank_class = find_rank("./test/empty_team.json", "./test/empty_tasks.json")
        find_rank_class.run()
        self.assertTrue(len(find_rank_class.get_rank_skill()) == 0)
    
    def test_rank1(self):
        find_rank_class = find_rank("./test/test_team.json", "./test/test_tasks.json")
        find_rank_class.run()
        self.assertTrue(find_rank_class.get_rank_skill() == 
        [{'Name': 'Britta', 'Skills': {'Kafka': 2, 'Flutter': 1, 'Hazelcast': 5, 'TypeScript': 5, 'Apache Flink': 5, 'C': 2, 'BashScripting': 2, 'Apache Storm': 4, 'Java': 5}, 'Total score': 1}, 
        {'Name': 'Amelie', 'Skills': {'Kafka': 1, 'Flutter': 2, 'Hazelcast': 4, 'TypeScript': 2, 'Apache Flink': 3, 'C': 3, 'BashScripting': 4, 'Apache Storm': 5}, 'Total score': 5}, 
        {'Name': 'Arjun', 'Skills': {'Flutter': 3, 'SQL': 5, 'Hazelcast': 2, 'TypeScript': 1, 'Apache Flink': 2, 'C': 5, 'Java': 5}, 'Total score': 6},
         {'Name': 'Chang', 'Skills': {'Kafka': 5, 'SQL': 4, 'TypeScript': 4, 'C': 5, 'BashScripting': 1, 'Java': 3}, 'Total score': 12},
          {'Name': 'Natasha', 'Skills': {'Flutter': 2, 'TypeScript': 4, 'Apache Flink': 5, 'C': 3, 'BashScripting': 2, 'Apache Storm': 2}, 'Total score': 11},
           {'Name': 'Abed', 'Skills': {'Kafka': 1, 'Flutter': 5, 'Hazelcast': 1, 'TypeScript': 5}, 'Total score': 17}, 
           {'Name': 'Annie', 'Skills': {'Kafka': 5, 'SQL': 1, 'Hazelcast': 5}, 'Total score': 22}, 
           {'Name': 'Sam', 'Skills': {'Flutter': 3, 'C': 5, 'Java': 2}, 'Total score': 16}, 
           {'Name': 'Brandon', 'Skills': {'SQL': 3, 'TypeScript': 5}, 'Total score': 26}, 
           {'Name': 'Lee', 'Skills': {'Apache Storm': 3}, 'Total score': 28}])
    
        self.assertTrue(find_rank_class.get_rank_cost() == 
        [{'Name': 'Britta', 'Skills': {'Kafka': 2, 'Flutter': 1, 'Hazelcast': 5, 'TypeScript': 5, 'Apache Flink': 5, 'C': 2, 'BashScripting': 2, 'Apache Storm': 4, 'Java': 5}, 'Total score': 1}, 
        {'Name': 'Amelie', 'Skills': {'Kafka': 1, 'Flutter': 2, 'Hazelcast': 4, 'TypeScript': 2, 'Apache Flink': 3, 'C': 3, 'BashScripting': 4, 'Apache Storm': 5}, 'Total score': 5}, 
        {'Name': 'Arjun', 'Skills': {'Flutter': 3, 'SQL': 5, 'Hazelcast': 2, 'TypeScript': 1, 'Apache Flink': 2, 'C': 5, 'Java': 5}, 'Total score': 6},
        {'Name': 'Natasha', 'Skills': {'Flutter': 2, 'TypeScript': 4, 'Apache Flink': 5, 'C': 3, 'BashScripting': 2, 'Apache Storm': 2}, 'Total score': 11}, 
        {'Name': 'Chang', 'Skills': {'Kafka': 5, 'SQL': 4, 'TypeScript': 4, 'C': 5, 'BashScripting': 1, 'Java': 3}, 'Total score': 12}, 
        {'Name': 'Sam', 'Skills': {'Flutter': 3, 'C': 5, 'Java': 2}, 'Total score': 16}, 
        {'Name': 'Abed', 'Skills': {'Kafka': 1, 'Flutter': 5, 'Hazelcast': 1, 'TypeScript': 5}, 'Total score': 17}, 
        {'Name': 'Annie', 'Skills': {'Kafka': 5, 'SQL': 1, 'Hazelcast': 5}, 'Total score': 22}, 
        {'Name': 'Brandon', 'Skills': {'SQL': 3, 'TypeScript': 5}, 'Total score': 26}, 
        {'Name': 'Lee', 'Skills': {'Apache Storm': 3}, 'Total score': 28}])
    

    
    def test_rank2(self):
        find_rank_class = find_rank("./test/test_team1.json", "./test/test_tasks1.json")
        find_rank_class.run()
        self.assertTrue(find_rank_class.get_rank_skill() == 
        [{'Name': 'Annie', 'Skills': {'MongoDB': 3}, 'Total score': 2}, 
        {'Name': 'Jack', 'Skills': {'MongoDB': 1, 'C++': 2}, 'Total score': 0}, 
        {'Name': 'Chang', 'Skills': {'C++': 2}, 'Total score': 3}])
        self.assertTrue(find_rank_class.get_rank_cost() == 
        [{'Name': 'Jack', 'Skills': {'MongoDB': 1, 'C++': 2}, 'Total score': 0}, 
        {'Name': 'Annie', 'Skills': {'MongoDB': 3}, 'Total score': 2}, 
        {'Name': 'Chang', 'Skills': {'C++': 2}, 'Total score': 3}])

    def test_rank3(self):
        find_rank_class = find_rank("./test/test_team2.json", "./test/test_tasks1.json")
        find_rank_class.run()
        self.assertTrue(find_rank_class.get_rank_skill() == 
        [{'Name': 'Annie', 'Skills': {'MongoDB': 3}, 'Total score': 2}, 
        {'Name': 'Chang', 'Skills': {'MongoDB': 2}, 'Total score': 2}, 
        {'Name': 'Jack', 'Skills': {'MongoDB': 1}, 'Total score': 2}])
        self.assertTrue(find_rank_class.get_rank_cost() == 
        [{'Name': 'Annie', 'Skills': {'MongoDB': 3}, 'Total score': 2}, 
        {'Name': 'Chang', 'Skills': {'MongoDB': 2}, 'Total score': 2}, 
        {'Name': 'Jack', 'Skills': {'MongoDB': 1}, 'Total score': 2}])

    def test_rank3(self):
        find_rank_class = find_rank("./test/test_team3.json", "./test/test_tasks1.json")
        find_rank_class.run()
        self.assertTrue(find_rank_class.get_rank_skill() == 
        [{'Name': 'Annie', 'Skills': {'MongoDB': 3, 'C++': 3}, 'Skill difference': 1}, 
        {'Name': 'Chang', 'Skills': {'MongoDB': 3, 'C++': 2}, 'Skill difference': 0}, 
        {'Name': 'Jack', 'Skills': {'MongoDB': 3, 'C++': 1}, 'Total score': 0}])
        self.assertTrue(find_rank_class.get_rank_cost() == 
        [{'Name': 'Chang', 'Skills': {'MongoDB': 3, 'C++': 2}, 'Skill difference': 0}, 
        {'Name': 'Annie', 'Skills': {'MongoDB': 3, 'C++': 3}, 'Skill difference': 1}, 
        {'Name': 'Jack', 'Skills': {'MongoDB': 3, 'C++': 1}, 'Total score': 0}])

    def test_rank4(self):
        find_rank_class = find_rank("./test/test_team4.json", "./test/test_tasks1.json")
        find_rank_class.run()
        self.assertTrue(find_rank_class.get_rank_skill() == 
        [{'Name': 'Annie', 'Skills': {'MongoDB': 3, 'C++': 3}, 'Skill difference': 1},
         {'Name': 'Chang', 'Skills': {'MongoDB': 4, 'C++': 2}, 'Skill difference': 1}, 
         {'Name': 'Jack', 'Skills': {'MongoDB': 3, 'C++': 2}, 'Skill difference': 0}])
        self.assertTrue(find_rank_class.get_rank_cost() ==
         [{'Name': 'Jack', 'Skills': {'MongoDB': 3, 'C++': 2}, 'Skill difference': 0},
          {'Name': 'Annie', 'Skills': {'MongoDB': 3, 'C++': 3}, 'Skill difference': 1}, 
          {'Name': 'Chang', 'Skills': {'MongoDB': 4, 'C++': 2}, 'Skill difference': 1}])

        

        


if __name__ == "__main__":
    unittest.main()