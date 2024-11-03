def evaluation_scores(gold, pred):
    """Print precision, recall, and F1 score.
    
    Arguments:
        gold: The set with the gold-standard values.
        pred: The set with the predicted values.
    
    Returns:
        A tuple or list containing the precision, recall, and F1 values
        (in that order), computed based on the specified sets.
    """

    
    TP = gold & pred
    FP = pred - gold
    FN = gold - pred

    TP=len(TP)
    FP=len(FP)
    FN=len(FN)

    # Calculate Precision, Recall, and F1 Score
    precision = TP / (TP + FP)        #True positive/(true positive+false positive)
    recall = TP / (TP + FN)           # True positive/(true positive+false Negative)
    f1_score = 2 * (precision * recall) / (precision + recall) 

    return precision, recall, f1_score
