import numpy as np

def score_fn(gold: str, pred: str):
    
    if type(gold) is not str or type(pred) is not str:
        raise TypeError("Invalid data type.")
    gold_arr, pred_arr = gold.split('\n'), pred.split('\n')
    if gold_arr[0] != pred_arr[0]:
        raise ValueError("These files do not correspond to each other.")
    if len(gold_arr[-1]) == 0:
        gold_arr = gold_arr[:-1]
    pred_arr, gold_arr = pred_arr[1:], gold_arr[1:]
    
    fn = np.array([g_elem for g_elem in gold_arr if g_elem not in pred_arr]).shape[0]
    fp = np.array([p_elem for p_elem in pred_arr if p_elem not in gold_arr]).shape[0]
    tp = np.array([g_elem for g_elem in gold_arr if g_elem in pred_arr]).shape[0]
    
    if tp == 0:
        raise ValueError("An error occurred. Please make sure that gold and pred answers follow this structure: "\
                "Named-entity-mention <TAB> base-form <TAB> category <TAB> cross-lingual ID")
    
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * (precision * recall) / (precision + recall)
    return f1