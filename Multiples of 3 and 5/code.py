# coding=utf-8
'''
sn1=1+2+3+...ceil(N/3-1)
sn2=1+2+3+...ceil(N/5-1)
sn3=1+2+3+...ceil(N/15-1)
result=3*sn1+5*sn2-15*sn3
时间复杂度:O(1)
'''
import math


def compute(N):
	seq_num_1 = math.ceil(N / 3 - 1)
	seq_num_2 = math.ceil(N / 5 - 1)
	seq_num_3 = math.ceil(N / 15 - 1)
	seq_sum_1 = seq_num_1 + seq_num_1 * (seq_num_1 - 1) / 2
	seq_sum_2 = seq_num_2 + seq_num_2 * (seq_num_2 - 1) / 2
	seq_sum_3 = seq_num_3 + seq_num_3 * (seq_num_3 - 1) / 2
	return 3 * seq_sum_1 + 5 * seq_sum_2 - 15 * seq_sum_3


print(compute(1000))
