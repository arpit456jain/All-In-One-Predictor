from django.shortcuts import render,HttpResponse
import pickle
import os
from django.conf import settings


# Create your views here.
def home(request):
    return render(request,'diseases/home.html')


def heart(request):
    if (request.method == 'POST'):
        print("posts")
        age = request.POST['age']
        sex = request.POST['sex']
        cp = request.POST['cp']
        trestbps = request.POST['trestbps']
        chol = request.POST['chol']
        fbs = request.POST['fbs']
        restecg = request.POST['restecg']
        thalach = request.POST['thalach']
        exang = request.POST['exang']
        oldpeak = request.POST['oldpeak']
        slope = request.POST['slope']
        ca = request.POST['ca']
        thal = request.POST['thal']
        input_var =[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        for i in range(len(input_var)):
            input_var[i] = float(input_var[i])
        print(input_var)
        input_var_in_2d = []
        input_var_in_2d.append(input_var)
        #reading the model
        with open('models/heart_disease_model','rb') as file:
            model = pickle.load(file)
            
        prediction = model.predict(input_var_in_2d)
        print(prediction)

        if (prediction[0]== 0):
            return HttpResponse("The Person does not have a Heart Disease")
        else:
            return HttpResponse('The Person has Heart Disease')
    else:
        print("get")
        # # file_ = open()
        # with open(os.path.join(settings.BASE_DIR, 'models//heart_disease_model'),'rb') as file:
        #     model = pickle.load(file)
            
        # model.predict([[1,2,3,4,5,6,7,8,9,10,11,12,13]])
        return render(request,'diseases/heart.html')



def parkinson(request):
    if (request.method == 'POST'):
        print("posts")
        pregnancies = request.POST['pregnancies']
        glucose = request.POST['glucose']
        bloodpressure = request.POST['bloodpressure']
        skinthickness = request.POST['skinthickness']
        insulin = request.POST['insulin']
        bmi = request.POST['bmi']
        diabetespedigreefunction = request.POST['diabetespedigreefunction']
        age = request.POST['age']
        input_var =[pregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,diabetespedigreefunction,age]
        for i in range(len(input_var)):
            input_var[i] = float(input_var[i])
        print(input_var)
        input_var_in_2d = []
        input_var_in_2d.append(input_var)
        #reading the model
        with open('models/parkinson_disease_model','rb') as file:
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
        return render(request,'diseases/parkinson.html')



