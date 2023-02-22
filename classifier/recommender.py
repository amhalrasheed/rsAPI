import json
import pickle


class rs:
    def __init__(self):
        self.pred = {}

dict = {
    '0': 83,
    '1': 84,
    '2': 86,
    '3': 85,
    '4': 87,
    '5': 88,
    '6': 78,

    'جامعة الامام محمد بن سعود': 0,
    'جامعة الملك سعود': 1,
    'جامعة الاميرة نورة': 2,
    'جامعة الامير سطان': 3,
    'جامعة ام القرى': 4,
    'جامعة الملك عبدالله': 5,
    'جامعة الملك فهد لي البترول والمعادن': 6,
    'جامعة الملك عبدالعزيز': 7,

    'امن الشبكات': 0,
    'الحوسبة السحابية': 1,
    'ذكاء اصطناعي': 2,
    'تطوير التطبيقات': 3,

    'خريج': 1,
    'طالب جامعي': 0,
}

def most_frequent(List):
    return max(set(List), key=List.count)



def api_call(features):
    tempObject = json.loads(features)
    classifierss = pickle.load(open('./classifier/models/classifiers.sav', 'rb'))

    gba = tempObject['gba']
    interest = tempObject['interest']
    university = tempObject['university']
    isgrad = tempObject['isgrad']


    recommendation = rs()

    gbas       = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    interests  = [0, 0, 0, 0]
    universities = [0, 0, 0, 0, 0, 0, 0, 0]
    isgrads    = [0, 0]

    arr = []

    if gba >= 4.75:
        gbas[0] = 1
    elif gba >= 4.5:
        gbas[1] = 1
    elif gba >= 4.0:
        gbas[2] = 1
    elif gba >= 3.5:
        gbas[3] = 1
    elif gba >= 3.0:
        gbas[4] = 1
    elif gba >= 2.5:
        gbas[5] = 1
    elif gba >= 2.0:
        gbas[6] = 1
    elif gba >= 1.0:
        gbas[7] = 1
    else:
        gbas[8] = 1
    
    interests[dict[interest]] = 1
    universities[dict[university]] = 1
    isgrads[dict[isgrad]] = 1
    toPred = gbas + interests + universities + isgrads

    for clf in classifierss:
        pred = clf.predict([toPred])
        arr.append(dict[str(pred[0])])

    if (len(set(arr)) == len(arr)):
        recommendation.pred["pred"] = arr[0]
    else:
        recommendation.pred["pred"] = most_frequent(arr)

    recommendation.pred["possible"] = arr

    return recommendation.pred
