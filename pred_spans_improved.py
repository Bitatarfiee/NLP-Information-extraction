def pred_spans_improved(df):
    """Run and evaluate spaCy's NER, with post-processing to improve the results.

    Arguments:
        df: A data frame.

    Yields:
        The predicted mention spans in the specified data frame as
        triples consisting of the sentence id, start position, and end
        position of each span.
    """
   
    # CARDINAL, DATE, EVENT, FAC, GPE, LANGUAGE, LAW, LOC, MONEY, NORP, ORDINAL, ORG, PERCENT, PERSON, PRODUCT, QUANTITY, TIME, WORK_OF_ART
    Filtered_label= ["CARDINAL", "DATE","ORDINAL", "MONEY", "TIME", "QUANTITY", "PERCENT"]
    for row in df.itertuples():
        sentence_id=row.sentence_id
        doc = nlp(row.sentence)
        for ent in doc.ents:
            if ent.label_ not in Filtered_label:
                yield ( sentence_id, ent.start, ent.end)
 
