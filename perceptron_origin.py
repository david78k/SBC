import random

#threshold = 0.49999
threshold = 0.5
learning_rate = 0.1
weights = [0, 0, 0]
training_set = [((1, 0, 0), 1), ((1, 0, 1), 1), ((1, 1, 0), 1), ((1, 1, 1), 0)]
 
 
def dot_product(values, weights):
    return sum(value * weight for value, weight in zip(values, weights))
 
cycle = 1
t = 0
while True:
    print('-' * 30 + ' cycle ' + str(cycle) + ' ' + '-' * 30)
    #print('-' * 60)
    error_count = 0
    for input_vector, desired_output in training_set:
        print '%.2f'% t, weights
        #print (weights)
        result = dot_product(input_vector, weights) > threshold
        #result = dot_product(input_vector, weights) >= threshold
        error = desired_output - result
        if error != 0:
            error_count += 1
            for index, value in enumerate(input_vector):
                weights[index] += learning_rate * error * value
        t += random.random()        
    if error_count == 0:
        break
    cycle += 1
