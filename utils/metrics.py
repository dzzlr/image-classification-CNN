from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score

def image_classification_metrics(list_actual, list_predict):
    metrics = {}
    metrics["ACC"] = accuracy_score(list_actual, list_predict)
    metrics["F1"] = f1_score(list_actual, list_predict, average='macro')
    metrics["REC"] = recall_score(list_actual, list_predict, average='macro')
    metrics["PRE"] = precision_score(list_actual, list_predict, average='macro')
    return metrics
