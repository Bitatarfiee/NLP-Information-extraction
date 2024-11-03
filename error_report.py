from collections import defaultdict

def error_report(df, spans_gold, spans_pred):
    false_pos = defaultdict(list)
    for s, b, e in spans_pred - spans_gold:
        false_pos[s].append((b, e))
    false_neg = defaultdict(list)
    for s, b, e in spans_gold - spans_pred:
        false_neg[s].append((b, e))
    for row in df.drop_duplicates('sentence_id').itertuples():
        if row.sentence_id in false_pos or row.sentence_id in false_neg:
            print('Sentence:', row.sentence)
            for b, e in false_pos[row.sentence_id]:
                print('  FP:', ' '.join(row.sentence.split()[b:e]))
            for b, e in false_neg[row.sentence_id]:
                print('  FN:', ' '.join(row.sentence.split()[b:e]))
