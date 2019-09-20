from analiser import Analiser

# start analiser with set training data
an = Analiser(training_data='data/training_all_random.csv')

# train new model
an.train(filename='model')

test = "Sbg mantan wartawan Tempo yg sudah lebih dari 10 tahun di luar kerja jurnalisme majalah itu, saya merasa bisa ambil jarak dari padanya.  Tempo bisa keliru, bisa punya bias, tapi saya tahu dlm kritiknya tak terkandung sikap a priori anti "
print test
print an.testFromTrained([an.tfidf_data.transform(test)])

test = "ahok itu pemimpin yang ga beres memimpin"
print test
print an.testFromTrained([an.tfidf_data.transform(test)])
