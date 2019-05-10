"""
https://programmers.co.kr/learn/courses/30/lessons/49993
"""
import re

def solution(skill, skill_trees):
    answer = 0
    p = re.compile('['+skill+']')
    for t in range(len(skill_trees)):
        skill_trees[t] = ''.join(p.findall(skill_trees[t]))
        if skill_trees[t] == skill[:len(skill_trees[t])]:
            answer += 1
    return answer