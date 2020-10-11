### Notes 

-  [Gitbook Notes](https://harshityadav95.gitbook.io/macine-learning-notes/)





### Machine Learning Code Snippets

1. Uploading the data in the code run-time :

   ```shell
   from google.colab import files
   uploaded = files.upload()
   ```

   

2. Mounting the Google Drive 

```shell
from google.colab import drive
drive.mount('/content/gdrive')

#then upload the data in the google drive and then acces sit
test_data = pd.read_csv('/content/gdrive/My Drive/Housing-Price-Prediction/data/test.csv')

```

3. Directly uploading to the Current VM Instance  : 

   ```shell
   !wget  https://github.com/harshityadav95/Notex/blob/master/src/hyembosslogo.jpg
   ```

4. Display Image in Jupyter Notebook

   ```shell
   ## To display image on the Jupyter notebook
   from IPython.display import display
   display(image)
   ```

   

5. Inspecting the Image type and Details :  

   ```shell
   import inspect
   print("The type of the image is " + str(type(image)))
   inspect.getmro(type(image))
   ```

6. Open and Save Image 

   ```shell
   import PIL
   from PIL import Image
   from IPython.display import display
   file="readonly/msi_recruitment.gif"
   image=Image.open(file)
   image.save("msi_recruitment.png")
   image=Image.open("msi_recruitment.png")
   
   ```

   

7. Image Filter Library Pillow

   ```shell
   from PIL import ImageFilter
   help(ImageFilter)
   ```

8. Dimensions of the Image 

   ```shell
   display(image.crop((50,0,190,150)))
   ```

9. Blur an Image using in built feature

   ```shell
   image=image.convert('RGB')
   # this stands for red, green blue mode other is CMYK
   blurred_image=image.filter(PIL.ImageFilter.BLUR)
   display(blurred_image)
   ```

10.  Cropping the Image 

    ```shell
    display(image.crop((50,0,190,150)))
    ```

    

11.  Write Text on Image 

    ```python
    from PIL import ImageDraw
    drawing_object=ImageDraw.Draw(image)
    drawing_object.rectangle((50,0,190,150), fill = None, outline ='red')
    display(image)
    ```

    

12 . Enhance Image

```python
from PIL import ImageEnhance
# load image in enhancer class
enhancer=ImageEnhance.Brightness(image)
images=[]
for i in range(0, 10):

    images.append(enhancer.enhance(i/10))

print(images)
```

13.  Create a new Image 

```python
# new image with RGB mode and dimensionnina  tuple
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))

```

14. Iterate over a 3X3 Image and Paste Image 

    ```python
    x=0
    y=0
    
    for img in images[1:]:
       
        contact_sheet.paste(img, (x, y) )
    
        if x+first_image.width == contact_sheet.width:
            x=0
            y=y+first_image.height
        else:
            x=x+first_image.width
            
    ```

15. Resize an Image

    ```python
    contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
    # Now lets display that composite image
    display(contact_sheet)
    ```

    
