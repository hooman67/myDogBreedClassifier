def Resnet50_model_predict_breed(img_path):
    # extract bottleneck features
    bottleneck_feature = extract_Resnet50(path_to_tensor(img_path))
    # obtain predicted vector
    predicted_vector = Resnet50_model.predict(bottleneck_feature)
    # return dog breed that is predicted by the model
    return dog_names[np.argmax(predicted_vector)]


def idendifyBreed(img_path):
    breed = Resnet50_model_predict_breed(img_path)
    if face_detector(img_path):
        print("human detected, the most similar dog breed is: ", breed)
        return breed
    elif dog_detector(img_path):
        breed = Resnet50_model_predict_breed(img_path)
        print("dog detected, the predicted breed is: ", breed)
        return breed
    else:
        print("Error: neither human nore dog detected in the image")


for imPath in glob("hsImages/*"):
    idendifyBreed(imPath)
    img = cv2.imread(imPath)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(imgRGB)
    plt.show()
    print("\n")