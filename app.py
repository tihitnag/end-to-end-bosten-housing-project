import pickle 
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd


app=Flask(__name__)
#load the pikel file
model=pickle.load(open('regmodel.pkl','rb'))
scaler=pickle.load(open('scaling.pkl','rb'))
#load model 
#regmodel=pickle.load(open('regmodel.pkl'))
#scaler=pickle.load(open('scaler.pkl'))
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict_api',methods=['POST'])
def predict_api():
    data_set=request.json['data']
    print(data_set)
    print(np.array(list(data_set.values())).reshape(1,-1))
    new_data=scaler.transform(np.array(list(data_set.values())).reshape(1,-1))
    print(new_data)
    output=model.predict(new_data)
    print(output[0])
 
    return jsonify(output[0])

if __name__=='__main__':
    app.run(debug=True)
    
    
    
    

# def predict_api():
#     # Step 1: Ensure that request contains JSON
#     if not request.is_json:
#         return jsonify({"error": "Request body must be JSON"}), 400
    
#     # Debug: Print the entire JSON payload
#     print("Received JSON payload:", request.json)
    
#     # Step 2: Check if 'data' key exists
#     if 'data' not in request.json:
#         return jsonify({"error": "'data' key not found in the request"}), 400
    
#     # Step 3: Extract and process data
#     try:
#         data_set = request.json['data']
#         print("Extracted 'data' from request:", data_set)
        
#         # Convert the data to a numpy array and reshape it
#         data_array = np.array(list(data_set.values())).reshape(1, -1)
#         print("Reshaped data array:", data_array)

#         # Check if the number of features is correct (assuming 13 features expected)
#         if data_array.shape[1] != 13:
#             return jsonify({"error": "Expected 13 features, got {}".format(data_array.shape[1])}), 400
        
#         # Step 4: Transform data using scaler (assuming scaler is preloaded)
#         new_data = scaler.transform(data_array)
#         print("Transformed data:", new_data)
        
#         # Step 5: Predict using model (assuming model is preloaded)
#         output = model.predict(new_data)
#         print("Prediction output:", output)
        
#         return jsonify({"prediction": output[0]})
    
#     except Exception as e:
#         # Step 6: Catch any unexpected errors and print for debugging
#         print("Error during processing:", str(e))
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)