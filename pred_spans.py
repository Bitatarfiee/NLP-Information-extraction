def pred_spans(df):
    """Run and evaluate spaCy's NER.

    Arguments:
        df: A data frame.

    Yields:
        The predicted mention spans in the specified data frame as
        triples consisting of the sentence id, start position, and end
        position of each span.
    """

    
    for row in df.itertuples():
        sentence_id=row.sentence_id
        doc = nlp(row.sentence)
        for ent in doc.ents:
            yield ( sentence_id, ent.start, ent.end)
