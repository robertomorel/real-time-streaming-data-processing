import random

from faker import Faker
from time import sleep

fake = Faker()
filePath = '/home/rober/workspace/kafka/origem.txt'

def poll():
    while True:
        f = open(filePath, 'a')
        msg = "O(a) sr(a) '{}' tem '{}' porc. de chance de ser cientista de dados".format(
                fake.name(), random.randint(1, 100))
        f.write(msg + '\n')
        f.close()
        sleep(2)

if __name__ == '__main__':
  poll()   