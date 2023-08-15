# Pnemonia_disease_prediction

Certainly! Here's a description of the provided code without the actual code snippets:

The provided code demonstrates a binary image classification task using chest X-ray images. The process can be summarized in the following steps:

1. **Data Loading and Preprocessing:**
   The code begins by loading chest X-ray images from a directory. These images are resized to a uniform size of (100, 100) pixels. The images are then converted into arrays for further processing. Labels are assigned to each image based on their directory structure. Images labeled as "NORMAL" are given the label `0`, while other cases are labeled `1`.

2. **Data Preparation:**
   After loading and preprocessing the images, they are organized into a format suitable for model training. The images are reshaped into a flat representation to be used as input data. The dataset is then split into training and testing sets. The labels are converted into one-hot encoded vectors to facilitate binary classification.

3. **First Model (Dense Neural Network):**
   The code defines and trains a dense neural network model. This model consists of two hidden layers with ReLU activation functions. The output layer uses the softmax activation function to classify images into two categories. The model is compiled with an optimizer, loss function, and evaluation metrics. It is trained on the training data and evaluated on the testing data.

4. **Displaying Images:**
   The code visualizes two images from the dataset using the Matplotlib library. This provides a visual representation of the processed images.

5. **Second Model (Convolutional Neural Network - CNN):**
   A more sophisticated model architecture is introduced in this section. A convolutional neural network (CNN) is defined and trained. The CNN consists of convolutional layers that automatically learn relevant features from the images. Max-pooling layers downsample the feature maps, and the network is then flattened to be fed into fully connected layers. Similar to the first model, this CNN is trained and evaluated.

6. **Saving the Model:**
   The trained CNN model is saved to a file named 'arun'. This allows for future use without the need to retrain the model.

In summary, the code showcases the process of loading, preprocessing, and classifying chest X-ray images using both a dense neural network and a convolutional neural network. The goal is to accurately classify these images into two categories (normal and abnormal) and save the trained CNN model for potential future use.
