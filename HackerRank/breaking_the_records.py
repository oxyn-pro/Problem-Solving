# The link for a problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# The difficulty of the problem is EASY
# All test cases passed

games = int(input())
game_scores = list(map(int, input().split()))

def score_minmax_counter(game_scores):
  """This function counts the breaks(min/max) of scores that player had during plays""""
  for i in game_scores:
        if i >= max_score:
            if i > max_score:
                max_times += 1
            max_score = i

        if i <= min_score:
            if i < min_score:
                min_times += 1
            min_score = i
            
    result = [max_times, min_times]
    return result
