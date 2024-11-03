# NLP-Information-extraction
The Jupyter notebook is a part of the Text mining course Labs.

Information extraction (IE) is the task of identifying named entities and semantic relations between these entities in text data.
The code includes two sub-tasks in IE:
- Named entity recognition (identifying mentions of entities)
- Entity linking (matching these mentions to entities in a knowledge base)

1. Defining Evaluation measures
2. Span recognition
  -  implementing a generator function that yields the gold-standard spans in a given data frame.
3. Error analysis spans a data frame, including prints of the false positives and negatives.
4. write a code to post-process the output produced by spaCy. To filter out specific labels it is useful to know the named entity label scheme
  - labels:  Filtered_label= ["CARDINAL", "DATE","ORDINAL", "MONEY", "TIME", "QUANTITY", "PERCENT"]
5. Entity linking
6. Extending the training data using the knowledge base
7. Context-sensitive disambiguation
 


