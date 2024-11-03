def gold_spans(df):
    """Yield the gold-standard mention spans in a data frame.

    Arguments:
        df: A data frame.

    Yields:
        The gold-standard mention spans in the specified data frame as
        triples consisting of the sentence id, start position, and end
        position of each span.
    """
    
    # YOUR CODE HERE
    for span in df.itertuples(index=False):
        yield (span[0],span[2],span[3])
