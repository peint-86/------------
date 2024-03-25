def avg_max_min(input_list):
    avg_value=0
    max_value=-1
    min_value=101
    sum_value=0
    results=[]
    
    for v in range(len(input_list)):
        sum_value=sum_value+int(input_list[v])
        if int(input_list[v])>max_value:
            max_value=int(input_list[v])
        if int(input_list[v])<min_value:
            min_value=int(input_list[v])
    avg_value=sum_value/len(input_list)
    results.append(avg_value)
    results.append(max_value)
    results.append(min_value)
    print(results)
avg_max_min([30,39,29,95,70,67,29,56,45,68])