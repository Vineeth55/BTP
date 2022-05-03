# BTP
Different Benchmark circuit files are converted into graphs using task1s.py and task1c.py for sequential circuits and combinational circuits respectively. The benchmark circuit files are available in 'bench' directory and their corresponding graphs are written as edgelists in the 'edgelist' directory. The resulting edgelists are passed into node2Vec algorithm (which is available online) to get feature vectors for each edglist. 

The numbers representing nodes in the edgelist are not the same as numbers present in benchmark circuit files, every node in benchmark circuit is assigned a unique number and this is the number shown in the edgelists. This is done because, in some of the benchmark circuit files nodes are represented as strings, but node2Vec algorithm requires nodes to represented as integers, hence strings are converted into integer and are stored in Dictionary.   

There are a few changes to be made to gensim library which is used in main.py for WordtoVec function. In the default code of Word2Vec function the variable 'sentence' is a map object for which len() function cannot be applied, hence the map object is converted into list by using list(sentence).

In main.py, line 86 is modified to "model.wv.save_word2vec_format(args.output)" instead of "model.save_word2vec_format(args.output)" as in original code.

# Issues
In c1196.bench file, G45 is given as both input and output.

In benchmark circuit files starting with "b", there were calculation mistakes of number of gates which are fixed now.
 
