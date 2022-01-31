from django.shortcuts import render
from django.shortcuts import render,HttpResponse
import pickle
import os
# Create your views here.
def home(request):
    return render(request,'home.html')

def gold(request):
    if (request.method == 'POST'):
        print("posts")
        spx = request.POST['spx']
        uso = request.POST['uso']
        slv = request.POST['slv']
        eur_sud = request.POST['eur_sud']
       
        input_var =[spx, uso, slv,eur_sud]
        for i in range(len(input_var)):
            input_var[i] = float(input_var[i])
        print(input_var)
        input_var_in_2d = []
        input_var_in_2d.append(input_var)
        #reading the model
        with open('models/gold_model','rb') as file:
            model = pickle.load(file)
            
        prediction = model.predict(input_var_in_2d)
        print(prediction)
     
        if (prediction[0]== 0):
            return HttpResponse("The person is not diabetic")
        else:
            return HttpResponse('The person is diabetic')
    else:
        print("get")
        # # file_ = open()
        # with open(os.path.join(settings.BASE_DIR, 'models//heart_disease_model'),'rb') as file:
        #     model = pickle.load(file)
            
        # model.predict([[1,2,3,4,5,6,7,8,9,10,11,12,13]])
        return render(request,'gold.html')
