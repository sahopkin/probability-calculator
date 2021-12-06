import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.balls = kwargs
    self.contents = []
    for key, val in self.balls.items():
      for i in range(val):
        self.contents.append(key)
  
  def draw(self, num):
    self.num = num
    self.chosen = []
    if self.num > len(self.contents):
      return self.contents
    else:
      for i in range(self.num):
        self.pulled = random.choice(self.contents)
        self.chosen.append(self.pulled)
        self.contents.remove(self.pulled)
      return self.chosen

      
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  M = 0                #Counts number of matched results
  N = num_experiments  #Total experiments to run

  exp_num = 0          #Number of experiments run so far
  while exp_num < num_experiments:
    hat_copy = copy.deepcopy(hat)

    #draw the balls
    actual_balls_list = hat_copy.draw(num_balls_drawn)

    #add actual balls to a dictionary so that the result can be compared to the expected_balls dictionary.
    actual_balls = {}
    for ball in actual_balls_list:
      if ball not in actual_balls:
        actual_balls[ball] = 1
      else:
        actual_balls[ball] += 1
    
    #compare actual_balls to expected_balls.  If the expected balls are found in actual_balls, increase true_count by 1.  
    true_count = 0
    expected_balls_len = len(expected_balls)

    for key, val in expected_balls.items():
      if key not in actual_balls:
        pass
      elif actual_balls[key] >= val:
        true_count += 1
    #if true_count == expected _balls_len, then the expected result has occured; increase M by 1
    if true_count == expected_balls_len:
      M += 1
    #increase the experiment counter by 1
    exp_num += 1
  #probability of the expected outcome occuring after n experiments
  return M/N

