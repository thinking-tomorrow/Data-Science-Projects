
import pickle

model=pickle.load(open('model.pkl', 'rb'))

print(model.predict([[10, 60, 3, 2, 6, 1, 3, 0, 0, 1, 8, 5, 0,0 , 0,0 ,0, 0, 0, 0, 1, 0, 0]]))