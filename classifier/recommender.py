import json
import pickle


class rs:
    def __init__(self):
        self.pred = {}


def most_frequent(List):
    return max(set(List), key=List.count)


def api_call(features):
    tempObject = json.loads(features)

    recommendation = rs()

    classifierss = pickle.load(open('classifier\models\classifiers.sav', 'rb'))
    arr = []
    toPred = [tempObject['gba'], tempObject['interest'],
              tempObject['university'], tempObject['grad']]

    for clf in classifierss:
        pred = clf.predict([toPred])
        arr.append(pred[0])

    if (len(set(arr)) == len(arr)):
        recommendation.pred["pred"] = arr[0]
    else:
        recommendation.pred["pred"] = most_frequent(arr)

    recommendation.pred["possible"] = arr

    return recommendation.pred
