import datetime
from numpy import linalg as LNG 


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def get_routine(routine: str, give_time: str)-> int:
    time_stamp = datetime.datetime.fromisoformat(give_time)
    if routine == "morning" and time_in_range(datetime.time(5, 0, 0),datetime.time(9, 0, 0),time_stamp.time()):
        return 1
    elif routine == "daytime" and time_in_range(datetime.time(9, 0, 0),datetime.time(17, 0, 0),time_stamp.time()):
        return 1
    elif routine == "evening" and time_in_range(datetime.time(17, 0, 0),datetime.time(21, 0, 0),time_stamp.time()):
        return 1
    elif routine == "sleep" and time_in_range(datetime.time(21, 0, 0),datetime.time(5, 0, 0),time_stamp.time()):
        return 1
    else: 
        return 0


def euclidean(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

# return Series of distance between each point and his distance with the closest centroid
def getDistanceByPoint(data, model):
    distance = pd.Series()
    # pd.DataFrame(index=dataset.index) 
    # pd.Series(dtype=int)
    for i in range(0,len(data)):
        Xa = np.array(data.loc[i])
        Xb = model.cluster_centers_[model.labels_[i]-1]
        # print(np.linalg.norm(Xa-Xb))
        # distance.at[i, np.linalg.norm(Xa-Xb)]
        distance.loc[i]=np.linalg.norm(Xa-Xb)
    return distance

if __name__=="__main__":
    print(get_routine("morning", "2016-04-12 06:27:00"))
    print(get_routine("evening", "2016-04-12 07:27:00"))
    print(get_routine("morning", "2016-04-12 10:27:00"))
    print(get_routine("evening", "2016-04-12 18:27:00"))
    print(get_routine("sleep", "2016-04-12 21:27:00"))
    print(get_routine("sleep", "2016-04-25 21:05:00"))