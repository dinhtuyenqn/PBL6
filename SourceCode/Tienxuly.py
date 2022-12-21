train_dir = '/PBL/PBL6'
i = 0 

for img in os.listdir('/content/drive/MyDrive/images2'):

  if img.endswith('.jpg'):
     try:
       img_array = cv2.imread("/content/drive/MyDrive/images2/" + img)

       img_array = cv2.resize(img_array, (128,128))
       lr_img_array = cv2.resize(img_array,(32,32))
       cv2.imwrite(train_dir+ "/hr_images/" + img, img_array)
       cv2.imwrite(train_dir+ "/lr_images/"+ img, lr_img_array)
     except:
       continue
   if i == 4000: 
     break 
   i +=1