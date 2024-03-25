import csv
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
    
link=r'C:\Users\reoha\東大データマイニング講座/exam_score.csv'
    
def exam_stat():
    kokugo_score=[]
    shakai_score=[]
    sugaku_score=[]
    rika_score=[]
    score=open("exam_score.csv",'rt',encoding="ms932", errors='ignore')
    score_reader = csv.reader(score)
    score_data = list(score_reader)

    for row in score_data:
              kokugo_score.append(int(row[0]))
              shakai_score.append(int(row[1]))
              sugaku_score.append(int(row[2]))
              rika_score.append(int(row[3])) 


    kokugo_stat=avg_max_min(kokugo_score)
    shakai_stat=avg_max_min(shakai_score)
    sugaku_stat=avg_max_min(sugaku_score)
    rika_stat=avg_max_min(rika_score)
    results={"kokugo":kokugo_stat,"shakai":shakai_stat,"sugaku":sugaku_stat,"rika":rika_stat,}
    print(results)
    
exam_stat()
    
    