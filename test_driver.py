import unittest
import json
from find_rank import find_rank

class TestCase(unittest.TestCase):
    def test_empty(self):
        find_rank_class = find_rank("./test/empty_team.json", "./test/empty_tasks.json")
        find_rank_class.run()
        self.assertTrue(len(find_rank_class.filtered_skill()) == 0)
    
    def test_rank_skill(self):
        find_rank_class = find_rank("./test/test_team.json", "./test/test_tasks.json")
        find_rank_class.run()
        self.assertTrue(find_rank_class.filtered_skill() == 
        [{'Name': 'Britta', 'Skills': {'Kafka': 2, 'Flutter': 1, 'Hazelcast': 5, 'TypeScript': 5, 'Apache Flink': 5, 'C': 2, 'BashScripting': 2, 'Apache Storm': 4, 'Java': 5}, 'Total score': 2}, 
        {'Name': 'Amelie', 'Skills': {'Kafka': 1, 'Flutter': 2, 'Hazelcast': 4, 'TypeScript': 2, 'Apache Flink': 3, 'C': 3, 'BashScripting': 4, 'Apache Storm': 5}, 'Total score': -5}, 
        {'Name': 'Arjun', 'Skills': {'Flutter': 3, 'SQL': 5, 'Hazelcast': 2, 'TypeScript': 1, 'Apache Flink': 2, 'C': 5, 'Java': 5}, 'Total score': -6}, 
        {'Name': 'Chang', 'Skills': {'Kafka': 5, 'SQL': 4, 'TypeScript': 4, 'C': 5, 'BashScripting': 1, 'Java': 3}, 'Total score': -7}, 
        {'Name': 'Natasha', 'Skills': {'Flutter': 2, 'TypeScript': 4, 'Apache Flink': 5, 'C': 3, 'BashScripting': 2, 'Apache Storm': 2}, 'Total score': -11}, 
        {'Name': 'Abed', 'Skills': {'Kafka': 1, 'Flutter': 5, 'Hazelcast': 1, 'TypeScript': 5}, 'Total score': -17}, 
        {'Name': 'Annie', 'Skills': {'Kafka': 5, 'SQL': 1, 'Hazelcast': 5}, 'Total score': -18}, 
        {'Name': 'Sam', 'Skills': {'Flutter': 3, 'C': 5, 'Java': 2}, 'Total score': -19}, 
        {'Name': 'Brandon', 'Skills': {'SQL': 3, 'TypeScript': 5}, 'Total score': -21}, 
        {'Name': 'Lee', 'Skills': {'Apache Storm': 3}, 'Total score': -26}])
        

        


if __name__ == "__main__":
    unittest.main()