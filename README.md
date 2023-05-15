# Video Ads Detection

## Description of the project :-  
* This project deals with detecting ads in a streamed recorded video.  
* The ads are stored in folder named 'ads'. With file name as ad1, ad2,... adn and so on.  
* The recorded livestream is to be stored in folder named 'livestream' With file name as 'LiveStream.mp4'.  
* Sample Video Link contaning above ads is https://drive.google.com/file/d/1O9RthDHUs2FqlHmko8RN6ZGRuvG2lCQ7/view?usp=share_link
  
### Steps to run the project :-  
* Install library virtualenv  
```
pip install virtualenv
```
* Create a Virtual Environment.
```
virtualenv .env
```
* Activate the Virtual environment.
```
./env/Scripts/activate
```
* Install OpenCV.
```
pip install opencv-python
```
* Run the file captureData.
```
python captureData.py
```
* Finally, run the file adDetection.
```
python adDetection.py
```
#
